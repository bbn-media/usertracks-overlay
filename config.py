import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "bBN23-11530caRMEl"