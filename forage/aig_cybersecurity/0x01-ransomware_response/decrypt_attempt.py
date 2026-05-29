import zipfile

zip_file = "encrypted_backup.zip"
wordlist = "wordlist.txt"


def attempt_decrypt(zip_path, wordlist_path):
    with zipfile.ZipFile(zip_path) as zf:
        with open(wordlist_path, "r") as words:
            for word in words:
                password = word.strip().encode()
                try:
                    zf.extractall(pwd=password)
                    print(f"[+] Password found: {password.decode()}")
                    return
                except:
                    pass
    print("[-] Password not found in wordlist")


if __name__ == "__main__":
    attempt_decrypt(zip_file, wordlist)
