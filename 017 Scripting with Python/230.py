import requests
import hashlib


def password_sha1_hash(password):
    # Hash SHA-1 logic: hashlib.sha1(x.encode('utf-8')).hexdigest().upper()
    hashed_password = hashlib.sha1(
        password.encode('utf-8')).hexdigest().upper()
    return hashed_password


def query_if_password_pwned(hashed_password):
    baseurl = 'https://api.pwnedpasswords.com/range/'
    url = baseurl + hashed_password[0:5]
    res = requests.get(url)
    # print(res.content)
    res_hashes = (line.split(":") for line in res.text.splitlines())
    li_hash, li_count = [], []
    for res_hash in res_hashes:
        li_hash.append(res_hash[0])
        li_count.append(res_hash[1])
    # print(li_hash, li_count)

    try:
        index = li_hash.index(hashed_password[5:])
        # Return number of times pwned
        return li_count[index]

    except:
        return 0


li_pwd = ['hello00o', 'test', 'august', 'myPassw0rdCann0tBEhackeD']

for i, pwd in enumerate(li_pwd):
    hashed_password = password_sha1_hash(pwd)
    hacked_count = query_if_password_pwned(hashed_password)

    if hacked_count == 0:
        print(f'The password {pwd} is safe.')
    else:
        print(f'The password {pwd} is hacked {hacked_count} times.')
