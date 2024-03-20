#chislo = int(input("Vvedite chislo:"))
#def proverka(chislo, t=5):
    #if chislo//t:
        #print("yes")
    #else:
        #print("No")
#proverka(chislo, t = 7)

def a(chislo1):
    try:
        delenie = 200 / chislo1
        return delenie
    except ValueError:
        print( "Ne chislo")
    except ZeroDivisionError:
        print("Na 0 delit nelza")
chislo1 = int(input("Vvedite chislo:"))
if a(chislo1):
    print("yes")

#def tri():
    #data = input("vvedite datu")
    #day, month, year = map(int, data.split("."))
    #if day * month == int(str(year)[-2:]):
        #return "yes"
    #else:
        #return "no"
#print(tri())

