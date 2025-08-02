def calculate_salary(**employee_details):
    """
    Calculates salary based on various employee details provided as keyword arguments.
    """
    base_salary = employee_details.get('base_salary', 0)
    bonus = employee_details.get('bonus', 0)
    deductions = employee_details.get('deductions', 0)
    overtime_hours = employee_details.get('overtime_hours', 0)
    hourly_rate = employee_details.get('hourly_rate', 0)

    total_salary = base_salary + bonus - deductions + (overtime_hours * hourly_rate)

    print(f"Calculating salary for: {employee_details.get('name', 'Unnamed Employee')}")
    print(f"Base Salary: ${base_salary}")
    print(f"Bonus: ${bonus}")
    print(f"Deductions: ${deductions}")
    if overtime_hours > 0 and hourly_rate > 0:
        print(f"Overtime Pay: ${overtime_hours * hourly_rate}")
    print(f"Total Salary: ${total_salary}\n")


# Example usage:
calculate_salary(name="Alice", base_salary=50000, bonus=5000, deductions=2000)
calculate_salary(name="Bob", base_salary=60000, overtime_hours=10, hourly_rate=25)
calculate_salary(name="Charlie", base_salary=45000, bonus=2000, deductions=1000, overtime_hours=5, hourly_rate=30)
calculate_salary(name="David")  # Only name provided, other values default to 0