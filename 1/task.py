import requests
import yaml


with open('config.yaml') as f:
    data = yaml.safe_load(f)


def get_token():
    respons = requests.post(url=data['url'],
                            data={'username': data['username'],
                            'password': data['password']})
    return respons.json()['token']


def get(token: str):
    response = requests.get(data['url_posts'],
                            headers={'X-Auth-Token': token},
                            params={'owner': ''})
    return response.json()


def post(token: str, title: str, description: str, content: str):
    response = requests.post(data['url_posts'],
                             headers={'X-Auth-Token': token},
                             params={'title': title,
                             'description': description, 'content': content})
    return response.json()


if __name__ == '__main__':
    token = get_token()
    # print(post(token, '000', 'ghbdtn', 'ghjkkldfgh'))
    # print()
    print(get(token))
