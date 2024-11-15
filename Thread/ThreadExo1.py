import threading
import time

# Création de la fonction Thread1
def thread(name, count):
    for i in range(count): # Compte à rebours
        print(f"Je suis la thread {name}")
        time.sleep(1)
        

start = time.perf_counter() # début de la prise de temps.

t1 = threading.Thread(target=thread, args=[1,7]) # création de la thread1 | Target vise la fonction thread1 | l'argument vise 'i'
t1.start() # je démarre la thread

t2 = threading.Thread(target=thread, args=[2,6]) # création de la thread2 | Target vise la fonction thread2 | l'argument vise 'i'
t2.start() # je démarre la thread


t1.join() # attend la fin de la thread pour ne pas laissez le thread en arrière plan (mode zombie)
t2.join()


end = time.perf_counter()  # fin de la prise de temps.

print(f"Tasks ended in {round(end - start, 2)} second(s)")