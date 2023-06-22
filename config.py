import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv()

Token = os.getenv('BOT_TOKEN')
Server_username = os.getenv('SERVER_USERNAME')
Server_password = os.getenv('SERVER_PASSWORD')
Server_host = os.getenv('HOST_NAME')
Server_port = os.getenv('PORT')
Database = os.getenv('DATABASE')
Ssh_username = os.getenv('SSH_USERNAME')
Ssh_password = os.getenv('SSH_PASSWORD')
Admins = os.getenv('ADMINS_ID')
Database_URL = os.getenv('DATABASE_URL')


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
