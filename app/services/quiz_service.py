import random

def get_num_quiz(mode: str):
    config = {
        "01": 10,
        "02": 20,
        "03": 30
    }
    return config.get(mode, 10)

def generate_lv01_question(mode: str):
    match mode:
        case "01":
            a = random.randint(0, 10)
            b = random.randint(0, 10)

        case "02":
            a = random.randint(0, 10)
            b = random.randint(0, 10)

        case "03":
            a = random.randint(1, 100)
            b = random.randint(1, 100)

        case _:
            raise ValueError(f"Invalid mode: {mode}")
    
    op = random.choice(["+", "-"])

    if op == "+":
        answer = a + b
    else:
        if a < b and mode == "01":
            a, b = b, a
        answer = a - b

    return {
        "question": f"{a} {op} {b}",
        "answer": answer
    }

def generate_lv02_question(mode: str):
    match mode:
        case "01":
            a = random.randint(1, 12)
            b = random.randint(1, 12)

        case "02":
            a = random.randint(11, 100)
            b = random.randint(2, 12)

        case "03":
            a = random.randint(11, 100)
            b = random.randint(11, 100)

        case _:
            raise ValueError(f"Invalid mode: {mode}")

    answer = a * b

    return {
        "question": f"{a} x {b}",
        "answer": answer
    }

def generate_lv03_question(mode: str):
    match mode:
        case "01":
            answer = random.randint(1, 12)
            b = random.randint(1, 12)

        case "02":
            answer = random.randint(11, 50)
            b = random.randint(1, 12)

        case "03":
            answer = random.randint(11, 50)
            b = random.randint(13, 30)

        case _:
            raise ValueError(f"Invalid mode: {mode}")

    a = answer * b

    return {
        "question": f"{a} ÷ {b}",
        "answer": answer
    }

QUIZ_GENERATORS = {
    "01": generate_lv01_question,
    "02": generate_lv02_question,
    "03": generate_lv03_question
}

def generate_questions(n: int, quiz_id: str, mode: str):
    generator = QUIZ_GENERATORS.get(quiz_id)

    if not generator:
        raise ValueError(f"Invalid quiz id: {quiz_id}")

    return [generator(mode) for _ in range(n)]

