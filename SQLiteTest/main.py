from flask import Flask, render_template, request, redirect, url_for
#import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
#Optional: But it will silence the deprecation warning in the console.
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    #Optional: this will allow each book object to be identified by its title when printed.
    #def __repr__(self):
        #return f'<Book {self.title}>'

#new_book = Book( title="Test", author="Louis Sachar", rating=9.8)
#with app.app_context():
    #db.create_all()
    #db.session.add(new_book)
    #book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter and the Chamber of Secrets")).scalar()
    #book_to_update.title = "Harry Potter"
    #db.session.commit() 
    
#Update A Particular Record By Query---------------
#with app.app_context():
    #book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    #book_to_update.title = "Harry Potter and the Chamber of Secrets"
    #db.session.commit() 

#Update A Record By PRIMARY KEY----------------------
#book_id = 1
#with app.app_context():
#    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#    # or book_to_update = db.session.get(Book, book_id)  
#    # Note Book.query.get() is deprecated
#    book_to_update.title = "Harry Potter and the Goblet of Fire"
#    db.session.commit() 

#Delete A Particular Record By PRIMARY KEY-----------------------
#book_id = 1
#with app.app_context():
#    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#    db.session.delete(book_to_delete)
#    db.session.commit()


#Read All Records-------------------
#with app.app_context():
   #all_books = db.session.execute(db.select(Book)).scalars()
    # or all_books = db.session.query(Book).all()
    # or all_books = Book.query.all()

#Read A Particular Record By Query-------------------
#with app.app_context():
    #book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    # or book = db.session.query(Book).filter_by(title="Harry Potter").first()
    # or book = Book.query.filter_by(title="Harry Potter").first()



#db = sqlite3.connect("books-collection.db")
#cursor = db.cursor()
#cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#cursor.execute("INSERT or IGNORE INTO books VALUES('1', 'Harry Potter', 'J. K. Rowling', '9.3')")
#db.commit()
@app.route('/')
def home():
    ##READ ALL RECORDS
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
         # CREATE RECORD
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        #UPDATE RECORD
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit_rating.html", book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

