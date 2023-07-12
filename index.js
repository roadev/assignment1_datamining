// Function to load and parse the CSV data
function loadData() {
    Papa.parse('path_to_your_csv.csv', {
        download: true,
        header: true,
        complete: function(results) {
            displayData(results.data);
        }
    });
}

// Function to display the CSV data in the table
function displayData(data) {
    const tableBody = document.querySelector('#data-table tbody');
    data.forEach(row => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${row.Title}</td>
            <td><a href="${row.Link}">Link</a></td>
            <td>${row.Authors}</td>
            <td>${row.Date}</td>
            <td><a href="${row['PDF Link']}">PDF Link</a></td>
            <td>${row.Abstract}</td>
        `;
        tableBody.appendChild(tr);
    });
}

// Call the loadData function when the page loads
window.onload = loadData;
