# ВК бот с парсером расписания

- [x] Парсер (Готов. Переделать под функциональную парадигму)
- [ ] Ассинхронный парсер (В работе)
- [ ] ВК бот (Ожидание)

### Главная цель
Упростить доступ студентов к актуальному расписанию. Уменьшить случайные пропуски пар.

### Задачи для достижения главной цели
1. Разработать парсер расписания.
2. Разработать ВК бота.
3. (необязательно) Разработать телеграмм бота.

### Функциональные требования к парсеру

* Парсер должен уметь вытягивать все группы из документа, чтобы заполнять по ним расписание.
* Парсер должен уметь заполнять расписание по группам в формате:
`Группа: Тип недели: День недели`

### Функциональные требования к боту

* Бот должен уметь выводить расписание по запросу.

Запросы могут выглядеть следующим образом:
`[группа][тип недели][день недели]>`

* Бот должен уметь сравнивать новое и текущее расписание, чтобы проверять изменения. Если изменения есть, тогда запустить парсер и уведомить пользователей.
* Проверку на изменения можно запросить принудительно.
* Бот должен отсылать актуальное расписание на следующий день.

## Как запускать?

Управление приложением происходит через класс SPKRasp.
В main уже создан объект.

При инициализации объекта проверяется, есть ли расписание в каталоге. Если нет, вызовется метод **download_rasp**.
После проверки запускается парсер через метод **start_parser**.

**P.S. Расписание находится в каталоге assets/info**

Парсер должен вызываться лишь в двух случаях:
1. При инициализации объекта класса SPKRasp;
2. При изменениях в расписании.

Все методы нужно вызывать в main через SPKRasp, иначе парсер не будет иметь доступа к документу с расписанием (особенность относительных путей)

