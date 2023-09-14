document.addEventListener("DOMContentLoaded", function () {
    var selectButtons = document.querySelectorAll(".select-schedule");

    selectButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            var selectedElementId = button.getAttribute("data-element-id");

            // Сохраните выбранный ID в куки
            document.cookie = "selected_element_id=" + selectedElementId;
        });
    });
});