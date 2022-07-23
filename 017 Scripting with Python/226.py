import requests
import hashlib

li_pwd = ['hellooooo0', 'test', 'august',
          'skdcbjsbfd123bhvbadjbuhfba', '2022isayear']

# Hash SHA-1 logic: hashlib.sha1(x.encode('utf-8')).hexdigest().upper()
li_pwd_hash_sha1 = [hashlib.sha1(
    x.encode('utf-8')).hexdigest().upper() for x in li_pwd]


baseurl = 'https://api.pwnedpasswords.com/range/'

for i, hash in enumerate(li_pwd_hash_sha1):
    url = baseurl + hash[0:5]
    res = requests.get(url)
    # print(res.content)

    res_hashes = (line.split(":") for line in res.text.splitlines())
    li_hash, li_count = [], []
    for res_hash in res_hashes:
        li_hash.append(res_hash[0])
        li_count.append(res_hash[1])

    try:
        index = li_hash.index(hash[5:])
        print(f'The password {li_pwd[i]} is hacked {li_count[index]} times.')

    except:
        print(f'The Password {li_pwd[i]} is safe.')
