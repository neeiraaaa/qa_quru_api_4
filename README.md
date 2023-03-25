## Проект API автотестов reqres.in

<!-- Технологии -->

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="./tests/resources/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="./tests/resources/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="./tests/resources/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="./tests/resources/logo/selene.png"></code>
  <code><img width="5%" title="GitHub" src="./tests/resources/logo/github.png"></code>
  <code><img width="5%" title="Allure Report" src="./tests/resources/logo/allure_report.png"></code>
  <code><img width="5%" title="Jenkins" src="./tests/resources/logo/jenkins.png"></code>
  <code><img width="5%" title="Requests" src="./tests/resources/logo/requests.png"></code>
</p>

### Что выполняет тест:
![This is an image](tests/resources/screenshots/test.png)


## :computer: Запуск тестов из терминала
```bash
pytest tests/test_reqres.py --env=prod
```

В проекте используется встроенный logger - logging:
![This is an image](tests/resources/screenshots/logger.png)

<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="tests/resources/logo/jenkins.png"> Запуск проекта в Jenkins

### [Job](https://jenkins.autotests.cloud/job/test_reqres/)

##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение
![This is an image](tests/resources/screenshots/jenkins1.png)

<!-- Allure report -->

### <img width="3%" title="Allure Report" src="tests/resources/logo/allure_report.png"> Allure report

##### После прохождения тестов, результаты автоматически сохраняются. Чтобы посмотреть Allure отчет нужно нажать на иконке allure report у сборки.
![This is an image](tests/resources/screenshots/allure.png)

##### Во вкладке Suites находятся подробные данные о прохождении теста с приложенными логами
![This is an image](tests/resources/screenshots/allure_suites.png)
