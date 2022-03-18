import os

pin_len = 6

for i in range(999999):
    bruteforce = (str(i).zfill(pin_len))
    os.system("echo " + bruteforce + " | ./bin >> out.txt")
    print(i)
