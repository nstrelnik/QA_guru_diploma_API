# Пример проекта API автотестов

###  Используемые технологии
<p align="center">
  <code><img src="tests/images/logo/python.svg" width="40" height="40"  alt="A-d-am" title="Python"></code>
  <code><img src="tests/images/logo/pytest.png" width="40" height="40"  alt="A-d-am" title="PyTest"></code>
  <code><img src="tests/images/logo/requests.png" width="40" height="40"  alt="A-d-am" title="Requests"></code>
  <code><img src="tests/images/logo/selene.png" width="40" height="40"  alt="A-d-am" title="Selene"></code>
  <code><img src="tests/images/logo/pycharm.png" width="40" height="40"  alt="A-d-am" title="PyCharm"></code>
  <code><img src="tests/images/logo/Jenkins.svg" width="40" height="40"  alt="A-d-am" title="Jenkins"></code>
  <code><img src="tests/images/logo/Allure_new.png" width="40" height="40"  alt="A-d-am" title="Allure Report"></code>
  <code><img src="tests/images/logo/allure_testops.png" width="40" height="40"  alt="A-d-am" title="Allure TestOps"></code>
</p>

## Покрываемый функционал
- Проверка валидации полей при регистрации/авторизации
- Обработка запросов с невалидными данными
- Создание/удаление пользователей

## Запуск тестов
#### Все API тесты можно запустить как удалённо (Jenkins), так и локально

### Локально

Для запуска тестов локально, нужно выполнить следующие шаги
1. Склонировать репозиторий
2. Открыть проект в PyCharm
3. Ввести в териминале следующие команды
``` 
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
context=api pytest -m api  
```

### С помощью [Jenkins](https://jenkins.autotests.cloud/job/QA_guru_diploma_API/)
#### Для запуска автотестов необходимо:
 - Открыть [джобу](https://jenkins.autotests.cloud/job/QA_guru_diploma_API/) в jenkins
 - Нажать на Build
<img src="tests/images/screenshots/Jenkins_build.png">

## Отчет о прохождении тестов (Allure)

### Локально
Для получения отчета нужно:
 - Запустить тесты
 - Ввести команду 
```
allure serve allure-results
```
Ниже представлен пример allure отчета 
<img src="tests/images/screenshots/allure_report_example_api.png">

### Если тесты запускались в Jenkins

Для получения отчета нужно нажать на иконку allure report'a в строке билда 
<img src="tests/images/screenshots/jenkins_allure_report.jpg">
У него будет точно такой же формат, как и при получении локально
<img src="tests/images/screenshots/allure_report_example_api.png">

### В проекте реализована интеграция с Allure TestsOps
<img src="tests/images/screenshots/allure_test_ops.png">
