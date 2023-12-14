$(document).ready(function() {
    $.ajax({
        url: "print_schedule/",
        method: "GET",
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            print_schedule(data);
        }
    });
});

function print_schedule(data) {
    data.forEach(function(item) {
        var cellClass = item.cellName;
        var parentCell = item.group;
        var dataElementId = item.dataElementId;
        var cells = document.getElementsByClassName(cellClass);
        if (cells.length > 0) {
            for (var i = 0; i < cells.length; i++) {
                (function(cell) { // Создаем замыкание для сохранения текущей ячейки
                    var parentText = cell.parentElement.textContent.trim();
                    var parts = parentText.split(/\s+/);
                    if (cell.classList.value === cellClass && parentCell === parts[0]) {
                        cell.dataset.id = dataElementId;
                        cell.textContent = item.text;

                        // AJAX-запрос для получения информации о кабинете по dataElementId
                        $.ajax({
                            url: "get_cabinet_info/",
                            method: "GET",
                            data: { dataElementId: dataElementId },
                            dataType: 'json',
                            success: function (cabinetInfo) {
                                console.log("Второй ajax");
                                console.log(cabinetInfo.title);
                                console.log(cabinetInfo.building);
                                var title = cabinetInfo.title;
                                var building = cabinetInfo.building;
                                console.log( building+ ', ауд. ' + title);
                                cell.textContent += building+ ', ауд. ' + title;
                            }
                        });
                    }
                })(cells[i]); // Передаем cells[i] в функцию-замыкание
            }
        }
    });
}
