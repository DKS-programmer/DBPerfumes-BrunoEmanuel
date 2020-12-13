import sqlite3

path = r"C:\Users\Bruno\Desktop\Programação\PyCharm\BDPerfume"
banco = sqlite3.connect(path + r"\data.db")
cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Marcas (id integer, nome text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Fixacoes (id integer, nome text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Perfumes (id integer, nome text, quantidade real, id_volume_FK integer, id_marca_FK integer, id_fixacao_FK integer)")
cursor.execute("CREATE TABLE IF NOT EXISTS Volumes (id integer, nome text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Essencia_Perfume(id_essencia_FK integer, id_perfume_FK integer)")
cursor.execute("CREATE TABLE IF NOT EXISTS Essencias(id integer, nome text)")
