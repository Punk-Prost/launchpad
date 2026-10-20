from pydantic import BaseModel,EmailStr,Field,ConfigDict
from .models import UserRole,StartupStage,ApplicationStatus
class UserCreate(BaseModel):name:str=Field(min_length=2,max_length=100);email:EmailStr;password:str=Field(min_length=8);role:UserRole=UserRole.member
class Login(BaseModel):email:EmailStr;password:str
class UserOut(BaseModel):model_config=ConfigDict(from_attributes=True);id:int;name:str;email:EmailStr;role:UserRole
class Token(BaseModel):access_token:str;token_type:str='bearer';user:UserOut
class StartupBase(BaseModel):name:str=Field(min_length=2,max_length=100);slug:str=Field(pattern=r'^[a-z0-9-]+$');tagline:str=Field(max_length=180);description:str=Field(min_length=20);industry:str;stage:StartupStage;location:str;funding_goal:int=Field(gt=0);team_size:int=Field(ge=1);progress:int=Field(ge=0,le=100);is_featured:bool=False;open_roles:list[str]=[]
class StartupCreate(StartupBase):pass
class StartupOut(StartupBase):model_config=ConfigDict(from_attributes=True);id:int;owner_id:int
class ApplicationCreate(BaseModel):message:str=Field(min_length=20,max_length=2000)
class ApplicationOut(BaseModel):model_config=ConfigDict(from_attributes=True);id:int;message:str;status:ApplicationStatus;startup_id:int;applicant_id:int
