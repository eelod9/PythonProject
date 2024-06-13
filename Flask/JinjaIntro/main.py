from flask import Flask, render_template
import random
import datetime
app = Flask(__name__)
import requests

current_Year = datetime.datetime.now().year
@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_Year = datetime.datetime.now().year
    return render_template('index.html',num = random_number, year= current_Year)

@app.route('/guess/<userInput>')
def guess(userInput):
    response_agify = requests.get(url=f"https://api.agify.io?name={userInput}")
    response_agify.raise_for_status()
    data_agify = response_agify.json()
    age = data_agify["age"]
    response_genderize = requests.get(url=f"https://api.genderize.io?name={userInput}")
    response_genderize.raise_for_status()
    data_genderize = response_genderize.json()
    gender = data_genderize["gender"]
    return render_template('guess.html',name = userInput.title(), year= current_Year,age=age,gender=gender)
    #return f'<h1>Hey {userInput.upper()}</h1>\
    #            <p>I think you are {gender}</p>\
    #                <p>And maybe {age} years old.<p>'

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/f6881e6a31642c1236c0"   
    response = requests.get(url=blog_url)
    response.raise_for_status()
    all_posts= response.json() 
    return render_template("blog.html",posts = all_posts)
if __name__ == "__main__":
    app.run(debug=True)


