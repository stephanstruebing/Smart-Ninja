# -*- coding: utf-8 -*-
secret = 64
guess = int(raw_input("errate die richtige Zahl, wähle eine Zahl zwischen 1 and 100:"))
if guess == secret:
    print("Glückwunsch, du bist ein Gewinner")
else:
    print("tut uns leid, das war leider nichts.. bitte versuche es erneut")
