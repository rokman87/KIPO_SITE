function drag(event) {
    console.log("[drag event]");
    var draggableElement = event.target;

    // Ищем блок с классом 'draggable' внутри перетаскиваемого элемента и получаем его текстовое содержимое
    var draggableContainer = draggableElement.closest(".element");
    var draggableContentElement = draggableContainer.querySelector('.draggable');

    if (draggableContentElement) {
        var draggableContent = draggableContentElement.textContent;
        console.log("draggableContent = " + draggableContent);

        // Если вы хотите продолжить перетаскивание и использовать этот текст:
        event.dataTransfer.setData("text/plain", draggableContent);

        // Для сохранения цвета фона перетаскиваемого элемента используйте следующий код:
        var bgColor = window.getComputedStyle(draggableContentElement).getPropertyValue("background-color");
        event.dataTransfer.setData("color", bgColor);
    } else {
        console.error("Ошибка: не найден элемент с классом 'draggable' внутри перетаскиваемого элемента.");
    }
}


function allowDrop(event) {
    event.preventDefault();
}

function drop(event) {
  console.log("[drop event]");
  event.preventDefault();

  // Получаем данные из объекта перетаскивания
  var data = event.dataTransfer.getData("text");
  var color = event.dataTransfer.getData("color");
  var target = event.target;

  // Находим целевой элемент, который содержит перетаскиваемый элемент
  while (target.className.indexOf("cell") === -1) {
    target = target.parentNode;
  }
  var targetClass = target.getAttribute("class");
  console.log("targetClass = " + targetClass);

  // Получаем класс целевого контейнера-урока
  var container = event.currentTarget;
  var containerClass = container.getAttribute("class");

  // Получаем значение блока с классом 'caption', находящимся в одном родительском элементе с целевым элементом
  var captionValue = target.parentNode.querySelector('.caption').textContent;
  console.log("captionValue = " + captionValue);

  // Изменяем текст целевого элемента и его фоновый цвет на значения, полученные из перетаскиваемого элемента
  target.textContent = data;
  target.style.backgroundColor = color;

}
