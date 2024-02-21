nomer = int(input("введите номер места"))
if (nomer % 2 == 0) and (nomer >= 37) and (nomer <= 54):
    print(nomer, "- верхнее боковое место ")
elif (nomer % 2 != 0) and (nomer >= 37) and (nomer <= 54):
    print(nomer, "- нижнее боковое место ")
if (nomer % 2 == 0) and (nomer <= 37) and (nomer >= 54):
    print(nomer, "- верхнее место в купе")
elif (nomer % 2 != 0) and (nomer <= 37) and (nomer >= 54):
    print(nomer, "- нижнее место в купе ")
elif not ((nomer % 2 != 0) and (nomer <= 37) and (nomer >= 54)):
    print( "такого места нет")