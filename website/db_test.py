import os
os.environ['DATABASE_URL'] = 'mysql+pymysql://'
import unittest
from unittest import TestCase
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from website import create_app, db
from .create_db import User


class TestWebApp(TestCase):
    def setUp(self):
        self.app = create_app()
        #self.app.config['WTF_CSRF_ENABLED'] = False
        self.appctx = self.app.app_context()
        self.appctx.push()
        db.create_all()
        self.populate_db()
        self.client = self.app.test_client()

    def tearDown(self):
        db.drop_all()
        self.appctx.pop()
        self.app = None
        self.appctx = None
        self.client = None

    def populate_db(self):
        user = User( email='susan@example.com',first_name='susan',password=generate_password_hash(
                '1234567', method='sha256',salt_length=16))
        db.session.add(user)
        db.session.commit()

    def test_registration_form(self):
        response = self.client.get('/sign-up')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert 'name="email"' in html
        assert 'name="firstName"' in html
        assert 'name="password1"' in html
        assert 'name="password2"' in html

    def test_home_page_redirect(self):
        response = self.client.get('/', follow_redirects=True)
        assert response.status_code == 200
        assert response.request.path == '/'



    def login(self):
        self.client.post('/auth/login', data={
            'email': 'susan@example.com',
            'password': check_password_hash(
                '1234567', method='sha256',salt_length=16),
        })

    def test_app(self):
        assert self.app is not None
        assert current_app == self.app


if __name__ == '__main__':
    unittest.main()
