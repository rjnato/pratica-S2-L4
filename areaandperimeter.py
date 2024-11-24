import math

def calculate_square():
    side = float(input("Inserisci la lunghezza del lato del quadrato: "))
    area = side ** 2
    perimeter = 4 * side
    print(f"Area del quadrato: {area}")
    print(f"Perimetro del quadrato: {perimeter}")

def calculate_circle():
    radius = float(input("Inserisci il raggio del cerchio: "))
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    print(f"Area del cerchio: {area:.2f}")
    print(f"Circonferenza del cerchio: {perimeter:.2f}")

def calculate_rectangle():
    length = float(input("Inserisci la lunghezza del rettangolo: "))
    width = float(input("Inserisci la larghezza del rettangolo: "))
    area = length * width
    perimeter = 2 * (length + width)
    print(f"Area del rettangolo: {area}")
    print(f"Perimetro del rettangolo: {perimeter}")

def main():
    print("Scegli una figura geometrica per calcolarne il perimetro e l'area:")
    print("1. Quadrato")
    print("2. Cerchio")
    print("3. Rettangolo")
    
    choice = input("Inserisci il numero che preferisci (1-3): ")
    
    if choice == "1":
        calculate_square()
    elif choice == "2":
        calculate_circle()
    elif choice == "3":
        calculate_rectangle()
    else:
        print("Scelta non valida! Inserisci un numero compreso tra 1 e 3.")

if __name__ == "__main__":
    main()
