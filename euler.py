#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- py-python-command: "/usr/bin/python3"; -*-
# Copyright (C) 2012 by Sascha Biermanns
# Die Lösungen zu den 50 Aufgaben Eulers
# Zu finden bei: http://projecteuler.net/

import pickle   # euler_12
import datetime # euler_19
import prime    # euler_23
import math     # euler_25

def addiere_ziffern(zahl):
    summe = 0
    while zahl > 0:
        summe += zahl % 10
        zahl //= 10
    return summe

def faktor(n):
    f = 1
    for x in range(1, n+1):
        f *= x
    return f

def fibonacciGenerator():
    f0, f1 = 0, 1
    while True:
        yield f0
        f0, f1 = f1, f0+f1
            
def permutation(orig_nums, n):
    nums = list(orig_nums)
    perm = []
    while len(nums):
        teiler = faktor(len(nums)-1)
        pos = n // teiler
        n %= teiler
        perm.append(nums[pos])
        nums = nums[0:pos] + nums[pos+1:]
    return perm

def primzahlGenerator():
    yield 2
    yield 3
    primzahlen = [2,3]
    i = 5
    while True:
        if all(i % p for p in primzahlen):
            primzahlen.append(i)
            yield i
        i += 2

def euler_01():
    "Add all the natural numbers below one thousand that are multiples of 3 or 5."
    summe = 0
    liste = []
    for i in range(1,1000):
        if not (i % 3):
            summe += i
            liste.append(i)
        elif not (i % 5):
            summe += i
            liste.append(i)
    print("Liste aller Zahlen:", liste)
    print("Summe:", summe,)
##Liste aller Zahlen: [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48, 50, 51, 54, 55, 57, 60, 63, 65, 66, 69, 70, 72, 75, 78, 80, 81, 84, 85, 87, 90, 93, 95, 96, 99, 100, 102, 105, 108, 110, 111, 114, 115, 117, 120, 123, 125, 126, 129, 130, 132, 135, 138, 140, 141, 144, 145, 147, 150, 153, 155, 156, 159, 160, 162, 165, 168, 170, 171, 174, 175, 177, 180, 183, 185, 186, 189, 190, 192, 195, 198, 200, 201, 204, 205, 207, 210, 213, 215, 216, 219, 220, 222, 225, 228, 230, 231, 234, 235, 237, 240, 243, 245, 246, 249, 250, 252, 255, 258, 260, 261, 264, 265, 267, 270, 273, 275, 276, 279, 280, 282, 285, 288, 290, 291, 294, 295, 297, 300, 303, 305, 306, 309, 310, 312, 315, 318, 320, 321, 324, 325, 327, 330, 333, 335, 336, 339, 340, 342, 345, 348, 350, 351, 354, 355, 357, 360, 363, 365, 366, 369, 370, 372, 375, 378, 380, 381, 384, 385, 387, 390, 393, 395, 396, 399, 400, 402, 405, 408, 410, 411, 414, 415, 417, 420, 423, 425, 426, 429, 430, 432, 435, 438, 440, 441, 444, 445, 447, 450, 453, 455, 456, 459, 460, 462, 465, 468, 470, 471, 474, 475, 477, 480, 483, 485, 486, 489, 490, 492, 495, 498, 500, 501, 504, 505, 507, 510, 513, 515, 516, 519, 520, 522, 525, 528, 530, 531, 534, 535, 537, 540, 543, 545, 546, 549, 550, 552, 555, 558, 560, 561, 564, 565, 567, 570, 573, 575, 576, 579, 580, 582, 585, 588, 590, 591, 594, 595, 597, 600, 603, 605, 606, 609, 610, 612, 615, 618, 620, 621, 624, 625, 627, 630, 633, 635, 636, 639, 640, 642, 645, 648, 650, 651, 654, 655, 657, 660, 663, 665, 666, 669, 670, 672, 675, 678, 680, 681, 684, 685, 687, 690, 693, 695, 696, 699, 700, 702, 705, 708, 710, 711, 714, 715, 717, 720, 723, 725, 726, 729, 730, 732, 735, 738, 740, 741, 744, 745, 747, 750, 753, 755, 756, 759, 760, 762, 765, 768, 770, 771, 774, 775, 777, 780, 783, 785, 786, 789, 790, 792, 795, 798, 800, 801, 804, 805, 807, 810, 813, 815, 816, 819, 820, 822, 825, 828, 830, 831, 834, 835, 837, 840, 843, 845, 846, 849, 850, 852, 855, 858, 860, 861, 864, 865, 867, 870, 873, 875, 876, 879, 880, 882, 885, 888, 890, 891, 894, 895, 897, 900, 903, 905, 906, 909, 910, 912, 915, 918, 920, 921, 924, 925, 927, 930, 933, 935, 936, 939, 940, 942, 945, 948, 950, 951, 954, 955, 957, 960, 963, 965, 966, 969, 970, 972, 975, 978, 980, 981, 984, 985, 987, 990, 993, 995, 996, 999]
##Summe: 233168

def euler_02():
    "By considering the terms in the Fibonacci sequenzuence whose values do not exceed four million, find the sum of the even-valued terms."
    fibgen = fibonacciGenerator()
    summe = 0
    x = next(fibgen)
    while x < 4000000:
        if not x % 2:
            summe += x
        x = next(fibgen)
    print("Summe:", summe)
##Summe: 4613732

def euler_03(zahl=600851475143):
    "Find the largest prime factor of a composite number."
    i = 2
    liste = []
    while i < zahl:
        while not zahl % i:
            zahl /= i
            liste.append(i)
        i += 1
    liste.append(i)
    print("Liste der Primfaktoren:", liste)
    print("Größter Primfaktor:", liste.pop())
##Liste der Primfaktoren: [71, 839, 1471, 6857]
##Größter Primfaktor: 6857

def euler_04():
    "Find the largest palindrome made from the produkt of two 3-digit numbers."
    palindrom = 0
    for i in range(999,100, -1):
        for j in range(i, 100, -1):
            zahl = i * j
            folge = str(zahl)
            if folge == folge[::-1]:
                if zahl > palindrom:
                    palindrom = zahl
    print("Lösung:", palindrom)
