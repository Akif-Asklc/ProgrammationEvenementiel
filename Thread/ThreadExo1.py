import threading
import time

# Création de la fonction Thread1
def thread1(i):
    for i in range(5):
        print("Je suis la thread 1")
        time.sleep(1)
        
# Création de la fonction Thread2
def thread2(i):
    for i in range(5):
        print("Je suis la thread 2")
        time.sleep(1) # 1sec

start = time.perf_counter()

t1 = threading.Thread(target=thread1, args=[1]) # création de la thread1 | Target vise la fonction thread1 | l'argument vise 'i'
t1.start() # je démarre la thread

t2 = threading.Thread(target=thread2, args=[2]) # création de la thread2 | Target vise la fonction thread2 | l'argument vise 'i'
t2.start() # je démarre la thread


t1.join() # attend la fin de la thread pour ne pas laissez le thread en arrière plan (mode zombie)
t2.join()


end = time.perf_counter()

print(f"Tasks ended in {round(end - start, 2)} second(s)")