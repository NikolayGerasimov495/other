from requests.auth import HTTPBasicAuth
import requests
import click


@click.command()
@click.argument('user')
@click.argument('password')
def get_auth(user, password):
    basic = HTTPBasicAuth(username=user, password=password)
    a = requests.get('https://httpbin.org/basic-auth/user/pass', auth=basic)
    click.echo(a)

    # for retries in range(10):
    #     r = requests.post('https://httpbin.org/post', data={'request'.upper(): f'{retries + 1}'})
    #     print(r.text)

    print('The end')


if __name__ == '__main__':
    get_auth()