##Lösung: 906609

def euler_05():
    "What is the smallest number divisible by each of the numbers 1 to 20?"
    def ggt(a,b):
        "Ermittelt den größten gemeinsamen Teiler zweier Zahlen"
        return b and ggt(b, a % b) or a
    def kgv(a,b):
        "Ermittelt das kleinste gemeinsame Vielfache zweier Zahlen"
        return a * b / ggt(a,b)
    zahl = 1
    for i in range(2,21):
        zahl = kgv(zahl, i)
    print("Lösung:", int(zahl))
##Lösung: 232792560

def euler_06():
    "What is the difference between the sum of the squares and the square of the sums?"
    summe = 0
    quadratsumme = 0
    for i in range(1, 101):
        summe += i
        quadratsumme += i**2
    summenquadrat = summe**2
    print("(1+2+...+100)² =", summenquadrat)
    print("1²+2²+...+100² =", quadratsumme)
    print(summenquadrat, "-", quadratsumme, "=", summenquadrat-quadratsumme)
##(1+2+...+100)² = 25502500
##1²+2²+...+100² = 338350
##25502500 - 338350 = 25164150

def euler_07():
    "Find the 10001st prime."
    primzahl = primzahlGenerator()
    for x in range(10000):
        next(primzahl)
    x = next(primzahl)
    print("Lösung:", x)
##Lösung: 104743

def euler_08():
    "Discover the largest produkt of five consecutive digits in the 1000-digit number."
    zahl = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    n = 0    
    for i in range(0, len(zahl)-4):
        p = 1
        for j in range(i,i+5):
            p = p * int(zahl[j])
        if p > n:
            n = p
            liste = zahl[j-4:j+1]
    print("Lösung:", end=" ")
    for i in range(4):
        print(liste[i], end="*")
    print(liste[4], end="=")
    print(n)
##Lösung: 9*9*8*7*9=40824

def euler_09():
    "Find the only Pythagorean triplet, {a, b, c}, for which a + b + c = 1000."
    for a in range(1, 500):
         for b in range(a, 500):
             c = 1000 - a - b
             if c > b:
                 if a**2 + b**2 == c**2:
                     print("Pythagoras: %d²+%d²=%d² entspricht %d+%d=%d\n\nLösung: %d+%d+%d=%d" % (a,b,c,a**2,b**2,c**2,a,b,c,a+b+c))
                     break
##Pythagoras: 200²+375²=425² entspricht 40000+140625=180625
##Produkt von a*b*c=31875000
##Lösung: 200+375+425=1000

def euler_10():
    "Calculate the sum of all the primes below two million."
    sieb = [True] * 1999999 # Bitfeld mit einem Bit für jede Zahl
    def markiere(sieb, x):
        "Markiert mehrfache von Zahlen - und damit alle Zahlen, die keine Primzahlen sein können"
        for i in range(2*x, len(sieb), x):
            sieb[i] = False
    for x in range(2, int(len(sieb)**0.5)+1): # Reichweite von 2 bis zur (Wurzel von 1999999) + 1
        if sieb[x]:
            markiere(sieb, x)
    print("Lösung:", sum(i for i in range(2, len(sieb)) if sieb[i])) # Addition aller Längen, die Primzahlen symbolisieren
##Lösung: 142913828922

def euler_11():
    "What is the greatest product of four adjacent numbers on the same straight line in the 20 by 20 grid?"
    zahlen = (( 8, 2,22,97,38,15, 0,40, 0,75, 4, 5, 7,78,52,12,50,77,91, 8,),
              (49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48, 4,56,62, 0,),
              (81,49,31,73,55,79,14,29,93,71,40,67,53,88,30, 3,49,13,36,65,),
              (52,70,95,23, 4,60,11,42,69,24,68,56, 1,32,56,71,37, 2,36,91,),
              (22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80,),
              (24,47,32,60,99, 3,45, 2,44,75,33,53,78,36,84,20,35,17,12,50,),
              (32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70,),
              (67,26,20,68, 2,62,12,20,95,63,94,39,63, 8,40,91,66,49,94,21,),
              (24,55,58, 5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72,),
              (21,36,23, 9,75, 0,76,44,20,45,35,14, 0,61,33,97,34,31,33,95,),
              (78,17,53,28,22,75,31,67,15,94, 3,80, 4,62,16,14, 9,53,56,92,),
              (16,39, 5,42,96,35,31,47,55,58,88,24, 0,17,54,24,36,29,85,57,),
              (86,56, 0,48,35,71,89, 7, 5,44,44,37,44,60,21,58,51,54,17,58,),
              (19,80,81,68, 5,94,47,69,28,73,92,13,86,52,17,77, 4,89,55,40,),
              ( 4,52, 8,83,97,35,99,16, 7,97,57,32,16,26,26,79,33,27,98,66,),
              (88,36,68,87,57,62,20,72, 3,46,33,67,46,55,12,32,63,93,53,69,),
              ( 4,42,16,73,38,25,39,11,24,94,72,18, 8,46,29,32,40,62,76,36,),
              (20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74, 4,36,16,),
              (20,73,35,29,78,31,90, 1,74,31,49,71,48,86,81,16,23,57, 5,54,),
              ( 1,70,54,71,83,51,54,69,16,92,33,48,61,43,52, 1,89,19,67,48,))
    maximal = 0
    liste = []
    def tabelle(zahlen):
        "Generator, der die ganze Tabelle abarbeitet."
        for reihe in range(0, len(zahlen)-4):
            for spalte in range(0, len(zahlen[reihe])-4):
                for sequenz in abschnitt(zahlen, reihe, spalte):
                    yield sequenz
    def abschnitt(zahlen, reihe, spalte):
        "Generator, der alle 4 Sequenzen eines Abschnitts abarbeitet."
        # horizontale Reihe
        yield list(zahlen[i][spalte] for i in range(reihe, reihe+4))
        # vertikale Spalte
        yield list(zahlen[reihe][i] for i in range(spalte, spalte+4))
        # Diagonale von links oben nach rechts unten
        yield list(zahlen[reihe+i][spalte+i] for i in range(0,4))
        # Diagonale von rechts oben nach links unten
        yield list(zahlen[reihe+i][spalte-i] for i in range(0,4))
    def produkt(sequenz):
        "Liefert das Produkt einer überlieferten Sequenz."
        n = 1
        for x in sequenz:
            n *= x
        return n
    for sequenz in tabelle(zahlen): # Alle Sequenzen einer Tabelle abarbeiten ...
        n = produkt(sequenz)
        if n > maximal: # ... und die Sequenz mit dem höchsten Produkt festhalten
            maximal = n
            liste = sequenz        
    print("Lösung:", end=" ")
    for i in range(3):
        print(liste[i], end="*")
    print(liste[3], end="=")
    print(maximal)
