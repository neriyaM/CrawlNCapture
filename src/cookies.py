from src.consts import ConfigKeys
from dataclasses import dataclass, asdict
from urllib import parse


@dataclass
class Cookie:
    name: str
    value: str


def parse_raw_cookies(raw_cookies):
    cookies = {}
    for chunk in raw_cookies.split(str(';')):
        if str('=') in chunk:
            key, val = chunk.split(str('='), 1)
        else:
            # Assume an empty name per
            # https://bugzilla.mozilla.org/show_bug.cgi?id=169091
            key, val = str(''), chunk
        key, val = key.strip(), val.strip()
        if key or val:
            # unquote using Python's algorithm.
            cookies[key] = parse.unquote(val)
    return cookies


def from_config(raw_cookies):
    cookies = []
    cookies_dict = parse_raw_cookies(raw_cookies)
    for name, val in cookies_dict.items():
        cookies.append(Cookie(name, parse.unquote(val)))

    return cookies
