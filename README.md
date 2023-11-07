# Условия домашки

Популярность магазина значительно выросла. В связи с этим продакт-менеджер предложил добавить возможность пользователям
заполнять карточки продуктов и при этом расширить функционал веб-приложения.

Критерий выполнения заданий
Результат всего задания залейте в GitHub и сдайте в виде ссылки на репозиторий.

## Задание 1

Продолжаем работать с проектом из предыдущего домашнего задания. Для модели продуктов реализуйте механизм CRUD,
задействовав модуль

django.forms
.

Условия для пользователей:

могут создавать новые продукты;
не могут загружать запрещенные продукты на платформу.
Для исключения загрузки запрещенных продуктов реализуйте валидацию названия и описания продукта таким образом,
чтобы нельзя было в них добавлять слова: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.

## Задание 2

Добавьте новую модель «Версия», которая должна содержать следующие поля:

продукт,
номер версии,
название версии,
признак текущей версии.
При наличии активной версии реализуйте вывод в список продуктов информации об активной версии.

## Задание 3

Для работы с версиями продукта добавьте реализацию работы с формами. При этом версия может быть внесена только в
существующий продукт.