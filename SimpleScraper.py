import requests
from bs4 import BeautifulSoup
import os

def menu():
    os.system("clear")
    print("URL (https://example.com) :")
    url = str(input())
    res = ""
    try :
        res = requests.get(url)
    except:
        print("Invalid URL")
        input()
        return 0

    if res.ok :
        html_text = BeautifulSoup(res.text, "html.parser")

        choix = ""
        t = ""
        a = ""
        v = ""

        while choix != "q":
            print("-----------------------")
            print("t : Search tags in selection")
            print("a : Search attributes in selection")
            print("p : Print code")
            print("v : View selection")
            print("r : Reset selection")
            print("l : Launch")
            print("q : Back\n")

            choix = str(input())


            if choix == "p":
                print("\n\n"+str(html_text.prettify())+"\n")
            if choix == "v":
                if v != "":
                    print(v)
            if choix == "t":
                t = str(input("t : "))
            if choix == "a":
                if t != "":
                    a = str(input("a : "))
            if choix == "l":
                if t != "":
                    pass
            if choix == "r":
                t = ""
                a = ""
                v = ""

            t = ""
            a = ""
            
    else:
        print("Invalid URL")
        input()
