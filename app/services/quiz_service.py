import random

def get_mode_config(mode: str):
    config = {
        "01": 10,
        "02": 20,
        "03": 30
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

def generate_lv02_question():
    a = random.randint(1, 12)
    b = random.randint(1, 12)

    answer = a * b

    return {
        "question": f"{a} x {b}",
        "answer": answer
    }

def generate_lv03_question():
    answer = random.randint(1, 12)
    b = random.randint(1, 12)

    a = answer * b  # ทำให้หารลงตัวแน่นอน

    return {
        "question": f"{a} ÷ {b}",
        "answer": answer
    }

QUIZ_GENERATORS = {
    "01": generate_lv01_question,
    "02": generate_lv02_question,
    "03": generate_lv03_question
}

def generate_questions(n: int, quiz_id: str):
    generator = QUIZ_GENERATORS.get(quiz_id)

    if not generator:
        raise ValueError(f"Invalid quiz id: {quiz_id}")

    return [generator() for _ in range(n)]

