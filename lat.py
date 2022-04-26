from array import array
from calendar import prmonth
from encodings import utf_8
from fileinput import close
import sys
import os
import random
from turtle import position
from xml.dom.expatbuilder import Rejecter
import dependencies

#Main function latinskog
class main():
    def _start_():
        n = 10 
        ispit_latinski.nauci_me(n)
        ponvno = input("Zelis li jos: Da ili Ne : ")
        if ponvno == "Da":
            n = int(input("Koliko rijeci: "))
            ispit_latinski.nauci_me(n)

#Klasa svih stvari koje zna ispitat iz latinskog
class ispit_latinski():
    def nauci_me( koliko_trazis ):
        with open('dependencies/rijeci-lat.txt', encoding="utf-8") as latinski:
            with open("dependencies/rijeci-hrv.txt", encoding="utf-8") as hrvatina:
                rimljanin = latinski.readlines()
                tomson = hrvatina.readlines()

                print("Primjer 1: \namica,-ae,f.= prijateljica")
                print("Primjer 2: \nvoda= aqua,-ae,f.")

                k = int()
                ispitani = []
                broj_rijeci = len(rimljanin)-1
                misc.radnom_pitanje(broj_rijeci, ispitani)
                dependencies.misc.radnom_pitanje(broj_rijeci, ispitani)

                while k != koliko_trazis:
                    x = random.randint(0,1)
                    vrijednost = dependencies.misc.radnom_pitanje(broj_rijeci, ispitani)
                    if x==0: 
                        rijesenje = input(rimljanin[vrijednost] + "= ")
                    else:
                        rijesenje = input(tomson[vrijednost] + "= ")
                    faktor = ispit_latinski.cirni_rjesenje(x, rijesenje, vrijednost, tomson, rimljanin)
                    k = k + faktor
                    ispitani.append(vrijednost)

                    print("Moras ih rijesiti jos: ", koliko_trazis-k)

    def cirni_rjesenje(x, rijesenje, vrijednost, tomson, rimlanjin):
        if x==0 and rijesenje == tomson[vrijednost].replace("\n",""):
            print("točan" + "\n" + rimlanjin[vrijednost]+ "=" + tomson[vrijednost]) 
            print("\n")
            print(tomson[vrijednost])
            print(rijesenje)
            return 1

        elif x==1 and rijesenje == rimlanjin[vrijednost].replace("\n",""):
            print("točan" + "\n" + rimlanjin[vrijednost]+ "=" + tomson[vrijednost]) 
            print("\n")
            print(rimlanjin[vrijednost])
            print(rijesenje)
            return 1      
        else:
            print("kriv" + "\n" + rimlanjin[vrijednost]+ "=" + tomson[vrijednost]) 
            print("\n" + rimlanjin[vrijednost] + "\n" + tomson[vrijednost])
            print(rijesenje)
            return -1

#Klasa svih ostalih funkcija za latinski 
class misscelanious_latinski():
    def ocisti_rici():
        with open("dependencies/sporke_rici.txt", encoding='utf8') as set:
            neocisceno = set.readlines()
            cisto = []
            hrvatski = []
            latinski = []

            for i in range(len(neocisceno)):
                x = neocisceno[i].lower()
                problemi = ["\n", " "]
                x = dependencies.misc.zamijeni_str(x, problemi, ["–","="], ["-"]) 
                cisto.append(x)

            with open("dependencies/rijeci-hrv.txt", "a", encoding="utf-8") as hrvat:
                with open("dependencies/rijeci-lat.txt", "a", encoding="utf-8") as rimljanin:
                    for i in range(len(cisto)):   
                        x = cisto[i][::-1]
                        a, b = x.split("-", 1)
                        a = a[::-1]
                        b = b[::-1]
                        latinski.append(b)
                        hrvatski.append(a)
                    rimljanin.writelines("\n".join(latinski))
                    hrvat.writelines("\n".join(hrvatski))
        with open("dependencies/brojac_kreacija") as broj:
            seks = broj.readlines()
            n = int(seks[0])+1

        with open("dependencies/brojac_kreacija", "w") as broj:
            broj.write(str(n))

        os.replace("dependencies/sporke_rici.txt","smece/set_rici_broj"+str(n)+".txt")
        with open("dependencies/sporke_rici.txt", "w") as fp:
            fp.write(" ")
            pass
