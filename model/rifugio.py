from dataclasses import dataclass

@dataclass
class Rifugio:
    _id: int
    _nome: str
    # localita: str
    # altitudine: int
    # capienza: int
    # aperto: int

    @property
    def nome(self):
        return self._nome
    @property
    def id(self):
        return self._id

    def __str__(self):
        return f'{self.id},  {self.nome}'

    def __hash__(self):
        return hash(self.id)