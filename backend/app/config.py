from pydantic import field_validator
from pydantic_settings import BaseSettings,SettingsConfigDict
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
            return value.replace('postgresql://','postgresql+psycopg://',1)
        return value
settings=Settings()
