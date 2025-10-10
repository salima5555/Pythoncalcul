def get_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Erreur: Veuillez entrer un nombre valide")
            print("ERROR")