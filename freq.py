import sys

s = sys.argv

counter = {}
try:
    num1 = open(s[1])
    num2 = num1.read()
    num3 = num2.strip()
    num4 = num3.split()
    for i in num4:
        if not i in counter:
             counter[i] = 1
        else:
            counter[i] += 1
    print(counter)
    counter1 = str(counter)
    file = open("file", "w")
    file.write(counter1)
finally:
    num1.close()
    file.close()
