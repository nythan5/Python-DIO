from pymongo import MongoClient
import pymongo as pyM
import datetime 
import pprint

# Configure a string de conexão
uri = "mongodb+srv://nythan5:windows2011@cluster0.v7ymvwd.mongodb.net/?retryWrites=true&w=majority"

# Conecte-se ao cluster
client = MongoClient(uri)

# Criando e acessando o banco de dados e coleções
db = client.testdb
collection = db.test_collection

posts = db.posts

# Contando o total de documentos
total_documentos = posts.count_documents({"author":"Outra"}) # dentro do {} eu coloco um parametro caso n tenha apenas deixe vazio

print(f"O numero total de documentos persistidos são: {total_documentos}")

#for post in posts.find().sort("author"):
#    pprint.pprint(post)
#    print("\n")

#result = db.profiles.create_index([("author",pyM.ASCENDING)], unique = True)
#print(sorted(list(db.profiles.index_information())))

user_profile_user = [
    {'user_id': 211, 'name': 'Luke'},
    {'user_id': 212, 'name': 'Maria'}
]

result = db.profile_user.insert_many(user_profile_user)

colletions = db.list_collection_names()

# Printando as Colletions do DB
for collection in colletions:
    print(collection)


#removendo as colections 
db.posts.drop()

for collection in colletions:
    print(collection)
    

# print(posts.delete_one({"author": "Mike"}))
# print(db.profile_user.drop())

# Nome do banco de dados a ser excluído
db_name = 'testdb'

# Exclua o banco de dados
client.drop_database(db_name)