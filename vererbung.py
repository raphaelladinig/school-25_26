class Tier:
    def __init__(self, name):
        self.name = name

    def sprich(self):
        return "Ein unbestimmtes Geräusch..."

    def beschreibung(self):
        return f"Ich bin ein Tier und heiße {self.name}."


class Hund(Tier):
    def sprich(self):
        return "Wuff! Wuff!"


class Katze(Tier):
    def sprich(self):
        return "Miau!"


mein_hund = Hund("Bello")
meine_katze = Katze("Minka")

print(mein_hund.beschreibung())

print(f"{mein_hund.name} sagt: {mein_hund.sprich()}")
print(f"{meine_katze.name} sagt: {meine_katze.sprich()}")
