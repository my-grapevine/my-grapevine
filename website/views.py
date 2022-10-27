from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .create_db import Note
from . import db
from .api.events import get_events, get_event_by_id
import json

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", user=current_user)


@views.route('/events')
def events():
    event_details = get_events()
    return render_template("events.html", user=current_user, event_details=event_details)


@views.route('/event/<event_id>')
def event(event_id):
    event = get_event_by_id(event_id)
    return render_template("event.html", user=current_user, event=event)


@views.route('/search')
def search():
    return render_template("search.html", user=current_user)


@views.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("notes.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
