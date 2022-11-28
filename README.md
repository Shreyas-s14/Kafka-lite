# BD1_397_408_424_652
Project Title: Yet another Kafka (YaK)
## Current Implementation Status:
* zookeeper skeleton(?) is done, mainly for the setup and connections.
* flask servers setup done.
* brokers communicate with producer and consumer

## Issues to be fixed:
* the ip's and ports of the clients ( from zookeeper perspective) ie brokers are inputted into the program that runs the zookeeper
* The threading aspect needs to be fixed ie the threads created to handle the messages sent to/ received from brokers need to run infinitely ( or until the zookeeper is running).
* In general, feels too hardcoded.
* Producers and Consumers need to be created dynamically.
* Broker functionalities need to be implemented.


## Instructions to run servers
* Open three terminals to run "python broker_name.py" to setup three broker servers.
* Run "python consumer.py" to run consumer.
* Run "python producer.py" to run producer.
