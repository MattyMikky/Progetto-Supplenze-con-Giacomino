# print("Hello Mondus") a caso ahhaha
# from database import quelche è...

'''
I professori che hanno ore di supplenza sono:
Agazzi, Amantea, Benes, Bonini, Brigante, Cecchetto, 
Chiandussi, Coronica, Costessi, Epicoco, Faganel, Floris,
Iacono, Magno, Selva Mirizzi, Selva Patrizia, Ziccolella
'''


Agazzi = [14, 31, 35, 44, 51]
Amantea = [43]
Benes = [12, 15, 24, 42, 43, 44]
Bonini = [25, 36, 37, 45, 55]
Brigante = [26, 27, 44]
Cecchetto = [12, 13, 22, 23]
Chiandussi = [44, 51, 52]
Coronica = [12, 13, 21, 22, 24, 25, 53, 54]
Costessi = [32, 35]
Epicoco = [13, 27, 42, 43, 44, 52, 54, 55]
Faganel = [13, 16, 31, 34, 35, 42, 43]
Floris = [14, 15, 23, 33, 34, 35, 43, 45, 46, 54, 55, 56]
Iacono = [22, 36, 54, 55]
Magno = [31, 32, 52]
SelvaMirizzi = [13, 15, 24, 25, 32, 45, 52, 54]
SelvaPatrizia = [13, 33, 45]
Ziccolella = [11, 14, 23, 24, 41, 51, 53]

par = 0

# Raccolta dell'input dell'utente

ErroreD1 = "Non hai inserito un giorno della settimana"
ErroreD2 = "Inserisci l'ora di supplenza"
ErroreG = "Il giorno inserito non va bene, prova ad inserire un giorno tra lunedì e venerdì"

try:
    dom1 = str(input(
        "In che giorno serve la supplenza? --> Inserisci un giorno della settimana \n\n"))
except TypeError:
    exit(ErroreD1)
except ValueError:
    exit(ErroreD1)
except SyntaxError:
    exit(ErroreD1)
try:
    dom2 = int(input(
        "A che ore serve la supplenza? --> Inserisci un ora, ad esempio 1, 2, 3, ecc. \n\n"))
except ValueError:
    exit(ErroreD2)
except TypeError:
    exit(ErroreD2)
except SyntaxError:
    exit(ErroreD2)


# Controllo giorno inserito e somma con il numero dell'ora
ErroreG = "Il giorno inserito non va bene, prova ad inserire un giorno tra lunedì e venerdì"

if dom1 == "Lunedì" or dom1 == "lunedì" or dom1 == "Lunedi" or dom1 == "lunedi":
    par = 10 + dom2
elif dom1 == "Martedì" or dom1 == "martedì" or dom1 == "Martedi" or dom1 == "martedi":
    par = 20 + dom2
elif dom1 == "Mercoldì" or dom1 == "mercoldì" or dom1 == "Mercoldi" or dom1 == "mercoledi":
    par = 30 + dom2
elif dom1 == "Giovedì" or dom1 == "giovedì" or dom1 == "Giovedi" or dom1 == "giovedi":
    par = 40 + dom2
elif dom1 == "Venerdì" or dom1 == "venerdì" or dom1 == "Venerdi" or dom1 == "venerdi":
    par = 50 + dom2
else:
    exit(ErroreG)

# Stampa a video dei professori disponibili per la supplenza

    print("")

if par in Agazzi:
    print("Agazzi")
if par in Amantea:
    print("Amantea")
if par in Benes:
    print("Benes")
if par in Bonini:
    print("Bonini")
if par in Brigante:
    print("Brigante")
if par in Cecchetto:
    print("Cecchetto")
if par in Chiandussi:
    print("Chiandussi")
if par in Coronica:
    print("Coronica")
if par in Costessi:
    print("Costessi")
if par in Epicoco:
    print("Epicoco")
if par in Faganel:
    print("Faganel")
if par in Floris:
    print("Floris")
if par in Iacono:
    print("Iacono")
if par in Magno:
    print("Magno")
if par in SelvaMirizzi:
    print("Selva Mirizzi")
if par in SelvaPatrizia:
    print("Selva Patrizia")
if par in Ziccolella:
    print("Ziccolella")

print("")

'''
I professori che hanno ore in compresenza sono:
Aceto, Di Mattia, Dreossi, Maggio, Marchesan Mattea,
Miani, Morelli, Nazzareno, Pierdomenico, Rieppi, Vescovi
'''

