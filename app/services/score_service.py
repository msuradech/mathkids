from db.oci import get_connection

def get_score_daily_service(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT USER_ID, SCORE, SEC, AVG_SCORE
        FROM mathkids.v_score_daily_by_user
        WHERE user_id = :user_id
    """

    cursor.execute(query, {"user_id": user_id})

    columns = [col[0].lower() for col in cursor.description]
    rows = cursor.fetchall()

    data = [dict(zip(columns, row)) for row in rows]

    cursor.close()
    conn.close()

    return data

def get_score_monthly_service(user_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT USER_ID, SCORE, SEC, AVG_SCORE
        FROM mathkids.v_score_monthly_by_user
        WHERE user_id = :user_id
    """

    cursor.execute(query, {"user_id": user_id})

    columns = [col[0].lower() for col in cursor.description]
    rows = cursor.fetchall()

    data = [dict(zip(columns, row)) for row in rows]

    cursor.close()
    conn.close()

    return data

