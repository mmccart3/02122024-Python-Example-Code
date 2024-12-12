employee_35 = {
    "employee_number": 35,
    "first_name": "Mark",
    "family_name": "McCarthy",
    "NI_number": "NE123456A",
    "DOB": "29/04/1965",
    "start_date":"23/02/2022",
    "department": "delivery"
}
employee_36 = {
    "employee_number": 36,
    "first_name": "Tom",
    "family_name": "Sawyer",
    "NI_number": "NE98576A",
    "DOB": "29/01/2002",
    "start_date":"30/04/2022",
    "department": "delivery"
}
employees = [employee_35, employee_36]

for i in employees:
    print(i["first_name"])
    print(i["family_name"])
    print(i["DOB"])



# enemy_type_1 = {
#     "attacking_strength": 78,
#     "defensive_strength": 65,
#     "name": "orc"
# }

# print(enemy_type_1["attacking_strength"])



print(employees[0]["first_name"])