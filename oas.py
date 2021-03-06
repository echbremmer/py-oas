''' Class representing a oas/swagger file

This code is in very rudimentary state and requires some effort before it is in a usable
state. Enjoy!
'''
import error

import yaml

class OpenAPISpec: # maybe call this OAS

    SWAGGER_ELEMENTS = ['swagger', 'info', 'paths']
    OAS_ELEMENTS = ['openapi', 'info', 'paths']
    OPERATIONS = ['get','put', 'post', 'delete', 'options', 'head', 'patch', 'trace']

    def __init__(self, file):

        parsed_yaml = yaml.safe_load(file) # should add try/catch here
        file.close

        if (OpenAPISpec.validate(parsed_yaml)):

            self.parsed_oas = parsed_yaml

            if 'swagger' in self.parsed_oas:
                self.version = self.parsed_oas['swagger']
            elif 'openapi' in self.parsed_oas:
                self.version = self.parsed_oas['openapi']
            else:
                raise error.OASError('File does not contain version')
        else:
            raise error.OASError('File not a valid Swagger or Open Api Specification')

    @staticmethod
    def validate(parsed_yaml):
        ''' This method validates a parsed yaml file to ensure it is a valid
        swagger 2.0 or OAS 2.*.* OAS 3.0.0

        todo:
            - replace this with more mature python library for swagger/oas to do
            the validation. This class can extend that library by adding operations
            such as deleting or adding things
            - if nothing available then more thorough validation; currently only 
            root is checked to contain mandatory elements
        '''

        if 'swagger' in parsed_yaml:
            if parsed_yaml['swagger'] == '2.0':
                ELEMENTS = OpenAPISpec.SWAGGER_ELEMENTS
            else:
                return False
        elif 'openapi' in parsed_yaml:
            if parsed_yaml['openapi'] == '3.0.0': # replace with regex
                ELEMENTS = OpenAPISpec.OAS2_ELEMENTS
            else:
                return False
        else:
            return False
        
        for e in ELEMENTS:
            if e in parsed_yaml:
                pass
            else:
                return False

        return True

    def delete_parameter(self, name, type):
        '''This deletes parameter of given name and type

        todo:
            - remove items related to the parameter: two examples:
                1) header may have (security) definition which must also be removed. 
                2) removal of path parameter is not supported in this class since it has 
                too many related things (like the path itself which contains the path 
                paramter: /somePath/{foo} )
        '''

        SUPPORTED_TYPES = ['header', 'query', 'cookie']

        if type in SUPPORTED_TYPES:
            for path in self.parsed_oas['paths']:
                for ops in self.parsed_oas['paths'][path]:
                    if ops in OpenAPISpec.OPERATIONS:
                        parameters = self.parsed_oas['paths'][path][ops]['parameters']
                        for i, val in enumerate(parameters):
                            if ('name' in val.keys() ):
                                if ( ( parameters[i]['name'] == name ) & ( parameters[i]['in'] == type ) ) :
                                    del self.parsed_oas['paths'][path][ops]['parameters'][i]
        else:
            raise error.OASError('Provided type is not supported in Swagger or OAS:: ', type)

    def add_path(self, path):
        pass

    def add_operation(self, path, operation):
        pass

    def add_parameter(self, path, operation, parameter):
        '''This adds a parameter in a given location

        todo:
            - prevent adding a parameter that is already present
            - throw error when trying to add 'path' parameter since it will cause an invalid
            swagger/oas file if the name of paramter is not added to the path (i.e. in case 
            of path parameter 'petId' the path should be updated to be '/pet/{petId}'
            - add validation on the given content to ensure that it is valid oas spec for
            the content it represents (e.g. a header, path or query)
        '''
        parameter_parsed = yaml.load(parameter)

        temp_oas = self.parsed_oas

        if path not in self.parsed_oas['paths']:
            raise error.OASError('Specified path does not exist')
        elif operation not in self.parsed_oas['paths'][path]:
            raise error.OASError('Specified operation does not exist')

        if 'parameters' not in self.parsed_oas['paths'][path][operation]:
            temp_oas['paths'][path][operation]['parameters'] = []

        temp_oas['paths'][path][operation]['parameters'].append(parameter_parsed)

        if(self.validate(temp_oas)): # current validation is not sufficient
            self.parsed_oas = temp_oas
        else:
            raise error.OASError('Provided parameter not according to open api specification')

    def dump(self):
        "This returns itself as a yaml"

        return yaml.safe_dump(self.parsed_oas)
