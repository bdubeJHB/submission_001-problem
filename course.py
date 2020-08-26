from random import randint


def create_outline():
    topics = {"Introduction to Python", "Tools of the Trade", "How to make decisions", "How to repeat code", "How to structure data", "Functions", "Modules"}

    topics = sorted(list(topics))

    print("Course Topics:")
    for topic in topics:
        print("* " + topic)

    problems = dict()
    for topic in topics:
        problems.update({topic: ["Problem 1", "Problem 2", "Problem 3"]})

    print("Problems:")
    for problem in problems:
        print("* " + problem + " : " + ", ".join(problems[problem]))

    status = ("STARTED", "COMPLETED", "GRADED")

    students = list()
    students.append(make_student("Moses", problems, status))
    students.append(make_student("Daniel", problems, status))
    students.append(make_student("Sarah", problems, status))
    students.append(make_student("Paul", problems, status))
    students.append(make_student("Ruth", problems, status))
    students.append(make_student("Isaac", problems, status))
    students.append(make_student("Jonah", problems, status))

    students = sorted(students, key=lambda detail: detail[3], reverse=True)

    print("Student Progress:")
    num = 1
    for student in students:
        print(str(num) + ". " + student[0] + " - " + student[1] + " - " + ", ".join(student[2]) + " [" + student[3] + "]")
        num += 1


def make_student(id, all_problems, statuses):
    topics = list(all_problems.keys())
    problems = list(all_problems.values())

    student = (id, topics[randint(0, len(topics) - 1)], problems[randint(0, len(problems) - 1)], statuses[randint(0, len(statuses) - 1)])
    return student


def sort_criterion(data):
    return data[1]


if __name__ == "__main__":
    create_outline()
