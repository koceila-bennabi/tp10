def afficher(p):
    terms = []
    degree = len(p) - 1
    for i, coef in enumerate(reversed(p)):
        if coef != 0:
            terms.append(f"{coef}x^{degree - i}" if degree - i > 0 else str(coef))
    print(" + ".join(terms))
def get_valeur(p, x):
    valeur = 0
    for i, coef in enumerate(p):
        valeur += coef * (x ** i)
    return valeur
def deriver(p):
     derivee = [i * p[i] for i in range(1, len(p))]
     
     return derivee
if __name__ == "__main__":
    # Exemple de polynôme p(x) = 3 + 2x + x^2 (représenté par [3, 2, 1])
    p = [3, 2, 1]

    # Affichage du polynôme
    print("Polynôme :")
    afficher(p)

    # Calcul de la valeur du polynôme pour x = 2
    x = 2
    print(f"Valeur de p({x}) :", get_valeur(p, x))

    # Calcul de la dérivée du polynôme
    derivee = deriver(p)
    print("Dérivée du polynôme :")
    afficher(derivee)
