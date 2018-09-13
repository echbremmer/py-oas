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
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
@pass_config
def delete(config, header, path, query, input, output):
    '''Delete parameters from swagger file'''
    
    print('verbose mode: ', pass_config.verbose)
        
    if (header):
        s = oas.OpenAPISpec(input)    
        s.delete_parameter(s.parsed_oas, header, 'header')
        
        click.echo(s.dump(), output)
    
    elif (path):
        print('path: not implemented yet')
    
    elif (query):
        print('query: not implemented yet')
    
