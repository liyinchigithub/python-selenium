import hashlib


def get_md5(file):
    m = hashlib.md5()
    with open(file, 'rb') as f:
        for line in f:
            m.update(line)
    md5code = m.hexdigest()
    return md5code

if __name__ == '__main__':
    print(get_md5("D:\\A\\storm.rar"))