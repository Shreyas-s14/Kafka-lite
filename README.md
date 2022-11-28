# BD1_397_408_424_652
Project Title: Yet another Kafka (YaK)
## Current Implementation Status:
* zookeeper skeleton(?) is done, mainly for the setup and connections.
* 

## Issues to be fixed:
* the ip's and ports of the clients ( from zookeeper perspective) ie brokers are inputted into the program that runs the zookeeper
* The threading aspect needs to be fixed ie the threads created to handle the messages sent to/ received from brokers need to run infinitely ( or until the zookeeper is running).
* In general, feels too hardcoded.
