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

def get_result_history_by_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    rows = cursor.execute("""
    SELECT 
        CREATED_AT7,
        USERNAME,
        QUIZ_LEVEL,
        TOTAL_QUESTIONS,
        SCORE,
        SEC,
        AVG_SEC
    FROM mathkids.v_result_history
    WHERE USER_ID = :user_id
    ORDER BY CREATED_AT7 DESC
""", {"user_id": user_id}).fetchall()

    data = []
    for r in rows:
        data.append({
            "created_at": str(r[0]),
            "username": r[1],
            "quiz_level": r[2],
            "total_questions": r[3],
            "score": r[4],
            "sec": r[5],
            "avg_sec": r[6],
        })

    return data