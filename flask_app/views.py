from flask_app import app, db
from flask_app.models import Book, Writer, User
from flask import render_template

@app.route("/addbook")
def addBook():
    try:
        writer = Writer(name="Elham")
        book = Book(name="The Book", writer=writer)
        writer.books.append(book)
        db.session.add(book)
        db.session.commit()
        return "Adding book successfully ==>> " + "<a href='/books'> All Books </a>"
    except Exception as e:
        return "Adding book failed ==>> " + str(e)

@app.route('/books')
def showBook():
    books = Book.query.all()
    return render_template("result.html", books=books)

@app.route('/')
def home():
    # users = User.query.filter(User.name.like("re%")).all()
    # users = User.query.filter(User.name.contains("re")).all()
    # users = User.query.filter(User.name.ilike("re%")).all()
    users = User.query.all()


    return render_template("result.html", users=users)

@app.route('/add')
def addUser():
    try:
        user = User()
        user.name = "Reza"
        db.session.add(user)
        db.session.commit()
        return "Adding user successfully!"
    except Exception as e:
        return "Adding user failed! error is: " + str(e)

@app.route('/update')
def updateUser():
    try:
        user = User.query.filter_by(name="Reza").first()
        user.name = "Mohammad"
        db.session.commit()
        return "User updated successfully " + "<a href='/'> Home </a>"
    except Exception as e:
        return "Updating user failed, error is: " + str(e)
    

@app.route('/delete')
def deleteUser():
    try:
        user = User.query.filter_by(name="Reza").first()
        db.session.delete(user)
        db.session.commit()
        return "User deleted successfully " + "<a href='/'> Home </a>"
    except Exception as e:
        return "Deleting user failed, error is: " + str(e)
    
@app.errorhandler(404)
def showError(error):
    return "The error is " + str(error)