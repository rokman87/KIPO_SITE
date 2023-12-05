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
        var dataElementId = item.dataElementId;
        var cells = document.getElementsByClassName(cellClass);
        if (cells.length > 0) {
            for (var i = 0; i < cells.length; i++) {
                var parentText = cells[i].parentElement.textContent.trim();
                var parts = parentText.split(/\s+/);
                if (cells[i].classList.value === cellClass && parentCell === parts[0]) {
                    cells[i].dataset.id = dataElementId;
                    cells[i].textContent = item.text;
                }
            }
        }
    });
}
