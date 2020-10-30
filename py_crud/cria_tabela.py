import psycopg2

sql_create = '''CREATE TABLE Alex_teste 
                (RA int PRIMARY KEY, 
                Nome_do_aluno varchar(50),
                Email_do_aluno varchar(50),
                Logradouro varchar(50),
                Numero varchar(5),
                Cep varchar(10),
                Complemento varchar(20))'''

def create_table():
    try:
        connection = psycopg2.connect(
            host = "dbimpacta.postgresql.dbaas.com.br",
            user = "dbimpacta",
            password = "impacta#2020",
            dbname = "dbimpacta"
        )
        cursor = connection.cursor()
        cursor.execute(sql_create)
        connection.commit()
        cursor.close()
        connection.close()
        print("Tabela criada")
    except:
        print("Erro ao criar a Tabela")            

create_table()