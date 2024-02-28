import random
N = random.randint (2,10)
print("Введите",N, "слов:")
s = []
while N > 0:
    slovo = input()
    N = N - 1
    s.append(slovo + "")
print(s)
