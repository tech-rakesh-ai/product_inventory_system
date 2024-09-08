from pydantic_settings import BaseSettings


# Define a settings class using Pydantic
class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_ALGORITHM: str = "HS256"
    authjwt_header_type: str = "Bearer"
    JWT_SECRET_KEY: str
    AUTOCOMMIT: bool = False
    AUTOFLUSH: bool = False

    class Config:
        env_file = '.env'  # set the env file path.
        env_file_encoding = 'utf-8'


setting = Settings()
