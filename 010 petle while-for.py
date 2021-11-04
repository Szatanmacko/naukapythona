# number = 1
#
## petla while wykonuje zlecenie do wyczerpania mozliwosci!!!
#
# while number < 6:
#     print(number)
#     number += 2

## petla for wykonuje sie zdefiniowana ilosc razy!!!
## break zatrzymuje wywolanie petli, continue ponawia wywolanie petli, ale z pominieciem wartosci podanej po if!

for number in range(0, 10, 2):
    if number == 5:
        continue
    print(number)
