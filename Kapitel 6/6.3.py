import requests #importerar libraries

url ="https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
r = requests . get ( url )
response_dictionary = r . json ()

print("--- ARTIST DB ---")
print("   Ariana Grande")
print("     Avicii")
print("    Blink-182")
print("   Brad Paisley")
print("  Imagine Dragons")
print("     Maroon 5")
print("    Scorpions") #databasen


q=input("Which artist do you want to know more about?: ")
a=q.title() #Gör så att det inte spelar någon roll om användaren skriver med liten bokstav eller inte



for b in response_dictionary["artists"]:
    if b["name"]==a:
        c=b["id"] #om inputen är samma som namnet i databasen så tar den id:t

url2="https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"+c #och sätter det i slutet av api::n
r2 = requests . get ( url2 )
response_dictionary2 = r2 . json ()

e=response_dictionary2["artist"]["genres"]
f=response_dictionary2["artist"]["years_active"]
g=response_dictionary2["artist"]["members"] #tar de olika värdena ut dictionaryt

i=""

for h in e:
    i+=h + ", " 

k="" 

for j in g:
    k+=j + ", "

m=""

for l in f:
    m+=l + " " #sätter ihop värdena i en string så att de kan printas


print("Genres: " + i)
print("Members: " + k)
print("Years active: " + m) #printar värdena


       


