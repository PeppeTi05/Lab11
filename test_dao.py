from database.dao import DAO

lista_rifugi = DAO().read_rifugi()
print(lista_rifugi)

lista_connessioni = DAO.read_connessione()
print(lista_connessioni)