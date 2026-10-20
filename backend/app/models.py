import enum
from datetime import datetime
from sqlalchemy import String,Integer,Text,Boolean,ForeignKey,DateTime,Enum,JSON,UniqueConstraint,func
from sqlalchemy.orm import Mapped,mapped_column,relationship
from .database import Base
class UserRole(str,enum.Enum):founder='founder';member='member';mentor='mentor';admin='admin'
class StartupStage(str,enum.Enum):idea='idea';prototype='prototype';mvp='mvp';growth='growth'
class ApplicationStatus(str,enum.Enum):pending='pending';accepted='accepted';rejected='rejected'
class User(Base):
    __tablename__='users';id:Mapped[int]=mapped_column(primary_key=True);name:Mapped[str]=mapped_column(String(100));email:Mapped[str]=mapped_column(String(255),unique=True,index=True);password_hash:Mapped[str]=mapped_column(String(255));role:Mapped[UserRole]=mapped_column(Enum(UserRole),default=UserRole.member);created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),server_default=func.now());startups:Mapped[list['Startup']]=relationship(back_populates='owner')
class Startup(Base):
    __tablename__='startups';id:Mapped[int]=mapped_column(primary_key=True);name:Mapped[str]=mapped_column(String(100));slug:Mapped[str]=mapped_column(String(120),unique=True,index=True);tagline:Mapped[str]=mapped_column(String(180));description:Mapped[str]=mapped_column(Text);industry:Mapped[str]=mapped_column(String(80),index=True);stage:Mapped[StartupStage]=mapped_column(Enum(StartupStage));location:Mapped[str]=mapped_column(String(100));funding_goal:Mapped[int]=mapped_column(Integer);team_size:Mapped[int]=mapped_column(default=1);progress:Mapped[int]=mapped_column(default=0);is_featured:Mapped[bool]=mapped_column(Boolean,default=False);open_roles:Mapped[list[str]]=mapped_column(JSON,default=list);owner_id:Mapped[int]=mapped_column(ForeignKey('users.id',ondelete='CASCADE'));owner:Mapped[User]=relationship(back_populates='startups');applications:Mapped[list['Application']]=relationship(back_populates='startup',cascade='all, delete-orphan')
class Application(Base):
    __tablename__='applications';__table_args__=(UniqueConstraint('startup_id','applicant_id'),);id:Mapped[int]=mapped_column(primary_key=True);message:Mapped[str]=mapped_column(Text);status:Mapped[ApplicationStatus]=mapped_column(Enum(ApplicationStatus),default=ApplicationStatus.pending);startup_id:Mapped[int]=mapped_column(ForeignKey('startups.id',ondelete='CASCADE'));applicant_id:Mapped[int]=mapped_column(ForeignKey('users.id',ondelete='CASCADE'));created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),server_default=func.now());startup:Mapped[Startup]=relationship(back_populates='applications')
