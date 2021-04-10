from http.cookies import SimpleCookie, CookieError
from urllib import parse

raw = 'sb=ZI-aW9BvRfBOj33x5Vv7vYM8; c_user=1749961189; datr=rUZdX4JwkpGVnHFpSv5D2aFy; dpr=1.5; presence=C{"t3":[],"utc3":1617834371731,"v":1}; spin=r.1003598403_b.trunk_t.1617976059_s.1_v.2_; xs=8:9AoDdfMtBogkMQ:2:1576433006:5499:15162::AcVua5hGeYjgs5MxLjWUXhY6PzdSIdShYjnldEZ_97jJ; fr=14beTpbZN3wsKbGVw.AWXRDDwFjv3NL3Z1eVH-3OVGINk.BgcGci.HG.AAA.0.0.BgcGci.AWWyxOkr-FI'


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

print(parse_raw_cookies(raw))