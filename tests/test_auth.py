import unittest
from app import create_app, db
from app.models import User

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('config.TestConfig')
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()
        self.user_data = {'username': 'testuser', 'password': 'password'}

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_signup(self):
        response = self.client.post('/auth/signup', json=self.user_data)
        self.assertEqual(response.status_code, 201)
    
    def test_signin(self):
        self.client.post('/auth/signup', json=self.user_data)
        response = self.client.post('/auth/signin', json=self.user_data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
