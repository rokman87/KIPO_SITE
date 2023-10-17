document.addEventListener('DOMContentLoaded', (event) => {
    const saveButton = document.getElementById("saveButton");

    saveButton.addEventListener("click", (event) => {
        event.preventDefault();

        const cells = document.querySelectorAll(".cell");
        let cellsData = [];

        cells.forEach((cell) => {
            const dataElementId = cell.getAttribute("data-id");
            const text = cell.textContent.trim();
            const cellName = cell.className;

            // Сохраняем данные только для заполненных ячеек
            if (dataElementId && text) {
                cellsData.push({
                    text: text,
                    dataElementId: dataElementId,
                    cellName: cellName
                });
            }
        });

        // Отправляем данные на бэкенд Django
        fetch('url-django', {
            method: 'POST',
            body: JSON.stringify(cellsData),
            headers:{
                'Content-Type': 'application/json'
            }
        }).then(res => res.json())
        .catch(error => console.error('Ошибка:', error))
        .then(response => console.log('Успех:', response));
    });
});
