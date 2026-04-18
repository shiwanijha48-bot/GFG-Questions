def insert_dict(query, d):
    key = query[1]
    value = int(query[2])
    d[key] = value
    return "Inserted"


def del_dict(query, d):
    key = query[1]
    
    if key in d:
        del d[key]
        return "Deleted"
    else:
        return "-1"


def print_dict(key, d):
    if key in d:
        return "Marks of " + key + " is " + str(d[key])
    else:
        return "-1"
