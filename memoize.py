#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- py-python-command: "/usr/bin/python3"; -*-

"""
Filename:  memoize.py
Description:  Memo-Funktion als Python-Decorator
Version:  07.01.2015
Created:  07.01.2015
Revision:  none
Language: Python 3

Author:  Sascha K. Biermanns (Silberbogen), skkd.h4k1n9 AT yahoo PUNKT de
License:  ISC
Copyright (C)  2015, Sascha K. Biermanns

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

def memoize(f):
    '''Dekorator. Dient zur Beschleunigung von Funktionsausfrufen.'''
    memo = {}
    def helferlein(x):
        '''Funktion. Prüft ob das Ergebnis bekannt ist und gibt es zurück, oder veranlasst die Berechnung und speichert das Ergebnis.'''
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helferlein
