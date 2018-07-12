#import sys
import time
print ("********************************************************************************")
print ("********************************************************************************")
r=3
while r!=1 and r!=2:
    r=eval(input("  to continue in english  : press (1) ** ** to continue in french : press (2)\n "))
    if r==1:
        m=(input("what's your name : \n"))

        a=eval(input("how old are you : \n"))

        n=(input("are you male or female: \n"))

        c=(input( "where are you from \n(casablanca, rabat,marakach):"))
        print("wait ...")
        while c!="rabat" or c!="casablanca" or c!="marakach":
            if c=="rabat" or c=="casablanca" or c=="marakach":
                time.sleep(5)
                print("*******************************************************************************")
                print("*******************************************************************************")
                print ("to use docfinder you must follow these steps:")
                print("wait ...")
                time.sleep(4)
                print("first step : ")
                print("     choose your city.")
                time.sleep(4)
                print("second step")
                print("     choose the nearest clinic.")
                time.sleep(4)
                print("third step")
                print("     check that the doctor is present.")
                time.sleep(4)
                print("fourth step")
                print("     chec the number of patients with doctor.")
                time.sleep(4)
                print ("to go directly to DOCFINDER :")
            else :
                print ("sorry ,docfinder does not support this city :  ",c)
    elif r==2: 
        m=(input(" : quel est votre nom :  \n"))
        a=eval(input("quel age avez vous : \n"))
        n=(input(":vous etes un homme ou une femme \n"))
        c=(input( "ou vivez vous: \n(casablanca, rabat,marakach):"))
        print("wait ...")
        while c!="rabat" or c!="casablanca" or c!="marakach":
            if c=="rabat" or c=="casablanca" or c=="marakach":
                time.sleep(5)
                print("*******************************************************************************")
                print("*******************************************************************************")
                print ("pour utiliser,suivez ces etapes:")
                print("wait ...")
                time.sleep(4)
                print("la premiere etape : ")
                print("     choisissez votre ville: .")
                time.sleep(4)
                print("la deuxieme etape: ")
                print("    choisissez la clinique la plus proche: .")
                time.sleep(4)
                print("la troisieme etape: ")
                print("     check that the doctor is present.")
                time.sleep(4)
                print("la quatrieme etape: ")
                print("     verifiez le nombre de patients avec le medecin.")
                time.sleep(4)
                print ("pour aller directement a DOCFINDER cliquez ici : ")
            else :
                print ("docfinder n'inclut pas cette ville :  ",c)
            
