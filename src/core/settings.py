from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = "localhost"
    port: int = 9999
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_pass: str
    postgres_db: str
    postgres_user: str
    postgres_password: str
    jwt_secret: str
    jwt_algorithm: str
    jwt_expires_seconds: int
    admin_username: str
    admin_password: str
    model_expire_seconds: int
    connection_string: str = ''


settings = Settings(
    _env_file="../.env",
    _env_file_encoding="utf-8"
)

settings.connection_string = f'postgresql://{settings.db_user}:{settings.db_pass}@{settings.db_host}:{settings.db_port}/{settings.db_name}'
