from sqlalchemy import create_engine, text

db_connection_string = (
    "mysql+pymysql://shruti:shruti1234@89.58.6.79:3307/shruti?charset=utf8mb4"
)


engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)
def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.all():
            jobs.append(dict(row._mapping))  
        return jobs

