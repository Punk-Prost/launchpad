from sqlalchemy import select
from .database import Base,engine,SessionLocal
from .models import User,UserRole,Startup,StartupStage
from .security import hash_password
def run():
    Base.metadata.create_all(engine);db=SessionLocal()
    if db.scalar(select(User).limit(1)):db.close();return
    founder=User(name='Алия Каримова',email='founder@launchpad.dev',password_hash=hash_password('Founder123!'),role=UserRole.founder)
    mentor=User(name='Тимур Азимов',email='mentor@launchpad.dev',password_hash=hash_password('Mentor123!'),role=UserRole.mentor)
    admin=User(name='LaunchPad Admin',email='admin@launchpad.dev',password_hash=hash_password('Admin123!'),role=UserRole.admin)
    db.add_all([founder,mentor,admin]);db.flush()
    rows=[('TerraLoop','terraloop','Циркулярная вода для индустрии','Модульная система очистки и повторного использования воды на производстве.','ClimateTech',StartupStage.mvp,'Ташкент',120000,6,68,True,['ML Engineer','Sales Lead']),('AeroCrop','aerocrop','Точное земледелие без сложной техники','Дроны и аналитика для оценки состояния посевов.','AgriTech',StartupStage.prototype,'Алматы',80000,4,42,True,['Product Designer']),('NeuroNote','neuronote','Знания команды, которые отвечают сами','Корпоративная база знаний с семантическим поиском.','AI',StartupStage.growth,'Астана',300000,11,84,False,['Backend Engineer','Growth'])]
    for r in rows:db.add(Startup(name=r[0],slug=r[1],tagline=r[2],description=r[3],industry=r[4],stage=r[5],location=r[6],funding_goal=r[7],team_size=r[8],progress=r[9],is_featured=r[10],open_roles=r[11],owner_id=founder.id))
    db.commit();db.close()
if __name__=='__main__':run()
