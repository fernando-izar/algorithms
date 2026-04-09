from collections import defaultdict
import json


def add_module(l: str) -> str:
    if not ("]" in l):
        return ""
    result = ""
    for i in l:
        if i == "[":
            continue
        elif i == "]":
            break
        else:
            result += i
    return result


def convert_type(value: str | int | bool) -> str | int | bool:
    try:
        value = int(value)
    except:
        try:
            value = True if value == "True" else value
            value = False if value == "False" else value
        except:
            pass
    return value


try:
    with open("parser.txt", "r") as file:
        result = defaultdict(dict)
        key_module = None
        for l in file:
            if l.strip().startswith("#") or l == "\n":
                continue
            elif l.strip().startswith("["):
                key_module = add_module(l)

            elif not key_module:
                continue
            elif "=" in l:
                key, value = l.split("=")
                key = key.strip()
                value = value.strip().rstrip("\n")
                value = convert_type(value)
                if key and value:
                    result[key_module].update({key: value})

        res_dict = dict(result)
        json_string = json.dumps(res_dict, indent=3)
        print(json_string)
except Exception as e:
    print(e)
