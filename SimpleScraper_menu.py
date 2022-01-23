from bs4 import BeautifulSoup
import SimpleScraper as SScrap

def run():
    ss = SScrap.SimpleScraper()
    is_good = "n"
    selection = None
    indice = 0

    ss.url = input("URL : ")
    html = ss.request_fn()

    while is_good == "n":
        if indice == 0:
            parse = ss.parse_fn(html)
        else:
            selection_text = []

            for item in selection:
                selection_text.append(str(item))

            selection_text = " ".join(selection_text)
            parse = ss.parse_fn(selection_text)


        tags = input("Tag: ")
        tags_list = []

        for tag in tags:
            tags_list.append(tag)

        att = input("Attribute (None = Leave Blank): ")

        if att == "":
            selection = ss.find_fn(parse, tags_list)
            print(selection)

        elif att != "":
            selection = ss.find_fn(parse, tags_list, att)
            print(selection)

        is_good = input("\nIs it Good ? [y/n] (return value): ")

        indice += 1

    return selection
