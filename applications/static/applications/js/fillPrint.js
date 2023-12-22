$(document).ready(function() {
    var allDataElementIds = []; // Массив для хранения dataElementId

    // AJAX-запрос для получения расписания
    $.ajax({
        url: "print_schedule/",
        method: "GET",
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            print_schedule(data);
        }
    });

    // Функция для обработки расписания
    function print_schedule(data) {
        data.forEach(function(item) {
            var cellClass = item.cellName;
            var parentCell = item.group;
            var dataElementId = item.dataElementId;
            allDataElementIds.push(dataElementId); // Добавляем в массив

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
                            getCabinetInfo(dataElementId, cell);
                        }
                    })(cells[i]);
                }
            }
        });
    }

// Функция для выполнения AJAX-запроса и обработки информации о кабинете
function getCabinetInfo(dataElementId, cell) {
    $.ajax({
        url: "get_cabinet_info/",
        method: "GET",
        data: { dataElementId: dataElementId },
        dataType: 'json',
        success: function(cabinetInfo) {
            handleCabinetInfo(cabinetInfo, cell);
        },
        error: function(error) {
            console.error('Ошибка получения информации о кабинете:', error);
        }
    });
}

// Функция для обработки информации о кабинете
function handleCabinetInfo(cabinetInfo, cell) {
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
});
