const selectScheduleButtons = document.querySelectorAll(".select-schedule");

// Добавляем обработчик событий для каждой кнопки
selectScheduleButtons.forEach(function(button) {
  button.addEventListener("click", function(event) {
    event.preventDefault(); // Предотвращаем действие по умолчанию
    // Получаем значение атрибута "data-element-id" кнопки
    const elementId = button.getAttribute("data-element-id");
    console.log("Set Cookie: ", elementId);

    // Устанавливаем куки с использованием значения "el.id"
    document.cookie = `selectedElementId=${elementId}; path=/; max-age=3600;`

    // Выводим все куки в консоль
    console.log("All cookies:", document.cookie);
  });
});