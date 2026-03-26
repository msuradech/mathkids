import oracledb
import os

DB_USER = os.getenv("OCI_USER")
DB_PASSWORD = os.getenv("OCI_PASSWORD")
WALLET_PASSWORD = os.getenv("WALLET_PASSWORD")
DB_DSN = "OCI"
WALLET_PATH = "./wallet"

pool = oracledb.create_pool(
    user=DB_USER,
    password=DB_PASSWORD,
    dsn=DB_DSN,
    config_dir=WALLET_PATH,
    wallet_location=WALLET_PATH,
    wallet_password=WALLET_PASSWORD,
    min=2,
    max=5,
    increment=1
)

def get_connection():
    return pool.acquire()