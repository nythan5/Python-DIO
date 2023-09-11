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
#print(db.test_collection)

# Criando um post (arquivo)
post = {
    "author": "Gabriel",
    "text": "My first mongodb aplication based on python",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.utcnow()
}

# Preparando para submeter as informaçoes
posts = db.posts
post_id = posts.insert_one(post).inserted_id
#print(post_id)

#print(db.posts.find_one())

#imprimir de forma formatada
#pprint.pprint(db.posts.find_one())

#bulk inserts
new_posts = [{
        "author": "Cristiane",
        "text": "My Second mongodb aplication based on python",
        "tags": ["bulk", "post", "insert"],
        "date": datetime.datetime.utcnow()
        },
        {                 
        "author": "Outra",
        "text": "My third mongodb aplication based on python",
        "title":"A outra da outra",
        "date": datetime.datetime.utcnow()
        }
            ]

result = posts.insert_many(new_posts)
print("\n Recuperando e Alterando informações ")
pprint.pprint(db.posts.find_one_and_update({"author":"Outra"},{'$set':{"author": "Josefina"}}))

print("\n")
pprint.pprint(db.posts.find_one({"author":"Josefina"}))

print("\nPRINTANDO TODOS OS POSTS")
for post in posts.find():
    pprint.pprint(post)
    print("\n")

