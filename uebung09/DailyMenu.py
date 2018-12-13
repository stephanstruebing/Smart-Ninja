# -*- coding: utf-8 -*-
print "Daily Menu"

menu = {}

while True:
    tages_name = raw_input("Welches Menu gibt es heute?: ")
    tages_preis = raw_input("Was kostet das Menu?: ")
    menu[tages_name] = tages_preis

    neu = raw_input("Möchtest du noch ein weiteres Menu hinzufügen? (y/n) ")

    if neu == "n":
        break

print "Menu: %s" % menu
with open ("menu.txt", "w") as menu_file:
    for tages in menu:
        menu_file.write("%s, %s €\n" % (tages, menu [tages]))