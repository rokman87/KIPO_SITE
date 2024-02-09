$(document).ready(function() {
    var allDataElementIds = []; // Массив для хранения dataElementId
    var scheduleData = null; // Переменная для хранения расписания

    // AJAX-запрос для получения расписания
    $.ajax({
        url: "print_schedule/",
        method: "GET",
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            scheduleData = data; // Сохраняем расписание
            collectDataElementIds(data); // Вызываем функцию для сбора dataElementId
        }
    });

    // Функция для сбора dataElementId в массив
    function collectDataElementIds(data) {
        data.forEach(function(item) {
            var dataElementId = item.dataElementId;
            allDataElementIds.push(dataElementId); // Добавляем в массив
        });

        processScheduleData(); // Вызываем функцию для обработки расписания после сбора всех dataElementId
    }

    // Функция для обработки расписания после сбора всех dataElementId
    function processScheduleData() {
        scheduleData.forEach(function(item) {
            var cellClass = item.cellName;
            var parentCell = item.group;
            var dataElementId = item.dataElementId;

            var cells = document.getElementsByClassName(cellClass);
            if (cells.length > 0) {
                for (var i = 0; i < cells.length; i++) {
                    (function(cell) {
                        var parentText = cell.parentElement.textContent.trim();
                        var parts = parentText.split(/\s+/);
                        if (cell.classList.value == cellClass && parentCell == parts[0]) {
                            cell.dataset.id = dataElementId;
                            cell.textContent = item.text;
                        }
                    })(cells[i]);
                }
            }
        });

        // После завершения обработки расписания вызываем функцию для обработки собранных данных
        processCollectedData(allDataElementIds);
    }

    // Функция для выполнения AJAX-запроса и обработки информации о кабинете
   function getCabinetInfo(dataElementIds) {
    console.log("Собранные dataElementIds:", dataElementIds);
    var uniqueDataElementIds = Array.from(new Set(dataElementIds));
    console.log("Уникальные dataElementIds:", uniqueDataElementIds);
    $.ajax({
        url: "get_cabinet_info/",
        method: "GET",
        data: {
            dataElementIds: JSON.stringify(uniqueDataElementIds) // Передача массива как строки JSON
        },
        dataType: 'json',
        success: function(Auditoriums) {
            handleCabinetInfo(Auditoriums);
        },
        error: function(error) {
            console.error('Ошибка получения информации о кабинете:', error);
        }
    });
}


    // Функция для обработки информации о кабинете
function handleCabinetInfo(Auditoriums) {
    // Проверяем, является ли Auditoriums объектом и имеет ли числовые свойства
    if (typeof Auditoriums === 'object' && Auditoriums !== null && !Array.isArray(Auditoriums)) {
        // Получаем массив значений из объекта
        var auditoriumsArray = Object.values(Auditoriums);

        // Итерируем по внешнему массиву
        auditoriumsArray.forEach(outerItem => {
            // Итерируем по внутреннему массиву
            outerItem.forEach(innerItem => {
                // Обработка информации о кабинетах
                const cabinetBuilding = innerItem.cabinets[0].building;
                const cabinetTitle = innerItem.cabinets[0].title;
                console.log(cabinetBuilding, "Кабинет:", cabinetTitle);

                // Итерируем по ячейкам уроков
                innerItem.lessons_cells.forEach(lessonCell => {
                    // Обработка информации о каждой ячейке урока
                    console.log("Ячейка урока:", lessonCell.cellName, lessonCell.group);
                    var elements = document.getElementsByClassName(lessonCell.cellName);
                    if (elements) {
                        // Ваш код для обработки найденной ячейки
                        console.log("Найденная ячейка:", elements);
                    } else {
                        console.log("Ячейка не найдена");
                    }
                });
            });
        });
    } else {
        console.error("Ошибка: Auditoriums не является объектом с числовыми свойствами.");
    }
}

    // Функция для обработки собранных данных
    function processCollectedData(dataElementIds) {

        getCabinetInfo(dataElementIds);
    }
});
