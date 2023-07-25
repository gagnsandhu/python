 FROM  %(table)s", {"table": AsIs("device_db.device")})
        # print(cur.fetchone())