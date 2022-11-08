from flask import Blueprint, request, render_template, flash, url_for, redirect
from flask_login import login_required, current_user
from .create_db import Note, User
from . import db
from .api.combined_events import CombinedEventManager
from .create_note import create_note


views = Blueprint('views', __name__)

combined_event_manager = CombinedEventManager()


@views.route('/')
def home():
    return render_template("home.html", user=current_user)


@views.route('/events')
def events():
    event_details = combined_event_manager.get_events()
    return render_template("events.html", user=current_user, event_details=event_details)


@views.route('/event/<event_id>')
def event(event_id):
    event = combined_event_manager.get_event_by_id(event_id)
    return render_template("event.html", user=current_user, event=event)


@views.route('/search')
def event_search():
    query = request.args.get('query')
    event_data = combined_event_manager.get_events(query) if query else None
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
    noteID = db.session.query(Note.id).all()
    if noteID == []:
        flash("Sorry, there is nothing to share at the moment.\n"
              "Please add your thoughts")
        return redirect(url_for('views.add_note'))
    else:
        notes = db.session.query(User.first_name, Note.user_id, Note.title, Note.content, Note.date).join(Note,Note.user_id == User.id, isouter=True).all()
        return render_template("notes.html", user=current_user, notes=notes)


@views.route('/add_notes', methods=['GET', 'POST'])
@login_required
def add_note():
    form = create_note()
    return render_template("add_note.html",user=current_user, form=form)

