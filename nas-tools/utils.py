def clean_string(string):
    string.strip()
    string.replace('\n', '')
    temp = ' '.join(string.split())
    return temp
