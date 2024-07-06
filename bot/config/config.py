from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    FARM_TIME: int = 21600                # 6 hours
    TAPS_COUNT: list[int] = [50000, 100000]
    SLEEP_BETWEEN_CLAIM: list[int] = [3600, 5600]
    MOON_BONUS: int = 1000000
    BUY_BOOST: bool = True
    AUTO_TASK: bool = True
    CLAIM_MOON: bool = True
    USE_REF: bool = True
    DEFAULT_BOOST: str = "x3"
    BOOSTERS: dict = {
        "x2": 4000000,
        "x3": 30000000,
        "x5": 200000000
    }
    USE_PROXY_FROM_FILE: bool = False


settings = Settings()


