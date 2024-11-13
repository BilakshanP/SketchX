from typing import Any
from re import compile, Pattern


class Compiled:
    env_match: Pattern[Any] = compile(r"^[a-zA-Z]\w+\s?=\s?.+$") # matches .env type files i.e X123 = SomeVal
    config_dict_match_1: Pattern[Any] = compile(r"\([a-zA-Z_]\w*\s*,\s*.*?\),*") # matches (var, val), ... you can add ,* and \s*
    config_dict_match_2: Pattern[Any] = compile(r"[a-zA-Z_]\w*\s*:\s*.*?;") # matches var:val; ... you can add ;* and \s*

    command_match: Pattern[Any] = compile(r"\.\w+\s+(((-\w\s?)|(--\w{2,}\s?=\s?\w+\s?))+)*")
    command_match_args: Pattern[Any] = compile(r"(?<=-)\w(?!\w)")
    compile_match_kwargs: Pattern[Any] = compile(r"(--(\w{2,})\s?=\s?([^;]+))(?=;)") # --(\w{2,})\s?=\s?(\w+)")

def str_to_dict(text: str, format_type: int = 1) -> dict[str, str]:
    """
    Keyword argument `format_type == 1|2`. There are total `2` format types for now: `(key, val), ...` and `key:val;`
    First style is the default.
    """

    if format_type - 1:
        matches: list[str] = Compiled.config_dict_match_2.findall(text)
    else:
        matches: list[str] = Compiled.config_dict_match_1.findall(text)

    keys: list[str] = []
    values: list[str] = []

    for match in matches:
        if format_type - 1:
            key_and_val = match.strip(";").split(":", 1)
        else:
            key_and_val = match.strip(",")[1:-1].split(",", 1)

        keys.append(key_and_val[0].strip())
        values.append(key_and_val[1].strip())

    return dict(zip(keys, values))