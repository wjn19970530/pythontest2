import os

def get_token_write(response):
    response = response.json["access_token"]
    basc_path = os.path.dirname(os.path.realpath(__file__))
    txt_path = os.path.join(basc_path,"data/token.txt")
    with open(txt_path, 'w',encoding='utf-8') as f:
        f.write(response)
def get_token_use():
    basc_path = os.path.dirname(os.path.realpath(__file__))
    txt_path = os.path.join(basc_path,"data/token.txt")
    with open(txt_path, 'r', ) as f:
        lines = f.readline()
        return lines