from flask import Blueprint, render_template, flash, url_for,redirect
from flask_login import login_required, current_user
from .create_db import Note, User
from . import db
from .api.events import get_events,get_event_details, get_attraction_details,  get_event_by_id, search
from .create_note import create_note, add_event



views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", user=current_user)


@views.route('/')
def get_event_data():
    event_details = get_event_details()
    return event_details

@views.route('/attraction')
def get_attraction_data():
    attraction_details = get_attraction_details()
    return attraction_details

@views.route('/events')
def events():
    event_details = get_events()
    return render_template("events.html", user=current_user, event_details=event_details)


@views.route('/event/<event_id>')
def event(event_id):
    event = get_event_by_id(event_id)
    return render_template("event.html", user=current_user, event=event)


@views.route('/search', methods=['GET', 'POST'])
def search_events():
    event_data = search()
    return render_template("search.html", user=current_user, event_data=event_data)


@views.route('/admin')
@login_required
def admin():
    id = current_user.id
    if id == 1:
        return render_template("admin.html", user=current_user, id=id)
    else:
        flash("Sorry you must be the Admin to access the Admin Page...")
        return redirect(url_for('home.html'))

@views.route('/notes')
@login_required
def notes():
    notes = db.session.query(User.first_name, Note.user_id, Note.title, Note.content, Note.date).join(Note, Note.user_id == User.id, isouter=True).all()
    return render_template("notes.html", user=current_user, notes=notes)


@views.route('/add_note', methods=['GET', 'POST'])
@login_required
def add_note():
    form = create_note()
    return render_template("add_note.html",user=current_user, form=form)


@views.route('/event', methods=['GET', 'POST'])
@login_required
def add_event():
    event = add_event
    return render_template("events.html", user=current_user, event=event)



