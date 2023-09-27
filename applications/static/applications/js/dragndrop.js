function drag(event) {
    console.log("[drag event]");
    var draggableElement = event.target;

    var draggableContainer = draggableElement.closest(".element");
    var draggableContentElement = draggableContainer.querySelector('.draggable');
    var data = draggableContentElement.getAttribute("data");

    draggableContainer.id = "draggable-container";
    event.dataTransfer.setData("container-id", draggableContainer.id);
    event.dataTransfer.setData("element-id", data);

    var draggableContent = draggableContentElement.textContent;
    console.log("draggableContent = " + draggableContent);

    event.dataTransfer.setData("text/plain", draggableContent);

    var bgColor = window.getComputedStyle(draggableContentElement).getPropertyValue("background-color");
    event.dataTransfer.setData("color", bgColor);

    pChange(draggableContainer);
}

function pChange(draggableContainer) {
    // Получаем элемент <p> и его текстовое содержимое
    var pElement = draggableContainer.querySelector('p');
    var pContent = parseInt(pElement.textContent, 10);
    // Вычитаем единицу и обновляем текстовое содержимое элемента <p>
    pContent -= 1;
    pElement.textContent = pContent;
}

function allowDrop(event) {
    event.preventDefault();
}

function drop(event) {
    console.log("[drop event]");
    event.preventDefault();

    var data = event.dataTransfer.getData("text/plain");
    var color = event.dataTransfer.getData("color");
    var elementId = event.dataTransfer.getData("element-id");
    var containerId = event.dataTransfer.getData("container-id");

    var target = event.target;

    // Ищем элемент с классом cell
    while (target.className.indexOf("cell") === -1) {
        target = target.parentNode;
    }

    var targetClass = target.getAttribute("class");
    console.log("targetClass = " + targetClass);

    var container = event.currentTarget;
    var containerClass = container.getAttribute("class");

    var captionValue = target.parentNode.querySelector('.caption').textContent;
    console.log("captionValue = " + captionValue);

    target.textContent = data; // Устанавливаем текстовый контент
    target.style.backgroundColor = color; // Устанавливаем фоновый цвет
    target.dataset.id = elementId; // Устанавливаем значение атрибута data-id
    console.log("elementId = " + elementId);

    // Установим значение data в div с классом "cell"
    target.dataset.elementData = data;

}
