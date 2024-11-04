def divEntier(x: int, y: int) -> int:
    if x < y:
        return 0
    else:
        x = x - y
        return divEntier(x, y) + 1
    
if __name__ == '__main__':
    try:
        try:
           
            x = -1
            y = 2
            if x < 0:
                raise ValueError("La valeur négative.")
            if x == 0:
                raise ValueError("La valeur est égale à 0.")
            print(divEntier(x, y))
        except RecursionError:
            print("La valeur 0 n'est pas accepté pour Y.")
    except ValueError: 
        print("Veuillez rentrer une valeur numérique.")

