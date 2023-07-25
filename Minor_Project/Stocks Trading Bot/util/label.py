import json


def get_labels():
    file='config//config.json'
    fhandle=open(file,encoding='utf-8')
    config_data=json.load(fhandle)
    return config_data