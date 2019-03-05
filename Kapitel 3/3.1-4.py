male=["Erik", "Lars", "Karl", "Anders", "Johan"] #Listan med male namn
female=["Maria", "Anna", "Margaretha", "Elisabeth", "Eva"] #listan med female namn

a=len(female)-1 # längden av female minus ett

male.append("Nils") #Lägger till mitt eget namn i listan

male.sort() 
female.sort() #sorterar i alfabetisk ordning

print(male[0])
print(female[2])
print(female[a])
print(male[1]) #skriver ut på positionerne vi säger åt den att göra

male.remove(male[1]) 
male.remove(male[2])
female.remove(female[0]) #tar bort på de positionerna vi säger åt den att göra