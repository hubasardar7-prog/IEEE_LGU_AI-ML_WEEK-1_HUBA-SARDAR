def get_non_empty_text(prompt):
    """Get text input that is not empty."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_mark(subject):
    """Get a valid mark from 0 to 100."""
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_non_negative_integer(prompt):
    """Get a non-negative whole number."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Please enter 0 or a positive number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_grade(average):
    """Return a letter grade based on the assignment rules."""
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"


def main():
    print("\n--- Student Grade & Attendance Tracker ---")

    name = get_non_empty_text("Enter student name: ")
    roll_number = get_non_empty_text("Enter roll number: ")

    subjects = {}
    print("\nEnter marks for at least 3 subjects.")
    subject_count = get_non_negative_integer("How many subjects? ")

    while subject_count < 3:
        print("Please enter at least 3 subjects.")
        subject_count = get_non_negative_integer("How many subjects? ")

    for number in range(1, subject_count + 1):
        subject = get_non_empty_text(f"Enter subject {number} name: ")
        while subject in subjects:
            print("That subject has already been entered.")
            subject = get_non_empty_text(f"Enter subject {number} name: ")
        subjects[subject] = get_mark(subject)

    total_marks = sum(subjects.values())
    average = total_marks / len(subjects)
    grade = get_grade(average)

    print("\nAttendance Details")
    total_classes = get_non_negative_integer("Enter total number of classes held: ")

    while True:
        attended_classes = get_non_negative_integer("Enter classes attended: ")
        if attended_classes <= total_classes:
            break
        print("Classes attended cannot be greater than classes held.")

    if total_classes == 0:
        attendance = 0
    else:
        attendance = (attended_classes / total_classes) * 100

    eligible = attendance >= 75

    print("\n" + "=" * 45)
    print("              STUDENT REPORT CARD")
    print("=" * 45)
    print(f"Name: {name}")
    print(f"Roll Number: {roll_number}")
    print("-" * 45)
    print("Subject Marks:")
    for subject, mark in subjects.items():
        print(f"  {subject}: {mark:.1f}")
    print("-" * 45)
    print(f"Average Percentage: {average:.2f}%")
    print(f"Final Grade: {grade}")
    print(f"Attendance Rate: {attendance:.2f}%")
    print(f"Exam Eligibility: {'Eligible' if eligible else 'Not Eligible'}")
    print("=" * 45)


if __name__ == "__main__":
    main()
