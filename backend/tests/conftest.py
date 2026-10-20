import os
os.environ['DATABASE_URL']='sqlite:///./test.db'
import pytest
from fastapi.testclient import TestClient
from app.database import Base,engine
from app.main import app
@pytest.fixture(autouse=True)
def database():
    Base.metadata.drop_all(engine);Base.metadata.create_all(engine);yield;Base.metadata.drop_all(engine)
@pytest.fixture
def client():return TestClient(app)
@pytest.fixture
def founder(client):
    data={'name':'Test Founder','email':'founder@test.dev','password':'StrongPass1!','role':'founder'}
    out=client.post('/auth/register',json=data).json();return {'Authorization':f"Bearer {out['access_token']}"}
@pytest.fixture
def member(client):
    data={'name':'Test Member','email':'member@test.dev','password':'StrongPass1!','role':'member'}
    out=client.post('/auth/register',json=data).json();return {'Authorization':f"Bearer {out['access_token']}"}
@pytest.fixture
def startup_data():return {'name':'Solar Mesh','slug':'solar-mesh','tagline':'Energy for everyone','description':'Distributed renewable energy platform for local communities.','industry':'ClimateTech','stage':'mvp','location':'Tashkent','funding_goal':100000,'team_size':4,'progress':50,'is_featured':False,'open_roles':['Engineer']}
