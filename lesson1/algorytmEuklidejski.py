x = int(input("Podaj pierwszą liczbę\n"))
y = int(input("Podaj drugą liczbę\n"))

while x != y:
    if x < y:
        y -= x
    else:
        x -= y

print("NWD to {}".format(x))