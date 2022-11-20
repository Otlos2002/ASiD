from ListaWpis_klasa import ListaWpis
from typing import Any, Callable


class Lista_2k_2w:
    def __init__(self):
        self.przed_pie = ListaWpis(None)
        self.za_ost = ListaWpis(None)

        self.przed_pie.nast = self.za_ost
        self.za_ost.poprz = self.przed_pie

    def pobierz_el(self, idx: int) -> ListaWpis:
        itr = self.przed_pie.nast
        count = 0
        if idx < 0:
            while itr != self.za_ost:
                if count - idx == self.podaj_dlugosc():
                    return itr
                count += 1
                itr = itr.nast
        else:
            while itr != self.za_ost:
                if count == idx:
                    break
                itr = itr.nast
                count += 1
            return itr

    def dodaj_za_koniec(self, wart: Any) -> None:
        node = ListaWpis(wart)
        node.poprz = self.za_ost.poprz
        self.za_ost.poprz.nast = node
        node.nast = self.za_ost
        self.za_ost.poprz = node

    def dodaj_przed_poczatkiem(self, wart: Any) -> None:
        node = ListaWpis(wart)
        node.poprz = self.przed_pie
        node.nast = self.przed_pie.nast
        self.przed_pie.nast.poprz = node
        self.przed_pie.nast = node

    def usun_pierwszy(self) -> str:
        assert self.przed_pie.nast is not self.za_ost, f'Lista jest pusta!'
        temp = self.przed_pie.nast
        self.przed_pie.nast = self.przed_pie.nast.nast
        self.przed_pie.nast.poprz = None
        return temp.wart

    def usun_ostatni(self) -> str:
        assert self.przed_pie.nast is not self.za_ost, f'Lista jest pusta!'
        node = self.za_ost.poprz
        self.za_ost.poprz = node.poprz
        node.poprz.nast = self.za_ost
        return node.wart

    def podaj_dlugosc(self) -> int:
        count = 0
        itr = self.przed_pie.nast
        while itr != self.za_ost:
            itr = itr.nast
            count += 1
        return int(count)

    def odwroc(self) -> 'Lista_2k_2w':
        itr = self.za_ost.poprz
        llist = Lista_2k_2w()
        while itr != self.przed_pie:
            llist.dodaj_za_koniec(itr.wart)
            itr = itr.poprz
        return llist

    def obrob_wartosci(self, funkcja: Callable[[str], str]) -> None:
        itr = self.przed_pie.nast

        while itr != self.za_ost:
            itr.wart = funkcja(itr.wart)
            itr = itr.nast

    def print(self) -> None:
        assert self.przed_pie.nast is not self.za_ost, f'Lista jest pusta!'
        itr = self.przed_pie.nast
        listastr = ""
        while itr != self.za_ost:
            listastr += str(itr.wart) + "<>"
            itr = itr.nast
        print(listastr)

    def print_od_tylu(self) -> None:
        assert self.przed_pie.nast is not self.za_ost, f'Lista jest pusta!'
        itr = self.za_ost.poprz
        listastr = ""
        while itr != self.przed_pie:
            listastr += str(itr.wart) + "<>"
            itr = itr.poprz
        print(listastr)
