import random
import time #importerar libraries som behövs

Dimsdale_Dimmadome=["Dimsdale Dimmadome", "Höger", "Bostadsblocket", 2, 29, "Doug Dimmadome"]
Pinnets_Liv=["Pinnets Liv", "Vänster", "Middagsblocket", 1, 7, "Edward Blom"]
Träskpartiet=["Träskpartiet", "Vänster", "Bostadsblocket", 4, 14, "Shrek"]
Surahammarspartiet=["Surahammarspartiet", "Vänster", "Bostadsblocket", 1, 6, "Filip CS"]
Veggie_Tales=["Veggie Tales", "Höger", "Middagsblocket", 18, 23, "Bob the tomato"]
BABA_IS_YOU=["BABA IS YOU", "Höger", "Inget", 17, 28, "BABA"]
Spetsland=["Spetsland", "Höger", "Spetsblocket", 1, 50, "Jonas Westerholm"] #listor med våra partier
Partier=[Dimsdale_Dimmadome, Pinnets_Liv, Träskpartiet, Surahammarspartiet, Veggie_Tales, BABA_IS_YOU, Spetsland] #lista med listorna 
dummaSaker=["sade att Shrek var en dålig film", "sade 'Fortnite good, Minecraft bad'", "tog inte pannkakor till Pannkakstorsdag", "skrattade åt en minion-meme", "påstod att prequels var bra", "tog fler kycklingar än man fick", "åt en nutellasemla", "läste inte Daniels instruktioner" , "spoilade Endgame", "blev Ridley down specialed"]
fusk2=0
runningVote=True
changeHappened=False #variablar som sätts för att användas i funktioner




while runningVote==True: #ska kunna repeteras om det blir med än 100% som röstar
    fusk=0
    Röster=[] #tom lista
    for a in Partier: 
        b=random.randint(a[3], a[4])
        Röster.append(b) #ta ett slumptal mellan partiets min och max och lägg till det i vå tomma lista

    for a in Röster:
        fusk+=a #lägg till varje värde från röster till fusk så vi kan räkna valdeltagande
    if fusk<=100:
        runningVote=False #om fusk är mindre än eller lika med 100 kommer loopen avslutas 
    else:
        print("Oj, det blev ryssval") #annars forsätter den loopa
        time.sleep(1)

rond=[] 
count=0 #sätter variablar som ska användas i funktionen

def Show():
    if count==0:
        rond=Röster.copy()  #om det är första gången vi kör kommer den första röstlistan blir rond en kopia av första röstomgången
    else:
        rond=nyaRöster.copy() #annars blir det en kopia av den andra
    loop=0
    while loop < (len(Partier)): # loop räknar upp till antalet partier
        if rond[loop]>3: #om partiet har med än 4% röster
            print(Partier[loop][0]+" fick "+ str(rond[loop])+ "% röster") #printas partier med sina röster ut 
        loop+=1
        time.sleep(1) #väntar så man hinner se vad som printas
    winVotes=max(rond)
    winPos=rond.index(winVotes) #hämtar ut positionen på det parti som fick flest röster

    print(Partier[winPos][0]+ " vann valet med " + str(winVotes) + "% röster") #skriver vem som vann valet med hur många röster
    time.sleep(1)

    block={} #tomt dictionary

    for x in Partier:
        if x[2] not in block: #om blocket inte finns
            block[x[2]]=rond[Partier.index(x)] #lägger till blocket och antalet röster
        else: #om blocket redan finns
            block[x[2]]+=rond[Partier.index(x)] #lägger till antalet röster till blockets värde

    blockInv = dict() #tomt dictionary
    for key, value in block.items(): #för varje key och value
        blockInv.setdefault(value, list()).append(key) #lägg till key som value till value som key 

    blockMax=(max(blockInv)) #kolla vilken key som är störst 

    blockWin=blockInv[blockMax][0] #hämtar korresponderande blocket
    print("Det vinnande blocket var " + blockWin + " med " + str(blockMax)+ "% röster") #printat att det vann
    time.sleep(1)

    Inriktning={}

    for x in Partier:
        if x[1] not in Inriktning:
            Inriktning[x[1]]=rond[Partier.index(x)]
        else:
            Inriktning[x[1]]+=rond[Partier.index(x)]

    #print(Inriktning)

    InriktningInv = dict()
    for key, value in Inriktning.items():
        InriktningInv.setdefault(value, list()).append(key)


    InriktningMax=(max(InriktningInv))

    InriktningWin=InriktningInv[InriktningMax][0]
    print("Flest människor röstade " + InriktningWin + " med " + str(InriktningMax)+ "% röster" ) #samma sak med inriktning istället för block
    time.sleep(1)
    print("Det totala valdeltagandet var " + str(fusk-fusk2)+ "%") #printar vad valdelatagandet är, om vi redan har kört en gång kommer fusk2 vara antalet förlorade röster


Show() #runnar funktionen
time.sleep(1)

rand=0
nyaRöster=[] 

#print(Röster)

for x in Röster: #för varje rösttal
    if x>3: #om partier har 4% eller mer 
        rand=random.randint(1, 3) #finns det en tredjedels chans att en partiledare ska säga någonting sumt
        checkAgain=True
        if rand==1:
            changeHappened=True 
            if x<10:
                randx=random.randint(1, x)
            else:
                randx=random.randint(1, 10) #slumpar ett tal mellan 1 och 10 för att subtrahera från deras röster 
            print(Partier[count][5] +" " + dummaSaker[random.randint(0,9)]+ " och förlorade " + str(randx)+ "% röster") #printar en av 10 dumma saker som ledarna kan göra pch hur många röster de förlorade
            x-=randx
            fusk2+=randx #lägger till de förlorade rösterna till fusk2
            if x<0:
                x=0 #om x är under 0 så blir x 0 för att ett parti inte kan ha negativa röstprocent
    nyaRöster.append(x) # 
    count+=1

#print(nyaRöster)
           

if changeHappened==True: #om det har blivit någon förändring
    print("Det nya resulatet är: ") 
    time.sleep(2)
    Show() #runnas funktionen igen













