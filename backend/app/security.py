from datetime import datetime,timedelta,timezone
from jose import jwt,JWTError
from passlib.context import CryptContext
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings
from .database import get_db
from .models import User,UserRole
pwd=CryptContext(schemes=['bcrypt'],deprecated='auto');oauth=OAuth2PasswordBearer(tokenUrl='/auth/login')
def hash_password(value:str):return pwd.hash(value)
def verify_password(value:str,hashed:str):return pwd.verify(value,hashed)
def create_token(user:User):
    exp=datetime.now(timezone.utc)+timedelta(minutes=settings.access_token_expire_minutes)
    return jwt.encode({'sub':str(user.id),'role':user.role.value,'exp':exp},settings.jwt_secret,algorithm='HS256')
def current_user(token:str=Depends(oauth),db:Session=Depends(get_db)):
    error=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Недействительный токен')
    try:user_id=int(jwt.decode(token,settings.jwt_secret,algorithms=['HS256'])['sub'])
    except (JWTError,KeyError,ValueError):raise error
    user=db.get(User,user_id)
    if not user:raise error
    return user
def require_roles(*roles:UserRole):
    def check(user:User=Depends(current_user)):
        if user.role not in roles:raise HTTPException(403,'Недостаточно прав')
        return user
    return check
