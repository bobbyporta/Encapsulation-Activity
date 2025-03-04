class GradeComputer:
    def __init__(self):
        self._science_grade     = 0.0
        self._math_grade        = 0.0
        self._english_grade     = 0.0
        self._programming_grade = 0.0
        self._final_grade       = 0.0

    def set_science_grade(self, grade):
        if 0 <= grade <= 100:
            self._science_grade = grade
        else:
            print("Invalid Input! Grade must be within 0 to 100.")
            return False
        return True

    def set_math_grade(self, grade):
        if 0 <= grade <= 100:
            self._math_grade = grade
        else:
            print("Invalid Input! Grade must be within 0 to 100.")
            return False
        return True

    def set_english_grade(self, grade):
        if 0 <= grade <= 100:
            self._english_grade = grade
        else:
            print("Invalid Input! Grade must be within 0 to 100.")
            return False
        return True

    def set_programming_grade(self, grade):
        if 0 <= grade <= 100:
            self._programming_grade = grade
        else:
            print("Invalid Input! Grade must be within 0 to 100.")
            return False
        return True

    def calculate_final_grade(self):
        
        total_grades = (self._science_grade + self._math_grade + self._english_grade + self._programming_grade) / 4
        self._final_grade = total_grades
        return total_grades

    def display_result(self):
        
        if self._final_grade >= 95.9:
            print(f"With Highest Honor! {self._final_grade:.2f}")
        elif self._final_grade >= 90.9:
            print(f"With High Honor! {self._final_grade:.2f}")
        elif self._final_grade >= 85.9:
            print(f"Excellent! {self._final_grade:.2f}")
        elif self._final_grade >= 75.9:
            print(f"Passed! {self._final_grade:.2f}")
        else:
            print(f"Failed! {self._final_grade:.2f}")

def main():
    grade_computer = GradeComputer()

    while True:
        try:
           
            science_grade = float(input("Enter science grade      : "))
            if not grade_computer.set_science_grade(science_grade):
                continue

            math_grade = float(input("Enter math grade         : "))
            if not grade_computer.set_math_grade(math_grade):
                continue

            english_grade = float(input("Enter english grade      : "))
            if not grade_computer.set_english_grade(english_grade):
                continue

            programming_grade = float(input("Enter programming grade  : "))
            if not grade_computer.set_programming_grade(programming_grade):
                continue

           
            grade_computer.calculate_final_grade()
            grade_computer.display_result()

            break 
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

    print("\nRe-run the program to restart.")

if __name__ == "__main__":
    main()
