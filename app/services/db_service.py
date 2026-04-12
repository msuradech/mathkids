from db.oci import get_connection

def insert_quiz_result(user_id, quiz_level, total_questions, score, total_time_sec):
    conn = get_connection()
    cursor = conn.cursor()

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

def get_all_user():
    conn = get_connection()
    cursor = conn.cursor()
    rows = cursor.execute("SELECT user_id, username FROM mathkids.users order by user_id").fetchall()
    return rows