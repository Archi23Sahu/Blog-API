Requirements:

Design and implement a RESTful API using Python Flask.

The API should have endpoints for:

Creating a new blog post

Retrieving a list of all blog posts

Retrieving a single blog post by its ID

Updating an existing blog post

Deleting a blog post

Implement basic authentication for the API. Users should be able to sign up, sign in, and authenticate their requests to create, update, or delete blog posts.

Use a database of your choice (e.g., MongoDB, PostgreSQL, MySQL) to store blog post data.

Write some unit tests to ensure the reliability of your code.

-------------------------------


MySQL Database query:

CREATE SCHEMA blog_platform;

CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(64) NOT NULL UNIQUE,
    password_hash VARCHAR(128) NOT NULL
);

CREATE TABLE blog_post (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(128) NOT NULL,
    content TEXT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
);

To Run Code python API:

1. Download Postman
2. Download python code
3. Where you kept the python code open cmd and Install Flask and Flask-HTTPAuth "pip install Flask Flask-HTTPAuth Flask-Migrate Flask-SQLAlchemy mysqlclient"
4. to verify installation "pip show Flask Flask-HTTPAuth Flask-Migrate Flask-SQLAlchemy mysqlclient"
5. in cmd set env variable "export DATABASE_URL='mysql://username:password@localhost/blog_platform'
							export SECRET_KEY='my_secret_key' "
6. Now run "python run.py"

7. Go to postman
8. For SignUp: use url http://127.0.0.1:5000/auth/signup and select POST request 
    in body add
	{
  "username": "username1",
  "password": "password"
	}
	click send
	
9. For SignIn: use url http://127.0.0.1:5000/auth/signin and select POST request 
	in body add
	{
  "username": "username1",
  "password": "password"
	}
	click send
	
10. To create Blog:  use url http://127.0.0.1:5000/api/posts, select POST request  and in the "Authorization" tab, select "Basic Auth" and enter your username and password.
 
	in body select raw and JSON
	{
	  "title": "My First Post",
	  "content": "Hello, world!"
	}
	click Send

11. All Blogs:   use url http://127.0.0.1:5000/api/posts and select GET request  

12.  Single Blog Post:  use url http://127.0.0.1:5000/api/posts/1 and select GET request

13. Update a Blog Post: use url http://127.0.0.1:5000/api/posts/1, select PUT request and in the "Authorization" tab, select "Basic Auth" and enter your username and password.
	in body select raw and JSON
	{
	  "title": "Updated My First Post",
	  "content": "Updated Hello, world!"
	}
	click Send
	
14. Delete a Blog Post:  use url http://127.0.0.1:5000/api/posts/1, select DELETE request and in the "Authorization" tab, select "Basic Auth" and enter your username and password.click Send.


To run TEST cases:

1. pip install pytest
2. python -m unittest tests/test_auth.py
3. python -m unittest tests/test_blog.py
