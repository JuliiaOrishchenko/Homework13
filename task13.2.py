def mr(name):
    return f"Hello Mr {name}"


def mrs(name):
    return f"Hello Mrs {name}"


def define_gender(gender: str):
    if gender == "m":
        return mr
    elif gender == "f":
        return mrs
    else:
        return "Only 'm' or 'f'"


person = define_gender("f")('Smith')
print(person)
