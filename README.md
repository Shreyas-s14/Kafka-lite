# BD1_397_408_424_652
Project Title: Yet another Kafka (YaK)
## Current Implementation Status:
* Zookeeper class has been created. Uses socketserver library now( which makes life sooo much better)
* The zookeeper can now accept connection requests from multiple brokers ie not hardcoded to 3 now
* Keeps track of port numbers in a list and also removes if the heartbeat method yields no response. Leader election done simultaneously
* brokers communicate with producer and consumer via sockets in different threads.
* number of consumers and producers created is now user defined.
* topics are partitioned now and RF= 3. Consumer talks to the leader regarding topic availibility and subscribes to whatever it wants
* --from-beginning flag has been implemented

## Issues:
