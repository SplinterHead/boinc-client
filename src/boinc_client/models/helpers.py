def create_indexes(data, key: str, idx_key: str):
    data[key] = {d[idx_key]: d for d in data[key]}
    return data


def flatten_data(data, key: str, subkey: str):
    data[key] = data[key][subkey] if data[key] else data[key]
    return data


def normalise_none_to_list(data, key: str):
    data[key] = [] if not data[key] else data[key]
    return data


def remove_key(data, key: str):
    del data[key]
    return data
