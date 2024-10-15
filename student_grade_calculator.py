
def calculate_average(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

def letter_grade(average):
    if (average >= 90 and average <= 100):
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
    
def main():
    num_subject = 0
    while num_subject <= 0:
        try:
            num_subject = int(input("Enter the number of subjects: "))
            if num_subject <= 0:
                print("Enter positive number!")
        except ValueError:
            print("Invalid input! Enter integer number")
        
    grades = []
    subject = 1
    while subject <= num_subject:
        try:
            grade = float(input(f"Enter the grades for {subject } subjects: "))
            if grade >= 0 and grade <= 100:
                grades.append(grade)
                subject += 1
            else:
                print("grade must be between 0 to 100")
        except ValueError:
            print("invalid input, please enter a valid number")
        
    average = calculate_average(grades)

    letter = letter_grade(average)

    print(f"Average grade: {average:.2f}")
    print(f"Letter grades: {letter}")

main()