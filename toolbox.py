#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2012 by Sascha Biermanns

"""
Filename:  toolbox.py

Description:  Python-Vorlagen für Programme

Version:  0.02
Created:  26.06.2012
Revision:  22.07.2012
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


def ask_ok(prompt = "Bitte antworten sie mit Ja oder Nein: ",
           versuche = None,
           positiv = 'ja',
           negativ = 'nein',
           beschwerde = None):
    """ask_ok stellt eine Frage und gibt die Antwort auf diese Frage zurück,
soweit diese der positiven oder negativen Antwort entspricht.
Die Anzahl der Versuche ist unendlich, es sei denn das man dies
durch eine entsprechende Parameterübergabe begrenzt"""
    if beschwerde == None:
        beschwerde = 'Bitte ' + positiv + ' oder ' + negativ + '!'
    # sofern die Anzahl der Versuche nicht eingegrenzt wird,
    # ist dies eine Endlosschleife
    while True and versuche == None or versuche > 0:
        # Hole eine Eingabe
        # Die Eingabe kann jederzeit abgebrochen werden        
        try:
            eingabe = input(prompt)
        except EOFError:
            return None
        except KeyboardInterrupt:
            return None
        if eingabe == "" and versuche != None:
            versuche -= 1
        # eine positive Antwort durchbricht die Endlosschleife
        # und liefert True als Antwort zurück
        elif soweit_gleich(eingabe, positiv):
            return True
        # eine negative Antwort durchbricht die Endlosschleife
        # und liefert False als Antwort zurück
        elif soweit_gleich(eingabe, negativ):
            return False
        elif versuche != None:
            versuche -= 1
        # Da die Schleife erfolglos abgearbeitet wurde,
        # erinnern wir den Nutzer daran, worum es geht,
        # der Beschwerdetext wird ausgegeben
        if versuche == None or versuche > 0:
            print(beschwerde)
    # Wird die Schleife verlassen, weil wir sie mit einer
    # begrenzten Anzahl an Versuchen begrenzt haben,
    # und diese Anzahl an Versuchen wurde nicht genutzt,
    # teilen wir dies mit indem wir None zurückliefern
    else:
        return None

def faktor(x):
    """faktor liefert zum Parameter x den entsprechenden Faktor zurück,
so z.B. faktor(3) = 6 oder faktor(4) = 24"""
    r = 1
    assert x > 0, "x ist keine positive Ganzzahl"
    for i in range(1, x+1):
        r *= i
    return r

def get_float(prompt = "Bitte eine Fliesspunktzahl eingeben: ",
              versuche = None,
              beschwerde = None):
    """get_float stellt eine Frage und gibt die Antwort auf diese Frage zurück,
soweit diese einer Fliesspunktzahl entspricht. Die Anzahl der Versuche ist
unendlich, es sei denn das man dies durch eine entsprechende Parameterübergabe
begrenzt"""
    if beschwerde == None:
        beschwerde = "Als Eingabe wird eine Fliesspuntzahl/Realzahl erwartet."
    # sofern die Anzahl der Versuche nicht eingegrenzt wird,
    # ist dies eine Endlosschleife
    while True and versuche == None or versuche > 0:
        # Hole eine Eingabe
        # Die Eingabe kann jederzeit abgebrochen werden
        try:
            eingabe = input(prompt)
        except EOFError:
            return None
        except KeyboardInterrupt:
            return None
        # Drückt der Nutzer nur die Eingabetaste, ohne eine Antwort
        # eingegeben zu haben, vermindert das seine möglichen
        # Antwortmöglichkeiten.
        # Sicherheitshalber geben wir in so einem Fall dann auch noch
        # die Beschwerde aus, aber nur, wenn noch Eingabemöglichkeiten
        # verbleiben
        if eingabe == "" and versuche != None:
            versuche -= 1
            if versuche == None or versuche > 0:
                print(beschwerde)
            continue
        try:
            # eine positive Antwort durchbricht die Endlosschleife
            # und liefert die Fliesspunktzahl als Antwort zurück
            zahl = float(eingabe)
            return zahl
        # Entspricht die Antwort nicht dem von uns erwarteten Typ,
        # erinnern wir den Nutzer noch einmal daran, was wir erwarten,
        # jedoch nur, wenn er noch weitere Eingabemöglichkeiten hat
        except ValueError as fehler:
            print(fehler)
            if versuche != None and versuche > 0:
                versuche -= 1
            if versuche == None or versuche > 0:
                print(beschwerde)
                continue
    # Wird die Schleife verlassen, weil wir sie mit einer
    # begrenzten Anzahl an Versuchen begrenzt haben,
    # und diese Anzahl an Versuchen wurde nicht genutzt,
    # teilen wir dies mit indem wir None zurückliefern
    else:
        return None
                
def get_int(prompt = "Bitte eine Ganzzahl eingeben: ",
              versuche = None,
              beschwerde = None):
    """get_int stellt eine Frage und gibt die Antwort auf diese Frage zurück,
