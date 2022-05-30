from flask import Flask, request, redirect, render_template, jsonify
from models import db, connect_db, Users

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sqla_info'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route("/")
def list_info():
    users = Users.query.all()
    return render_template("list.html", users=users) 

@app.route("/" , methods = ["POST"])
def add_user():

    name = request.form['name']
    address = request.form['address']
    users = Users(name=name, address=address)
    db.session.add(users)
    db.session.commit()

    return redirect(f"/{users.id}")

@app.route("/<int:users_id>" )
def show_user(users_id):
    # users = Users.get_or_404(users_id)
    users = Users.query.filter_by(id=users_id).first_or_404()
    return render_template("detail.html", users=users)


@app.route("/<int:users_id>/delete" , methods=["GET","POST"])
def delete_user(users_id):
    # print('users_id...', users_id)
    users = Users.query.filter_by(id=users_id).one()
    # users = Users.query.get(users_id)
    if request.method == "POST" :
        if users:
            db.session.delete(users)
            db.session.commit()
            return redirect('/')

    return render_template("delete.html", users=users) 
    # return "Successfully deleted"


@app.route("/<int:users_id>/update" , methods=["GET","POST"])
def update_user(users_id):
    users = Users.query.filter_by(id=users_id).first_or_404()
    if request.method == "POST" :
        if users:
            users.name = request.form['name']
            users.address = request.form['address']
            db.session.commit()
            return redirect(f"/{users.id}")
            
        # return f"User with id = {id} Does nit exist"
    return render_template("update.html", users=users) 



# @app.route("/button",  methods=["POST"])
# def button(users_id):
#     print('button...', users_id)
#     return render_template("delete.html") 