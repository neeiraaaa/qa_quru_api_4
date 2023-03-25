## Проект UI автотестов demoqa.com

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
  <code><img width="5%" title="Selenoid" src="./tests/resources/logo/selenoid.png"></code>
</p>

### Что выполняет тест:
- [x] Заполняет данные формы
- [x] Отправляет заполненные данные
- [x] Проверяет правильность заполненных данных

<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="tests/resources/logo/jenkins.png"> Запуск проекта в Jenkins

### [Job](https://jenkins.autotests.cloud/job/qa_quru_jenkins/)

##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение, через виртуальную машину при помощи Selenoid.
![This is an image](tests/resources/screenshots/jenkins1.png)

<!-- Allure report -->

### <img width="3%" title="Allure Report" src="tests/resources/logo/allure_report.png"> Allure report

##### После прохождения тестов, результаты автоматически сохраняются. Чтобы посмотреть Allure отчет нужно нажать на иконке allure report у сборки.
![This is an image](tests/resources/screenshots/allure.png)

##### Во вкладке Suites находятся подробные данные о прохождении теста с приложенными логами, скриншотами и видео о прохождении теста
![This is an image](tests/resources/screenshots/allure_suites.png)

##### Видео прохождение теста
![This is an image](tests/resources/video/tests_ui.gif)