soweit diese einer Integerzahl entspricht. Die Anzahl der Versuche ist
unendlich, es sei denn das man dies durch eine entsprechende Parameterübergabe
begrenzt"""
    if beschwerde == None:
        beschwerde = "Als Eingabe wird eine Ganzzahl/Integerzahl erwartet."
    # sofern die Anzahl der Versuche nicht eingegrenzt wird,
    # ist dies eine Endlosschleife
    while True and versuche == None or versuche > 0:
        # Hole eine Eingabe
        # Die Eingabe kann jederzeit abgebrochen werden        
        try:
            eingabe = input(prompt)
        except EOFError:
            return None
        except KeyboardInterrupt:
            return None
        # Drückt der Nutzer nur die Eingabetaste, ohne eine Antwort
        # eingegeben zu haben, vermindert das seine möglichen
        # Antwortmöglichkeiten.
        # Sicherheitshalber geben wir in so einem Fall dann auch noch
        # die Beschwerde aus, aber nur, wenn noch Eingabemöglichkeiten
        # verbleiben        
        if eingabe == "" and versuche != None:
            versuche -= 1
            if versuche == None or versuche > 0:
                print(beschwerde)
            continue
        try:
            # eine positive Antwort durchbricht die Endlosschleife
            # und liefert die Integerzahl als Antwort zurück
            zahl = int(eingabe)
            return zahl
        # Entspricht die Antwort nicht dem von uns erwarteten Typ,
        # erinnern wir den Nutzer noch einmal daran, was wir erwarten,
        # jedoch nur, wenn er noch weitere Eingabemöglichkeiten hat
        except ValueError as fehler:
            print(fehler)
            if versuche != None and versuche > 0:
                versuche -= 1
            if versuche == None or versuche > 0:
                print(beschwerde)
                continue
    # Wird die Schleife verlassen, weil wir sie mit einer
    # begrenzten Anzahl an Versuchen begrenzt haben,
    # und diese Anzahl an Versuchen wurde nicht genutzt,
    # teilen wir dies mit indem wir None zurückliefern
    else:
        return None

def invert_dict(ab):
    """invert_dict nimmt ein dictionary entgegen - und liefert ein invertiertes
Wörterbuch zurückt. Es ist wie bei einem richtigen Wörterbuch, wo man ein
deutsch-italienisches erhält, und ein italienisch-deutsches zurückerhält."""
    ba = {} # Leeres Wörterbuch erzeugen
    for b in ab: # Für jeden Eintrag b in den Schlüsseln des Ursprungswörterbuchs
        # Wenn man einen Eintrag wie Farbe: color, colour hat, möchte man ja
        # zwei Einträge im neuen Wörtebuch erhalten:
        # wie in color: Farbe
        #       colour: Farbe
        for a in ab[b]:
            # Für jeden Eintrag a in den Werten des Ursprungswörterbuchs
            # Man kennt das ja, verschiedene Begriffe können dasselbe bedeuten,
            # wie in color: Farbe
            #       colour: Farbe
            # also muss der Eintrag umgekehrt entstehen:
            #        Farbe: color, colour
            if a in ba: # wenn bereits ein Eintrag existiert
                ba[a] += [b] # wird ein weiterer Wert zum Schlüsssel hinzugefügt
            else: # es existiert noch kein Eintrag
                ba[a] = [b] # dann werden Schlüssel und Wert angelegt
    # Liefere das neu erstellte Wörterbuch zurück
    return ba
        

def programm_beenden(sicherheitsabfrage=True,
                     prompt="Programm beenden? (ja/nein) ",
                     sicherungsfrage="Sind Sie sicher? (ja/nein)"):
    '''programm_beenden stellt einen Mechanismus zur sauberen
Beendung eines Programms bereit.'''
    from sys import exit
    try:
        antwort = input(prompt)
        if soweit_gleich(antwort, "ja"):
            exit()
    except EOFError:
        return None
    except KeyboardInterrupt:
        return None            
    except SystemExit:
        if not sicherheitsabfrage:
            exit(0)
        elif sicherheitsabfrage:
            antwort = input(sicherungsfrage)
            if soweit_gleich(antwort, "ja"):
                exit(0)

def soweit_gleich(a, # ein String der ein Teilstring von b sein sollte
                  b, # ein String
                  fallunabhängig=True):
    """soweit gleich führt eine Überprüfung zweier Strings auf
Gleichheit aus, wobei beide von Anfang an - und bis zur Länge
von a geprüft werden.
Ist b kürzer als a, liegt ein Fehler vor, die Antwort könnte
niemals positiv ausfallen"""
    # Zuerst prüfen wir, das alle Grundvoraussetzungen zutreffen
    assert type(a) == str, "a muss ein String sein"
    assert type(b) == str, "b muss ein String sein"
    assert len(a) <= len(b), "a muss kleiner oder gleichlang wie b sein"
    # ist Gross-/Kleinschreibung nicht von Bedeutung,
    # wandle a und b in Grossbuchstaben um
    if fallunabhängig:
        a = a.upper()
        b = b.upper()
    # Nur wenn a eine Länge größer als 0 hat, macht eine Antwort Sinn
    if len(a) > 0:
        # Ist eine Antwort vorhanden, überprüfe ob sie von Anfang an mit
        # b über die gesamte Länge von a übereinstimmt
        if a == b[0:len(a)]:
            return True
        else:
            return False
    # Ist a leer, so teilen wir mit, das eine Antwort nicht möglich ist,
    # indem wir None zurückliefern
    else: 
        return None
