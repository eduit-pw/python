import re
def kod(tekst):
    return re.search(r"[0-9]{2}-[0-9]{3}", tekst) is not None
