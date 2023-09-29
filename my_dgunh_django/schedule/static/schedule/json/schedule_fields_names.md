# Названия полей при обращении к JSON файлу расписания
Общий вид
```schedule[week][day of the week][events][...]```

```[...]``` включает в себя обращение к полям events.

## week
Тип поля week – ```int```.
Если мы хотим обратиться к первой или второй неделе мы должны прописать 
```schedule[0][...]``` или ```schedule[1][...]``` соответственно.

## day of the week
Если мы хотим достать данные по какому-либо дню недели, логика следующая
допустим у нас есть массив ```daysoftheweek = ['Monday', 'Tuesday', ... , 'Saturday']```,
тогда при обращении ```schedule[0][daysoftheweek[0-6]]```, получаем список event'ов.

## events
При обращении к какому-либо дню недели возвращается список мероприятий
со следующими полями:
```json
{
    "num": "1",
    "title": "Mathematics",
    "type": "Lecture",
    "presenter": "Magomedov M.A",
    "place": "3/11",
    "links": {
      "useful_links": "",
      "task": "",
      "conference": ""
    }
}
```

### Разбор полей Event'ов