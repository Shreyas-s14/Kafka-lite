import psutil
# Iterate over all running process
pids = []
for proc in psutil.process_iter():
    try:
        # Get process name & pid from process object.
        processName = proc.name()
        processID = proc.pid
        if(processName == "python.exe"):
            pids.append(processID)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
print(pids)

'''
broker_process_ids = []
producer_process_ids = []
consumer_process_ids = []

print(broker_process_ids)
print(producer_process_ids)
print(consumer_process_ids)
'''


