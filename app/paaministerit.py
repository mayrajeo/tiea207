import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import csv

#Hoitaa paaministerin tietojen hakemisen paaministerit.csv:sta
def hae_paaministeri(year):
    paaministeri_tiedot = []
    etsittava_vuosi = str(year)
    path = os.path.join(os.path.dirname(__file__), '../data/paaministerit.csv')

    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if etsittava_vuosi in row['vuosi']:
                paaministeri_tiedot.append(row['nimi'])
                paaministeri_tiedot.append(row['kuvan_url'])
                paaministeri_tiedot.append(row['tietoja_sivu'])
    return paaministeri_tiedot