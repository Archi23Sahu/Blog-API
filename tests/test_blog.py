import unittest
from app import create_app, db
from app.models import User, BlogPost

class BlogTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('config.TestConfig')
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()
        self.user_data = {'username': 'testuser', 'password': 'password'}
        self.client.post('/auth/signup', json=self.user_data)
        self.client.post('/auth/signin', json=self.user_data)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_create_post(self):
        response = self.client.post(
            '/api/posts',
            json={'title': 'Test Post', 'content': 'Test Content'},
            auth=(self.user_data['username'], self.user_data['password'])
    )
        self.assertEqual(response.status_code, 201)
    
    def test_get_posts(self):
        response = self.client.get('/api/posts')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
