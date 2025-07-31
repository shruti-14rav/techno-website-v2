from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)

@app.route("/")
def hello_jovian():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Job not found", 404
    return render_template('jobpage.html', job=job)

@app.route("/api/job/<id>")
def show_job_json(id):
    job = load_job_from_db(id)
    return jsonify(job)

@app.route("/job/<id>/apply", methods=['POST'])
def apply_to_job(id):
    job = load_job_from_db(id)

    application_data = {
        'full_name': request.form.get('full_name'),
        'email': request.form.get('email'),
        'linkedin_url': request.form.get('linkedin_url'),
        'resume_url': request.form.get('resume_url'),
        'work_experience': request.form.get('experience')
    }

    add_application_to_db(id, application_data)
    return render_template('application_submitted.html', application=application_data, job=job)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
