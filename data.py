import sqlite3

path = r"C:\Users\Bruno\Desktop\Programação\PyCharm\BDPerfume"
banco = sqlite3.connect(path + r"\data.db")
cursor = banco.cursor()

#Marcas
cursor.execute("INSERT INTO Marcas VALUES (1, 'O Boticário ')")
cursor.execute("INSERT INTO Marcas VALUES (2, 'Natura')")

#Fixacoes
cursor.execute("INSERT INTO Fixacoes VALUES (1, 'bot')")
cursor.execute("INSERT INTO Fixacoes VALUES (2, 'nat')")

#Perfumes
cursor.execute("INSERT INTO Perfumes VALUES (1, 'Malbec', 3, 2, 1, 1)")
cursor.execute("INSERT INTO Perfumes VALUES (2, 'Kaiak', 2, 1, 2, 2)")


#Volumes
cursor.execute("INSERT INTO Volumes VALUES (1, '200ml')")
cursor.execute("INSERT INTO Volumes VALUES (2, '100ml')")

#Essencias
cursor.execute("INSERT INTO Essencias VALUES (1, 'Fraca')")
cursor.execute("INSERT INTO Essencias VALUES (2, 'Forte')")

#Essencia_Perfume
cursor.execute("INSERT INTO Essencia_Perfume VALUES (1, 1)")
cursor.execute("INSERT INTO Essencia_Perfume VALUES (2, 2)")
