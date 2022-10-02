# Описание
Данная программа создана для тренировки памяти.

## Использование
Пользователь записывает вопросы,варианты и ответ в файл "questions.txt" 
после чего запускается программа командой
```
python3 main.py
```

После запуска появляется такое меню:
<center>
    <img src="https://cdn.discordapp.com/attachments/716063419299528777/1026115721735974922/unknown.png">
</center>

Нажимайте 1 и Enter. После чего будет показан 1 из n-ых вопросов, выбраных в случайном порядке, которых вы ранее записали в questions.txt с соответствующими вариантами ответов, которые так же перемешаны.
<center>
    <img src="https://cdn.discordapp.com/attachments/716063419299528777/1026115899926773861/unknown.png")
</center>

Если вы не знаете как это сделать,то просмотрите [ТУТ](#Запись).

После этого вам нужно выбрать 1 из вариантов ответов и написать его цифру.
В случае если вы ввели правильно или нет,то вам напишется об этом и предложиться продолжить либо повторить.

## Недоработки
В случае если введено мало вопросов, то 1 вопрос может очень часто повторяться.

## Запись в questions.txt
<a name="Запись"></a>
На данный момент не сделан редактор Editor.py для редактирования этого файла в более простом виде. Поэтому придётся вручную настраивать все вопросы через любой текстовый редактор.

После открытия файла,у вас должны быть записаны там уже 3 ранее заготовленных строки мною.
Запись в файл происходит в следующем порядке
```
"Вопрос" "Вариант1" "Вариант2" "Вариант3" "Вариант4" "Ответ"
```

При этом Ответ должен быть абсолютно таким же как и правильный вариант.
