function openPanel() {
    fetch('/get_panel')  // GET запрос для получения HTML панели
        .then(response => response.text())
        .then(html => {
            document.getElementById('panel').innerHTML = html;
            document.getElementById('panel').style.display = 'block';  // Показываем панель
        })
        .catch(error => console.error('Ошибка:', error));
}

function renderTable(users) {
    const tableBody = document.querySelector('#users-table tbody');
    tableBody.innerHTML = '';  // Очищаем таблицу

    users.forEach(user => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${user.id}</td>
            <td>${user.name}</td>
            <td>${user.email}</td>
        `;
        tableBody.appendChild(row);
    });
}
// Функция для отправки данных из панели
function submitPanel() {
    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
    };

    fetch('/submit_panel', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),  // Отправляем данные в формате JSON
    })
        .then(response => response.json())
        .then(data => {
            alert(data.message);  // Показываем сообщение об успехе
            document.getElementById('panel').style.display = 'none';  // Скрываем панель
        })
        .catch(error => console.error('Ошибка:', error));
}