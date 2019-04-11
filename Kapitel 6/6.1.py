import requests #importerar biblioteket

a=input("Ange ett positivt heltal: ") #frågar användaren efter ett värde

url = "http://77.238.56.27/examples/numinfo/?integer="+a #skriv in det i slutet av httpn
r = requests . get ( url )
response_dictionary = r . json () #förkortar så att vi inte behöver skriva hela adressen varje gång

if response_dictionary["even"]==True:
    print (a+ " är ett jämnt tal") #om talet är jämnt så skriv det
else:
    print (a + " är ett udda tal") #annars skriv att det är udda
if response_dictionary["prime"]==True:
    print(a+ " är ett primtal") # om det är ett primtal så skriver den det
else: 
    print(a+ " är ett inte ett primtal") #annars skriver den ut att det itne är det
    print("Talets faktorer är: ")
    c=len(response_dictionary["factors"])
    for b in response_dictionary["factors"]:         #For loopen tar bort de hårda paranteserna runt faktorerna 
        if (b==response_dictionary["factors"][c-1]): #och skriver "," mellan raderna
            print("och "+ str(b))                    #Om b är samma som den sista i responde_dictionary skriver den också 
        else:                                        #"och" innan
            print(str(b) + ",")



