print("Введите слова:")
slovo = ""
stroka = ""
while slovo != "stop":
    slovo = input()
    stroka = stroka + slovo + " "
print(stroka[:-5])