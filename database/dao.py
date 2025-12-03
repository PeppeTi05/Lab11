from database.DB_connect import DBConnect
from model.rifugio import Rifugio
from model.connessione import Connessione

class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """
    def __init__(self):
        pass

    @staticmethod
    def read_rifugi(anno):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT DISTINCT r.id, r.nome, r.localita
            FROM rifugio r, connessione c
            WHERE c.anno <= %s 
              AND (r.id = c.id_rifugio1 OR r.id = c.id_rifugio2)
            GROUP BY r.nome ASC
        """

        cursor.execute(query, (anno,))
        for row in cursor:
            result.append(Rifugio(row['id'], row['nome'], row['localita']))

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def read_connessione(anno):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT id, id_rifugio1, id_rifugio2
            FROM connessione
            WHERE anno <= %s
        """

        cursor.execute(query, (anno,))
        for row in cursor:
            result.append(Connessione(row['id'], row['id_rifugio1'], row['id_rifugio2']))

        cursor.close()
        conn.close()
        return result


