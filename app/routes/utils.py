from fastapi import APIRouter
from db.oci import get_connection

router = APIRouter()

@router.get("/test-db")
def test_db():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT SYSDATE FROM dual")
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return {
            "status": "success",
            "sysdate": str(result[0])
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }