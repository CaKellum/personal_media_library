from application import app, database
from .data_connection import DataBase
from application.models import Media, Format
from flask import render_template, url_for, flash, redirect, request


@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    media_list = [
        Media.tuple_to_media(item) for item in database.get_media_list()
    ]
    return render_template('home.html', title="home", media_list=media_list)


@app.route("/add", methods=["GET", "POST"])
def add():
    format_list = [
        Format.tuple_to_format(item) for item in database.get_format_list()
    ]
    if request.method == "POST":
        title = request.form.get("title")
        format = request.form.get("format")
        if title == None or format == None:
            flash("Title and Format are required")
        else:
            shared_discs = request.form.get("shared_disc")
            run_time = request.form.get("run_time")

            insert = Media(title=title,
                           format=format,
                           runtime=run_time,
                           shared_disc=shared_discs)
            database.insert_media(data=insert)
            return redirect(url_for('index'))
    return render_template('add.html', format_list=format_list)