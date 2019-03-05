a=input("Ange kön: ")
b=input("Ange hårfärg: ")
c=input("Ange ögonfärg: ")

Daniel_Radcliffe=["Daniel Radcliffe", "man","brun","brun"]
Rupert_Grint=["Rupert Grint", "man","brun","brun"]
Emma_Watson=["Emma Watson", "kvinna", "brun", "brun"]
Selena_Gomez=["Selena Gomez", "kvinna", "brun","brun"]
Khetdan_Phopat=["Khetdan Phopat" "man", "svart", "brun"]
Joakim_Flink=["Joakim_Flink", "man", "blond", "blå"]
Nils_Borg=["Nils Borg", "man", "brun","blå"]
Jonas_Västerholm=["Jonas Västerholm", "man","vit", "blå"]
Cool_Bean=["Cool_Bean", "man", "inget", "svart"]

personer=[Daniel_Radcliffe, Rupert_Grint, Emma_Watson, Selena_Gomez, Khetdan_Phopat, Joakim_Flink, Nils_Borg, Jonas_Västerholm, Cool_Bean]

print("Din beskrivning passar på: ")

for folk in personer:
    if a == folk[1] and b == folk[2] and c == folk[3]:
        print(folk[0])



