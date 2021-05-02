# pocketbook-623-annotations
## A simple script for importing annotation from PocketBook Touch2 623
This is an old script written in 2014 for `python-2.7`. 

###  PocketBook Touch2: export highlights
По просьбе жены сделал экспорт конспекта из электрокниги PocketBook Touch2.

Разработчики книги PocketBook Touch2 сделали некие «заметки» — возможность 
выделять куски текста, а потом смотреть их все в одном месте. 
Получается своеобразный (в худшем смысле слова) конспект книги. 
Но, к сожалению, разработчики поленились сделать экспорт этого конспекта из устройства. 
Впрочем, быстрое гугление показало, что это, видимо, и не такая уж востребованная функция. 
Тем не менее некоторым бывает нужно.

Итак, заметки в книге можно делать двух видов:
1) явно выделять кусок текста;
2) ставить закладку на страницу.
Во втором случае в «конспекте» отображается не весь текст, а только тот кусок, который находится вначале помеченной страницы. Из-за этой неоднозначности обрабатывать такие закладки я не стал.

В самом устройстве файлы «конспекта» лежат тут: 
`Pocket623/system/profiles/Username/config/Active Contents` 
в виде весьма кривого HTML-файла. 
(Наверняка это и есть основная причина того, что вменяемого экспорта до сих пор нет.) 
Логично пропарсить его при помощи `BeautifulSoup`. Пишем простенький код на питоне.

```python
#! encoding: utf8

from sys import argv
from bs4 import BeautifulSoup

inFile = argv[1]
outFile = inFile.replace('html', 'txt')
soup = BeautifulSoup(open(inFile),'html5')

with open(outFile, 'w') as f:
    for tag in soup.find_all('font'):
        if tag.div:
            f.write('\n')
        else:
            f.write(tag.string.encode('utf8'))
```

### Использование
После этого находим в папке, указанной выше, конспект нужной нам книги. Например, это foo.html.
И говорим:

```bash
python export.py foo.html
```
Результат будет записан в `foo.txt` в той же папке. 
Кривизна полученного файла в точности соответствует кривизне исходного. 
Например, если выделенный кусок в книге переходит на новую страницу, 
то и тут он окажется разбит на две части. Но это лучше, чем совсем ничего.

### Системные требования
Работает в python 2.7.x, в линуксе. 
В других версиях питона и ОС я не проверял, но по идее должно работать, если у вас системная кодировка — UTF8.
