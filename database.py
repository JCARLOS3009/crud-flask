import sqlite3

# Conecte ao banco de dados (substitua 'seu_banco_de_dados.db' pelo caminho do seu banco de dados)
conexao = sqlite3.connect('dapodik.db')
cursor = conexao.cursor()

# Consulta para obter o nome de todas as tabelas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tabelas = cursor.fetchall()

# Exibir dados de cada tabela
for tabela in tabelas:
    nome_tabela = tabela[0]
    print(f"\nTabela: {nome_tabela}")

    # Consulta para obter todos os dados da tabela atual
    cursor.execute(f"SELECT * FROM {nome_tabela};")
    dados = cursor.fetchall()

    # Exibir os dados
    if dados:
        # Exibir o cabeçalho (nomes das colunas)
        colunas = [descricao[0] for descricao in cursor.description]
        print(" | ".join(colunas))
        print("-" * 40)

        # Exibir cada linha de dados
        for linha in dados:
            print(" | ".join(str(valor) for valor in linha))
    else:
        print("A tabela está vazia.")

# Fecha a conexão
conexao.close()
