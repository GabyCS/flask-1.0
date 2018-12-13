import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-s3cr3t-k3y-1245'
