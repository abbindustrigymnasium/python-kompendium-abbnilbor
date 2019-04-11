from random import randint #importerar möjliget till random nummer

print(".: THE HIGHER OR LOWER GAME :.")
print("--------------------------")
print("Welcome to The Higher Lower")
print("Game. I will randomise a")
print("number between 0 and 99.")
print("Can you guess it?")
print("--------------------------") #skriver fina grejer

a = randint(0, 99) #genererar ett slumpmäsigt nummer mellan 0 och 99

b= int(input("Your guess: "))
c = "playing"
d=0 #sätter variablar

while c=="playing": #för att ha någonting att loopa med
    d+=1 #räknar antal 
    if b<a: 
        print("HIGHER")
        b=int(input("Try again: ")) #om det är för lite så säger den HIGHER och att man ska gissa igen
    elif b>a:
        print("LOWER")
        b=int(input("Try again: ")) #samma sak fast med LOWER och om det är för högt
    else:
        print(str(b)+ " is correct!")
        print("It took you " + str(d) + " guesses.")
        print("Good job!") #printar att man vann
        c="over" #avslutar loopen

    