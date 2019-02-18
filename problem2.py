import math

number = int(input("Enter number to print: "))

number_list = ["sıfır","Bir","Iki","Üç","Dörd","Beş","Altı","Yeddi","Səkkiz","Doqquz"]
teen_list = ["On","On bir","On iki","On üç","On dörd","On beş","On altı","On yeddi","On səkkiz","On doqquz"]
decades_list =["Iyirmi","Otuz","Qırx","Əlli","Altmış","Yetmiş","Səksən","Doxsan"]


if number <= 9:
    print(number_list[number].capitalize())
elif number >= 10 and number <= 19:
    tens = number % 10
    print(teen_list[tens].capitalize())
elif number > 19 and number <= 99:
    ones = math.floor(number/10)
    twos = ones - 2
    tens = number % 10
    if tens == 0:
        print(decades_list[twos].capitalize())
    elif tens != 0:
        print(decades_list[twos].capitalize() + " " + number_list[tens])
