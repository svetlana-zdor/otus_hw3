Напиши готовый к запуску Python-скрипт с автотестами на базе pytest и requests для REST API.

Базовый URL сервиса: https://jsonplaceholder.typicode.com

Реализуй 3 теста:
1. `test_get_single_post`:
   - Отправь GET-запрос на `/posts/1`.
   - Проверь HTTP-статус 200.
   - Проверь контракт: наличие полей 'userId', 'id', 'title', 'body' и соответствие их типов (int, int, str, str).

2. `test_create_post`:
   - Отправь POST-запрос на `/posts` с JSON: {"title": "foo", "body": "bar", "userId": 1}.
   - Проверь HTTP-статус 201.
   - Проверь, что в ответе присутствуют отправленные данные и ключ 'id'.

3. `test_get_nonexistent_post`:
   - Отправь GET-запрос на несуществующий эндпоинт `/posts/999999`.
   - Проверь HTTP-статус 404.

Требования к ответу:
- Верни ТОЛЬКО валидный код Python.
- Не добавляй текстовые пояснения, вступления или заключения.
- Импортируй библиотеки pytest и requests.