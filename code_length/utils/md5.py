from settings import Config
import hashlib


def md5(arg):
    hash = hashlib.md5(Config.SALT)
    hash.update(bytes(arg, encoding='utf-8'))
    return hash.hexdigest()
