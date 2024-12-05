Практическая работа 2

 Необходимо, совместно с одногруппниками, разработать приложение «калькулятор»,
 фиксируя изменения каждой реализованной функции в системе контроля версий GIT,
 и заливая изменения на единый сервер.
 При загрузке изменений необходимо выполнятьоперации слияния различных веток (Marge)
 и разрешение конфликтных ситуаций.
 Приложение «калькулятор» представляет собой набор кнопок, которые выполняют соответствующие операции:

 1. Операции сложения
 2. Операция вычитания
 3. Операция умножения
 4. Операция деления
 5. Операция остаток от деления
 6. Sin
 7. Cos
 8. Возведение в степень
 9. Квадратный корень от числа
 10. Округление в меньшую сторону (floor)
 11. Округление в большую сторону (ceil)
 12. Работа с памятью (функции m+ mc итд)
 13. Построение графиков функции
 Данные операции  и прочий функционал приложения «калькулятор»(например ввод значений, интерфейс приложения) распределяются между студентами группы.

## Структура приложения:

task2/  
├── main.py — основной файл, запускающий приложение  
├── super_calc.py — основной функционал калькулятора  
├── gui.py — графический интерфейс приложения  
├── graphics.py — отвечает за функционал по графикам  
├── requirements.txt — все библиотеки проекта (чтобы их установить: pip install -r requirements.txt)  
├── .gitignore — для тех данных, которые не будете использовать  
└── README.md — основная информация о проекте  

## Распределение обязанностей:

- **Галя** —  1-4 пункты
- **Настя** —  
- **Полина** —  