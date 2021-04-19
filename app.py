import requests
import hashlib

def request_to_api(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(
            "Too much time to get response, please check the url and try again")
    return response
  


def hash_password(password_query):
    sha1password = hashlib.sha1(password_query.encode('UTF-8')).hexdigest().upper()
    first, tail = sha1password[:5], sha1password[5:]
    response = request_to_api(first)
    print(response.text)

hash_password('1234556')


def 