import random

def get_mode_config(mode: str):
    config = {
        "easy": 10,
        "normal": 20,
        "hard": 50
    }
    return config.get(mode, 10)

def generate_lv01_question():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    op = random.choice(["+", "-"])

    if op == "+":
        answer = a + b
    else:
        if a < b:
            a, b = b, a
        answer = a - b

    return {
        "question": f"{a} {op} {b}",
        "answer": answer
    }

def generate_questions(n: int):
    return [generate_lv01_question() for _ in range(n)]


