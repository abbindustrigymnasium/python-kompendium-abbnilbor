a = range(501)
b=0

for tal in a:
    if tal % 2 !=0:
        b+=tal

c=str(b)

print("Summan av alla udda tal mellan 0 och 500 är " + c)
