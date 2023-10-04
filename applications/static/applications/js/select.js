// Находим все кнопки с классом "select-schedule"
const selectScheduleButtons = document.querySelectorAll(".select-schedule");

// Добавляем обработчик событий для каждой кнопки
selectScheduleButtons.forEach(function(button) {
  button.addEventListener("click", function(event) {
    event.preventDefault(); // Предотвращаем действие по умолчанию
    // Получаем значение атрибута "data-element-id" кнопки
    const elementId = button.getAttribute("data-element-id");
    console.log("cookies: " + elementId);
    // Устанавливаем куки с использованием значения "el.id" и указываем домен
    document.cookie = `selectedElementId=${elementId}; domain=localhost; path=/`;
  });
});