# BD1_397_408_424_652
Project Title: Yet another Kafka (YaK)
## Current Implementation Status:
* Zookeeper class has been created. Uses socketserver library now( which makes life sooo much better)
* (Hopefully) The zookeeper can now accept connection requests from multiple brokers ie not hardcoded to 3 now
* Keeps track of port numbers in a list and also removes if the heartbeat method yields no response. Makes it a tad bit easier to implement leader election.
* flask servers setup done.
* brokers communicate with producer and consumer

## Issues to be fixed:
* Heartbeat method inside zookeeper now closes connection if no response is detected in 10 seconds. 
* Producers and Consumers need to be created dynamically.
* Broker functionalities need to be implemented.
* **THE ENTIRE PARTITIONING SECTION IS STILL LEFT !!!!**


## Instructions to run servers
* Open three terminals to run "python broker_name.py" to setup three broker servers.
* Run "python consumer.py" to run consumer.
* Run "python producer.py" to run producer.
