# Документация пользователя
## Древо файлов:
- Исходный код интерфейса (dev_wgui/)
- Скомпилированный GUI (wgui/)
- Файл для сборки EXE (build.bat)
- Исходный текст (main.py, pairs.py, template.py, example.py, config.py)
- Файл собрки (main.spec)
- Ярлык для запуска (main.lnk)

## Сборка интерфейса
Установить Node.JS, NPM, а через него - Yarn:
```bash
npm i -g yarn
```
Далее открываем терминал в папке dev_wgui. Для загрузки модулей прописываем:
```bash
yarn
```
Для сборки Release прописываем:
```bash
yarn build
```
Для сборки Debug (не будет backend, но можно редактировать код GUI в реальном времени) прописываем:
```bash
yarn serve
```

## Сборка EXE
Устанавливаем Python 3.9, библиотеки:
```bash
pip install eel requests pyinstaller
```
Запускаем **build.bat** из терминала(cmd), иначе закроется.

## Руководство пользователя
Выбор режима: 
* тренировочный, 
* контрольный (для контрольного требуется ввести имя, фамилию и класс). 

Перед вами случайно сгенерированный пример, ваша задача решить его и последующие, пока не закончатся примеры или время. Вводим ответ в поле для ответа и нажимаем далее. В тренировочном режиме есть возможность подсмотреть ответ. В конце можно посмотреть ваш результат.

### Интерфейс состоит из:
* Начального экрана с названием программы и перечнем ее синтаксиса
* Выбора режима тестирования
* Поле для ввода данных пользователя
* Во время выполнения задания пользователю показывает время и кол-во выполненных заданий
* Отображение результата, правильных ответов и времени прошедшего с начала тестирования

### Как работает программа:
Программа состоит из двух частей: 
* frontend (Vue.js=html) 
* backend (Python) 

Связаны эти две вещи посредством EEL. То есть, сам интерфейс является обычным сайтом, за тем исключением, что может вызывать функции из Python, что он и делает. Пользователь вводит регистрационные данные, выбирает режим тестирования. В этот момент интерфейс вызывает с данными параметрами серверную функцию GenTest, которая возвращает тест с ответами или без, в зависимости от режима. Далее пользователь заполняет массив с ответами и отправляет его на сервер, вызывая функцию Judge, которая выдает ему результаты тестирования и оценку. Если режим был контрольным, то результаты отправляются на сервер.
