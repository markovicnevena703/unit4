from flask import Flask, render_template
from data import test,users

app = Flask(__name__)

@app.route("/")
def feed():
    return render_template('feed.html', posts=test, title="Feed Page")

@app.route("/post/<int:post_id>")
def post_page(post_id):
    post=test[post_id]
    return render_template('post.html', post=post, title=post["RouteName"])

@app.route("/users/<string:username>")
def profile(username):
    user=users[username]
    return render_template('profile.html', user=user)
    
