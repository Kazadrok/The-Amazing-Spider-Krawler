#!/usr/bin/python3
import SimpleScraper_menu as SScrap_menu

import os

def menu():
    choix = ""
    while choix != "q":
        os.system("clear")
        print("\tTASK (The Amazing Spider Krawler)\n")
        print("ss : SimpleScraper")
        print("h : Help")
        print("q : Quit\n")

        choix = str(input())

        return choix

def my_help():
    pass

def main():
    while True:
        choix = menu()

        if choix == "q":
            exit()
        elif choix == "h":
            my_help()
        elif choix == "ss":
            SScrap_menu.run()
        else:
            print("Invalid choice\n")


main()
