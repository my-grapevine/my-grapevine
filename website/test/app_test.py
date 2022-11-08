import unittest
from unittest import TestCase
from flask import current_app
from werkzeug.security import generate_password_hash
from website import create_app, db
from website.create_db import User
from flask_login import login_user

from dotenv import find_dotenv, load_dotenv
dotenv_test_path = find_dotenv(".env.test")
load_dotenv(dotenv_test_path, override=True)
from website.db_init import create_database, drop_database


class TestWebApp(TestCase):

    @classmethod
    def setUpClass(cls):

        def setUp(self):
            create_database()
            db.create_all()
            self.populate_db()

    def setUp(self):
        self.app = create_app()
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()

    @classmethod
    def tearDownClass(cls) -> None:

        def tearDown(self):
            db.drop_all()
            drop_database()
            self.appctx.pop()
            self.app = None
            self.appctx = None
            self.client = None


    def populate_db(self):
        user = User(email='susan@example.com',first_name='susan',password=generate_password_hash(
                '1234567', method='sha256', salt_length=16))
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)

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
            'password': '1234567'
        })

    def test_app(self):
        assert self.app is not None
        assert current_app == self.app


    def test_register_user_correct_data(self):
        response = self.register(first_name='llonna',
                                 email='llonna@mail.com',
                                 password1='1234567',
                                 password2='1234567')
        self.assertEqual(response.status_code, 200)

    def register(self, first_name, email, password1, password2):
        return self.client.post(
            '/sign-up',
            data=dict(firstName=first_name,
                      email=email,
                      password1=password1,
                      password2=password2),
            follow_redirects=True)

    def test_register_user_mismatched_passwords(self):
        response = self.register(first_name='pat',
                                 email='me@mail.com',
                                 password1='Flask',
                                 password2='Flask')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Password must be at least 7 characters.',
                      response.data)

    def register(self, first_name, email, password1, password2):
        return self.client.post(
            '/sign-up',
            data=dict(firstName=first_name,
                      email=email,
                      password1=password1,
                      password2=password2),
            follow_redirects=True)

    def test_registered_user_query(self):
            expected = [('llonna',)]
            result = db.session.query(User.first_name).all()
            self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()