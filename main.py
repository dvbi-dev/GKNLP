import re


path=r"D:\pythonProject2\text.txt"
with open(path, mode='r', encoding="utf-8") as f:
    while True:
        data = f.read()
        if data == '':
            break
        print(data)
        tag = re.sub(r"[^a-zA-Z0-9]", " ", data)
        print(tag)
        a=re.sub(r"\s+"," ",tag)

        print(a)
