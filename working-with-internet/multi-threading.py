from threading import Thread
import time

def sleep(name):
    time.sleep(8)
    print(f"You sleep {name}")

def eat():
    time.sleep(2)
    print("You eat")

def workout():
    time.sleep(5)
    print("You work out")

chore_1 = Thread(target=sleep, args=("Jacob",))
chore_1.start()

chore_2 = Thread(target=eat)
chore_2.start()

chore_3 = Thread(target=workout)
chore_3.start()

chore_1.join()
chore_2.join()
chore_3.join()

print("All chores in completed.")




