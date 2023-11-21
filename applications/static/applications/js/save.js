document.addEventListener('DOMContentLoaded', () => {
    const saveButton = document.getElementById("saveButton");

    saveButton.addEventListener("click", (event) => {
        console.log("Обработчик события для кнопки сохранения");
        event.preventDefault();
        const cells = document.querySelectorAll(".cell");

        let cellsData = [];

        cells.forEach((cell) => {
            const dataElementId = cell.getAttribute("data-id");
            const text = cell.textContent.trim();
            const cellName = cell.className;
            const originalString = cell.parentElement.textContent.trim();// Текст родительского элемента
            const parentText = originalString.substring(0, originalString.indexOf('\n'));
            // Проверка и сохранение данных только для заполненных ячеек
            if (dataElementId && text) {
                console.log("Сохраняем данные ячейки");

                let cellData = {
                    text: text,
                    dataElementId: dataElementId,
                    cellName: cellName,
                    group: parentText // Добавляем текст родительского элемента
                };

                console.log(cellData); // Выводим каждое сохраняемое значение перед добавлением его в массив

                cellsData.push(cellData);
            }
        });
        console.log("Отправляем данные на бэкенд Django");
        // Отправляем данные на бэкенд Django

        // Получаем CSRF токен из cookie
        const csrftoken = document.cookie.split('; ')
                       .find(row => row.startsWith('csrftoken'))
                       .split('=')[1];

        fetch('url-django/', {
            method: 'POST',
            body: JSON.stringify(cellsData),
            headers:{
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken // Добавляем CSRF токен в заголовок запроса
            }
        }).then(res => res.json())
        .catch(error => console.error(error))
        .then(response => console.log("Успех: ", response));
    });
});
