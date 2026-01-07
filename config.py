# -----------------------------------------------------------------------------------------------
# Author : Manuel Portero Leiva 
# -----------------------------------------------------------------------------------------------
# Purpose : Variables security configuration for Marea Chatbot.
# -----------------------------------------------------------------------------------------------

import os
from pydantic import validator
from pydantic_settings import BaseSettings, SettingsConfigDict
import logging



class ApiSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='/home/titansax/marea_lite/.env', 
                                    env_file_encoding='utf-8', 
                                    env_prefix="API_KEYS_", 
                                    extra='ignore')

    OPENWEATHER: str
    CURRENTAPI:str
    TMDB:str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='/home/titansax/marea_lite/.env', 
                                    env_file_encoding='utf-8', 
                                    extra='ignore')

    api_settings: ApiSettings = ApiSettings()

settings = Settings()