##Lösung: 89*94*97*87=70600674

def euler_12():
    "What is the value of the first dreieck number to have over five hundred divisors?"
    for i in range(1, 1000000000):
        n = i * (i+1) // 2
        if prime.num_factors(n) > 500:
            print("Lösung:", n)
            break

def euler_13():
    "Find the first ten digits of the sum of one-hundred 50-digit numbers."
    print(str(sum((
        37107287533902102798797998220837590246510135740250,
        46376937677490009712648124896970078050417018260538,
        74324986199524741059474233309513058123726617309629,
        91942213363574161572522430563301811072406154908250,
        23067588207539346171171980310421047513778063246676,
        89261670696623633820136378418383684178734361726757,
        28112879812849979408065481931592621691275889832738,
        44274228917432520321923589422876796487670272189318,
        47451445736001306439091167216856844588711603153276,
        70386486105843025439939619828917593665686757934951,
        62176457141856560629502157223196586755079324193331,
        64906352462741904929101432445813822663347944758178,
        92575867718337217661963751590579239728245598838407,
        58203565325359399008402633568948830189458628227828,
        80181199384826282014278194139940567587151170094390,
        35398664372827112653829987240784473053190104293586,
        86515506006295864861532075273371959191420517255829,
        71693888707715466499115593487603532921714970056938,
        54370070576826684624621495650076471787294438377604,
        53282654108756828443191190634694037855217779295145,
        36123272525000296071075082563815656710885258350721,
        45876576172410976447339110607218265236877223636045,
        17423706905851860660448207621209813287860733969412,
        81142660418086830619328460811191061556940512689692,
        51934325451728388641918047049293215058642563049483,
        62467221648435076201727918039944693004732956340691,
        15732444386908125794514089057706229429197107928209,
        55037687525678773091862540744969844508330393682126,
        18336384825330154686196124348767681297534375946515,
        80386287592878490201521685554828717201219257766954,
        78182833757993103614740356856449095527097864797581,
        16726320100436897842553539920931837441497806860984,
        48403098129077791799088218795327364475675590848030,
        87086987551392711854517078544161852424320693150332,
        59959406895756536782107074926966537676326235447210,
        69793950679652694742597709739166693763042633987085,
        41052684708299085211399427365734116182760315001271,
        65378607361501080857009149939512557028198746004375,
        35829035317434717326932123578154982629742552737307,
        94953759765105305946966067683156574377167401875275,
        88902802571733229619176668713819931811048770190271,
        25267680276078003013678680992525463401061632866526,
        36270218540497705585629946580636237993140746255962,
        24074486908231174977792365466257246923322810917141,
        91430288197103288597806669760892938638285025333403,
        34413065578016127815921815005561868836468420090470,
        23053081172816430487623791969842487255036638784583,
        11487696932154902810424020138335124462181441773470,
        63783299490636259666498587618221225225512486764533,
        67720186971698544312419572409913959008952310058822,
        95548255300263520781532296796249481641953868218774,
        76085327132285723110424803456124867697064507995236,
        37774242535411291684276865538926205024910326572967,
        23701913275725675285653248258265463092207058596522,
        29798860272258331913126375147341994889534765745501,
        18495701454879288984856827726077713721403798879715,
        38298203783031473527721580348144513491373226651381,
        34829543829199918180278916522431027392251122869539,
        40957953066405232632538044100059654939159879593635,
        29746152185502371307642255121183693803580388584903,
        41698116222072977186158236678424689157993532961922,
        62467957194401269043877107275048102390895523597457,
        23189706772547915061505504953922979530901129967519,
        86188088225875314529584099251203829009407770775672,
        11306739708304724483816533873502340845647058077308,
        82959174767140363198008187129011875491310547126581,
        97623331044818386269515456334926366572897563400500,
        42846280183517070527831839425882145521227251250327,
        55121603546981200581762165212827652751691296897789,
        32238195734329339946437501907836945765883352399886,
        75506164965184775180738168837861091527357929701337,
        62177842752192623401942399639168044983993173312731,
        32924185707147349566916674687634660915035914677504,
        99518671430235219628894890102423325116913619626622,
        73267460800591547471830798392868535206946944540724,
        76841822524674417161514036427982273348055556214818,
        97142617910342598647204516893989422179826088076852,
        87783646182799346313767754307809363333018982642090,
        10848802521674670883215120185883543223812876952786,
        71329612474782464538636993009049310363619763878039,
        62184073572399794223406235393808339651327408011116,
        66627891981488087797941876876144230030984490851411,
        60661826293682836764744779239180335110989069790714,
        85786944089552990653640447425576083659976645795096,
        66024396409905389607120198219976047599490197230297,
        64913982680032973156037120041377903785566085089252,
        16730939319872750275468906903707539413042652315011,
        94809377245048795150954100921645863754710598436791,
        78639167021187492431995700641917969777599028300699,
        15368713711936614952811305876380278410754449733078,
        40789923115535562561142322423255033685442488917353,
        44889911501440648020369068063960672322193204149535,
        41503128880339536053299340368006977710650566631954,
        81234880673210146739058568557934581403627822703280,
        82616570773948327592232845941706525094512325230608,
        22918802058777319719839450180888072429661980811197,
        77158542502016545090413245809786882778948721859617,
        72107838435069186155435662884062257473692284509516,
        20849603980134001723930671666823555245252804609722,
        53503534226472524250874054075591789781264330331690,
    )))[0:10])


