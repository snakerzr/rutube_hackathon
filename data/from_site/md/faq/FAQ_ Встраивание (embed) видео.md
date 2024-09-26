# Встраивание видео с RUTUBE

## Содержание

[Что такое встраивание (embed) видео?](https://rutube.ru/info/embed/#embed001)

[Как эмбедировать видео с RUTUBE?](https://rutube.ru/info/embed/#embed002)

[Дополнительные возможности](https://rutube.ru/info/embed/#embed003)

[Как встроить на сайт приватное видео, доступное только по прямой
ссылке?](https://rutube.ru/info/embed/#embed004)

[Расширенные параметры для встраивания видео с RUTUBE и управления
плеером](https://rutube.ru/info/embed/#embed005)

[Настройка воспроизведения](https://rutube.ru/info/embed/#embed006)

[Автоподстройка размера для нестандартных окон и мобильных
устройств](https://rutube.ru/info/embed/#embed007)

[Управление плеером](https://rutube.ru/info/embed/#embed008)

[События плеера и отслеживание статуса
проигрывания](https://rutube.ru/info/embed/#embed009)

## Что такое встраивание (embed) видео?

Эмбед или эмбедирование — функция, которая позволяет встраивать плеер RUTUBE с
конкретным видео на сторонние веб-страницы.

## Как эмбедировать видео с RUTUBE?

Чтобы встроить (эмбедировать) видео с RUTUBE на сторонний сайт, нужно добавить
код вставки плеера в код страницы, на которую хотите встроить плеер. Встроить
можно любое видео, которое не скрыто автором. Видео, доступное только по
прямой ссылке, тоже можно встроить — для этого понадобится доступ в студию
RUTUBE автора этого видео.

**Шаг 1**. Найдите нужное видео на сайте RUTUBE и нажмите «Поделиться» → «Код
вставки плеера»

**Шаг 2**. Скопируйте код. Чтобы это сделать, кликните на код или на кнопку
«Скопировать»

**Шаг 3**. Вставьте код вставки плеера в код страницы, на которую хотите
встроить видео

### Дополнительные возможности

Чтобы изменить размер окна плеера, цвет элементов управления, выбрать момент
начала и конца воспроизведения, показать название и автора видео, добавьте
дополнительные параметры в код вставки плеера с помощью настроек параметров.
Все изменения и дополнительные параметры отобразятся в коде для вставки,
поэтому копируйте его только после их добавления и настройки.



В расширенной форме можно настроить следующие параметры:

1\. **Изменение размера окна плеера** : замените размер в одном из полей в
блоке «Размеры, px» на нужный. Второе поле подстроится автоматически, чтобы
сохранить пропорции оригинального плеера.

2\. **Изменение цвета элементов плеера** : нажмите «Изменить» в блоке
«Основной цвет» и выберите нужный цвет из палитры.

3\. **Выбор моментов начала и конца воспроизведения** : поставьте галочку в
чекбоксе «Начало» и/или «Конец» добавьте таймкод нужного момента. Выбор часов
будет доступен, только если видео длится больше 59 минут 59 секунд. Если
указать значение 99 минут, то оно автоматически пересчитается в часы и остаток
в минутах. Аналогично пересчитываются секунды в минуты.

4\. **Отображение названия видео** : поставьте галочку в чекбоксе «Показывать
название видео». Отображение может не работать на платформах, на которых не
используется язык HTML.

5\. **Отображение автора видео** : можно добавить, только если включено
отображение названия видео. Чтобы включить отображение автора, поставьте
галочку в чекбоксе «Показывать автора канала». Отображение может не работать
на платформах, на которых не используется язык HTML.

### Настройки параметров в коде вставки

После вставки кода видео в код страницы в него можно вносить дополнительные
изменения параметров, меняя значения в коде вставки.

### Пример

Стандартный код вставки плеера без дополнительных настроек параметров для
встраивания видео из общего доступа по ссылке
https://rutube.ru/play/embed/7716bd3e665725c3c008ae7ab4ff02e2:

**< iframe width="720" height="405"
src="https://rutube.ru/play/embed/7716bd3e665725c3c008ae7ab4ff02e2"
frameBorder="0" allow="clipboard-write; autoplay" webkitAllowFullScreen
mozallowfullscreen allowFullScreen></iframe>**  



Код вставки этого же видео с дополнительными настройками параметров: размером
окна плеера 864х486 пикселей, с красным цветом интерфейса, началом
воспроизведения с 5й минуты и окончанием на отметке 8 минут с отображением
названия видео и имени автора канала.

**Код для вставки:**

**< iframe width="864" height="486"
src="https://rutube.ru/play/embed/7716bd3e665725c3c008ae7ab4ff02e2?skinColor=e53935&t=300&stopTime=480"
frameBorder="0" allow="clipboard-write; autoplay" webkitAllowFullScreen
mozallowfullscreen allowFullScreen></iframe>  <p><a
href="https://rutube.ru/video/7716bd3e665725c3c008ae7ab4ff02e2/">«Тотальный
футбол»: топовый дебют Миранчука, как поменять наш футбол – реформы
Гогниева</a> от <a href="//rutube.ru/metainfo/tv/23137/">Тотальный футбол</a>
на <a href="https://rutube.ru/">RUTUBE</a>**



Подробнее:

  * **width="864" height="486"  **— ширина и высота окна плеера,
  * **https://rutube.ru/play/embed/7716bd3e665725c3c008ae7ab4ff02e2  **— эмбедироваванная ссылка на видео,
  * **skinColor=e53935  **— основной цвет интерфейса (красный),
  * **t=300  **— время в секундах, с которого начнётся воспроизведение (300 секунд = 5 минут),
  * **stopTime=480  **— время в секундах, на котором воспроизведение завершится (480 секунд = 8 минут),
  * **frameborder  **— параметр, отвечающий за активацию рамки по периметру окна плеера. Может задаваться значением 1 (вкл) и 0 (выкл, по умолчанию),
  * **allow="clipboard-write; autoplay"  **— параметры управления буфером копирования и автоматическим запуском видео, если выполнены все условия для автоматического запуска. Внимание: при удалении параметра "clipboard-write" пропадет возможность копирования ссылки на видео из расширенного меню по правой кнопке мыши, а также из кнопки "Поделиться" (расположена в правом верхнем углу плеера),
  * **webkitAllowFullScreen mozallowfullscreen  **— фрагмент кода, который позволяет запускать плеер в полноэкранном режиме на устаревших версиях браузеров,
  * **allowFullScreen  **— фрагмент кода, отвечающий за активацию функции полноэкранного просмотра из эмбеда. Если его удалить из кода, то функция будет недоступна,
  * **< a href="https://rutube.ru/video/7716bd3e665725c3c008ae7ab4ff02e2/">«Тотальный футбол»: топовый дебют Миранчука, как поменять наш футбол – реформы Гогниева</a> **— фрагмент кода, который отвечает за отображение названия видео; содержит ссылку на встариваемое видео и его название,
  * **< a href="//rutube.ru/metainfo/tv/23137/">Тотальный футбол</a> **— фрагмент кода, который отвечает за отображение автора канала, с которого взято видео,
  * **< a href="https://rutube.ru/">RUTUBE</a> **— фрагмент кода, который отображает ссылку на видеохостинг и название RUTUBE. Добавляется при проставлении галочки «Показывать название видео».

## Как встроить на сайт приватное видео, доступное только по прямой ссылке?

Чтобы встроить видео, доступное только по прямой ссылке, понадобится ключ
доступа. Его можно скопировать из прямой ссылки на видео.

**Шаг 1**. Откройте видео с ограниченным доступом в Студии RUTUBE и скопируйте
его ссылку

Пример прямой ссылки на видео с его ID и **ключом доступа** :
https://rutube.ru/video/private/caafe83ff1c6ed38d394635b83ece578**/****?p=IBgzQQrKH4qB1bqm_91x7Q**



**Шаг 2**. Откройте видео по скопированной ссылке и нажмите «Поделиться» →
«Код для вставки»

Пример кода вставки с **ID видео** без ключа доступа:

<iframe width="720" height="405"
src="https://rutube.ru/play/embed/**caafe83ff1c6ed38d394635b83ece578** "
frameBorder="0" allow="clipboard-write; autoplay" webkitAllowFullScreen
mozallowfullscreen allowFullScreen></iframe>



**Шаг 3**. Скопируйте из ссылки в браузере ключ доступа — всё после последнего
«/» — и добавьте этот кусок в код вставки видео через слэш «/» сразу после ID
видео.

Все ключи видео начинаются с «/**?p=** »**.  **

Пример кода вставки с **ID видео**  и с **ключом доступа:**

<iframe width="720" height="405"
src="https://rutube.ru/play/embed/**caafe83ff1c6ed38d394635b83ece578**
/**?p=IBgzQQrKH4qB1bqm_91x7Q** " frameBorder="0" allow="clipboard-write;
autoplay" webkitAllowFullScreen mozallowfullscreen allowFullScreen></iframe>

Если добавить на страницу код вставки без ключа доступа, видео не будет
воспроизводиться.

 Если у вас возникли сложности, напишите нам на help@rutube.ru

## **Расширенные параметры для встраивания видео с RUTUBE и управления
плеером**

### Настройка воспроизведения

Чтобы встроить плеер RUTUBE на HTML-страницу, нужно добавить тэг iframe вида:

<iframe width="{width}" height="{height}"
src="https://rutube.ru/play/embed/{id_video_parаms}"  
  frameBorder="0" allow="clipboard-write; autoplay" webkitAllowFullScreen
mozallowfullscreen allowFullScreen>  
</iframe>  
---  
  
В нём:

**{width},  {height}** — ширина и высота встраиваемого плеера, которую можно
задать самостоятельно. Чтобы видео отображалось правильно, лучше сохранять
стандартные пропорции плеера.

**{id_video_params}**  — внутренний ID видео на RUTUBE, к которому добавляются
дополнительные параметры в формате:

**{id_video_params}** :
**{id_video}**[?**{параметр}**[&**{параметр}**[&**{параметр}**]]]  
---  
  
где **{параметр}** — один из трёх возможных параметров:

**t** — момент начала воспроизведения видео в секундах, например, "t=9876",

**skinColor** — цвет элементов управления плеера; задаётся 16-ричным кодом,
который содержит в себе информацию об интенсивности красного, зеленого и
синего цветов. Например, "skinColor=7cb342";

**getPlayOptions** — параметр, который вызывает событие
"player:playOptionsLoaded", см. раздел «Управление плеером». Параметр должен
сопровождаться перечнем атрибутов. Например, параметр
"getPlayOptions=pg_rating,is_adult,is_licensed,duration,title" вызывает
событие "player:playOptionsLoaded", параметр "data" которого содержит полную
информацию об атрибутах верхнего уровня
pg_rating,is_adult,is_licensed,duration,title.

**Обратите внимание:** в параметре можно указать только атрибуты верхнего
уровня. Если для работы страницы нужен вложенный атрибут, укажите его верхнего
«родителя».  
Полный перечень доступных атрибутов доступен по ссылке
[https://rutube.ru/api/play/options/{id_video}](https://rutube.ru/api/play/options/%7Bid_video%7D)



**Пример встраивания плеера RUTUBE с параметрами:**

<iframe **width** ="1066" **height** ="600" frameBorder="0" allow="clipboard-
write; autoplay"  
src="https://rutube.ru/play/embed/7716bd3e665725c3c008ae7ab4ff02e2**?getPlayOptions=pg_rating,is_adult
&skinColor=7cb342&t=6040**"  
  webkitAllowFullScreen mozallowfullscreen allowFullScreen>  
</iframe>  
---  
  
### Автоподстройка размера для нестандартных окон и мобильных устройств

Чтобы **размер окна плеера RUTUBE подстраивался под размер страницы** , тэг
iframe можно «обернуть» в тэг div так:

<div style="height:60vw; max-width: **{width}** px; max-height: **{height}**
px; min-height: 240px;">  
  <iframe width="100%" height="100%"
src="https://rutube.ru/play/embed/**{id_video_params}** "  
    frameBorder="0" allow="clipboard-write" webkitAllowFullScreen mozallowfullscreen allowFullScreen>  
  </iframe>  
</div>  
---  
  
**Обратите внимание:** в изменённом коде параметры **{width}  **и** {height}**
переехали из тэга iframe в тэг div.

**Пример встраивания плеера****RUTUBE****с параметрами и автоподстройкой
размера:**

<div style="height:60vw; max-width: 1066px; max-height: 600px; min-height:
240px;">  
  <iframe width="100%" height="100%"
src="https://rutube.ru/play/embed/7716bd3e665725c3c008ae7ab4ff02e2?t=6040"  
    frameBorder="0" allow="clipboard-write" webkitAllowFullScreen mozallowfullscreen allowFullScreen>  
  </iframe>  
</div>  
---  
  
**Пример поведения окна встроенного плеера  ****RUTUBE****  с автоподстройкой
размера и без неё:**



HTML-файл с кодом примера:

В примере видно, как работает автоподстройка размера видео. Чтобы проверить,
меняйте размер окна браузера во время воспроизведения видео.

## Управление плеером



Плеер может принимать и исполнять ряд команд. Команда передаётся плееру при
помощи механизма postMessage() из кода javascript:



<body>  
  <iframe id=**'my-player'**
src="https://rutube.ru/play/embed/**{id_video_params}** " {другие параметры}>  
  </iframe>  
</body>  
  
<script type="text/javascript">  
function doCommand() {  
  var player = document.getElementById('my-player');  
  player.contentWindow.postMessage(JSON.stringify(**{CommandJSON}**), '*');  
} ...  
</script>  
---  
  
, где

**'my-player'** — имя тэга <iframe>, содержащего плеер;  
**{id_video_params}** — внутренний ID видео на RUTUBE с дополнительными
параметрами;  
**{CommandJSON}** — команда и её параметры в формате JSON.

... - **вызовы части команд** , управляющих плеером с помощью CommandJSON (см.
ниже)

Стандартный формат команды CommandJSON:

doCommand(  
  {type:typeValue, data:dataValue}  
);  
---  
  
, где

**{type}** — тип команды;  
**{data}** — параметры команды в формате JSON.

### Примеры команд, управляющих плеером:

  * function do_pause() { doCommand( {type:'player:pause', data:{} } ); }
  * function do_changeVideo() { doCommand( {type:'player:changeVideo', data:{id:'aaf9fbe99fd8400d6096ef5cc1af404c'}} ); }
  * function do_setSkinColor() { doCommand( {type:'player:setSkinColor', data: color: Color value is invalid } ); }
  * function do_VolumeDown() { doCommand( {type:'player:setVolume', data: {change: -0.1} } ); }

### Параметры команд, управляющих плеером, передаваемые в doCommand:

// player:play Начать воспроизведение видео

{

    type: 'player:play',

    data: {}

}



// player:pause Поставить видео на паузу

{

    type: 'player:pause',

    data: {}

}



// player:stop Закончить цикл воспроизведения (сброс буфера видео и рекламы)

{

    type: 'player:stop',

    data: {}

}



//player:setCurrentTime Перейти к определённой секунде видео

{

    type: 'player:setCurrentTime',

    data: {

        time: 20

    }

}



// player:relativelySeek Перемотать видео на определённое количество секунд
вперёд или назад. time — количество секунд для перемотки,

// (знак минус «−») — перемотка назад,

// (знак плюс «+») — перемотка вперёд,

{

    type: 'player:relativelySeek',

    data: {

        time: +20

    }

}



// player:changeVideo Загрузить в плеер другое видео

{

    type: 'player:changeVideo',

    data: {

        id: 'xyz123' // id ролика

    }

}



// player:setSkinColor Изменить цветовую схему

{

    type: 'player:setSkinColor',

    data: {

        params: {

            color: '39a939' // цвет в RGB, HEX (без решётки «#»)

        }

    }

}



// player:mute Отключить звук

{

    type: 'player:mute',

    data: {}

}



// player:unMute — Включить звук

{

    type: 'player:unMute',

    data: {}

}



// player:setVolume — Установить уровень громкости

{

    type: 'player:setVolume',

    data: {

            volume: 0.20 //значение от 0 до 1

          }

}

// Или изменить уровень громкости

// (знак минус «−») — тише,

// (знак плюс «+») — громче,

{

    type: 'player:setVolume',

    data: {

            change: 0.20 //значение от 0 до 1

          }

}

**Пример управления плеером на странице:**

HTML-файл с кодом примера управления плеером:
[Example02_Player_postMessage.html](https://nc.ruform.ru/index.php/s/DWk6kffeCJzwGiT/download/Example02_Player_postMessage.html)

## События плеера и отслеживание статуса проигрывания

### **Пример подписки на сообщения от плеера:**

window.addEventListener('message', function (event) {

    var message = JSON.parse(event.data);

    console.log(message.type); // some type

    switch (message.type) {

        case 'player:changeState':

            console.log(message.data.state); // Текущее состояние плеера

            break;

    };

});

**Шаблон приходящих сообщений:**

{

    "type": 'player:type',

    "data": 'some data'



}

### События плеера

**Перечень типов сообщений "type" и структура значений параметра "data"**  

player:ready // Плеер загружен готов к воспроизведению. Отправляется один раз,
при вставке плеера на страницу.

data: {

"clientId":<strAlphanumeric>,

"videoId":<strAlphanumeric>,

  "playerId":<strAlphanumeric>

}



player:changeState // Изменилось состояние проигрывания

data: {

"state":<strAlpha>,// Значения:

  // playing — началось воспроизведение видео,

  // paused — видео на паузе,

  // stopped — конец воспроизведения видео,

// lockScreenOn — появление заглушки в плеере,

// lockScreenOff — заглушка исчезла.

"isLicensed":<boolean>,

  "playerId":<strAlphanumeric>

}



player:rollState // Информация о факте и статусе проигрывания рекламы в плеере

data: {

"type":<strAlphanumeric>,

"state":<strAlpha>,// Ожидаемые значения:

  // play — воспроизведение рекламы,

// complete — завершилось воспроизведения рекламы/ошибка/нет рекламы.

  "playerId":<strAlphanumeric>

}



player:durationChange // Обновление/уточнение длительности видео

data: {

"duration":<Number>,// Длительность видео в секундах

  "playerId":<strAlphanumeric>

}



player:currentTime // Информация о текущем моменте воспроизведения видео

data: {

"time":<Number>,// Текущий момент воспроизведения видео в секундах

"playerId":<strAlphanumeric>

}  



player:buffering

data: {

    "range": [

{

"start":0,

"end":0

},

{

"start":<Number>,

"end":<Number>

}

],

"playerId":<strAlphanumeric>

}



player:volumeChange // Информация о смене уровня громкости

data: {

"volume":<strNumeric>,// Текущий уровень громкости от 0 до 1

"muted":<boolean>,

"playerId":<strAlphanumeric>

}



player:changeFullscreen // Переход/выход из полноэкранного режима

data: {

"isFullscreen":<boolean>,

    "playerId":<strAlphanumeric>

}



player:error // Ошибка во время проигрывания

data: {

"code": <strNumeric>,

"text": <strAlphanumeric>,

"playerId":<strAlphanumeric>

}



player:playComplete // Окончание воспроизведения видео и рекламы. Переход
плеера на финальный экран

data: {

"playerId":<strAlphanumeric>

}



player:currentQuality // Текущее качество видео

data: {

"quality":{

"height":<Number>

},

"playerId":<strAlphanumeric>

}



player:qualityList // Текущее качество видео

data: {

"list":[<Number>,...,<Number>]// Перечень значений качества, доступных для
этого видео, например [232,360,480,720,1080]

"playerId":<strAlphanumeric>

}



player:playOptionsLoaded

data: {

<attributes>

"playerId":<strAlphanumeric>

}

      

, где

<strAlphanumeric> — текстовая строка в кавычках;

<strNumeric> — последовательность цифр / число в кавычках;

<Number> — число;

<boolean> — логическое значение **true** или **false** ;



<attributes> — атрибуты видео, доступные также по
"https://rutube.ru/api/play/options/{id_video}", но только те, которые
перечислены в параметре getPlayOptions, см. «Настройка воспроизведения
встроенного видео». Атрибуты также частично описаны в следующем разделе
«Получение атрибутов видео».

**Пример кода, управляющего плеером, с учётом его статуса:**

HTML-файл с кодом:
[Example03_Player_events.html](https://nc.ruform.ru/index.php/s/sz2KKQ8W5QiWb74/download/Example03_Player_events.html)



В примере:

  * видео начинает воспроизводиться с 100-й секунды,
  * по достижении 4-х минут воспроизведение продолжается с начала 2-й минуты и далее по циклу,
  * если принудительно перемотать проигрывание дальше 4:10, видео продолжает воспроизводиться до конца,
  * по достижении конца видео проигрывание переходит к началу 2-й минуты и приостанавливается,
  * под видео отображается информация, полученная из события "playOptionsLoaded".
