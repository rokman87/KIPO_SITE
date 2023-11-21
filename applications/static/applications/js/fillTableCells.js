$(document).ready(function() {
    $.ajax({
        url: "loadData/",
        method: "GET",
        type: 'GET',
        dataType: 'json',
        success: function(data) {
            fillTableCells(data);
        }
    });
});
function fillTableCells(data) {
    data.forEach(function(item) {
        var cellClass = item.cellName;
        var parentCell = item.group;
        var cells = document.getElementsByClassName(cellClass);

        if (cells.length > 0) {
            for (var i = 0; i < cells.length; i++) {
//                 Обращаемся к родительскому элементу для каждой ячейки
                var parentText = cells[i].parentElement.textContent.trim();
//                var parentText = originalString.substring(0, originalString.indexOf('\n'));
//                console.log(cells[i]);
//                console.log("parentText = " + parentText);
//                console.log("parentCell = " + parentCell);
                if (cells[i].classList.value === cellClass && parentCell === parentText) {
                    cells[i].textContent = item.text;
                }
            }
        }
    });
}





