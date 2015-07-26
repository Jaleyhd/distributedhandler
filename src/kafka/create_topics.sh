#Creating a topic
bin/kafka-create-topic.sh --zookeeper localhost:2181 --replica 1 --partition 1 --topic test
#Observe topics
bin/kafka-list-topic.sh --zookeeper localhost:2181


