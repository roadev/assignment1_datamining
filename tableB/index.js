const rowsPerPage = 50;
let currentPage = 0;

let data = [];

Papa.parse("tableB.csv", {
    download: true,
    header: true,
    complete: function(results) {
        data = results.data;
        renderPage(currentPage);
    }
});

function renderPage(page) {
    const tableBody = document.querySelector('#table tbody');
    const pagination = document.querySelector('#pagination');

    tableBody.innerHTML = '';
    pagination.innerHTML = '';

    const start = page * rowsPerPage;
    const end = start + rowsPerPage;

    const pageData = data.slice(start, end);

    for (let row of pageData) {
        const tr = document.createElement('tr');
        
        for (let cell of Object.values(row)) { 
            const td = document.createElement('td');
            td.textContent = cell;
            tr.appendChild(td);
        }
    
        tableBody.appendChild(tr);
    }
    

    const totalPages = Math.ceil(data.length / rowsPerPage);

    const paginationDiv = document.createElement('div');
    paginationDiv.className = 'pagination';

    for (let i = 0; i < totalPages; i++) {
        const button = document.createElement('button');
        button.className = 'page-link';
        button.textContent = i + 1;
        button.addEventListener('click', () => {
            currentPage = i;
            renderPage(currentPage);
        });

        if (i === page) {
            button.className += ' active';
        }

        const li = document.createElement('li');
        li.className = 'page-item';
        li.appendChild(button);
        paginationDiv.appendChild(li);
    }

    pagination.appendChild(paginationDiv);
}


renderPage(0);
