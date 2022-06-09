import os, logging
from pydantic import BaseSettings
from logging.handlers import TimedRotatingFileHandler



class Settings(BaseSettings):
    log_level: str = 'DEBUG'
    log_file: str = 'app.log'

    server_host: str = '127.0.0.1'
    server_port: int = 8009

    database_url: str = ''

    api_short_report_url: str = ''
    api_extended_report_url: str = ''
    api_state_contracts: str = ''
    api_fin_report: str = ''

    bl_auth_url: str = ''
    bl_auth_verify_url: str = ''
    bl_auth_user: str = ''
    bl_auth_password: str = ''


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)


file = os.path.join('logs', settings.log_file)
log_file = TimedRotatingFileHandler(file, when='midnight', encoding='UTF-8')

# Формируем наименование LOG файла
log_file.suffix = "%Y-%m-%d_%H-%M-%S"
log_file.namer = lambda name: name.replace(".log", "") + ".log"

if settings.log_level == 'DEBUG':
    log_msg_format = '%(asctime)s | %(name)s [%(levelname)s]: (%(filename)s,%(lineno)d).%(funcName)s - %(message)s'
else:
    log_msg_format = '%(asctime)s [%(levelname)s]: %(message)s'

logging.basicConfig(handlers=(log_file,), format=log_msg_format, level=settings.log_level)
LOGGER = logging.getLogger(__name__)
