from flask import Blueprint, render_template, url_for, request, redirect
from database import *

public = Blueprint('public', __name__)

@public.route('/')
def home():

    # FETCH GALLERY DATA
    q = "SELECT * FROM gallery"
    gallery = select(q)

    # FETCH TRAINING / PROVIDE DATA
    q1 = "SELECT * FROM training"
    provide = select(q1)

    return render_template(
        "home.html",
        gallery=gallery,
        provide=provide
    )


@public.route('/login', methods=['GET', 'POST'])
def login():

    if 'submit' in request.form:

        uname = request.form['username']
        passs = request.form['password']

        q = "SELECT * FROM login WHERE uname='%s' AND pass='%s'" % (uname, passs)

        res = select(q)

        if res:

            if res[0]['usertype'] == "admin":

                return redirect(url_for("admin.home"))

            else:

                return "Registration Under Process"

        else:

            return "You are Not Registered"

    return render_template("login.html")