from flask import flash, request, redirect, url_for
from .create_db import Note, NoteForm, UserEvent
from . import db
from flask_login import current_user


def create_note():
    form = NoteForm()

    if form.validate_on_submit():
        poster = current_user.id
        note = Note(title=form.title.data, content=form.content.data, user_id=poster, slug=form.slug.data)
        form.title.data = ""
        form.content.data = ""
        form.slug.data = ""

        db.session.add(note)
        db.session.commit()
        flash('Your thoughts have been saved')
    return form