AcetoFurlan = [16, 41, 42]
DiMattiaVinci = [11, 15, 16, 41, 42, 54, 55, 56]
DiMattiaLapira = [13, 14]
DiMattiaApollo = [35, 36]
DreossiCrachi = [14, 15, 16, 44, 45, 46]
DreossiColautti = [21, 22, 34, 35]
DreossiZanin = [23, 24, 53, 54]
DreossiAlbaneseMichele = [31, 32]
DreossiFaraone = [41, 42]
MaggioErsetig = [11, 12, 15, 16, 36, 51]
MaggioLeonardi = [14]
MaggioCacciatore = [53, 54]
MarchesanMatteaBuiatti = [11, 12, 25, 26, 27, 28, 46, 54]
MarchesanMatteaGardenal = [13, 14, 44, 45, 55, 56]
MarchesanMatteaCrachi = [33, 34]
MarchesanMatteaColautti = [41, 42]
MianiBertogna = [13, 34, 41, 42, 51, 52, 53]
MianiTerrosi = [15, 16]
MianiVassallo = [21, 22, 23]
MianiStano = [24, 25, 33, 36, 43, 54]
MorelliFaraone = [11, 12, 13, 15, 16, 21, 31, 32, 51]
MorelliGardenal = [23, 52, 53]
MorelliManià = [34, 35, 55]
MorelliBuiatti = [41, 42, 56]
NazzarenoLapira = [24, 25, 27, 28]
NazzarenoMarchesanMauro = [26, 52]
NazzarenoManiacco = [33, 34, 41]
PierdomenicoApollo = [11, 25, 26]
PierdomenicoVinci = [13, 14, 44, 45]
PierdomenicoLapira = [15, 33, 34, 51, 52]
PierdomenicoMarchesanMauro = [22, 23, 32, 35, 36, 46]
RieppiMasau = [13, 14, 15, 16, 55, 56]
RieppiDiMaso = [21, 22, 23, 24, 43]
RieppiPapa = [35, 36]
RieppiFurlan = [44, 45, 51, 53, 54]
VescoviColautti = [12, 13, 14]
VescoviZanin = [15, 31, 32, 33, 51, 52]
VescoviManià = [21, 22, 24, 25, 41, 42, 43]
VescoviCrachi = [53, 54]

dom3 = str(input(
    "Vuoi anche sapere quali professori stanno facendo lezioni in compresenza? \n\n"))


print("")


# Controllo se la risposta inserita va bene
while dom3 != "Sì" and dom3 != "Si" and dom3 != "sì" and dom3 != "si" and dom3 != "No" and dom3 != "no":
    print('La risposta inserita non va bene. Inserire "si" o "no"')
    dom3 = str(input())

while dom3 != "Sì" and dom3 != "Si" and dom3 != "sì" and dom3 != "si" and dom3 != "No" and dom3 != "no":
    dom3 = str(input())

# Se viene inserito "No" il programma finisce
if dom3 == "No" or dom3 == "no":
    print("Ok. Buona giornata ")

# Stampa a video dei professori che stanno facendo lezioni in compresenza
if dom3 == "Sì" or dom3 == "Si" or dom3 == "sì" or dom3 == "si":
    if par in AcetoFurlan:
        print("Aceto e Furlan")
    if par in DiMattiaVinci:
        print("Di Mattia e Vinci")
    if par in DiMattiaLapira:
        print("Di Mattia e Lapira")
    if par in DiMattiaApollo:
        print("Di Mattia e Apollo")
    if par in DreossiCrachi:
        print("Dreossi e Crachi")
    if par in DreossiColautti:
        print("Dreossi e Colautti")
    if par in DreossiZanin:
        print("Dreossi e Zanin")
    if par in DreossiAlbaneseMichele:
        print("Dreossi e Albanese Michele")
    if par in DreossiFaraone:
        print("Dreossi e Faraone")
    if par in MaggioErsetig:
        print("Maggio e Ersetig")
    if par in MaggioLeonardi:
        print("Maggio e Leonardi")
    if par in MaggioCacciatore:
        print("Maggio e Cacciatore")
    if par in MarchesanMatteaBuiatti:
        print("Marchesan Mattea e Buiatti")
    if par in MarchesanMatteaGardenal:
        print("Marchesan Mattea e Gardenal")
    if par in MarchesanMatteaCrachi:
        print("Marchesan Mattea e Crachi")
    if par in MarchesanMatteaColautti:
        print("Marchesan Mattea e Colautti")
    if par in MianiBertogna:
        print("Miani e Bertogna")
    if par in MianiTerrosi:
        print("Miani e Terrosi")
    if par in MianiVassallo:
        print("Miani e Vassallo")
    if par in MianiStano:
        print("Miani e Stano")
    if par in MorelliFaraone:
        print("Morelli e Faraone")
    if par in MorelliGardenal:
        print("Morelli e Gardenal")
    if par in MorelliManià:
        print("Morelli e Manià")
    if par in MorelliBuiatti:
        print("Morelli e Buiatti")
    if par in NazzarenoLapira:
        print("Nazzareno e Lapira")
    if par in NazzarenoMarchesanMauro:
        print("Nazzareno e Marchesan Mauro")
    if par in NazzarenoManiacco:
        print("Nazzareno e Maniacco")
    if par in PierdomenicoApollo:
        print("Pierdomenico e Apollo")
    if par in PierdomenicoVinci:
        print("Pierdomenico e Vinci")
    if par in PierdomenicoLapira:
        print("Pierdomenico e Lapira")
    if par in PierdomenicoMarchesanMauro:
        print("Pierdomenico e Marchesan Mauro")
    if par in RieppiMasau:
        print("Rieppi e Masau")
    if par in RieppiDiMaso:
        print("Rieppi e Di Maso")
    if par in RieppiPapa:
        print("Rieppi e Papa")
    if par in RieppiFurlan:
        print("Rieppi e Furlan")
    if par in VescoviColautti:
        print("Vescovi e Colautti")
    if par in VescoviZanin:
        print("Vescovi e Zanin")
    if par in VescoviManià:
        print("Vescovi e Manià")
    if par in VescoviCrachi:
        print("Vescovi e Crachi")


print("\n\nPremere invio per chiudere il programma.\n\n")

input()
