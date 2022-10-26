from flask import Flask, flash, request, render_template, redirect
from events import get_event_details, get_attraction_details, search

app = Flask(__name__)

@app.get('/')
def get_event_data():
    event_details = get_event_details()
    return event_details

@app.get('/attraction')
def get_attraction_data():
    attraction_details = get_attraction_details()
    return attraction_details

@app.get('/search')
def search_events():
    search_details = search()

    return search_details


if __name__ == '__main__':
    app.run()
