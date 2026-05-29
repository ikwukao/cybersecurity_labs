import hashlib


# Simple MD5 Cracker (Use with wordlists)
def crack_md5(hash_val, wordlist):
    with open(wordlist) as f:
        for word in f:
            if hashlib.md5(word.strip().encode()).hexdigest() == hash_val:
                return word.strip()
    return "Not found"


# Usage: crack_md5("hash_here", "rockyou.txt")
