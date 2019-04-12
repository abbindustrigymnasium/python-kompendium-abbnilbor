import web #importerar filen med get funktionen

a="" #den ville ha a som någonting
a=web.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/") #exempelurl för uppgift 6.3, get returnerar ett värde som vi sätter a till
print(a) 
