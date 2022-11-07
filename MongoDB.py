import pymongo
from bd import produtos
from pymongo import MongoClient

# Conectando no banco de dados
Cluster = MongoClient(
    "mongodb+srv://mateusboth18:<Parede2022!>@cluster0.os0ptcs.mongodb.net/?retryWrites=true&w=majority")
db = Cluster['Test']
collection = db['test']

class BancoMongo:

    def conectar_BD(self):
        # Conectando no banco de dados
        Cluster = MongoClient(
            "mongodb+srv://mateusboth18:<Parede2022!>@cluster0.os0ptcs.mongodb.net/?retryWrites=true&w=majority")
        db = Cluster['Test']
        collection = db['test']

    def inserir_produto(self,dados):
        collection.insert_many(dados)

    def procurar_produto(self,id):
        results = collection.find({_id: id})
        for result in results:
            print(result)

    def deletar_produto(self,id):
        results = collection.delete_one({_id: id})

Base1 =BancoMongo.conectar_BD()
Base1 =BancoMongo.procurar_produto(3)


