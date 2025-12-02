from dataclasses import dataclass

@dataclass
class Connessione:
    id : int
    id_rifugio1 : int
    id_rifugio2 : int
    #distanza( in km)
    #difficolta(facile, media, difficile)
    #durata(hh: mm:ss)
    #anno

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return f'{self.id}, {self.id_rifugio1}, {self.id_rifugio2}'
