from db.oci import get_connection

def get_current_user_id():
    # TODO: อนาคตเปลี่ยนเป็น decode JWT
    return 100  # dummy user

def insert_quiz_result(quiz_level, total_questions, score, total_time_sec):
    conn = get_connection()
    cursor = conn.cursor()

    user_id = get_current_user_id()

    avg_time = (
        total_time_sec / total_questions
        if total_questions > 0 else 0
    )

    sql = """
    INSERT INTO quiz_results (
        user_id,
        quiz_level,
        total_questions,
        score,
        total_time_sec,
        avg_time_sec
    ) VALUES (:1, :2, :3, :4, :5, :6)
    """

    cursor.execute(sql, [
        user_id,
        quiz_level,
        total_questions,
        score,
        total_time_sec,
        avg_time
    ])

    conn.commit()

    return user_id