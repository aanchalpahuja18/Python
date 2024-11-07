# Static Methods in Python


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions= ["cashier", "cook", "manager", "janitor"]
        return position in valid_positions
    
employee1 = Employee("Aanchal", "cook")
employee2 = Employee("Parv", "cashier")
employee3 = Employee("Riya", "manager")
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

print(Employee.is_valid_position("engineer"))