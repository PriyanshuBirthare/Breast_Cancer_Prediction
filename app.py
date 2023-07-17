from flask import Flask,render_template,request,session, redirect
from flask_mysqldb import MySQL
import numpy as np
import pickle
import datetime
from flask_mail import Mail, Message
filename = 'breast-cancer-prediction-knn-model.pkl'
model = pickle.load(open(filename, 'rb'))

app=Flask(__name__)
app.secret_key = "cancer"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'breast_cancer'
mysql = MySQL(app)

app.config['SECRET_KEY'] = 'cancer'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'gmail id'
app.config['MAIL_PASSWORD'] = 'your-email-password'

mail = Mail(app)
def send_email(name, email, message):
    msg = Message(
        'New Contact Form Submission',
        sender='your-gmail-username@gmail.com',
        recipients=['recipient-email-address'],
        body=f'Name: {name}\nEmail: {email}\nMessage: {message}')

    mail.send(msg)



# Define the feedback form route
@app.route('/feedback', methods=['POST'])
def feedback():
    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        email = request.form['email']
        rating = request.form['rating']
        comments = request.form['comments']
        cur = mysql.connection.cursor()
        # Insert the feedback data into the MySQL database
        sql = "INSERT INTO feedback (name, email, rating, comments) VALUES (%s, %s, %s, %s)"
        val = (name, email, rating, comments)
        cur.execute(sql, val)
        mysql.connection.commit()

       
        return render_template('feed.html')


@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        send_email(name, email, message)

        return 'Thank you for contacting us!'

    #return render_template('home.html')


@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM feedback")
    data = cur.fetchall()

    return render_template('home.html',data=data)


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/save', methods=['POST'])
def create_user():
    name = request.form['nam']
    email = request.form['email']
    pwd = request.form['pwd']
    contact = request.form['mob']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (name, email, pwd, contact) VALUES (%s, %s, %s, %s)", (name, email, pwd, contact))
    mysql.connection.commit()
    cur.close()
    return render_template('signup.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email='"+username+"' and pwd='"+password+"'")
        user = cur.fetchone()

        if user is None:
            return render_template('signup.html', error='Invalid credentials')
        
       
            
        else:
            session['logged_in'] = True
            session["username"]=username
            return render_template('user_panel.html',user=user)



@app.route("/user_home")
def profile():
    if 'logged_in' not in session:
        return redirect('/signup')
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE email='"+session["username"]+"'")
    user = cur.fetchone()

    # render the age template
    return render_template('user_panel.html',user=user)

@app.route("/hist")
def history():
    if 'logged_in' not in session:
        return redirect('/signup')
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM breast_cancer_data WHERE user='"+session["username"]+"'")
    user = cur.fetchall()

    # render the age template
    return render_template('history.html',data=user)

@app.route("/pred")
def predect():
    if 'logged_in' not in session:
        return redirect('/signup')
    

    # render the age template
    return render_template('pred.html')

@app.route("/feed")
def feedb():
    if 'logged_in' not in session:
        return redirect('/signup')
    

    # render the age template
    return render_template('feed.html')



@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        cdate=datetime.date.today()
        radius = float(request.form['radius_m'])
        tm = float(request.form['texture_m'])
        pm = float(request.form['perimeter_m'])
        aream = int(request.form['area_m'])
        smoothm = float(request.form['smooth_m'])
        compm = float(request.form['compact_m'])
        con_m = float(request.form['con_m'])
        cpm = float(request.form['cp_mean'])
        sym = float(request.form['symmetry_mean'])
        frac_m = float(request.form['fractal_mean'])
        radius_se = float(request.form['radius_se'])
        texture_se = float(request.form['texture_se'])
        pm_se = float(request.form['pm_se'])
        area_se = float(request.form['area_se'])
        smooth_se = float(request.form['smooth_se'])
        compact_se = float(request.form['compact_se'])
        con_se = float(request.form['con_se'])
        cp_se = float(request.form['cp_se'])
        symmetry_se = float(request.form['symmetry_se'])
        fractal_se= float(request.form['fractal_se'])
        radius_worst = float(request.form['radius_worst'])
        texture_worst = float(request.form['texture_worst'])
        pm_worst = float(request.form['pm_worst'])
        area_worst = int(request.form['area_worst'])
        smooth_worst = float(request.form['smooth_worst'])
        compact_worst = float(request.form['compact_worst'])
        con_worst = float(request.form['con_worst'])
        concavity_worst = float(request.form['concavity_worst'])
        symmetry_worst = float(request.form['symmetry_worst'])
        fractal_worst = float(request.form['fractal_worst'])


        
        
        data = np.array([[radius,tm,pm,aream,smoothm,compm,con_m,cpm,sym,frac_m,radius_se,pm_se,texture_se,area_se,smooth_se,compact_se,con_se,cp_se,symmetry_se,fractal_se,radius_worst,texture_worst,pm_worst,area_worst, smooth_worst,compact_worst,con_worst,concavity_worst,symmetry_worst,fractal_worst]])
        prediction = model.predict(data)
        if prediction =='M':
            res="cancer"
        else:
            res="normal"    
        cur = mysql.connection.cursor()    
        sql = "INSERT INTO breast_cancer_data (date_created,radius,tm,pm,aream,smoothm,compm,con_m,cpm,sym,frac_m,radius_se,texture_se,pm_se,area_se,smooth_se,compact_se,con_se,cp_se,symmetry_se,fractal_se,radius_worst,texture_worst,pm_worst,area_worst, smooth_worst,compact_worst,con_worst,concavity_worst,symmetry_worst,fractal_worst,user,result) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (cdate,radius,tm,pm,aream, smoothm,compm,con_m,cpm,sym,frac_m,radius_se,texture_se,pm_se,area_se,smooth_se,compact_se,con_se,cp_se,symmetry_se,fractal_se,radius_worst,texture_worst,pm_worst,area_worst, smooth_worst,compact_worst,con_worst,concavity_worst,symmetry_worst,fractal_worst,session["username"],res)
        cur.execute(sql, values)
        mysql.connection.commit()
        cur.close()
        # Render prediction results template with prediction string
        return render_template('result.html', pr=prediction)
        




@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


@app.route('/signin')
def signin():
    return render_template('signup.html')




if __name__=='__main__':
    app.run(debug=True)