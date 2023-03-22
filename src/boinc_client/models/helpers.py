def create_indexes(data, key: str, idx_key: str):
    data[key] = {d[idx_key]: d for d in data[key]}
    return data


def create_lists(data, keys: list[str]):
    for k in keys:
        if k not in data:
            data[k] = []
    return data


def flatten_data(data, key: str, subkey: str):
    if key in data and subkey in data[key]:
        data[key] = data[key][subkey] if data[key] else data[key]
    return data


def normalise_none_to_list(data, key: str):
    data[key] = [] if not data[key] else data[key]
    return data


def remove_key(data, key: str):
    del data[key]
    return data


def replace_none_string(data):
    for field in data:
        data[field] = data[field] if data[field] is not None else ""
    return data


def set_bools(data, keys: list[str]):
    for key in keys:
        data[key] = key in data
    return data
