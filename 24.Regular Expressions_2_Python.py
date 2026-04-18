def validate(str):
    pat= r'^[a-z]+[!@#$%]+\d+$'    ##your pattern here
    match = re.search(pat, str)
    if(match):
        return True
    else:
        return False
