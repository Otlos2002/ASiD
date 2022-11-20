from Lista_2k_2w_klasa import Lista_2k_2w


def dodaj_plusik(ciag: str) -> str:
    return ciag + '+'


ll = Lista_2k_2w()
ll.dodaj_za_koniec('napis1')
ll.dodaj_za_koniec('napis2')
ll.dodaj_za_koniec('napis3')
ll.dodaj_za_koniec('napis4')
ll.dodaj_za_koniec('napis5')
ll.dodaj_za_koniec('napis6')
ll.dodaj_za_koniec('napis7')
ll.print()
ll.odwroc()
ll.obrob_wartosci(dodaj_plusik)
ll.print()
