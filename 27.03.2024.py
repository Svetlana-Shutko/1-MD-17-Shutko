
def z1():
    spisok = (0, 1, 2, 3, 4)
    n = int(input("Введите число:"))
    if n in spisok:
        print("Поздравляю, вы угадали число!Ваше число:", n)
    else:
        print("Нет такого числа!")

def z2 ():
    spisok = []
    import random
    n = random.randint (2,10)
    while n > 0:
        znachenie = random.randint (2,20)
        n = n- 1
        spisok.append(znachenie)
    from collections import Counter
    c = Counter(spisok)
    print("Список чисел:", spisok, ", Повторяющиеся значения:", dict((x, spisok.count(x)) for x in set(spisok) if spisok.count(x) > 1))

def z3():
    n = int(input("Сколько выходных вы хотите?"))
    days = ("Понедельник","Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    vihod = days[-n:]
    work = days[:-n]
    print("Выходные дни:", ", ".join(vihod))
    print("Рабочие дни:", ", ".join(work))

def z4():
    my = ["Байрит", "Шутко", "Полонцкая", "Свистунов", "Шанина", "Степаненко", "Крылов","Черных", "Лесная"]
    dr = ["Агушев", "Баранов", "Волков", "Гардеев", "Данченко", "Ефимов", "Жорников", "Зорин", "Ильичев", "Йомаев", "Якуничев"]
    import random
    sport = tuple(random.sample(my,6) + random.sample(dr,6))
    print("Моя группа:",my)
    print ("Другая группа:", dr)
    print ("Спортивная команда:", sport)
    print("Длинна спортивной команды:", len(sport))
    sport2 = sorted(sport)
    print ("Отсортированная спортивная команда :", sport2)
    kolvo = sport2.count("Иванов")
    if kolvo > 0:
        print ("Количество участников с фамилией 'Иванов' :", kolvo)
    else:
        print("Участника с фамилией 'Иванов' нет")
z4()
