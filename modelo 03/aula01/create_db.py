import sqlite3

conn = sqlite3.connect('meu_banquinho.db')

print("Banco de dados 'meu_banquinho.db' criado com sucesso!")

conn.close()