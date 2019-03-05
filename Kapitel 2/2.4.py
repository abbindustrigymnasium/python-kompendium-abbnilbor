a=int(input("Hur gammal är du?: ")) # frågar användaren om ålder och gör om inputen till inte

if a >= 18:
    print("Du är myndig!") #om man är över 18 är man readn myndig
else:
    b=str(18-a)
    print("Du är mydig om " + b + "år!") # annars är man myndig om 18 minus ålder år
