from flask import Flask, render_template, request

app = Flask(__name__)

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# User registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Retrieve form data and create user profile
        name = request.form.get('name')
        age = request.form.get('age')
        # ... other user details
        # Save user profile to the database
        # ...
        return render_template('success.html', name=name)
    return render_template('register.html')

# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve form data and validate login credentials
        username = request.form.get('username')
        password = request.form.get('password')
        # ... validate credentials
        # Redirect user to their profile page
        return render_template('profile.html', username=username)
    return render_template('login.html')

# User profile
@app.route('/profile/<username>')
def profile(username):
    # Fetch user profile from the database based on username
    # ...
    return render_template('profile.html', username=username, profile=profile)

# Search and matching
@app.route('/search')
def search():
    # Implement search functionality based on user preferences
    # ...
    return render_template('search.html', results=results)

# Chatting
@app.route('/chat/<recipient>')
def chat(recipient):
    # Fetch chat history between current user and recipient
    # ...
    return render_template('chat.html', recipient=recipient, chat_history=chat_history)

# Reporting
@app.route('/report/<username>')
def report(username):
    # Implement reporting functionality for inappropriate behavior
    # ...
    return render_template('report.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
