import requests #importerar libraryt

def get(url): 
    r = requests . get ( url ) #requests get funktion som hämtar från api:n
    response_dictionary = r . json ()
    return(response_dictionary) #ger tillbaks allt i api:n