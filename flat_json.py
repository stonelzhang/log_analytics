import json
import os
import re


def read_json_file(file):
    if os.path.isfile(file):
        print(f'file {file}')
    else:
        exit()

    log = json.load(open(file, 'r'))

    return log


def flat_json_to_kv(an_object, key, kv_result, layer) -> object:
    '''

    :param key:
    :param layer:
    :param an_object:
    :param kv_result:
    :param json_object: a dict object with multiple layers
    :return: a flat dict
    '''

    if isinstance(an_object, dict):
        for key, value in an_object.items():
            flat_json_to_kv(value, key, kv_result, 0)
    elif isinstance(an_object, list):
        for item in an_object:
            flat_json_to_kv(item, key, kv_result, 0)
    else:
        if isinstance(an_object, int) or isinstance(an_object, float):
            an_object = str(an_object)
        if kv_result.get(key, None):
            kv_result[key] = kv_result[key] + " , " + an_object
        else:
            kv_result.update({key: an_object})

    return kv_result


if __name__ == "__main__":
    file = 'log.json'
    log = read_json_file(file)
    print(log)
    result = flat_json_to_kv(log, "", {}, 0)
    print(result)