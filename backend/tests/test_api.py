def test_health(client):assert client.get('/health').json()=={'status':'ok'}
def test_register(client):assert client.post('/auth/register',json={'name':'User Test','email':'user@test.dev','password':'Password1!','role':'member'}).status_code==201
def test_duplicate_email(client):
    x={'name':'User Test','email':'dup@test.dev','password':'Password1!','role':'member'};client.post('/auth/register',json=x);assert client.post('/auth/register',json=x).status_code==409
def test_login(client):
    client.post('/auth/register',json={'name':'User Test','email':'login@test.dev','password':'Password1!','role':'member'});assert client.post('/auth/login',json={'email':'login@test.dev','password':'Password1!'}).status_code==200
def test_bad_login(client):assert client.post('/auth/login',json={'email':'none@test.dev','password':'Password1!'}).status_code==401
def test_empty_catalog(client):assert client.get('/startups').json()==[]
def test_founder_creates_startup(client,founder,startup_data):assert client.post('/startups',json=startup_data,headers=founder).status_code==201
def test_member_cannot_create(client,member,startup_data):assert client.post('/startups',json=startup_data,headers=member).status_code==403
def test_get_startup(client,founder,startup_data):
    client.post('/startups',json=startup_data,headers=founder);assert client.get('/startups/solar-mesh').status_code==200
def test_application_requires_auth(client,founder,startup_data):
    item=client.post('/startups',json=startup_data,headers=founder).json();assert client.post(f"/startups/{item['id']}/applications",json={'message':'I have relevant engineering experience.'}).status_code==401
def test_member_applies(client,founder,member,startup_data):
    item=client.post('/startups',json=startup_data,headers=founder).json();assert client.post(f"/startups/{item['id']}/applications",json={'message':'I have relevant engineering experience.'},headers=member).status_code==201
def test_owner_deletes(client,founder,startup_data):
    item=client.post('/startups',json=startup_data,headers=founder).json();assert client.delete(f"/startups/{item['id']}",headers=founder).status_code==204
