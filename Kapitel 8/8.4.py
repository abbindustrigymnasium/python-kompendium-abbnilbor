import ui #importerar våra tidigare filer
import web 

ui.line()
ui.header("ARTIST DATABASE")
ui.line()
ui.echo("Welcome to a world of")
ui.echo("Music!")
ui.line()
ui.echo("L", "List artists")
ui.echo("V", "View artist profile")
ui.echo("E", "Exit application")
a=ui.prompt("Selection")

running="yes" #sätter någonting vi kan loopa med

while running=="yes":
    b=web.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/") #tidigare url:en, b kommer alltid att uppdateras när vi frågar efter information
    if a.title()=="L": #om valet är l eller L
        ui.line()
        ui.header("ARTIST DATABASE")
        ui.line()
        for x in b["artists"]: #för alla värden i artists
            ui.echo(x["name"]) #letar den efter namn och skriver ut det som finns där
        ui.line(True)
        ui.echo("L", "List artists")
        ui.echo("V", "View artist profile")
        ui.echo("E", "Exit application")
        a=ui.prompt("Selection") #möjlighet till att välja igen
    elif a.title()=="V":
        ui.line()
        ui.header("ARTIST DATABASE")
        ui.line()
        c=ui.prompt("Artist name") #frågar efter vilken artist
        ui.line(True)
        check=False
        for x in b["artists"]:
            if c.title()==x["name"]:
                ui.header(c.title())
                ui.line(True)
                check=True #om något av värdena matchar det i dictionaryt, kommer check bli true
        if check==True: #om ett värde har hittats
            for y in b["artists"]:
                if y["name"]==c.title():
                    ID=y["id"] #hämtas id ut ur dictionaryt
            response_dictionary2=web.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"+ID)
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
                m+=l + " "  #halvkopierat från uppgift 6.3
            ui.echo("Members: "+ k )
            ui.echo("Genres: "+ i )
            ui.echo("Years active: "+ m) #skriver ut detsamma
            ui.line()
            ui.echo("L", "List artists")
            ui.echo("V", "View artist profile")
            ui.echo("E", "Exit application")
            a=ui.prompt("Selection")
        else: #om inget värde har hittats kommer den skriva det och gå tillbaks till början 
            ui.echo("That artist does not exist") 
            ui.line(True) 
    elif a.title()=="E":
        ui.echo("Exiting")
        running="no" #tar bort kriteriet för att runna
    else: #om valet inte är L,V eller E kommer den fråga om ett nytt val
        a=""
        ui.line()
        ui.header("ARTIST DATABASE")
        ui.line()
        ui.echo("Invalid choice")
        ui.line()
        ui.echo("L", "List artists")
        ui.echo("V", "View artist profile")
        ui.echo("E", "Exit application")
        a=ui.prompt("Selection") 




        




