// Data passed from the Django view
const days = JSON.parse(document.getElementById('chart-data').dataset.days);
const donorData = JSON.parse(document.getElementById('chart-data').dataset.donorData);
const volunteerData = JSON.parse(document.getElementById('chart-data').dataset.volunteerData);
const eventData = JSON.parse(document.getElementById('chart-data').dataset.eventData);

// Donor Chart
const donorCtx = document.getElementById('donorChart').getContext('2d');
new Chart(donorCtx, {
    type: 'line',
    data: {
        labels: days,
        datasets: [{
            label: 'Donors',
            data: donorData,
            borderColor: 'rgba(75, 192, 192, 1)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderWidth: 1
        }]
    },
    options: { responsive: true }
});

// Volunteer Chart
const volunteerCtx = document.getElementById('volunteerChart').getContext('2d');
new Chart(volunteerCtx, {
    type: 'bar',
    data: {
        labels: days,
        datasets: [{
            label: 'Volunteers',
            data: volunteerData,
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        }]
    },
    options: { responsive: true }
});

// Event Chart
const eventCtx = document.getElementById('eventChart').getContext('2d');
new Chart(eventCtx, {
    type: 'line',
    data: {
        labels: days,
        datasets: [{
            label: 'Events',
            data: eventData,
            borderColor: 'rgba(255, 99, 132, 1)',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderWidth: 1
        }]
    },
    options: { responsive: true }
});
