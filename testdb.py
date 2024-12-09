from database import app, db, User

with app.app_context():
    user =db.session.query(User).filter_by(username='testuser').first()
    if user:
        print("user found: ", user.username)
        print("Password hash", user.password)
    else:
        print("User not found")