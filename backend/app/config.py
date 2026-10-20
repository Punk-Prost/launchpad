from pydantic import field_validator
from pydantic_settings import BaseSettings,SettingsConfigDict
from urllib.parse import parse_qsl,urlencode,urlsplit,urlunsplit
class Settings(BaseSettings):
    database_url:str='sqlite:///./launchpad.db'
    jwt_secret:str='development-only-secret-change-me'
    access_token_expire_minutes:int=60
    cors_origins:str='http://localhost:5173,http://localhost'
    model_config=SettingsConfigDict(env_file='.env',extra='ignore')

    @field_validator('database_url')
    @classmethod
    def normalize_postgres_driver(cls,value:str):
        if value.startswith('postgresql://'):
            value=value.replace('postgresql://','postgresql+psycopg://',1)
        if value.startswith('postgresql+psycopg://'):
            parts=urlsplit(value)
            query=urlencode([(key,item) for key,item in parse_qsl(parts.query) if key!='pgbouncer'])
            value=urlunsplit((parts.scheme,parts.netloc,parts.path,query,parts.fragment))
        return value
settings=Settings()
