a=input("Ange ditt namn: ")
b=input("Ange din ålder: ") #två prompts

sleepArray=[14,13,12,11.5,11,11,10.5,10,10,10,9.5,9,9,9,9,8.5]
ageArray=[1,2,3,4,5,6, 7, 8, 9, 10, 11, 12, 14, 15, 16] #arrays med värden

for x in ageArray:
    if x==int(b): #för varje värde mellan 1-16 så kollar den om det är samma sak som b
        c=sleepArray[x-1] #då hittar den motsvarande positioion i sleepArray och gör c till värdet

if int(b)>=17:
    c=8 #utifall värdet skulle vara 17 eller över så blir c 8
    
print("Hallå " + a+ "! Enligt Vårdguidens rekommendationer behöver individer i din ålder (" + b + " år) sova minst " + str(c) + " timmar per natt." )
