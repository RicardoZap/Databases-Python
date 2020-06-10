from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'
client = MongoClient(MONGO_URI)

db = client['compania']
collection1 = db['clientes']
collection2 = db['juegos']
collection3 = db['ventas']

collection1.insert_one({"_id": 1, "nombre": "Daniel", "apellido": "Zamarripa", "direccion": "Av. Bravo 4500 Nueva California"})
collection2.insert_one({"_id": 1, "nombre": "Age Of Empires 2 Definitive Edition", "precio": 200})
collection3.insert_one({"_id": 1, "nombre_cliente": "Daniel", "apellido_cliente": "Zamarripa", "juego_comprado": "Age Of Empires 2 Definitive Edition", "precio": 200})



