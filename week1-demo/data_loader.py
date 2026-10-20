import csv


def load_data(file_path):
    """Load student records from a CSV file into a list of dictionaries."""
    students = []

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            student = {
                "student_id": row["student_id"].strip(),
                "name": row["name"].strip(),
                "math": row["math"].strip(),
                "english": row["english"].strip(),
                "science": row["science"].strip(),
            }
            students.append(student)

    return students


def convert_grades(students):
    """Convert valid grade strings to numbers; invalid or blank grades become None."""
    converted_students = []

    for student in students:
        converted = {
            "student_id": student["student_id"],
            "name": student["name"],
        }

        for subject in ["math", "english", "science"]:
            value = student[subject]

            try:
                grade = float(value)
                if 0 <= grade <= 100:
                    converted[subject] = grade
                else:
                    converted[subject] = None
            except ValueError:
                converted[subject] = None

        converted_students.append(converted)

    return converted_students


def fill_missing_grades(students):
    """Replace missing grades with the average of available grades for that subject."""
    subjects = ["math", "english", "science"]
    subject_averages = {}

    for subject in subjects:
        valid_grades = []

        for student in students:
            grade = student[subject]
            if grade is not None:
                valid_grades.append(grade)

        if len(valid_grades) > 0:
            subject_averages[subject] = sum(valid_grades) / len(valid_grades)
        else:
            subject_averages[subject] = 0.0

    cleaned_students = []

    for student in students:
        cleaned = {
            "student_id": student["student_id"],
            "name": student["name"],
        }

        for subject in subjects:
            grade = student[subject]
            if grade is None:
                cleaned[subject] = subject_averages[subject]
            else:
                cleaned[subject] = grade

        cleaned_students.append(cleaned)

    return cleaned_students


def remove_duplicate_students(students):
    """Keep the first record for each student ID."""
    unique_students = []
    seen_ids = []

    for student in students:
        if student["student_id"] not in seen_ids:
            unique_students.append(student)
            seen_ids.append(student["student_id"])

    return unique_students


def clean_data(raw_students):
    """Run the cleaning steps in order."""
    converted = convert_grades(raw_students)
    filled = fill_missing_grades(converted)
    unique = remove_duplicate_students(filled)
    return unique


if __name__ == "__main__":
    raw = load_data("data/students.csv")
    cleaned = clean_data(raw)
    print("Raw records:", len(raw))
    print("Cleaned unique records:", len(cleaned))
    print("First cleaned record:", cleaned[0])
