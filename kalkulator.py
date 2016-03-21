prvo_stevilo = float(raw_input("Vnesi prvo stevilo: "))
drugo_stevilo = float(raw_input("Vnesi drugo stevilo: "))

operacija = raw_input("Katera operacija: ")

if operacija == "sestevanje" or operacija == "+":
    print prvo_stevilo + drugo_stevilo

elif operacija == "odstevanje" or operacija == "-":
    print prvo_stevilo - drugo_stevilo

elif operacija == "mnozenje" or operacija == "*":
    print prvo_stevilo * drugo_stevilo

elif operacija == "deljenje" or operacija == "/":
    print prvo_stevilo / drugo_stevilo
