import ui
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

running="yes"

while running=="yes":
    b=web.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/")
    if a.title()=="L":
        ui.line()
        ui.header("ARTIST DATABASE")
        ui.line()
        for x in b["artists"]:
            ui.echo(x["name"])
        ui.line(True)
        ui.echo("L", "List artists")
        ui.echo("V", "View artist profile")
        ui.echo("E", "Exit application")
        a=ui.prompt("Selection")
    elif a.title()=="V":
        ui.line()
        ui.header("ARTIST DATABASE")
        ui.line()
        c=ui.prompt("Artist name")
        ui.line(True)
        check=False
        for x in b["artists"]:
            if c.title()==x["name"]:
                ui.header(c.title())
                ui.line(True)
                check=True
        if check==True:
            for y in b["artists"]:
                if y["name"]==c.title():
                    ID=y["id"]
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
                m+=l + " " 
            ui.echo("Members: "+ k )
            ui.echo("Genres: "+ i )
            ui.echo("Years active: "+ m)
            ui.line()
            ui.echo("L", "List artists")
            ui.echo("V", "View artist profile")
            ui.echo("E", "Exit application")
            a=ui.prompt("Selection")
        else:
            ui.echo("That artist does not exist")
            ui.line(True)
    elif a.title()=="E":
        ui.echo("Exiting")
        running="no"
    else:
        ui.line()
        ui.header("ARTIST DATABASE")
        ui.line()
        ui.echo("Invalid choice")
        ui.line()
        ui.echo("L", "List artists")
        ui.echo("V", "View artist profile")
        ui.echo("E", "Exit application")
        a=ui.prompt("Selection")




        




