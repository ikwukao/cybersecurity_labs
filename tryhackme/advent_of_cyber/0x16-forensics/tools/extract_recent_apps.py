from Registry import Registry


def parse_recent_apps(hive_path):
    reg = Registry.Registry(hive_path)
    key = reg.open("Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\RecentApps")
    print("Recent Applications:")
    for subkey in key.subkeys():
        print(subkey.name())


# Usage: parse_recent_apps("NTUSER.DAT.sample")
