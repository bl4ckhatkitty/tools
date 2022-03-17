# luhn algorithm checker

test = input()
str_test = str(test)
len_test = len(str_test)
checksum = 0

for i in range(len_test):
    if i % 2 == 0:
        supp = int(str_test[i]) * 2
        if supp == 10:
            checksum += 1
        elif supp == 12:
            checksum += 3
        elif supp == 14:
            checksum += 5
        elif supp == 16:
            checksum += 7
        elif supp == 18:
            checksum += 9
        else:
            checksum += supp

    else:
        checksum += int(str_test[i])

if checksum % 10 == 0:
    print("ok")

else:
    print("shit")
