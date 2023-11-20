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

        var cells = document.getElementsByClassName(cellClass);

        if (cells.length > 0) {
            for (var i = 0; i < cells.length; i++) {
                if (cells[i].classList.value === cellClass) {
                    cells[i].textContent = item.text;
                }
            }
        }
    });
}





