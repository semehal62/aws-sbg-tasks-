import numpy as np


SUBJECTS = ["math", "english", "science"]


def get_score_array(students):
    """Convert cleaned student grades to a 2D NumPy array."""
    rows = []

    for student in students:
        row = []
        for subject in SUBJECTS:
            row.append(student[subject])
        rows.append(row)

    return np.array(rows, dtype=float)


def subject_averages(students):
    """Return the average score for each subject."""
    scores = get_score_array(students)
    averages = np.mean(scores, axis=0)

    result = {}
    for index in range(len(SUBJECTS)):
        result[SUBJECTS[index]] = float(averages[index])

    return result


def student_averages(students):
    """Return each student's average across the three subjects."""
    scores = get_score_array(students)
    averages = np.mean(scores, axis=1)

    result = []
    for index in range(len(students)):
        result.append({
            "name": students[index]["name"],
            "average": float(averages[index])
        })

    return result


def pass_rate(students, passing_score=50):
    """Calculate the percentage of students whose overall average meets the threshold."""
    averages = student_averages(students)
    passed_count = 0

    for student in averages:
        if student["average"] >= passing_score:
            passed_count += 1

    if len(averages) == 0:
        return 0.0

    return (passed_count / len(averages)) * 100


def top_student(students):
    """Return the student with the highest overall average."""
    averages = student_averages(students)

    if len(averages) == 0:
        return None

    best_student = averages[0]
    for student in averages:
        if student["average"] > best_student["average"]:
            best_student = student

    return best_student


if __name__ == "__main__":
    from data_loader import load_data, clean_data

    raw = load_data("data/students.csv")
    students = clean_data(raw)
    print("Subject averages:", subject_averages(students))
    print("Pass rate:", round(pass_rate(students), 2), "%")
    print("Top student:", top_student(students))
