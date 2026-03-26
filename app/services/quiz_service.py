import random

def get_mode_config(mode: str):
    config = {
        "easy": 10,
        "normal": 20,
        "hard": 50
    }
    return config.get(mode, 10)

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


