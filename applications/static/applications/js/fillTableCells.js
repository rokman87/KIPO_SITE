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
//        console.log("cellClass "+cellClass);
//        console.log("parentCell "+parentCell);
//        console.log(cells);
//        console.log(cells.length);
        if (cells.length > 0) {
            for (var i = 0; i < cells.length; i++) {
                var parentText = cells[i].parentElement.textContent.trim();
                var parts = parentText.split(/\s+/);
//                   console.log("parentText ="+parentText);
//                   console.log("parts[0] ="+parts[0]);
                if (cells[i].classList.value === cellClass && parentCell === parts[0]) {
//                 console.log("Вставляем текст");
                    cells[i].textContent = item.text;
                }
            }
        }
    });
}
