import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

db_connection_string = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
)

engine = create_engine(
    db_connection_string,
    connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}}
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        return [dict(row) for row in result.mappings().all()]

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), {"val": id})
        row = result.fetchone()
        if row is None:
            return None
        return dict(row._mapping)

def add_application_to_db(job_id, data):
    with engine.begin() as conn:
        query = text("""
            INSERT INTO applications (
                job_id, full_name, email, linkedin_url, work_experience, resume_url
            ) VALUES (
                :job_id, :full_name, :email, :linkedin_url, :work_experience, :resume_url
            )
        """)
        conn.execute(query, {
            "job_id": job_id,
            "full_name": data.get('full_name'),
            "email": data.get('email'),
            "linkedin_url": data.get('linkedin_url'),
            "work_experience": data.get('work_experience'),
            "resume_url": data.get('resume_url')
        })
