registerade=["Anna", "Eva", "Erik", "Lars", "Karl"]
avanmälningar= ["Anna" , "Erik" , "Karl"]

print(registerade)

for folk in registerade:
    if folk in avanmälningar:
        registerade.remove(folk)

print(registerade)
