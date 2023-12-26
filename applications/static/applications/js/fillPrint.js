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
                            // Вызов функции для получения информации о кабинете
//                            getCabinetInfo(dataElementId, cell);
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
        success: function(cabinetInfo) {
            handleCabinetInfo(cabinetInfo);
        },
        error: function(error) {
            console.error('Ошибка получения информации о кабинете:', error);
        }
    });
}


    // Функция для обработки информации о кабинете
    function handleCabinetInfo(cabinetInfo) {
        if (cabinetInfo && cabinetInfo.length > 0) {
            var Item = cabinetInfo[0];
            var title = Item.title;
            var building = Item.building;

            if (title && building) {
                cell.textContent += building + ', ауд. ' + title;
            } else {
                console.error('title или building пусты или не содержат ожидаемых данных');
            }
        } else {
            console.error('cabinetInfo пуст или не содержит ожидаемых данных');
        }
    }

    // Функция для обработки собранных данных
    function processCollectedData(dataElementIds) {

        getCabinetInfo(dataElementIds);
    }
});
