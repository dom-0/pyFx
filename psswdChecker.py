import requests
import hashlib

def request_api_data(query_char):

    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error received while querying - {res.status_code}")
    return res

def read_response(response):
    print (response.text)


def pwned_api_check(password):

    sha1obj = hashlib.sha1(password.encode('utf-8'))
    hexpasswd = sha1obj.hexdigest().upper()
    first5, tail = hexpasswd[0:5], hexpasswd[5:]
    print (first5)
    resp = request_api_data(first5)
    read_response(resp)


x = pwned_api_check('asdfa')
print(x)
