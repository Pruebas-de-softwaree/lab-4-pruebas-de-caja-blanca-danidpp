def process_grades(students):
    passed = []
    failed = []
    overall_average = 0
    total_grades = 0
    counter = 0

    for student in students:
        name = student['name']
        grades = student['grades']
        
        if not grades:  
            print(f"Student {name} has no grades")
            continue
        
        average = sum(grades) / len(grades)
        total_grades += average
        # counter += 1

        if average > 70:  
            passed.append(name)
        elif average >= 50:
            print(f"{name} is in recovery")
        else:
            failed.append(name)
    
    if counter > 0:  
        overall_average = total_grades / counter
    
    return {
        'passed': passed,
        'failed': failed,
        'overall_average': round(overall_average, 2)
    }


if __name__ == "__main__":
    print("=== Running decision coverage tests ===")

    students = [
        {'name': 'Ana', 'grades': [80, 90, 85]},   # average > 70
        {'name': 'Luis', 'grades': [70, 70, 70]},  # average == 70
        {'name': 'Marta', 'grades': [40, 45, 50]}, # average < 50
        {'name': 'Jorge', 'grades': []}            # lista vacía
    ]

    result = process_grades(students)
    print("\nFinal processing result:")
    print(result)
