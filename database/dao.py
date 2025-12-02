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
    def read_rifugi():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)

        query = """SELECT DISTINCT r.id, r.nome
                   FROM rifugio r, connessione c
                   WHERE anno <= %s AND (r.id = c.rifugio_id1 OR r.id = c.rifugio_id2)
                   GROUP BY r.nome
                """

        cursor.execute(query)
        for row in cursor:
            result.append(Rifugio(row['id'], row['nome']))

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def read_connessione(anno):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)

        # Utilizzare LEAST e GREATEST
        query = """ """

        cursor.execute(query, (anno,))
        for row in cursor:
            result.append(Connessione(row['id'], row['id_rifugio1'], row['id_rifugio2']))

        cursor.close()
        conn.close()
        return result


# TODO


