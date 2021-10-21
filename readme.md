---
created: 2021-10-21T16:14:57 (UTC +03:00)
source: https://parceljs.org/getting-started/webapp/
author: Ivan Yastrebov
---

---
## Установка

[#](https://parceljs.org/getting-started/webapp/#installation)

Прежде чем мы начнем, вам нужно будет установить Node и Yarn или npm, а также создать каталог для вашего проекта. Затем установите посылку в свое приложение с помощью Yarn:

```
yarn add --dev parcel
```

Или при использовании npm запустите:

```
npm install --save-dev parcel
```

## Настройка проекта

[#](https://parceljs.org/getting-started/webapp/#project-setup)

Теперь, когда посылка установлена, давайте создадим несколько исходных файлов для нашего приложения. Посылка принимает любой тип файла в качестве точки входа, но HTML-файл-хорошее место для начала. Посылка будет следовать всем вашим зависимостям оттуда, чтобы создать ваше приложение.

_src/index.html:_

```
<!doctype html><html lang="en">  <head>    <meta charset="utf-8"/>    <title>My First Parcel App</title>  </head>  <body>    <h1>Hello, World!</h1>  </body></html>
```

В Parcel встроен сервер разработки, который автоматически перестраивает ваше приложение по мере внесения изменений. Чтобы запустить его, запустите интерфейс `parcel`командной строки, указывающий на ваш файл ввода:

```
yarn parcel src/index.html
```

Теперь откройте [http://localhost:1234/](http://localhost:1234/) в вашем браузере, чтобы увидеть HTML - файл, созданный вами выше.

Затем вы можете начать добавлять зависимости в свой HTML-файл, такой как файл JavaScript или CSS. Например, вы можете создать `styles.css`файл и ссылаться на него из своего `index.html`файла с `<link>`помощью тега, а `app.js`также файла, на который ссылается `<script>`тег.

_src/стили.css:_

```
h1 {  color: hotpink;  font-family: cursive;}
```

_src/app.js:_

```
console.log('Hello world!');
```

_src/index.html:_

```
<!doctype html><html lang="en">  <head>    <meta charset="utf-8"/>    <title>My First Parcel App</title>    <link rel="stylesheet" href="styles.css" />    <script type="module" src="app.js"></script>  </head>  <body>    <h1>Hello, World!</h1>  </body></html>
```

По мере внесения изменений вы должны видеть, как ваше приложение автоматически обновляется в браузере, даже не обновляя страницу!

В этом примере мы показали, как использовать ванильный HTML, CSS и JavaScript, но Parcel также работает со многими распространенными веб-фреймворками и языками, такими как [React](https://parceljs.org/recipes/react/) и [TypeScript](https://parceljs.org/languages/typescript/) из коробки. Ознакомьтесь с разделами "Рецепты и языки" в документах, чтобы узнать больше.

## Сценарии пакетов

[#](https://parceljs.org/getting-started/webapp/#package-scripts)

До сих пор мы запускали `parcel`CLI напрямую, но может быть полезно создать некоторые сценарии в вашем `package.json`файле, чтобы упростить это. Мы также настроим сценарий для создания вашего приложения для [работы](https://parceljs.org/features/production/) с помощью этой `parcel build`команды. Наконец, вы также можете объявить свои [записи](https://parceljs.org/features/targets/#entries) в одном месте с помощью `source`поля, чтобы вам не нужно было дублировать их в каждой `parcel`команде.

_пакет.json:_

```
{  "name": "my-project",  "source": "src/index.html",  "scripts": {    "start": "parcel",    "build": "parcel build"  },  "devDependencies": {    "parcel": "latest"  }}
```

Теперь вы можете запустить`yarn build`, чтобы создать свой проект для производства и `yarn start`запустить сервер разработки.

## Объявление целевых объектов браузера

[#](https://parceljs.org/getting-started/webapp/#declaring-browser-targets)

По умолчанию посылка не выполняет никакой транспиляции кода. Это означает, что если вы напишете свой код с использованием функций современного языка, то именно это и будет выводить Parcel. Вы можете указать поддерживаемые браузеры вашего приложения, используя это `browserslist`поле. Когда это поле будет объявлено, Parcel соответствующим образом перенесет ваш код, чтобы обеспечить совместимость с поддерживаемыми браузерами.

_пакет.json:_

```
{  "name": "my-project",  "source": "src/index.html",  "browserslist": "> 0.5%, last 2 versions, not dead",  "scripts": {    "start": "parcel",    "build": "parcel build"  },  "devDependencies": {    "parcel": "latest"  }}
```

Вы можете узнать больше о целевых объектах, а также об автоматической поддержке дифференцированной комплектации посылок на странице [Целевые](https://parceljs.org/features/targets/) объекты.

## Следующие шаги

[#](https://parceljs.org/getting-started/webapp/#next-steps)

Теперь, когда вы настроили свой проект, вы готовы узнать о некоторых более продвинутых функциях Parcel. Ознакомьтесь с документацией о [разработке](https://parceljs.org/features/development/) и [производстве](https://parceljs.org/features/production/), а также с разделами "Рецепты и языки" для получения более подробных руководств по использованию популярных веб-фреймворков и инструментов.
###### tags: []