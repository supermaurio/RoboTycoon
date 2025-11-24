geld=10
teile=0
erz=0
eisen=0
tnt=0
roboter=0
ort="Fabrik"

def wo_bin_ich():
    print("Du bist hier: " + ort)

def was_habe_ich():
    print(f"""
          Geld: {geld}
          Teile: {teile}
          Roboter: {roboter}
          Erz: {erz}
          Eisen: {eisen}
          TNT: {tnt}
        """)

def fabrik():

    global geld
    global teile
    global erz
    global eisen
    global tnt
    global roboter
    global ort

    ort="Fabrik"
    wo_bin_ich()
    was_habe_ich()
    print("""
Was willst Du machen?
a) Roboter zusammen bauen
b) Teile kaufen
c) zur Mine gehen
        """)
    wahl = input(">")
    if wahl == "a":
        if teile>=10:
            roboter += 1
            teile -= 10
        else:
            print("Du brauchst 10 Teile um einen Roboter zu bauen")
    elif wahl == "b":
        wieviele_eingabe = input("Wieviele Teile willst Du kaufen? Ein Teil kostet 5 credits : ")
        wieviele = int(wieviele_eingabe)
        if wieviele < 0:
            print("witzig")
        else:
            kosten = 5 * wieviele
            if geld < kosten:
                print(f"Kannst Du Dir leider nicht leisten - das kostet {kosten} credits")
            else:
                geld -= kosten
                teile += wieviele
    else:
        print("Verstehe ich nicht...")

def schmiede():
    global ort
    ort="Schmiede"
    wo_bin_ich()


# Das ist unsere Hauptschleife
while True:
    print("---------------")
    fabrik()
    print("")
    schmiede()
    print("und nochmal von vorne")
