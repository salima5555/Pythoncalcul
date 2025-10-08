# main.py
from operations import add, subtract, multiply, divide
from utils import get_input

def main():
    print("Bienvenue dans la calculatrice!")
    num1 = get_input("Entrez le premier nombre: ")
    num2 = get_input("Entrez le second nombre: ")

    print("Choisissez une opération:")
    print("1: Addition")
    print("2: Soustraction")
    print("3: Multiplication")
    print("4: Division")

    choice = input("Entrez votre choix (1/2/3/4): ")

    if choice == '1':
        print(f"Résultat: {add(num1, num2)}")
    elif choice == '2':
        print(f"Résultat: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Résultat: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Résultat: {divide(num1, num2)}")
    else:
        print("Choix invalide.")

if __name__ == "__main__":
    main()

