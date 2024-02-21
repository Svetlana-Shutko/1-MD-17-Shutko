g = int(input("Введите год"))
if ((g // 4) and not (g//100)) or (g // 400):
    print("год", g,"- високосный")
else:
    print("год", g, "- не високосный")