def euler_14():
    "Find the longest sequence using a starting number under one million."
    cache = { 1: 1 }
    def kette(cache, n):
        if not cache.get(n,0):
            if n % 2:
                cache[n] = 1 + kette(cache, 3*n + 1)
            else:
                cache[n] = 1 + kette(cache, n/2)
        return cache[n]
    m,n = 0,0
    for i in range(1, 1000000):
        c = kette(cache, i)
        if c > m:
            m,n = c,i
#    print("Länge:", cache[i])
    print("Lösung:", n)   
##Lösung: 837799

def euler_15():
    "Starting in the top left corner in a 20 by 20 grid, how many routes are there to the bottom right corner?"

    faktor40 = faktor(40)
    faktor20 = faktor(20)
    print("Lösung:", faktor40 // faktor20 // faktor20)    
##Lösung: 137846528820

def euler_16():
    "What is the sum of the digits of the number 2^1000?"

    zahl=2**1000
    print("2^1000 =",zahl)
    print("Summe aller Ziffern =", addiere_ziffern(zahl))
##2^1000 = 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
##Summe aller Ziffern = 1366
    
def euler_17():
    "How many letters would be needed to write all the numbers in words from 1 to 1000?"    
    worte = [
        (   1,  'one'      , ''     ),
        (   2,  'two'      , ''     ),
        (   3,  'three'    , ''     ),
        (   4,  'four'     , ''     ),
        (   5,  'five'     , ''     ),
        (   6,  'six'      , ''     ),
        (   7,  'seven'    , ''     ),
        (   8,  'eight'    , ''     ),
        (   9,  'nine'     , ''     ),
        (  10,  'ten'      , ''     ),
        (  11,  'eleven'   , ''     ),
        (  12,  'twelve'   , ''     ),
        (  13,  'thirteen' , ''     ),
        (  14,  'fourteen' , ''     ),
        (  15,  'fifteen'  , ''     ),
        (  16,  'sixteen'  , ''     ),
        (  17,  'seventeen', ''     ),
        (  18,  'eighteen' , ''     ),
        (  19,  'nineteen' , ''     ),
        (  20,  'twenty'   , ''     ),
        (  30,  'thirty'   , ''     ),
        (  40,  'forty'    , ''     ),
        (  50,  'fifty'    , ''     ),
        (  60,  'sixty'    , ''     ),
        (  70,  'seventy'  , ''     ),
        (  80,  'eighty'   , ''     ),
        (  90,  'ninety'   , ''     ),
        ( 100,  'hundred'  , 'and'  ),
        (1000,  'thousand' , 'and'  ),
    ]
    worte.reverse()
    def spell(n, worte):
        word = []
        while n > 0:
            for zahl in worte:
                if zahl[0] <= n:
                    div = n // zahl[0]
                    n = n % zahl[0]
                    if zahl[2]: word.append(' '.join(spell(div, worte)))
                    word.append(zahl[1])
                    if zahl[2] and n: word.append(zahl[2])
                    break
        return word
    print("Lösung:", sum(len(word) for n in range(1, 1001) for word in spell(n, worte)))
##Lösung: 21124

def euler_18():
    "Find the maximum sum travelling from the top of the dreieck to the base."
    dreieck = (
        (                            75,                             ),
        (                          95, 64,                           ),
        (                        17, 47, 82,                         ),
        (                      18, 35, 87, 10,                       ),
        (                    20,  4, 82, 47, 65,                     ),
        (                  19,  1, 23, 75,  3, 34,                   ),
        (                88,  2, 77, 73,  7, 63, 67,                 ),
        (              99, 65,  4, 28,  6, 16, 70, 92,               ),
        (            41, 41, 26, 56, 83, 40, 80, 70, 33,             ),
        (          41, 48, 72, 33, 47, 32, 37, 16, 94, 29,           ),
        (        53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,         ),
        (      70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,       ),
        (    91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,     ),
        (  63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,   ),
        ( 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23, ),
    )
    def pfad(dreieck, num):
        summe = dreieck[0][0]
        spalte = 0
        for reihe in range(1, len(dreieck)):
            if num % 2:
                spalte += 1
            num //= 2
            summe += dreieck[reihe][spalte]
        return summe
    print("Lösung", max(pfad(dreieck, n) for n in range(0, 16384)))    
##Lösung 1074

def euler_19():
    "How many sonntage fell on the first of the month during the twentieth century?"
    sonntage = 0
    for jahr in range(1901, 2001):
        for monat in range(1, 13):
            tag = datetime.date(jahr, monat, 1)
            if tag.weekday() == 6:
                sonntage += 1
    print("Lösung:", sonntage)    
##Lösung: 171

def euler_20():
    "Find the sum of digits in 100!"
    zahl = 1
    for i in range(1,100):
        zahl *= i
    print("Lösung:", addiere_ziffern(zahl))
##Lösung: 648

def euler_21():
    "Evaluate the sum of all amicable pairs under 10000."
    def teiler(n):
        return list(i for i in range(1, n//2+1) if not n % i)
    paar = dict( ((n, sum(teiler(n))) for n in range(1, 10000)) )
    print("Lösung:", sum(n for n in range(1, 10000) if paar.get(paar[n], 0) == n and paar[n] != n))    
##Lösung: 31626

def euler_22():
    "What is the total of all the name scores in the file of first names?"
    def worth(name):
        return sum(ord(letter) - ord('A') + 1 for letter in name)
    names = open('names.txt').read().replace('"', '').split(',')
    names.sort()
    print("Lösung:", sum((i+1) * worth(names[i]) for i in range(0, len(names))))    
##Lösung: 871198282


def euler_23():
    "Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."
    MAX = 28124
    prime._refresh(MAX/2)
    abundants = [n for n in range(1, MAX) if sum(prime.all_factors(n)) > n+n]
    abundants_dict = dict.fromkeys(abundants, 1)
    total = 0
    for n in range(1, MAX):
        sum_of_abundants = 0
        for a in abundants:
            if a > n:
                break
            if abundants_dict.get(n - a):
                sum_of_abundants = 1
                break
        if not sum_of_abundants:
            total += n
    print("Lösung:", total)    
##Lösung: 4179871

def euler_24():
    "What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"
    print("Lösung", ''.join(str(x) for x in permutation(range(0,10), 999999)))
##Lösung 2783915460

def euler_25():
    "What is the first term in the Fibonacci sequence to contain 1000 digits?"
    phi = (1 + pow(5, 0.5)) / 2
    c = math.log10(5) / 2
    logphi = math.log10(phi)
    n = 1
    while True:
        if n * logphi - c >= 999:
            print("Lösung:", n)
            break
        n += 1
##Lösung: 4782

def euler_26():
    "Find the value of d < 1000 for which 1/d contains the longest recurring cycle."
    def zyklus_länge(n):
        i = 1
        if not n % 2:
            return zyklus_länge(n // 2)
        if not n % 5:
            return zyklus_länge(n // 5)
        while True:
            if (pow(10, i) - 1) % n == 0:
                return i
            else:
                i += 1
    m = 0
    n = 0
    for d in range(1,1000):
        c = zyklus_länge(d)
        if c > m:
            m = c
            n = d
    print("Lösung:", n)    
##Lösung: 983

def euler_27():
    "Find a quadratic formula that produces the maximum number of primes for consecutive values of n."
    max_paar = (0,0,0)
    for a in range(-999, 1000):
        for b in range(max(2, 1-a), 1000): # b >= 2, a + b + 1 >= 2
            n, count = 0, 0
            while True:
                v = n*n + a*n + b
                prime._refresh(v)
                if prime.isprime(v):
                    count += 1
                else:
                    break
                n += 1
            if count > max_paar[2]:
                max_paar = (a,b,count)
    print("Lösung:", max_paar[0] * max_paar[1])   
##Lösung: -59231

def euler_28():
    "What is the sum of both diagonals in a 1001 by 1001 spiral?"
    diagonal = 1
    start = 1
    for width in range(3, 1002, 2):
        increment = width - 1
        count = increment * 4
        diagonal = diagonal + start * 4 + increment * 10
        start = start + count
    print("Lösung:", diagonal)    
##Lösung: 669171001

def euler_29():
    "How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?"
    terms = {}
    count = 0
    for a in range(2,101):
        for b in range(2,101):
            c = pow(a,b)
            if not terms.get(c, 0):
               terms[c] = 1
               count += 1
    print("Lösung:", count)
##Lösung: 9183

def euler_30():
    "Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."
    def power_of_digits(n, p):
        s = 0
        while n > 0:
            d = n % 10
            n //= 10
            s += pow(d, p)
        return s
    print("Lösung:", sum(n for n in range(2, 200000) if power_of_digits(n, 5) == n))
##Lösung: 443839

def euler_31():
    "Investigating combinations of English currency denominations."
    coins = (1, 2, 5, 10, 20, 50, 100, 200)
    def balance(pattern):
        return sum(coins[x]*pattern[x] for x in range(0, len(pattern)))
    def gen(pattern, coinnum, num):
        coin = coins[coinnum]
        for p in range(0, num//coin+1):
            newpat = pattern[:coinnum] + (p,)
            bal = balance(newpat)
            if bal > num: return
            elif bal == num:
                yield newpat
            elif coinnum < len(coins)-1:
                for pat in gen(newpat, coinnum+1, num):
                    yield pat
    print("Lösung:", sum(1 for pat in gen((), 0, 200)))
##Lösung: 73682

def euler_32():
    "Find the sum of all numbers that can be written as pandigital products."
    from combinatorics import permutations
    def num(l):
        s = 0
        for n in l:
            s = s * 10 + n
        return s
    product = {}
    x = list(range(1,10))
    for perm in permutations(x):
        for cross in range(1,4):            # Number can't be more than 4 digits
            for eq in range(cross+1, 6):    # Result can't be less than 4 digits
                a = num(perm[0:cross])
                b = num(perm[cross:eq])
                c = num(perm[eq:9])
                if a * b == c:
                    product[c] = 1
    print("Lösung:", sum(p for p in product))
##Lösung: 45228

def euler_33():
    "Discover all the fractions with an unorthodox cancelling method."
    def brüche():
        for zähler in map(str, range(10, 100)):
            for nenner in map(str, range(int(zähler)+1, 100)):
                if zähler == nenner:
                    continue
                if zähler[1] == nenner[1] and zähler[1] == '0':
                    continue
                if zähler[0] == nenner[0] and int(zähler) * int(nenner[1]) == int(nenner) * int(zähler[1]):
                    yield(int(zähler), int(nenner))
                if zähler[0] == nenner[1] and int(zähler) * int(nenner[0]) == int(nenner) * int(zähler[1]):
                    yield(int(zähler), int(nenner))
                if zähler[1] == nenner[1] and int(zähler) * int(nenner[0]) == int(nenner) * int(zähler[0]):
                    yield(int(zähler), int(nenner))
                if zähler[1] == nenner[0] and int(zähler) * int(nenner[1]) == int(nenner) * int(zähler[0]):
                    yield(int(zähler), int(nenner))
    def ggt(a,b):
        return b and ggt(b, a % b) or a
    zähler = 1
    nenner = 1
    for bruch in brüche():
        zähler = zähler * bruch[0]
        nenner = nenner * bruch[1]
    g = ggt(zähler, nenner)
    print("Lösung:", nenner // g)    
##Lösung: 100

def euler_34():
    "Find the sum of all numbers which are equal to the sum of the factorial of their digits."
    fact = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)
    def sum_of_digits_factorial(n):
        s = 0
        while n > 0:
            d = n % 10
            s += fact[d]
            n //= 10
        return s
    print("Lösung:", sum(n for n in range(10, 100000) if n == sum_of_digits_factorial(n)))    
##Lösung: 40730

def euler_35():
    "How many circular primes are there below one million?"
    sieb = [True] * 1000000
    sieb[0] = sieb[1] = False
    def mark(sieb, x):
        for i in range(x+x, len(sieb), x):
            sieb[i] = False
    for x in range(2, int(len(sieb) ** 0.5) + 1):
        mark(sieb, x)
    def circular(n):
        ziffern = []
        while n > 0:
            ziffern.insert(0, str(n % 10))
            n //= 10
        for d in range(1, len(ziffern)):
            yield int(''.join(ziffern[d:] + ziffern[0:d]))
    count = 0
    for n, p in enumerate(sieb):
        if p:
            iscircularprime = True
            for m in circular(n):
                if not sieb[m]:
                    iscircularprime = False
                    break
            if iscircularprime:
                count += 1
    print("Lösung:", count)
##Lösung: 55


def euler_36():
    "Find the sum of all numbers less than one million, which are palindromic in base 10 and base 2."
    def ispalindrome(n, base):
        ziffern = []
        rückwärts = []
        while n > 0:
            d = str(n % base)
            ziffern.append(d)
            rückwärts.insert(0, d)
            n //= base
        return ziffern == rückwärts
    print("Lösung:", sum(n for n in range(1, 1000000) if ispalindrome(n, 10) and ispalindrome(n, 2)))
##Lösung: 872187

def euler_37():
    "Find the sum of all eleven primes that are both truncatable from left to right and right to left."
    digits = range(0, 10)
    prime_digits = (2, 3, 5, 7)
    def num(l):
        s = 0
        for n in l:
            s = s * 10 + n
        return s
    def is_left_truncatable(l):
        is_truncatable = 1
        for size in range(1, len(l)+1):
            n = num(l[:size])
            prime._refresh(int(math.sqrt(n)))
            if not prime._isprime(n):
                is_truncatable = 0
                break
        return is_truncatable
    def is_right_truncatable(l):
        is_truncatable = 1
        for size in range(0, len(l)):
            n = num(l[size:])
            prime._refresh(int(math.sqrt(n)))
            if not prime._isprime(n):
                is_truncatable = 0
                break
        return is_truncatable
    def gen(result, number):
        if len(number) > 6: return
        number = list(number)
        number.append('')
        for digit in digits:
            number[-1] = digit
            if is_left_truncatable(number):
                if is_right_truncatable(number) and len(number) > 1:
                    result.append(num(number))
                gen(result, number)
    result = []
    gen(result, [])
    print(result)
    print("Lösung:", sum(result))
##[23, 313, 3137, 317, 37, 373, 3797, 53, 73, 739397, 797]
##Lösung: 748317    

def euler_38():
    "What is the largest 1 to 9 pandigital that can be formed by multiplying a fixed number by 1, 2, 3, ... ?"
    def get_pandigital(n):
        pandigital = ''
        for x in range(1, 10):
            pandigital += str(x * n)
            if len(pandigital) >= 9:
                break
        if len(pandigital) == 9 and sorted(dict.fromkeys(list(pandigital)).keys()) == list("123456789"):
            return pandigital
        else:
            return ''
    max = 0
    for n in range(1, 10000):
        p = get_pandigital(n)
        if p:
            if int(p) > max:
                max = int(p)
    print("Lösung:", max)    
##Lösung: 932718654

def euler_39():
    "If p is the perimeter of a right angle triangle, {a, b, c}, which value, for p ≤ 1000, has the most solutions?"
    maxp, maxsol = 0, 0
    for p in range(12, 1001, 2):
        solutions = 0
        # a < b < c. So a is at most 1/3 of p. b is between a and (p-a)/2
        for a in range(1, p//3):
            a2 = a*a
            for b in range(a, (p-a)//2):
                c = p - a - b
                if a2 + b*b == c*c:
                    solutions = solutions + 1
        if solutions > maxsol:
            maxp, maxsol = p, solutions
    print("Lösung:", maxp)    
##Lösung: 840

def euler_40():
    "Finding the nth digit of the fractional part of the irrational number."
    def digit_at(n):
        digits = 1
        n = n - 1
        while True:
            numbers = 9 * pow(10, digits-1) * digits
            if n > numbers:
                n -= numbers
            else:
                break
            digits = digits + 1
        num = n // digits + pow(10, digits-1)
        return int(str(num)[n % digits])
    print("Lösung:", digit_at(1) * digit_at(10) * digit_at(100) * digit_at(1000) * digit_at(10000) * digit_at(100000) * digit_at(1000000))
##Lösung: 210

def euler_41():
    "What is the largest n-digit pandigital prime that exists?"
    from combinatorics import permutations
    # Pan-digital primes are 4 or 7 digits. Others divisible by 3
    prime._refresh(2766)    # sqrt(7654321)
    x = list(range(7, 0, -1))
    for perm in permutations(x):
        num = 0
        for n in perm:
            num = num * 10 + n
        if prime._isprime(num):
            print("Lösung:", num)
            break
##Lösung: 7652413

def euler_42():
    "How many triangle words does the list of common English words contain?"
    def worth(word):
        return sum(ord(letter) - ord('A') + 1 for letter in word)
    words = open('words.txt').read().replace('"', '').split(',')
    triangle_numbers = dict.fromkeys(list(n*(n+1)/2 for n in range(1, 100)), 1)
    print("Lösung:", sum(1 for word in words if worth(word) in triangle_numbers))
##Lösung: 162

def euler_43():
    "Find the sum of all pandigital numbers with an unusual sub-string divisibility property."
    from combinatorics import permutations
    def num(l):
        s = 0
        for n in l:
            s = s * 10 + n
        return s
    def subdiv(l, n):
        return not num(l) % n
    total = 0
    for perm in permutations((0,1,2,3,4,6,7,8,9)):
        perm.insert(5, 5)               # d6 must be 5
        if (subdiv(perm[7:10], 17) and
            subdiv(perm[6:9],  13) and
            subdiv(perm[5:8],  11) and
            subdiv(perm[4:7],   7) and
            subdiv(perm[3:6],   5) and
            subdiv(perm[2:5],   3) and
            subdiv(perm[1:4],   2)):
                total += num(perm)
    print("Lösung:", total)    
##Lösung: 16695334890

def euler_44():
    "Find the smallest pair of pentagonal numbers whose sum and difference is pentagonal."
    MAX = 2000
    pent = [ n * (3*n - 1) // 2 for n in range(1, 2*MAX) ]
    pdic = dict.fromkeys(pent)
    def main2():
        for j in range(0, MAX):
            for k in range(j+1, 2*MAX-1):
                p_j = pent[j]
                p_k = pent[k]
                p_sum = p_j + p_k
                p_diff = p_k - p_j
                if p_sum in pdic and p_diff in pdic:
                    return p_diff
    print("Lösung:", main2())
##Lösung: 5482660

def euler_45():
    "After 40755, what is the next triangle number that is also pentagonal and hexagonal?"
    MAX = 100000
    triangle = [ n * (  n + 1) // 2 for n in range(0, MAX) ]
    pentagon = [ n * (3*n - 1) // 2 for n in range(0, MAX) ]
    hexagon  = [ n * (2*n - 1)     for n in range(0, MAX) ]
    pentagon_dict = dict.fromkeys(pentagon, 1)
    hexagon_dict  = dict.fromkeys(hexagon, 1)
    for t in range(286, MAX):
        v = triangle[t]
        if v in pentagon_dict and v in hexagon_dict:
            print("Lösung:", v)
            break
##Lösung: 1533776805

def euler_46():
    "What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?"
    MAX = 10000
    squares = dict.fromkeys((x**2 for x in range(1, MAX)), 1)
    prime._refresh(MAX)
    for x in range(35, MAX, 2):
        if not prime.isprime(x):
            is_goldbach = False
            for p in prime.prime_list[1:]:
                if p >= x:
                    break
                if (x-p)//2 in squares:
                    is_goldbach = True
                    break
            if not is_goldbach:
                print("Lösung:", x)
                break
##Lösung: 5777

def euler_47():
    "Find the first four consecutive integers to have four distinct primes factors."
    def distinct_factors(n):
        return len(dict.fromkeys(prime.factors(n)).keys())
    factors = [0, 1, distinct_factors(2), distinct_factors(3)]
    while True:
        if factors[-4::] == [4,4,4,4]:
            break
        else: factors.append(distinct_factors(len(factors)))
    print("Lösung:", len(factors)-4)
##Lösung: 134043

def euler_48():
    "Find the last ten digits of 11 + 22 + ... + 10001000."
    s = 0
    mod = pow(10, 10)
    for x in range(1, 1001):
        s += pow(x, x)
    print("Lösung:", s % mod)
##Lösung: 9110846700

def euler_49():
    "Find arithmetic sequences, made of prime terms, whose four digits are permutations of each other."
    from combinatorics import permutations
    prime._refresh(10000)
    for num in range(1000, 10000):
        if str(num).find('0') >= 0:
            continue
        if prime.isprime(num):
            prime_permutations = { num: 1 }
            for x in permutations(list(str(num))):
                next_num = int(''.join(x))
                if prime.isprime(next_num):
                    prime_permutations[next_num] = 1
            primes = sorted(prime_permutations.keys())
            for a in range(0, len(primes)):
                if primes[a] == 1487:
                    continue
                for b in range(a+1, len(primes)):
                    c = (primes[a] + primes[b]) // 2
                    if c in prime_permutations:
                        print("Lösung:", str(primes[a]) + str(c) + str(primes[b]))
                        return
##Lösung: 296962999629

def euler_50():
    "Which prime, below one-million, can be written as the sum of the most consecutive primes?"
    MAX = 5000
    prime.prime(MAX)
    def check_length(n, below):
        maxprime = 0
        for x in range(0, below):
            total = sum(prime.prime_list[x:x+n])
            if total > below:
                break
            if prime.isprime(total):
                maxprime = total
        return maxprime
    for n in range(1000, 0, -1):
        maxprime = check_length(n, 1000000)
        if maxprime:
            print("Lösung:", maxprime)
            break
##Lösung: 997651

def euler_51():
    "Find the smallest prime which, by changing the same part of the number, can form eight different primes."
    from combinatorics import uniqueCombinations
    cache = {}
    def prime_family_length(n, digits):
        if (n, digits) in cache:
            return cache[n, digits]
        num, nums, count = list(str(n)), [], 0
        if len(dict.fromkeys(num[d] for d in digits).keys()) > 1:
            return cache.setdefault((n, digits), 0)                                # The digits must have the same number
        for d in range(0 in digits and 1 or 0, 10):                                 # Ensure 0 is not the first digit
            for x in digits:
                num[x] = str(d)
            n = int(''.join(num))
            if prime.isprime(n):
                count += 1
            nums.append(n)
        for n in nums:
            cache[n, digits] = count
        return count
    prime._refresh(100000)
    n, max, max_count, combos = 10, 0, 0, {}
    while max_count < 8:
        p = prime.prime(n)
        digits = range(0, len(str(p)))
        for size in range(1, len(digits)):
            patterns = combos.setdefault((len(digits), size),
                tuple(tuple(sorted(p)) for p in uniqueCombinations(digits, size)))
            for pat in patterns:
                count = prime_family_length(p, pat)
                if count > max_count: max, max_count = p, count
        n += 1
    print("Lösung:",p)
##Lösung: 121313

def euler_52():
    "Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits in some order."
    def multiples_have_same_digits(n):
        digit_keys = dict.fromkeys(list(str(n)))
        for x in range(2, 4):
            for d in list(str(x * n)):
                if not d in digit_keys:
                    return False
        return True
    n = 0
    while True:
        n += 9                           # n must be a multiple of 9 for this to happen
        if multiples_have_same_digits(n):
            print("Lösung:", n)
            break
##Lösung: 142857

def euler_53():
    "How many values of C(n,r), for 1 ≤ n ≤ 100, exceed one-million?"
    fact_c = { 0: 1, 1: 1 }
    def fact(n):
        return n in fact_c and fact_c[n] or fact_c.setdefault(n, n * fact(n-1))
    count = 0
    for n in range(1, 101):
        for r in range(0, n):
            ncr = fact(n) / fact(r) / fact(n-r)
            if ncr > 1000000:
                count += 1
    print("Lösung:", count)
##Lösung: 4075

def euler_54():
    "How many hands did player one win in the game of poker?"
    value = { '2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'T':10,'J':11,'Q':12,'K':13,'A':14 }
    all_kinds = tuple(reversed(sorted(value.values())))
    all_suits = list('DCSH')

    def make_hand(cards):
        hand = {}
        for card in cards:
            hand.setdefault(value[card[0]], {})[card[1]] = 1
            hand.setdefault(card[1], {})[value[card[0]]] = 1
        return hand

    def get(hash, arr):
        return ((i, hash.get(i, {})) for i in arr)
    def has(hash, arr):
        return not sum(1 for i in arr if i not in hash)

    def rank(hand):
        # Royal flush
        for suit, kinds in get(hand, all_suits):
            if has(kinds, tuple('TJQKA')):
                return (9,)

        # Straight flush
        for suit, kinds in get(hand, all_suits):
            kinds = sorted(kind for kind in kinds.keys())
            if len(kinds) == 5 and kinds[4] - kinds[0] == 4:
                return (8, kinds[0])

        # Four of a kind
        for kind, suits in get(hand, all_kinds):
            if len(suits.keys()) == 4:
                return (7, kind)

        # Full house
        for kind, suits in get(hand, all_kinds):
            if len(suits.keys()) == 3:
                for kind2, suits2 in get(hand, all_kinds):
                    if len(suits2.keys()) == 2:
                        return (6, kind, kind2)

        # Flush
        for suit, kinds in get(hand, all_suits):
            if len(kinds.keys()) == 5:
                return (5,)

        # Straight
        kinds = sorted(kind for kind in all_kinds if kind in hand)
        if len(kinds) == 5 and kinds[4] - kinds[0] == 4:
            return (4, kinds[0])

        # Three of a kind
        for kind, suits in get(hand, all_kinds):
            if len(suits.keys()) == 3:
                return (3, kind)

        # Two pairs
        for kind, suits in get(hand, all_kinds):
            if len(suits.keys()) == 2:
                for kind2, suits2 in get(hand, all_kinds):
                    if kind != kind2 and len(suits2.keys()) == 2:
                        return (2, kind, kind2)

        # One pair
        for kind, suits in get(hand, all_kinds):
            if len(suits.keys()) == 2:
                return (1, kind)

        for kind in all_kinds:
            if kind in hand:
                return (0, kind)
        return 0

    count = 0
    for hand in open('poker.txt'):
        hands = hand.split(' ')
        p1, p2 = make_hand(hands[0:5]), make_hand(hands[5:10])
        v1, v2 = rank(p1), rank(p2)
        if v1 > v2:
            count += 1
    print("Lösung:", count)
##Lösung: 376

def euler_55():
    "How many Lychrel numbers are there below ten-thousand?"
    def is_lychrel(n):
        n = str(n)
        for count in range(0, 50):
            n = str(int(n) + int(n[::-1]))
            if n == n[::-1]:
                return False
        return True
    print("Lösung:", sum(1 for n in range(0, 10000) if is_lychrel(n)))
##Lösung: 249

def euler_56():
    "Considering natural numbers of the form, ab, finding the maximum digital sum."
    max = 0
    for a in range(0, 100):
        for b in range(0, 100):
            ds = sum(int(digit) for digit in str(a**b))
            if ds > max:
                max = ds
    print("Lösung:", max)
##Lösung: 972

def euler_57():
    "Investigate the expansion of the continued fraction for the square root of two."
    num, den, count = 3, 2, 0
    for iter in range(0, 1000):
        num, den = num + den + den, num + den
        if len(str(num)) > len(str(den)):
            count += 1
    print("Lösung:", count)
##Lösung: 153

def euler_58():
    "Investigate the number of primes that lie on the diagonals of the spiral grid."
    prime._refresh(50000)
    width, diagonal, base, primes = 1, 1, 1, 0
    while True:
        width += 2
        increment = width - 1
        for i in range(0, 4):
            diagonal = diagonal + increment
            if i < 3 and prime._isprime(diagonal):
                primes += 1
        base = base + 4
        if primes * 10 < base:
            print("Lösung:", width)
            break
##Lösung: 26241

def euler_59():
    "Using a brute force attack, can you decrypt the cipher using XOR encryption?"
    from combinatorics import selections
    code = tuple(int(c) for c in open('cipher1.txt').read().split(','))
    def decrypt(code, password):
        l = len(password)
        return tuple(c ^ password[i % l] for i, c in enumerate(code))
    def text(code):
        return ''.join(chr(c) for c in code)
    n = 0
    for password in selections(tuple((ord(c) for c in list('abcdefghijklmnopqrstuvwxyz'))), 3):
        c = decrypt(code, password)
        t = text(c)
        if t.find(' the ') > 0:
            print("Text:", t)
            print("Lösung:", sum(c))
            break
##Text: (The Gospel of John, chapter 1) 1 In the beginning the Word already existed. He was with God, and he was God. 2 He was in the beginning with God. 3 He created everything there is. Nothing exists that he didn't make. 4 Life itself was in him, and this life gives light to everyone. 5 The light shines through the darkness, and the darkness can never extinguish it. 6 God sent John the Baptist 7 to tell everyone about the light so that everyone might believe because of his testimony. 8 John himself was not the light; he was only a witness to the light. 9 The one who is the true light, who gives light to everyone, was going to come into the world. 10 But although the world was made through him, the world didn't recognize him when he came. 11 Even in his own land and among his own people, he was not accepted. 12 But to all who believed him and accepted him, he gave the right to become children of God. 13 They are reborn! This is not a physical birth resulting from human passion or plan, this rebirth comes from God.14 So the Word became human and lived here on earth among us. He was full of unfailing love and faithfulness. And we have seen his glory, the glory of the only Son of the Father.
##Lösung: 107359
