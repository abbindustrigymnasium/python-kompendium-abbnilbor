import requests #importerar biblioteket

a=input("Skriv in en stad: ") #användaren skriver in en stad


url = "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/"+a 
r = requests . get ( url )
response_dictionary = r . json () #förkortar

print("--------------------------")
print("         FORECASTS")
print("**************************") #fina grejer
for b in response_dictionary["forecasts"]:
    print(b["date"]+"       "+b["forecast"]) #skriver ut det som finns inom varje forecasts på date på ett ställe och forecats på ett annat



