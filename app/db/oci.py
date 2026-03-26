import oracledb
import os

# 🔥 ปรับค่าตรงนี้ให้ตรงกับ DB ของมึง
DB_USER = "your_user"
DB_PASSWORD = "your_password"
DB_DSN = "localhost:1521/XEPDB1"  
# หรือแบบ OCI:
# DB_DSN = "hostname:1522/your_service_name"

pool = oracledb.create_pool(
    user=DB_USER,
    password=DB_PASSWORD,
    dsn=DB_DSN,
    min=2,
    max=5,
    increment=1
)

def get_connection():
    return pool.acquire()