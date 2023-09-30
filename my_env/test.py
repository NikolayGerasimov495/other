import random
#
import click
#
#
# @click.command()
# # basic option
# @click.option('--name', '-n', default='Nick', help='Firstname description')
# # multiple Values
# @click.option('--salary', '-s', nargs=2, help='Your Monthly Salary', type=int)
# # multiple option
# @click.option('--location', '-l', help='Places you visited', multiple=True)
# def main(name, salary, location):
#     click.echo(f"Hello! My name is {name}. My salary is {sum(salary)}!")
#     click.echo('\n'.join(location))

#
# @click.command()
# @click.argument('number1',type=int)
# @click.argument('number2',type=int)
# @click.argument('method', default='add')
#
# def main(number1, number2, method):
#     """ add number 1 and number 2"""
#     if method == 'add':
#         result = number1 + number2
#     elif method == 'substract':
#         result = number1 - number2
#     elif method == 'myltiply':
#         result = number1 * number2
#     click.echo(result)


# @click.command()
# @click.argument('source', nargs=-1)
# @click.argument('destination',nargs=1)
#
# def main(source, destination):
#     for f in source:
#         click.echo(f'Moving {f} to Folder {destination}')

#
# @click.command()
# @click.option('--name')
# @click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
#
#
# def main(name, password):
#     fname = click.prompt('Enter your Firstname')
#     click.echo(f'Your name is {name} and your firstname {fname} your password is {password}')





# @click.group()
# def main():
#     pass

# @main.command()
# @click.argument('text')
# def reverse(text):
#     """reverse a text"""
#     click.echo(text[::-1])
#
# @main.command()
# @click.argument('myword')
# def shufflize(myword):
#     """shuffize a text"""
#     click.echo(''.join(random.sample(myword,len(myword))))
#
#
#

if __name__ == '__main__':
    main()
