import random


def generate_single_question():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    op = random.choice(["+", "-"])

    if op == "+":
        answer = a + b
    else:
        answer = a - b

    return {
        "question": f"{a} {op} {b}",
        "answer": answer
    }


def generate_questions(n: int):
    return [generate_single_question() for _ in range(n)]
