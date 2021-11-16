import sqlite3
import argparse
import hashlib
import os
import datetime
import time

start_time = time.time()

parser = argparse.ArgumentParser(prog='GeraBase', usage='%(prog)s [options]')
parser.add_argument("-C","--category",  help="Atribui a categoria para os arquivos na base de dados", default="unspecified")
parser.add_argument("-D","--database",  help="Define o nome da base de dados", default="arquivos.db")
parser.add_argument("-P","--path", help="Indica localização dos arquivos", default=".")
args = parser.parse_args()

if not args.database[-3:] == ".db":
    args.database+=".db"

#Obtém HASH MD5 de arquivo
def getHashMD5(filename):
    with open(filename, "rb") as f:
        file_hash = hashlib.md5()    
        while byte_block := f.read(8192):
            file_hash.update(byte_block)
    return file_hash.hexdigest()

#Obtém SHA 256 de arquivo
def getHash256(filename):
    with open(filename, "rb") as f:
        file_hash = hashlib.sha256()    
        while byte_block := f.read(8192):
            file_hash.update(byte_block)
    return file_hash.hexdigest()

#Obtém arquivos do diretório/subdiretórios
def getFiles(mypath):
    allFiles = []
    for path, subdirs, files in os.walk(mypath):
        for name in files:
            allFiles.append(os.path.join(path, name))
    print(f"Há {len(allFiles)} arquivos.")
    return allFiles

def addToDB(conn, info):
    cursor = conn.cursor()
    cursor.execute("select id from arquivos where MD5=?", (info[0][4],))
    data = cursor.fetchall()
    if not data:
        cursor.executemany("""
            INSERT INTO arquivos (nome, extensao, criado_em, categoria, MD5, SHA256)
            VALUES (?,?,?,?,?,?)
            """, info)
        conn.commit()
    return conn

def createDB():
    conn = sqlite3.connect(args.database)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE arquivos (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            extensao TEXT,
            criado_em DATE NOT NULL,
            categoria TEXT NOT NULL,
            MD5 TEXT,
            SHA256 TEXT    
    );
    """)
    
    return conn

dataAtual = datetime.date.today()    
if not os.path.exists(args.database):
    conn = createDB()
else:
    conn = sqlite3.connect(args.database)

dados = []
for file in getFiles(args.path):
    if file != '.\\'+os.path.basename(__file__) and file != '.\\'+args.database:
        fileName = os.path.basename(file)
        ext = os.path.splitext(fileName)[-1]
        dados.append((fileName,ext,dataAtual.strftime('%d/%m/%Y'),args.category,getHashMD5(file),getHash256(file)))

addToDB(conn, dados)
conn.close()

print(f'Duração: {time.time() - start_time} Segundos')    
