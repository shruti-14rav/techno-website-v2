from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'location' : 'Ahmedabad',
        'salary': '80,000'
    },
    {
        'id':2,
        'title': 'Data Science',
        'location': 'Surat',
        'salary': '95,000'
    },
    {
        'id':3,
        'title':'Fronted developer',
        'location':'Rajkot',
        'salary':'55,000'
    },
    {
        'id':4,
        'title':'Backend developer',
        'location':'vadodara',
        'salary':'65,000'
    }
]

@app.route("/")
def home():
    return render_template('home.html',jobs=JOBS,company_name='')
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)
