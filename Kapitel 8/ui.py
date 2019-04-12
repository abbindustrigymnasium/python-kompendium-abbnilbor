def line(dots=False):
    loop=0
    text="" #sätter variablar för loopen
    if dots==True:
        while loop<30: #repeterar 30ggr
            loop+=1
            text+="*"
    else:
        while loop<30: #repeterar 30ggr
            loop+=1
            text+="-" #lägger ihop - i en string
    print(text) #printar den


def header(text):
    textCenter=text.center(28) #centrerar texten över 28 rader så att vi plus de två strecken får 30
    print("|"+textCenter+"|")

def echo(text1="", text2=""): #kan acceptera två argument
    if text2=="":
        print("| "+ text1) #om det bara finns ett argument så skriver den en 
    else: 
        print("| "+ text1 + " | "+ text2) #annars skriver den båda två

def prompt(text):  
    a=input("| "+text+ " > ")  #promptar användaren text
    return(a)    #om vi behöver a så returneras det också
 



