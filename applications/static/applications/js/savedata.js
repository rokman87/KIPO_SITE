// Функция для отправки данных на сервер
function sendDataToServer(data, color, container) {
console.log('sendDataToServer вызвана');
  const formData = new FormData();
  formData.append('block_text', data);
  formData.append('target_container', container);
  formData.append('color', color);

  // Получение CSRF-токена из мета-тега в HTML-документе
  const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
  formData.append('csrfmiddlewaretoken', csrfToken); // Добавление CSRF-токена в FormData
  fetch('/applications/record_block_move/', {
    method: 'POST',
    body: formData
  })
  .then(response => {
    if (response.ok) {
      // Если статус ответа равен 200 (OK), это считается успешным запросом
      console.log('Данные успешно отправлены на сервер.');
    } else {
      // В противном случае, можно получить код статуса и сообщение статуса
      console.error('Произошла ошибка при отправке данных на сервер. Код статуса:', response.status, 'Сообщение статуса:', response.statusText);
    }
  })
  .catch(error => {
    console.error('Произошла ошибка при отправке данных на сервер:', error);
  });
 }