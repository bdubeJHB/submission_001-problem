from random import randint


def create_outline():
    topics = {"Introduction to Python", "Tools of the Trade", "How to make decisions", "How to repeat code", "How to structure data", "Functions", "Modules"}

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

    students = [make_student("Moses", problems, status), make_student("Daniel", problems, status), make_student("Sarah", problems, status), make_student("Paul", problems, status), make_student("Ruth", problems, status), make_student("Isaac", problems, status), make_student("Jonah", problems, status)]

    print("Student progress:")
    num = 1
    for student in students:
        print(num + ". ", end='')
        for detail in student:
            print(detail, end='\t')
            num += 1
        print()



def make_student(id, all_problems, statuses):
    topics = list(all_problems.keys())
    problems = list(all_problems.values())

    student = (id, topics[randint(0, len(topics) - 1)], problems[randint(0, len(problems) - 1)], statuses[randint(0, len(statuses))])
    return student


if __name__ == "__main__":
    create_outline()
