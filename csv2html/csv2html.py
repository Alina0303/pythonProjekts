def table_start():
    return "<table>\n"


def table_end():
    return "</table>"


def row_start():
    return "<tr>\n"


def row_end():
    return "</tr>\n"


def coloumn_start():
    return " <td>"


def coloumn_end():
    return "</td>\n"


tekst_do_zapisania = ""
with open("test.csv") as plik:
    tekst_do_zapisania += table_start()

    for linia in plik:
        tekst_do_zapisania += row_start()

        for coloumn in linia.split(","):
            tekst_do_zapisania += coloumn_start()
            tekst_do_zapisania += coloumn.rstrip()
            tekst_do_zapisania += coloumn_end()

        tekst_do_zapisania += row_end()

    tekst_do_zapisania += table_end()

zapis = open("html.html", "w")
zapis.write(tekst_do_zapisania)
zapis.close()