from pydantic import BaseSettings


class Settings(BaseSettings):
    fh_key: str
    av_key: str
    ms_key: str

    class Config:
        # case_sensitive = false
        env_file = '.env'


settings = Settings()
