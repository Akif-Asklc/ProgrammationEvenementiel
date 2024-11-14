import threading
import time

# Création de la fonction Thread1
def thread(name, start):
    count = start # Variable qui sert à compter le nb de seconde
    print(f"Numéro de départ de {name} : {count}")
    while count > 0: # Le TIMER
        count -= 1
        print(f"{name} : {count}")
        time.sleep(1)


start = time.perf_counter()

t1 = threading.Thread(target=thread, args=("Thread1", 7)) # création de la thread n°1 | Target vise la fonction thread1 | l'argument vise 'i'
t2 = threading.Thread(target=thread, args=("Thread2", 5)) # création de la thread n°2 | Target vise la fonction thread2 | l'argument vise 'i'

t1.start() # je démarre la première thread
t2.start() # je démarre la deuxième thread


t1.join() # attend la fin de la thread pour ne pas laissez la thread en arrière plan (mode zombie)
t2.join()


end = time.perf_counter()

print(f"Tasks ended in {round(end - start, 2)} second(s)")