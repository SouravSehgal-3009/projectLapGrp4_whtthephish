from flask import Flask, render_template
from flask import redirect, url_for, request,session
from src.common.database import Database
from src.models.user import User
from src.models.question import Question  
from src.secrets import SECRET_KEY
import random
from src.common.calc_functions import cal_star


PORT = 8000

app = Flask("__main__")
app.secret_key=SECRET_KEY

@app.before_first_request
def initialize_database():
    Database.initialize()
    session['email']=None

@app.route("/")
def index():
    return "Welcome"

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        email=request.form['email']
        u_password=request.form['password']
        if User.login_valid(email=email,password=u_password):
            User.login(email)
            return redirect(url_for('dashboard'))
        else:
            return "Invalid Username Or Password"
    return render_template('index.html')



@app.route("/signUp",methods=["GET","POST"])
def signUp():
    if request.method == "POST":
        email=request.form['email']
        u_password=request.form['password']
        name=request.form['name']
        if not User.validate_Form(name,email,u_password):
            return "Form Validation Failed!"
        if User.get_by_email(email) is not None:
            return "Email Already Registered!"
        success=User.register(email,u_password,name)
        if not success:
            return "Something Went Wrong. Please try Again Later."
        return redirect('/dashboard')
        
    return render_template('signUp.html')


@app.route("/dashboard")
def dashboard():
    if session['email'] is not None:
        user=User.get_by_email(session['email'])
        return render_template('dashboard.html',user=user)
    else:
        return redirect(url_for('login'))

@app.route('/level<level>',methods=["GET","POST"])
def level(level):
    if session['email'] is not None: 
        if request.method=='POST':
            ans = []
            correct_ans = []
            for i in range(1,11):
                t = request.form.get(f"question{i}",-1)
                if "yes"==t:
                    ans.append("1")
                elif "no"==t:
                    ans.append("0")
                else:
                    ans.append("-1")
                correct_ans.append(request.form[f"{i}"])
            count = 0
            for i in range(10):
                if ans[i] == correct_ans[i]:
                    count+=1
            user = User.get_by_email(session["email"])
            
            star = cal_star(count)
            star = max(star,getattr(user, f"level{level}"))
            total_star = user.stars - getattr(user, f"level{level}") + star
            User.updateUser(user.email, {"stars": total_star, f"level{level}": star})
            
            return redirect(url_for('dashboard'))
        data_phishing = Question.get_by_category_and_phishing(int(level), 1)
        legitimate = Question.get_by_category_and_phishing(int(level), 0)
        data = random.sample(data_phishing, 6) + random.sample(legitimate, 4)
        random.shuffle(data)
      
        return render_template(f'Level{level}.html', data = data)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    User.logout()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = PORT, debug = True)