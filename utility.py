import employee 
import os

def check_employee():
    id = int(input("Enter ID Please:"))
    emp = employee.get_employee(id)
    if emp == 0:
        print("Employee Not Found")
    else:
        print("Employee found with name:", emp)


def add_employee():
    name = input("Please Enter Name:")
    id = employee.add_employee(name)
    print('New User added with ID', id)


def delete_employee():
    id = int(input("Enter ID to delete:"))
    if employee.delete_employee(id) != 0:
        print("User deleted with ID", id)
    else:
        print("No ID matched to delete")


def get_all_employees():
    employees = employee.get_employee()
    print("All Employee List - ")
    for id, name in employees.items():
        print(id, name)


def print_menu():
    print("---------- Options -----------")
    print("Press 1 to check employee:")
    print("Press 2 to add employee:")
    print("Press 3 to delete employee:")
    print("Press 4 to display all employees:")
    print("Press 5 to clear the screen:")
    print("Press 6 to exit:")


def clear_screen():
    os.system('cls')
    print_logo()


def print_logo():
    print(r"""
            ,..........   ..........,
     ,..,'          '.'          ',..,
    ,' ,'            :            ', ',
   ,' ,'             :             ', ',
  ,' ,'              :              ', ',
 ,' ,'............., : ,.............', ',
,'  '............   '.'   ............'  ',
 '''''''''''''''''';''';''''''''''''''''''
    
    """)