import psycopg2

def inserir_cliente(RA, Nome_do_aluno, Email_do_aluno, Logradouro, Numero, Cep, Complemento):
    try:
        connection = psycopg2.connect(
            host = "dbimpacta.postgresql.dbaas.com.br",
            user = "dbimpacta",
            password = "impacta#2020",
            dbname = "dbimpacta"
        )
        
        cursor = connection.cursor()
        sql = "INSERT INTO Alex_teste (RA, Nome_do_aluno, Email_do_aluno, Logradouro, Numero, Cep, Complemento) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, [RA, Nome_do_aluno, Email_do_aluno, Logradouro, Numero, Cep, Complemento])
        connection.commit()
        cursor.close()
        connection.close()
        print("Registro Inserido com sucesso")
    except Exception as erro:
        print(erro)


inserir_cliente(1901705, "Alex", "alex@alex.com.br", "Rua antartida", "23", "01154031", "teste")


#connection.rollback(). Cancela operação


