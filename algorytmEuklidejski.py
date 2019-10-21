x = int(input("Podaj pierwszą liczbę\n"))
y = int(input("Podaj drugą liczbę\n"))

while x != y:
    if x > y:
        x -= y
    else:
        y -= x

print("NWD to {}".format(x))