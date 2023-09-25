// Функция для начала перетаскивания

    function drag(event) {
      var draggableElement = event.target;
      event.dataTransfer.setData("text", draggableElement.textContent);
      event.dataTransfer.setData("color", window.getComputedStyle(draggableElement).backgroundColor);
    }

    // Функция для разрешения перетаскивания внутрь контейнера
    function allowDrop(event) {
      event.preventDefault();

    }

    // Функция для завершения перетаскивания
    function drop(event) {
      event.preventDefault();
      var data = event.dataTransfer.getData("text"); // Получаем текст перетаскиваемого элемента
      var color = event.dataTransfer.getData("color"); // Получаем цвет фона перетаскиваемого элемента
      var container = event.target; // Находим целевой контейнер

      container.innerHTML = data; // Заполняем контейнер текстом из перетаскиваемого элемента
      container.style.backgroundColor = color; // Устанавливаем цвет фона контейнера таким же, как у перетаскиваемого элемента
    }