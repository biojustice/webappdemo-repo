from flask import Flask, render_template, jsonify

app = Flask(__name__)
work= [
  {
      'id': 1,
      'title': 'Data Analyst',
      'location': 'Bengaluru, India',
      'salary': 'Rs. 10,00,000'
  },
  {
      'id': 2,
      'title': 'Security Analyst',
      'location': 'Ghana',
      'salary': 'Rs. 110,00,000'
  },  
  {
      'id': 3,
      'title': 'Project manager',
      'location': 'London',
      'salary': 'Rs. 120,00,000'
  }, 
  {
      'id': 4,
      'title': 'Backend Developer',
      'location': 'Paris',
      'salary': 'Rs. 20,00,000'
  }
]
@app.route('/')


@app.route('/')
def index():
 return render_template('home.html',
         jobs=work, company_name='krakye jt')
  
@app.route('/api/jobs')
def list_jobs():
  return jsonify(work)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)