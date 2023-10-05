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

        // выводим в консоль для проверки
        console.log(cellsData);

        // сохраняем в localStorage
        localStorage.setItem("cellsData", JSON.stringify(cellsData));
    });
});
