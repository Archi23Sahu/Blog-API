from flask import Blueprint, request, jsonify
from flask_httpauth import HTTPBasicAuth
from .models import BlogPost, User
from . import db

blog_bp = Blueprint('blog', __name__)
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    return None

@blog_bp.route('/posts', methods=['POST'])
@auth.login_required
def create_post():
    data = request.get_json()
    title = data['title']
    content = data['content']
    user_id = auth.current_user().id

    new_post = BlogPost(title=title, content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()

    return jsonify({'message': 'Post created successfully'}), 201

@blog_bp.route('/posts', methods=['GET'])
def get_posts():
    posts = BlogPost.query.all()
    result = [{'id': post.id, 'title': post.title, 'content': post.content, 'user_id': post.user_id} for post in posts]
    return jsonify(result), 200

@blog_bp.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    result = {'id': post.id, 'title': post.title, 'content': post.content, 'user_id': post.user_id}
    return jsonify(result), 200

@blog_bp.route('/posts/<int:post_id>', methods=['PUT'])
@auth.login_required
def update_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    if post.user_id != auth.current_user().id:
        return jsonify({'message': 'You can only update your own posts'}), 403
    
    data = request.get_json()
    post.title = data['title']
    post.content = data['content']
    db.session.commit()
    
    return jsonify({'message': 'Post updated successfully'}), 200

@blog_bp.route('/posts/<int:post_id>', methods=['DELETE'])
@auth.login_required
def delete_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    if post.user_id != auth.current_user().id:
        return jsonify({'message': 'You can only delete your own posts'}), 403
    
    db.session.delete(post)
    db.session.commit()
    
    return jsonify({'message': 'Post deleted successfully'}), 200
