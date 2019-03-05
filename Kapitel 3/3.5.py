male=["Erik", "Lars", "Karl", "Anders", "Johan"] #Listan med male namn
female=["Maria", "Anna", "Margaretha", "Elisabeth", "Eva"] #listan med female namn

print(male)
print(female) #skriver ut listorna

a=input("Vilket namn ska tas bort?: ") #promtar användaren för vilket namn som ska bort

if a in male:
    male.remove(a)
if a in female:
    female.remove(a)
else:
    print(a + " finns inte i någon lista")

#om det går att ta bort namnet ur listan male så gör den det, annars tar den bort ur female

print(male)
print(female) #skriver ut listorna igen

