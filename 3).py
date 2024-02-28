slovo = input("Введите слово:")
flag = 0
for bukva in slovo:
    if bukva == "ф":
        flag += 1
if flag > 0:
    print("Ого! Это редкое слово!")
else:
    print("Эх, это не очень редкое слово...")