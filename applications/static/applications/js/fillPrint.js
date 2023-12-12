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
                var parentText = cells[i].parentElement.textContent.trim();
                var parts = parentText.split(/\s+/);
                if (cells[i].classList.value === cellClass && parentCell === parts[0]) {
                    cells[i].dataset.id = dataElementId;
                    cells[i].textContent = item.text;

                    // AJAX-запрос для получения информации о кабинете по dataElementId
                    $.ajax({
                        url: "get_cabinet_info/", // Укажите URL для получения информации о кабинете
                        method: "GET",
                        data: {dataElementId: dataElementId},
                        dataType: 'json',
                        success: function(cabinetData) {
                            // Вставка информации о кабинете в ячейку расписания
                            console.log("Второй ajax");
                            console.log(cabinetInfo.title); // Выводит значение ключа 'title' из словаря
                            console.log(cabinetInfo.building);
                            var title = cabinetInfo.title;
                            var building = cabinetInfo.building;
                            console.log(title + ' в здании ' + building);
//                          cells[i].textContent += title + ' в здании ' + building;
                        }
                    });
                }
            }
        }
    });
}