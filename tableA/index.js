function loadData() {
    Papa.parse('tableA.csv', {
        download: true,
        header: true,
        complete: function(results) {
            displayData(results.data);
        }
    });
}

function displayData(data) {
    const tableBody = document.querySelector('#data-table tbody');
    data.forEach(row => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>${row.title}</td>
            <td>${row.authors}</td>
            <td>${row.abstract}</td>
            <td><a href="${row.url}">Link</a></td>
            <td>${row.date}</td>
        `;
        tableBody.appendChild(tr);
    });
}

window.onload = loadData;
