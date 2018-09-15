import click
import oas

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
@click.option('--header', '-H', help='Specify a header name') 
@click.option('--path', '-P', help='Specify a path name')
@click.option('--query', '-Q', help='Specify a query name')
@click.option('--cookie', '-C', help='Specify a cookie name')
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
@pass_config
def delete(config, header, path, query, cookie, input, output):
    '''Delete parameters from oas/swagger file'''
    
    # print('verbose mode: ', pass_config.verbose)
    s = oas.OpenAPISpec(input)    
        
    if (header):
        s.delete_parameter(header, 'header')
    elif (path):
        s.delete_parameter(path, 'path')
    elif (query):
        s.delete_parameter(query, 'query')
    elif (cookie):
        s.delete_parameter(cookie, 'cookie')

    click.echo(s.dump(), output)

@cli.command()
@click.option('--path', '-p', help='Specify location')
@click.option('--operation', '-o', help='Specify operation')
@click.argument('content', type=click.File('r'))
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
@pass_config
def addparam(config, path, operation, content, input, output):

    '''Adds parameter to oas/swagger file'''
    
    # print('verbose mode: ', pass_config.verbose)
    s = oas.OpenAPISpec(input)    
    
    if (path):
        # check validity of content specification
        print("gonna add parameter")
        s.add_parameter(path, operation, content)
    
    click.echo(s.dump(), output)

