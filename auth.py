from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

USERS = {
    "admin": {"password": "admin123", "role": "Admin"},
    "student": {"password": "stud123", "role": "Student"},
    "teacher": {"password": "teach123", "role": "Teacher"}
}

def create_token(data: dict, expires_minutes=60):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def login(username, password):
    if username in USERS and USERS[username]["password"] == password:
        return True, USERS[username]["role"]
    return False, None
