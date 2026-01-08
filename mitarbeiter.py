from enum import Enum

class Gender(Enum):
    MALE = "Männlich"
    FEMALE = "Weiblich"
    OTHER = "Divers"

class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Employee(Person):
    def __init__(self, name, gender, employee_id):
        super().__init__(name, gender)
        self.employee_id = employee_id

class DepartmentHead(Employee):
    def __init__(self, name, gender, employee_id):
        super().__init__(name, gender, employee_id)

class Department:
    def __init__(self, name):
        self.name = name
        self.members = []
        self.head = None

    def set_head(self, head: DepartmentHead):
        if head not in self.members:
            self.add_member(head)
        self.head = head

    def add_member(self, employee: Employee):
        if employee not in self.members:
            self.members.append(employee)

    def get_member_count(self):
        return len(self.members)

class Company:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_department(self, dept: Department):
        self.departments.append(dept)

    def get_total_employees(self):
        all_employees = set()
        for dept in self.departments:
            all_employees.update(dept.members)
        return list(all_employees)

    def count_heads(self):
        return sum(1 for dept in self.departments if dept.head is not None)

    def get_department_count(self):
        return len(self.departments)

    def get_strongest_department(self):
        if not self.departments:
            return None
        return max(self.departments, key=lambda d: d.get_member_count())

    def get_gender_distribution(self):
        employees = self.get_total_employees()
        if not employees:
            return 0, 0
        
        males = sum(1 for e in employees if e.gender == Gender.MALE)
        females = sum(1 for e in employees if e.gender == Gender.FEMALE)
        
        total = len(employees)
        return (males / total) * 100, (females / total) * 100

my_company = Company("HTL")

it_dept = Department("IT")
hr_dept = Department("HR")

boss_it = DepartmentHead("Leon", Gender.FEMALE, "E001")
dev1 = Employee("Julian", Gender.MALE, "E002")
dev2 = Employee("Peter", Gender.MALE, "E003")

boss_hr = DepartmentHead("Diana", Gender.FEMALE, "E004")
recruiter1 = Employee("Erik", Gender.MALE, "E005")

it_dept.add_member(dev1)
it_dept.add_member(dev2)
it_dept.set_head(boss_it) 

hr_dept.add_member(recruiter1)
hr_dept.set_head(boss_hr)

my_company.add_department(it_dept)
my_company.add_department(hr_dept)

print(f"Firma: {my_company.name}")
print(f"Anzahl Abteilungen: {my_company.get_department_count()}")
print(f"Gesamtanzahl Mitarbeiter: {len(my_company.get_total_employees())}")
print(f"Anzahl Abteilungsleiter: {my_company.count_heads()}")

strongest = my_company.get_strongest_department()
print(f"Größte Abteilung: {strongest.name} ({strongest.get_member_count()} Personen)")

m_perc, f_perc = my_company.get_gender_distribution()
print(f"Geschlechterverteilung: Männer {m_perc:.1f}%, Frauen {f_perc:.1f}%")
