import re



class Compiled:
    env_match: re.Pattern = re.compile(r"^[a-zA-Z]\w+\s?=\s?.+$") # matches .env type files i.e X123 = SomeVal
    config_dict_match_1: re.Pattern = re.compile(r"\([a-zA-Z_]\w*\s*,\s*.*?\),*") # matches (var, val), ... u can add ,* and \s*
    config_dict_match_2: re.Pattern = re.compile(r"[a-zA-Z_]\w*\s*:\s*.*?;") # matches var:val; ... u can add ;* and \s*

def str_to_dict(text: str, pattern: re.Pattern[str] = Compiled.config_dict_match_1) -> dict[str, str]:
    """
    `text` should be in teh format: `(key, value), ...` uness using non-default `pattern`
    """
    matches: list[str] = pattern.findall(text)

    keys: list[str] = []
    values: list[str] = []

    for match in matches:
        y = match.strip(",")[1:-1].split(",", 1)

        keys.append(y[0].strip())
        values.append(y[1].strip())
    
    return dict(zip(keys, values))