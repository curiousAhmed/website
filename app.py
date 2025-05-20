from flask import Flask, render_template, request, redirect, url_for
from flask_compress import Compress
import sqlite3
app = Flask(__name__,template_folder='templates')
Compress(app)


@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/HiringHrSurvey')
def survey():
    return render_template('HiringHRSurvey.html')

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/jobseekers')
def candidates():
    return render_template('jobseeker.html')

@app.route('/robots.txt')
def robots():
    return render_template('robots.txt')

@app.route('/hiringpricing')
def pricing():
    return render_template('hiringpricing.html')

@app.route('/hrpricing')
def pricing2():
    return render_template('hrpricing.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/sitemap.xml')
def sitemap():
    return render_template('sitemap.xml')

@app.route('/image-sitemap.xml')
def sitemap2():
    return render_template('image-sitemap.xml')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/vacancies')
def vacamcies():
    return render_template('vacancies.html')

# Blog posts
@app.route('/Why_Pakistan_is_the_Top_Choice_for_Remote_Talent')
def post1():
    return render_template('Why_Pakistan_is_the_Top_Choice_for_Remote_Talent.html')

@app.route('/real_worl_projects_in_hiring')
def post2():
    return render_template('real_worl_projects_in_hiring.html')

@app.route('/pros_and_cons_of_remote_workers')
def post3():
    return render_template('pros_and_cons_of_remote_workers.html')

@app.route('/is_remote_work_good')
def post4():
    return render_template('is_remote_work_good.html')

@app.route('/benefits_of_hiring_agency')
def post5():
    return render_template('benefits_of_hiring_agency.html')

@app.route('/outsource_to_FRIDAY')
def post6():
    return render_template('outsourcing_HR_to_FRIDAY.html')

@app.route('/role_of_HR')
def post7():
    return render_template('role_of_HR_in_an_organization.html')

@app.route('/employee_retention_strategies_for_2024')
def post8():
    return render_template('employee_retention_strategies_for_2024.html')

@app.route('/rushed_hiring_disaster')
def post9():
    return render_template('rushed_hiring_disaster.html')


# Function to create a SQLite connection and cursor
def get_db():
    conn = sqlite3.connect('friday_db.db')
    return conn, conn.cursor()

#Dashboard page
@app.route('/friday_sign_up_data_dashboard')
def dashboard():
    conn, cursor = get_db()

    # Query to get the total count of all applicants
    cursor.execute('SELECT COUNT(*) FROM formData')
    total_applicants = cursor.fetchone()[0]

    # Query to get the count of each category
    cursor.execute('SELECT domain, COUNT(*) FROM formData GROUP BY domain')
    category_counts = dict(cursor.fetchall())  # Convert result to a dictionary
    conn.close()

    return render_template('dashboard.html',total_applicants=total_applicants, category_counts=category_counts)


# Form on Contact / About page
@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    if request.method == 'POST':
        # Get data from the contact form
        username = request.form['username']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        conn, cursor = get_db()
        cursor.execute('''INSERT INTO contactFormData (username, email, subject,message)
                      VALUES (?, ?, ?, ?)''',
                   (username, email, subject,message))
        conn.commit()
        conn.close()
        # Redirect to a thank-you page or any other page
        return render_template('about_thank_you.html')


# Form inside  Footer area
@app.route('/email_list', methods=['POST'])
def email_list_submit():
    if request.method == 'POST':
        email= request.form['email']

        conn, cursor = get_db()
        cursor.execute('''INSERT INTO email_list (email)
                      VALUES (?)''',
                   (email,))
        conn.commit()
        conn.close()
        return redirect(request.referrer)

# Form on blog page
@app.route('/subscribe', methods=['POST'])
def subscribe():
    name = request.form.get('name')
    field_of_work = request.form.get('fow')
    email = request.form.get('email')

    conn, cursor = get_db()
    cursor.execute('''INSERT INTO subscribers (name,field_of_work,email)
                    VALUES (?, ?, ?)''',
                   (name,field_of_work,email))
    conn.commit()
    return render_template('blog_thank_you.html')

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0')