import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.Graph()
        self._lista_rifugi = []
        self._dict_rifugi = {}

    def build_graph(self, year: int):
        self.G.clear()

        # Carico i rifugi validi fino a quell'anno
        self._lista_rifugi = DAO.read_rifugi(year)

        # Mappo i rifugi
        self._dict_rifugi = {}
        for rifugio in self._lista_rifugi:
            self._dict_rifugi[rifugio.id] = rifugio

        # Aggiungo i nodi
        self.G.add_nodes_from(self._lista_rifugi)

        # Considero le connessioni valide
        connessioni = DAO.read_connessione(year)

        # Creo gli archi SOLO se entrambi i rifugi sono validi
        for c in connessioni:
            if c.id_rifugio1 in self._dict_rifugi and c.id_rifugio2 in self._dict_rifugi:
                r1 = self._dict_rifugi[c.id_rifugio1]
                r2 = self._dict_rifugi[c.id_rifugio2]
                self.G.add_edge(r1, r2)

        # TODO

    def get_nodes(self):
        """
        Restituisce la lista dei rifugi presenti nel grafo.
        :return: lista dei rifugi presenti nel grafo.
        """
        nodi = []
        for n in self._dict_rifugi:
            nodi.append(self._dict_rifugi[n])
        return nodi

        # TODO

    def get_num_neighbors(self, node):
        """
        Restituisce il grado (numero di vicini diretti) del nodo rifugio.
        :param node: un rifugio (cioè un nodo del grafo)
        :return: numero di vicini diretti del nodo indicato
        """
        grado = self.G.degree(node)
        return grado

        # TODO

    def get_num_connected_components(self):
        """
        Restituisce il numero di componenti connesse del grafo.
        :return: numero di componenti connesse
        """
        connessi = nx.number_connected_components(self.G)
        return connessi

        # TODO

    def dfs_ricorsivo(self, grafo, nodo_inizio, visitati=None):
        if visitati is None:
            visitati = set()

        if nodo_inizio in visitati:
            return visitati

        visitati.add(nodo_inizio)

        for vicino in grafo.neighbors(nodo_inizio):
            if vicino not in visitati:
                self.dfs_ricorsivo(grafo, vicino, visitati)

        return visitati

    def get_reachable(self, nodo_inizio):
        """
        Deve eseguire almeno 2 delle 3 tecniche indicate nella traccia:
        * Metodi NetworkX: `dfs_tree()`, `bfs_tree()`
        * Algoritmo ricorsivo DFS
        * Algoritmo iterativo
        per ottenere l'elenco di rifugi raggiungibili da `start` e deve restituire uno degli elenchi calcolati.
        :param start: nodo di partenza, da non considerare nell'elenco da restituire.

        ESEMPIO
        a = self.get_reachable_bfs_tree(start)
        b = self.get_reachable_iterative(start)
        b = self.get_reachable_recursive(start)

        return a
        """

        # nodo_inizio = self._view.dd_rifugio.value


        # METODO 1: NetworkX dfs_tree
        albero_nx = nx.dfs_tree(self.G, nodo_inizio)
        raggiungibili_nx = list(albero_nx.nodes())
        raggiungibili_nx.remove(nodo_inizio)  # tolgo il nodo di partenza


        # METODO 2: DFS ricorsiva
        visitati = self.dfs_ricorsivo(self.G, nodo_inizio)
        raggiungibili_ric = list(visitati)
        raggiungibili_ric.remove(nodo_inizio)

        return raggiungibili_ric

        # TODO