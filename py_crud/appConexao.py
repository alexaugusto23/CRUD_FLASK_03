import psycopg2
try:
    connection = psycopg2.connect(
        host = "ec2-52-44-235-121.compute-1.amazonaws.com",
        user = "xwaztxslppnkyn",
        password = "3cce96499e9b5b4f88c1885e26ddf903eeddf98654b7ffebdfe263024a0c9620",
        dbname = "d91oaqltutn28e"
    )
except psycopg2.OperationalError:
    print('NÃO CONECTADO')
else:
    print('CONECTADO')

'''
Banco de Dados (PostgreSQL) remotamente:
host = "dbimpacta.postgresql.dbaas.com.br",
user = "dbimpacta",
password = “impacta#2020",
dbname = "dbimpacta"
Nome da tabela >> grupo
Campos:
RA(PK) >> integer
Nome do aluno >> varchar(50)
Email do aluno >> varchar(50)
Logradouro >> varchar(50)
Numero >> varchar(5)
Cep >> varchar(10)
Complemento >> varchar(20)
'''