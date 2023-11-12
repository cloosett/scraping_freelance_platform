# scraping_freelance_platform
Цей скрипт на Python розроблено для використання як бот Telegram, який парсить оголошення з платформи Freelance.ua. Для інтеграції з Telegram використовується бібліотека Telebot, а для парсингу - BeautifulSoup. Нижче ви знайдете огляд структури коду та його функціональності.

                                       Залежності
Переконайтеся, що встановлені необхідні залежності. Ви можете встановити їх за допомогою наступної команди:
pip install telebot requests beautifulsoup4

                                       Налаштування
Перед запуском скрипту потрібно отримати токен бота Telegram від BotFather на Telegram (https://core.telegram.org/bots#botfather). Замініть заповнювач TOKEN на свій реальний токен у скрипті.

                                       Використання
Запустіть бота, виконавши скрипт.
Бот відповість на команду /start та надасть набір опцій.

                                      Доступні Команди
/start -> Запускає бота та надає набір опцій.
"Scraping programming order👨🏽‍💻" -> Запускає процес парсингу програмістських замовлень з Freelance.ua.
"Scraping full order😳" -> Парсить всі замовлення
"Enter the number of pages to be scraping👇" -> Дозволяє користувачу вказати кількість сторінок для парсингу.
"Scraping all order👁👁" -> Запускає процес парсингу всіх замовлень з Freelance.ua.
"Enter the number of pages to be scraping👇" -> Дозволяє користувачу вказати кількість сторінок для парсингу.
"Message, if new task😉" -> Моніторить Freelance.ua на наявність нових завдань та відсилає повідомлення при виявленні нового завдання.
                                      Доповнення
Також є файл "runbot.bat", якщо у вас немає сервера, цей файл запускається у фоновому режимі на комп'ютері.
