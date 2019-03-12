a=str(input("Mata in ett land: ")) #frågar användaren om ett land
b= a.title() #sätter stor bokstav på landet

nordenArray=["Danmark", "Finland", "Island", "Norge", "Sverige"]
storbritanienArray=["England", "Nordirland", "Skottland", "Wales"] #listor med länderna

if b in nordenArray:
    print(b + " tillhör Norden")
elif b in storbritanienArray:
    print(b +  " tillhör Storbritanien")
else:
    print(b + " tillhör varken Storbritanien eller Norden") #om landet finns i nordens array printas norden
                                                            #samma sak med storbritanien
                                                            #annars printas att det inte är det