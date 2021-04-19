import requests
import hashlib
import sys


def request_to_api(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(
            "Too much time to get response, please check the url and try again")
    return response


def get_the_leaks(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return print(count)
    return print(0)


def hash_password(password_query):
    sha1password = hashlib.sha1(
        password_query.encode('UTF-8')).hexdigest().upper()
    first, tail = sha1password[:5], sha1password[5:]
    response = request_to_api(first)
    get_the_leaks(response, tail)


def main(args):
    for password in args:
        hash_password(password)


if sys.argv[1:]:
    main(sys.argv[1:])
else:
    print('Please enter any password to check')