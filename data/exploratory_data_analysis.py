import requests
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from scipy.stats import zscore

def fetch_data():
    try:
        events_api = requests.get('http://127.0.0.1:8000/api/events')
        events_api.raise_for_status()
        events_api_data = events_api.json()

        volunteers_api = requests.get('http://127.0.0.1:8000/api/volunteers')
        volunteers_api.raise_for_status()
        volunteers_api_data = volunteers_api.json()

        return events_api_data, volunteers_api_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None, None


def clean_data(events_api_data, volunteers_api_data):

    edf = pd.DataFrame(events_api_data)
    vdf = pd.DataFrame(volunteers_api_data)

    merged_df = pd.merge(edf, vdf, on='id', how="inner")
    

    merged_df.ffill(inplace=True)

 
    merged_df.drop_duplicates(inplace=True)


    if 'category_column' in merged_df.columns:
        le = LabelEncoder()
        merged_df['category_column'] = le.fit_transform(merged_df['category_column'])

    numerical_columns = ['numerical_column1', 'numerical_column2'] 
    if all(col in merged_df.columns for col in numerical_columns):
        scaler = StandardScaler()
        merged_df[numerical_columns] = scaler.fit_transform(merged_df[numerical_columns])

 
    if 'numerical_column' in merged_df.columns: 
        merged_df['z_score'] = zscore(merged_df['numerical_column'])
        merged_df = merged_df[merged_df['z_score'].abs() <= 3] 

    return merged_df


def main():

    events_api_data, volunteers_api_data = fetch_data()

    if events_api_data and volunteers_api_data:
        cleaned_data = clean_data(events_api_data, volunteers_api_data)

        print("Missing values after cleaning:")
        print(cleaned_data.isnull().sum())  
        print("Duplicate rows after cleaning:")
        print(cleaned_data.duplicated().sum())

        print(cleaned_data.head())

        cleaned_data.to_csv("cleaned_data.csv", index=False)

if __name__ == "__main__":
    main()
