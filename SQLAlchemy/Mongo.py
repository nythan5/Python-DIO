from pymongo import MongoClient

# Configure a string de conexão
uri = "mongodb+srv://nythan5:<password>@cluster0.v7ymvwd.mongodb.net/?retryWrites=true&w=majority"

# Conecte-se ao cluster
client = MongoClient(uri)

# Acesse o banco de dados e as coleções
db = client.testdb
collection = db.my_collection
