import os

import redis
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

red = redis.Redis(
    host=str(os.getenv('HOST_REDIS')),
    port=15958,
    password=str(os.getenv('PASSWORD_REDIS'))
)
