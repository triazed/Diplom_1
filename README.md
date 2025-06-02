## Дипломный проект. Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `praktikum` - пакет, содержащий код программы
- `data` - пакет, содержащий тестовые данные
- `tests` - пакет, содержащий тесты, разделенные по классам:
-- test_bun.py - тесты класса Bun
-- test_burger.py - тесты класса Burger
-- test_database.py - тесты класса Database
-- test_ingredient.py - тесты класса Ingredient

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=bun --cov=burger --cov=ingredient --cov=database --cov-branch --cov-report=html`
