import psycopg2

connection = psycopg2.connect(
    host = "dbimpacta.postgresql.dbaas.com.br",
    user = "dbimpacta",
    password = "impacta#2020",
    dbname = "dbimpacta"
)
cursor = connection.cursor()
cursor.execute("SELECT RA, Nome_do_aluno, Email_do_aluno, Logradouro, Numero, Cep, Complemento FROM Alex_teste")
rows = cursor.fetchall()  # um resultado de uma intrução SELECT
for row in rows:
    for valor in row:
        print("valores: ", valor)
cursor.close()
connection.close()


# -----------------------------
'''
connection = psycopg2.connect(
    host="dbimpacta.postgresql.dbaas.com.br",
    user="dbimpacta",
    password="impacta#2020",
    dbname="dbimpacta"
)
cursor = connection.cursor()
cursor.execute("SELECT id_cliente, nome, comentario FROM cliente_SORVERTUNES")
row = cursor.fetchone()  # todos os resultados de uma intrução SELECT
print("valores: ", row[0], row[1], row[2])
cursor.close()
connection.close()
'''