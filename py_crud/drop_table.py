import psycopg2

def deletar_registros():
    try:
        connection = psycopg2.connect(
            host = "dbimpacta.postgresql.dbaas.com.br",
            user = "dbimpacta",
            password = "impacta#2020",
            dbname = "dbimpacta"
        )

        cursor = connection.cursor()
        destruir = "DROP TABLE Alex_teste"
        cursor.execute(destruir)
        connection.commit()
        cursor.close()
        connection.close()
        print("Tabela deletada com sucesso")
    except Exception as erro:
        print(erro)

deletar_registros()
