#iscript para conectar ao mysql e executar a query

import pymysql as mysql

#conectando ao banco de dados

conexao = mysql.connect(
    host = 'localhost',
    user = 'renatomota',
    password = 'Senha123@',
    db = 'cadastro'
)

#criando um cursor
cursor = conexao.cursor()

#criando a query

query = "SELECT * FROM pessoas"

#executando a query

cursor.execute(query)

#listando os dados

for linha in cursor:
    print(linha)

#fechando a conexao

conexao.close()


