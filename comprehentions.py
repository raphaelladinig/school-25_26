def main():
    # ListComprehension
    # Erstelle eine Liste aller Primzahlen zwischen 1 und 100
    prime = [n for n in range(2, 100) if isprime(n)]
    print(prime)
    # Erstelle mit einer einzigen Dictionary Comprehension
    # ein Dictionary, das die Wortlängen als Schlüssel
    # und Listen aller Wörter dieser Länge als Wert enthält.
    words = [
        "Apfel", "Banane", "Birne", "Mango", "Melone",
        "Pfirsich", "Kirsche", "Ananas", "Traube", "Feige"
    ]

    lendict = {len(w): [w2 for w2 in words if len(w2) == len(w)] for w in words}
    print(lendict)
    del words
    # Erstelle eine einzige Set Comprehension, die alle Buchstaben enthält,
    # die in mindestens zwei verschiedenen Wörtern vorkommen.
    # Groß- und Kleinschreibung soll ignoriert werden.
    words = [
        "Banane", "Ananas", "Mango", "Melone", "Kirsche",
        "Feige", "Birne", "Zitrone", "Papaya"
    ]
    letters = {l for l in sum([list(l1.lower()) for l1 in words], []) if
               sum([list(l1.lower()) for l1 in words], []).count(l) > 1}
    print(letters)


def isprime(n):
    for i in range(2, int((n / 2))):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    main()
