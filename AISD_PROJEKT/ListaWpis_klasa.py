from typing import Any


class ListaWpis:
    def __init__(self, wart: str = None, nast: 'ListaWpis' = None, poprz: 'ListaWpis' = None):
        self.wart = wart
        # referencja do nastepnego node'a
        self.nast = nast
        # referencja do poprzedniego node'a
        self.poprz = poprz

    def dodaj_po_nim(self, wart: Any) -> None:
        node = ListaWpis(wart)
        node.poprz = self
        node.nast = self.nast
        self.nast.poprz = node
        self.nast = node

    def dodaj_przed_nim(self, wart: Any) -> None:
        node = ListaWpis(wart)
        node.poprz = self.poprz
        node.nast = self
        self.poprz.nast = node
        self.poprz = node
