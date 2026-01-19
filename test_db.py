from gamification.database import SessionLocal, engine
from gamification.models_db import User
from sqlalchemy import text

def test_db():
    print("Testing DB connection...")
    try:
        db = SessionLocal()
        # Check if tables verify
        result = db.execute(text("SELECT name FROM sqlite_master WHERE type='table' AND name='users';"))
        if result.fetchone():
            print("✅ 'users' table exists.")
        else:
            print("❌ 'users' table MISSING.")
            
        # Check user
        user = db.query(User).first()
        if user:
            print(f"✅ Found user: {user.username}, XP: {user.xp}")
        else:
            print("ℹ️ No user found (will be created on first request).")
            
        db.close()
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_db()
