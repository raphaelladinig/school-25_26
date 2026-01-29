class Auto:
    def __init__(self, ps):
        self.ps = ps

    def __repr__(self):
        return f"Auto({self.ps} PS)"

    def __add__(self, other):
        if isinstance(other, Auto):
            return self.ps + other.ps
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Auto):
            return self.ps - other.ps
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Auto):
            return self.ps * other.ps
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Auto):
            return self.ps == other.ps
        return False

    def __lt__(self, other):
        if isinstance(other, Auto):
            return self.ps < other.ps
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Auto):
            return self.ps > other.ps
        return NotImplemented

a1 = Auto(50)
a2 = Auto(60)
a3 = Auto(50)

print(f"Addition (50+60): {a1 + a2}")       
print(f"Subtraktion (60-50): {a2 - a1}")    
print(f"Multiplikation (50*60): {a1 * a2}") 

print(f"Ist a1 == a3? {a1 == a3}")          
print(f"Ist a1 < a2? {a1 < a2}")            
print(f"Ist a2 > a1? {a2 > a1}")            

try:
    print(a1 + "Kein Auto")
except TypeError:
    print("Check funktioniert: Man kann kein Auto mit einem String addieren.")
