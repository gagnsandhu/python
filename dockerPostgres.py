import json
import  psycopg2
from psycopg2.extensions import AsIs

DB_NAME = "daas"
DB_USER = "daas"
DB_PASS = "reportdbtest"
DB_HOST = "localhost"
DB_PORT = "5432"
def lambda_handler():
    # TODO implement
    try:
        conn = psycopg2.connect(database=DB_NAME,
                                user=DB_USER,
                                password=DB_PASS,
                                host=DB_HOST,
                                port=DB_PORT)
        print("Database connected successfully")
        cur = conn.cursor()
        # dat = cur.fetchall()
        cur.execute("SELECT * FROM %(table)s", {"table": AsIs("wgc_1_ceded0650b574258838f.security_statistics")})
        print(cur.fetchall())
    except Exception as e:
        # print("Database not connected successfully")
        print(e)
        # print()
    return {
        "Connection established"
    }



lambda_handler()
# conn
# cur = conn.cursor()