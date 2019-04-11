b=input("Ange distans(skriv km eller miles efter): ") #frågar användaren om distansen
c=b.split() #delar upp distans i ord
 
def km_to_miles(dist):
    a= float(dist)/(1/1.609344) #dividerar med en konstant
    print(str(a)+ " miles") 

def miles_to_km(dist): 
    d= float(dist)*1/1.609344 #multiplicerar med en konstant
    print(str(d) + " km")



if "km" in c: # om km finns i arrayen c som vi delat upp
    km_to_miles(c[0]) # sätter första värdet i c till dist
elif "miles" in c:
    miles_to_km(c[0]) #samma sak men andra funktionen