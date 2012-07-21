#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C)  2012, Sascha K. Biermanns

"""
Filename:  zahlenraten.py

Description:  Ein kleines Ratespiel im Geiste von Glücksrad ... auch wenn auf
              das Rad bisher noch verzichtet wurde.

Version:  0.01
Created:  21.07.2012
Revision:  21.07.2012
Language: Python 3

Author:  Sascha K. Biermanns (skbierm), skbierm@gmail.com
License:  ISC
Copyright (C)  2012, Sascha K. Biermanns

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
"""

from toolbox import ask_ok, get_int
from random import randint
    
def rate_meine_zahl(minimum_zahl = 1, maximum_zahl = 1000):
    print("Sehr schön, dann errate du mal meine Zahl!")
    assert type(minimum_zahl) == int, "Die kleinste Zahl muss eine Ganzzahl sein."
    assert type(maximum_zahl) == int, "Die größte Zahl muss eine Ganzzahl sein."
    assert minimum_zahl < maximum_zahl, "Die kleinste Zahl muss kleiner als die größte Zahl sein."
    zufalls_zahl = randint(minimum_zahl,maximum_zahl)
    print("Meine Zahl liegt zwischen ", minimum_zahl, " und ", maximum_zahl, ".", sep='')
    geraten = 0
    while geraten != zufalls_zahl:
        geraten = get_int("Was denkst du, welche Zahl ich mir ausgedacht habe? ")
        if  geraten < zufalls_zahl:
            print("Deine Zahl ist zu klein.")
        elif geraten > zufalls_zahl:
            print("Deine Zahl ist zu gross.")
    else:
        print("Genau!", zufalls_zahl, "war die gesuchte Zahl.")

def rate_deine_zahl(minimum_zahl = 1, maximum_zahl = 1000):
    print("Also gut, dann errate ich deine Zahl!")
    gelöst = False
    while not gelöst:
        if minimum_zahl == maximum_zahl:
            print("Ich denke ich hab's! Es ist die ", minimum_zahl, "!", sep='', end='')
            geraten = minimum_zahl
        else:
            geraten = (minimum_zahl + maximum_zahl) // 2
            print("Ist es die", geraten, end='')
        gelöst = ask_ok(" (Ja/Nein)? ")
        if not gelöst:
            if randint(1,3) == 1:
                print("Mist! ", end='')
            antwort = ask_ok("War meine Zahl kleiner oder größer als deine (kleiner/größer)?", positiv="kleiner", negativ="größer")
            if antwort == True and (geraten - 1) >= minimum_zahl:
                maximum_zahl = geraten - 1
            elif antwort == False and (geraten +1) <= maximum_zahl:
                minimum_zahl = geraten + 1
            else:
                print("Verarschen kann ich mich auch selber ... *grummel*")
         
        else:
            print("Echt? Die", geraten, "war's ? Perfekt!")
    else:
        if randint(1,4) == 1:
            print("Ich war gut, nicht wahr?")
            
def zahlenraten():
    print("Du möchtest also, das wir eine Runde Zahlenraten spielen ...")
    print("Na schön ...")
    spieler_rät = ask_ok("Willst du raten (ja/nein)? ")
    standardzahlen = ask_ok("Spielen wir mit den Zahlen zwischen 1 und 1000  (ja/nein)? ")
    if not standardzahlen:
        minimum = 0
        maximum = 0
        while not minimum < maximum:
            print("Kleinste Zahl:", minimum)
            print("Größte Zahl:", maximum)
            print("So können wir natürlich nicht spielen.")
            minimum = get_int("Wie also lautet die kleinste von dir gewünschte Zahl? ")
            maximum = get_int("Und wie die größte Zahl? ")
    else:
        minimum = 1
        maximum = 1000
    print("Dann lass uns anfangen!")
    if spieler_rät:
        print("Viel Glück!")
        rate_meine_zahl(minimum, maximum)
    else:
        print("Wünsch mir Glück!")
        if randint(1, 5) == 1:
            print("... und wehe du pfuschst! Sowas bemerke ich!!!")
            rate_deine_zahl(minimum, maximum)
            

if __name__ == "__main__":
    zahlenraten()
    
