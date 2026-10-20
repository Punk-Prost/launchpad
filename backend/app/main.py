from fastapi import FastAPI,Depends,HTTPException,Query,status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.orm import Session
from .database import get_db
from .models import User,UserRole,Startup,Application
from .schemas import UserCreate,Login,Token,StartupCreate,StartupOut,ApplicationCreate,ApplicationOut
from .security import hash_password,verify_password,create_token,current_user,require_roles
from .repositories import StartupRepository
from .config import settings
app=FastAPI(title='LaunchPad API',version='1.0.0',description='REST API for startup discovery and team building',docs_url='/docs')
app.add_middleware(CORSMiddleware,allow_origins=[x.strip() for x in settings.cors_origins.split(',') if x.strip()],allow_credentials=True,allow_methods=['*'],allow_headers=['*'])
@app.get('/health')
def health():return {'status':'ok'}
@app.post('/auth/register',response_model=Token,status_code=201)
def register(data:UserCreate,db:Session=Depends(get_db)):
    if db.scalar(select(User).where(User.email==data.email)):raise HTTPException(409,'Email уже зарегистрирован')
    user=User(name=data.name,email=data.email,password_hash=hash_password(data.password),role=data.role);db.add(user);db.commit();db.refresh(user);return Token(access_token=create_token(user),user=user)
@app.post('/auth/login',response_model=Token)
def login(data:Login,db:Session=Depends(get_db)):
    user=db.scalar(select(User).where(User.email==data.email))
    if not user or not verify_password(data.password,user.password_hash):raise HTTPException(401,'Неверный email или пароль')
    return Token(access_token=create_token(user),user=user)
@app.get('/startups',response_model=list[StartupOut])
def list_startups(industry:str|None=None,stage:str|None=None,search:str|None=Query(None,max_length=100),db:Session=Depends(get_db)):return StartupRepository(db).list(industry,stage,search)
@app.get('/startups/{slug}',response_model=StartupOut)
def get_startup(slug:str,db:Session=Depends(get_db)):
    item=db.scalar(select(Startup).where(Startup.slug==slug))
    if not item:raise HTTPException(404,'Проект не найден')
    return item
@app.post('/startups',response_model=StartupOut,status_code=201)
def create_startup(data:StartupCreate,user:User=Depends(require_roles(UserRole.founder,UserRole.admin)),db:Session=Depends(get_db)):return StartupRepository(db).create(data,user.id)
@app.put('/startups/{startup_id}',response_model=StartupOut)
def update_startup(startup_id:int,data:StartupCreate,user:User=Depends(current_user),db:Session=Depends(get_db)):
    item=db.get(Startup,startup_id)
    if not item:raise HTTPException(404,'Проект не найден')
    if item.owner_id!=user.id and user.role!=UserRole.admin:raise HTTPException(403,'Недостаточно прав')
    for k,v in data.model_dump().items():setattr(item,k,v)
    db.commit();db.refresh(item);return item
@app.delete('/startups/{startup_id}',status_code=204)
def delete_startup(startup_id:int,user:User=Depends(current_user),db:Session=Depends(get_db)):
    item=db.get(Startup,startup_id)
    if not item:raise HTTPException(404,'Проект не найден')
    if item.owner_id!=user.id and user.role!=UserRole.admin:raise HTTPException(403,'Недостаточно прав')
    db.delete(item);db.commit()
@app.post('/startups/{startup_id}/applications',response_model=ApplicationOut,status_code=201)
def apply(startup_id:int,data:ApplicationCreate,user:User=Depends(current_user),db:Session=Depends(get_db)):
    if not db.get(Startup,startup_id):raise HTTPException(404,'Проект не найден')
    item=Application(**data.model_dump(),startup_id=startup_id,applicant_id=user.id);db.add(item)
    try:db.commit();db.refresh(item)
    except Exception:db.rollback();raise HTTPException(409,'Вы уже подали заявку')
    return item
@app.get('/admin/users',dependencies=[Depends(require_roles(UserRole.admin))])
def admin_users(db:Session=Depends(get_db)):return db.scalars(select(User)).all()
