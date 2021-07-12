class Employee:

    def __init__(self, name, salary, phone, start_date):        
        self.name = name
        self.salary = salary
        self.phone = phone
        self.start_date = start_date

    # create str method 
    def __str__(self):
        return self.name

    def get_employment_details(self):
        return (self.name, self.salary, self.start_date)

    def get_contact_deatils(self):
        return (self.name, self.phone) 

# create two employees
employee1 = Employee("Jane Day", 60000, "0432 345 676", "12/04/2019")
print(employee1.name)
print(employee1.phone)
print(employee1.get_contact_deatils())

employee2 = Employee("Fred Smyth", 40000, "0456 786 999", "30/01/2020")
print(employee2.name)
print(employee2.phone)
print(employee2.get_employment_details())

