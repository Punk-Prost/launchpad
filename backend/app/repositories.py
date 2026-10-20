from sqlalchemy import select
from sqlalchemy.orm import Session
from .models import Startup
from .schemas import StartupCreate
class StartupRepository:
    def __init__(self,db:Session):self.db=db
    def list(self,industry:str|None=None,stage:str|None=None,search:str|None=None):
        q=select(Startup)
        if industry:q=q.where(Startup.industry==industry)
        if stage:q=q.where(Startup.stage==stage)
        if search:q=q.where(Startup.name.ilike(f'%{search}%'))
        return list(self.db.scalars(q.order_by(Startup.is_featured.desc(),Startup.id.desc())))
    def create(self,data:StartupCreate,owner_id:int):
        item=Startup(**data.model_dump(),owner_id=owner_id);self.db.add(item);self.db.commit();self.db.refresh(item);return item
