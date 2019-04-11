a=int(input("Ange miltiplikationstabell: ")) #frågsar efter talbell

b=0
c=0 
d="ja" #sätter variablar som behhövs inom while och for


while d=="ja": #om användaren har skrivit ja
    b+=1
    c+=1 #lägger den på 1 på c och b
    print(str(c*a)) #och multiplicerar c med inputen
    if b==3: #om den har repeterats tre ggr så resetas b men c är densamma
        b=0
        d=input("Fortsätt?: ") #frågar användaren om den vill fortsätta
            




