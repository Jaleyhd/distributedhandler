__author__ = 'user'
from cassandra.cluster import Cluster


from kafka.client import KafkaClient
from kafka.consumer import SimpleConsumer

kafka = KafkaClient("localhost:9092")

print("After connecting to kafka")

consumer = SimpleConsumer(kafka, "test", "test")

for message in consumer:
    print(message)

#------------Cassandra Script -------
cluster = Cluster()
session = cluster.connect('demo')

session.execute("
insert into users (lastname, age, city, email, firstname) values ('Jaley', 24, 'Dholakiya', 'jaley.dholakiya@gmail.com', 'jaleyd')
")

result = session.execute("select * from users where lastname='Jones' ")[0]


#----------MySQL Script -----------


#---------Reddis Script ----------
