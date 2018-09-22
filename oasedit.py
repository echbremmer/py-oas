import click
from oas import oas

class Config(object):
    
    def __init__(self):
        self.verbose = False

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option('--verbose', '-V', is_flag=True, help='Run in verbose mode')
@pass_config
def cli(config, verbose):
    pass_config.verbose = verbose
    pass

@cli.command()
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
@pass_config
def parse(config, input, output):
    '''Only parse the oas/swagger file'''

    try:
        s = oas.OpenAPISpec(input)
        click.echo(s.dump(), output)
    except ValueError as err:
        click.echo('Error occured: %s' % err)

@cli.command()
@click.option('--header', '-H', help='Specify a header name') 
@click.option('--query', '-Q', help='Specify a query name')
@click.option('--cookie', '-C', help='Specify a cookie name')
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
@pass_config
def delete(config, header, query, cookie, input, output):
    '''Delete parameters from oas/swagger file'''
    
    # print('verbose mode: ', pass_config.verbose)
    try:
        s = oas.OpenAPISpec(input)
        if (header):
            s.delete_parameter(header, 'header')
        elif (query):
            s.delete_parameter(query, 'query')
        elif (cookie):
            s.delete_parameter(cookie, 'cookie')

        click.echo(s.dump(), output)
    except ValueError as err:
        click.echo('Error occured: %s' % err)

@cli.command()
#@click.option('--path', '-p', help='Specify location') # whether path is already in content
#@click.option('--operation', '-o', help='Specify operation') # whether operation is in content
@click.argument('content', type=click.File('r'))
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
@pass_config
def addparam(config, content, input, output):

    '''Adds parameter to oas/swagger file'''
    
    # print('verbose mode: ', pass_config.verbose)
    s = oas.OpenAPISpec(input, verbose)
    
    if (path):
        print("gonna add parameter")
        s.add_parameter(path, operation, content)
    
    click.echo(s.dump(), output)

