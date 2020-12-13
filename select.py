import sqlite3
import data

def titulo(n, s):
    print("=" * n)
    print(f"{s}".center(n))
    print("=" * n)

path = data.path
banco = data.banco
cursor = data.cursor

#Fixação
cursor.execute("SELECT * FROM Fixacoes AS P JOIN Marcas AS M ON P.ID = M.ID")
tabela = cursor.fetchall()

titulo(39, 'Fixação')
print("ID".ljust(5)+"FIXAÇÃO".ljust(20)+"MARCA")
for linha in tabela:
    print(str(linha[0]).ljust(5), end="")
    print(linha[1].ljust(20), end="")
    print(linha[3])

print("\n")

#Marca do perfume
cursor.execute("SELECT * FROM Perfumes AS P JOIN Marcas AS M ON P.ID_MARCA_FK = M.ID")
tabela = cursor.fetchall()

titulo(39, 'Marca do perfume')
print("ID".ljust(5)+"PERFUME".ljust(20)+"MARCA")
for linha in tabela:
    print(str(linha[0]).ljust(5), end="")
    print(linha[1].ljust(20), end="")
    print(linha[7])






