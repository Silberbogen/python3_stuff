#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C)  2012, Sascha K. Biermanns

"""
Filename:  ratedaszitat.py

Description:  Ein kleines Ratespiel im Geiste von Glücksrad ... auch wenn auf
              das Rad bisher noch verzichtet wurde.

Version:  0.08
Created:  17.07.2012
Revision:  24.07.2012
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

from toolbox import ask_ok
from random import randint
from sys import stdin
import shelve

UNGESPIELTDB = 'ungespieltezitate' # Name der Shelf-Datei für ungespielte Zitate
GESPIELTDB = 'gespieltezitate' # Name der Shelf-Datei für gespielte Zitate

# ----------------------------
# Die Behandlung der Datenbank
# ----------------------------

def hole_daten_aus_shelf(shelf):
    """ Per popitem-Methode die Datensätze aus einem  beliebigen Shelf abholen
und als passendes Tupel zurückgeben """
    datensatz, paar = shelf.popitem()
    gesucht, hinweis = paar
    return gesucht, hinweis

def datensatz_abrufen():
    """ Die Funktion dient zur Rückgabe des nächsten spielbaren Datensatzes.
Hierbei ruft sie nicht einfach nur die Daten ab, sondern verwaltet auch
bereits gespielte und ungespielte Daten.
Sollte er keine ungespielten Daten mehr geben, werden alle Datensätze aus
dem gespielten Shelf entnommen und im ungespielten Shelf gespeichert."""
    ungespielt = shelve.open(UNGESPIELTDB)
    gespielt = shelve.open(GESPIELTDB)
    # Wenn keine Datensätze in ungespielt verblieben sind, dann kopiere alle
    # Datensätze zurück in ungespielt und entferne sie aus gespielt
    if len(ungespielt) < 1:
        anzahl = len(gespielt)
        for datensatz in range(anzahl):
            ungespielt[str(len(ungespielt) + 1)] = hole_daten_aus_shelf(gespielt)
    # Hole den nächsten Datensatz aus dem Shelf der ungespielten Datensätze
    gesucht, hinweis = hole_daten_aus_shelf(ungespielt)
    # und kopiere den Datensatz in das Shelf der gespielten Datensätze
    gespielt[str(len(gespielt) + 1)] = gesucht, hinweis
    ungespielt.close()
    gespielt.close()
    return gesucht, hinweis

def datensatz_hinzufügen():
    """ Die Funktion dient zur Eingabe eines weiteren Datensatzes """
    db = shelve.open(UNGESPIELTDB)
    gesucht = input("Wonach wird gesucht? ")
    hinweis = input("Wie lautet der Hinweis? ")
    db[str(len(db)+1)] = (gesucht, hinweis)
    db.close()

def datensätze_eingeben():
    """ Die Funktion enthält eine bedingte Schleife zur bequemen Eingabe
mehrerer Datensätze """
    weiter = True
    while weiter:
        datensatz_hinzufügen()
        weiter = ask_ok("Einen weiteren Datensatz hinzufügen (ja/nein)? ")

# -----------------
# Das Spiel an sich
# -----------------

def intro():
    """Die Funktion intro enthält einen Begrüssungsbildschirm für den Spieler."""
    print()
    print("Herzlich willkommen zu einer kleinen Runde:")
    print()
    print("        ****************************       ")
    print("        ****** Rate das Zitat ******       ")
    print("        ****************************       ")
    print()
    print("Zum Antworten gib bitte einen Buchstaben ein ") 
    print("und drücke die ENTER-Taste oder löse das ")
    print("Zitat indem du es auf einen Rutsch und ")
    print("fehlerfrei eingibst und dann die ENTER-Taste")
    print("drückst.")
    print()      

def spiele_satz(satz, hinweis):
    """Die Funktion enthält die Hauptroutine zum Spielen des Spiels."""
    # Zuerst wird der gesuchte Satz in Grossbuchstaben umgewandelt
    # und dann als eine Menge gespeichert
    lösungs_menge = set()
    # Der Satz wir als Menge von alphanumerischen Grossbuchstaben und Ziffern
    # in der Variable lösungs_menge gespeichert
    for i in satz.upper():
        if i.isalnum():
            lösungs_menge.add(i)
    # Die Variable rate_menge wird alle von uns geratenen Buchstaben entgegen-
    # nehmen
    rate_menge = set()
    # Solange die lösungs_menge keine echte Teilmenge der rate_menge ist,
    # wird die Schleife durchlaufen. Sollte lösungs_mennge zu einer echten
    # Teilmenge werden, sind alle Buchstaben eingegeben  worden, der Spieler
    # hat quasi ohne es zu merken den Satz gelöst.
    while not lösungs_menge <= rate_menge:
        print("Hinweis: ", hinweis)
        print("Der gesuchte Satz lautet diesmal:")
        ausgabe = ''
        for i in satz:
            j = i.upper()
            if j in rate_menge and j in lösungs_menge:
                ausgabe += i
            elif j in [" ", ",", ".", ";", "?", "!", "'", "-", "`", "´", ":"]:                ausgabe += i
            else:
                ausgabe += '_'
        print(ausgabe)
        try:
            tip = input("Wie lautet dein Tip? ")
        except EOFError:
            print("Das Spiel wird beendet.")
            return None
        except KeyboardInterrupt:
            print("Das Spiel wird beendet.")
            return None
        # Versucht der Spieler auf einen Rutsch den Satz zu lösen?
        if tip.upper() == satz.upper():
            print("Das ist ... richtig!")
            print("Herzlichen Glückwunsch, du hast diese Runde gewonnen!")
            return True
        # Wenn der Spieler keine echte Eingabe gemacht, sondern nur Enter
        # gedrückt hat
        if tip == "":
            print("Du sollst einen Buchstaben, den du rätst eingeben, oder ...")
            print("die gesamte Lösung um aufzulösen und das Spiel zu gewinnen.")
        print("Du rätst: ", tip[0].upper())
        rate_menge.add(tip[0].upper())
        print("Deine bisher geratenen Buchstaben:")
        print(rate_menge)
    # Der Spieler hat alle Buchstaben erraten - aber nicht selber aufgelöst
    else:
        print(satz)
        print("Ohne es zu bemerken hast du alle Buchstaben ergänzt!")
        print("Das fühlt sich jetzt nicht wirklich wie ein Sieg an, oder?")
        return False

# Automatischer Start, falls dies ein Skript ist
if __name__ == '__main__':
    if stdin.isatty():
        weiter = True
        if ask_ok("Wollen wir eine Runde spielen (ja/nein)"):
            intro()       
            while weiter:
                satz, hinweis = datensatz_abrufen()
                spiele_satz(satz.strip(), hinweis.strip())
                weiter = ask_ok("Noch eine Runde (ja/nein)? ")
        elif ask_ok("Willst du Datensätze zum Spiel hinzufügen (ja/nein)? "):
            while weiter:
                datensatz_hinzufügen()
                weiter = ask_ok("Einen weiteren Datensatz hinzufügen (ja/nein)? ")                
    
    
    
