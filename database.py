from sqlalchemy import create_engine, text

db_connection_string = ("mysql+pymysql://qo66w5ulzm0l5ervly11:pscale_pw_daKV8Zdrdkt1yQmT6Q4VJZaLOzdUOeaHr5pGlUBMcfN@aws.connect.psdb.cloud/vanco-career?charset=utf8mb4")

engine = create_engine(db_connection_string,
            connect_args = {
                "ssl": {
                "ca": "/etc/ssl/cert.pem"
                }
            })

with engine.connect() as conn:
    result = conn.execute(text("SELECT * from jobs"))
    print(result.all())

