import click
from bs4 import BeautifulSoup

@click.command()
@click.argument('file', type=click.File('r'))

def echo(file):
    """Print Total regular_price"""
    soup = BeautifulSoup(file, 'xml')

    all_price = soup.find_all('regular_price')
    #
    table_price = []
    for item in all_price:
        all_item_price = float(item.text)
        table_price.append(all_item_price)
    click.echo(f'Total regular_price: {round(sum(table_price), 2)}')

if __name__ == '__main__':
    echo()



