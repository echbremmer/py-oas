''' Class representing a oas/swagger file

This code is in very rudimentary state and requires some effort before it is in a usable
state. Enjoy!
'''

import yaml

class OpenAPISpec:

    def __init__(self, file):

        self.parsed_oas = yaml.load(file)

        file.close

    def delete_parameter(self, name, type):
        '''This deletes parameter of given name and type"
        
        todo:
            - remove items related to the parameter: two examples:
                1) header may have (security) definition which must also be removed. 
                2) path parameter is represented in the path itself (e.g. /somePath/{foo})
                so this must be changed to /somePath
        '''

        for path in self.parsed_oas['paths']:

            valid_ops = ['get','put', 'post', 'delete', 'options', 'head', 'patch', 'trace']

            for ops in self.parsed_oas['paths'][path]:
                if ops in valid_ops:
                    parameters = self.parsed_oas['paths'][path][ops]['parameters']
                    
                    for i, val in enumerate(parameters):
                        if ( ( parameters[i]['name'] == name ) & ( parameters[i]['in'] == type ) ) :
                            del self.parsed_oas['paths'][path][ops]['parameters'][i]

    def add_parameter(self, path, operation, content):
        '''This adds a parameter in a given location

        todo:
            - prevent adding a parameter that is already present
            - check whether location is valid in the input yaml
            - add validation on the given content to ensure that it is valid oas spec for 
            the content it represents (e.g. a header, path or query)
            - ico adding path parameter we must also update the actual path value so adding 
            path paramter 'foo' means  we must add {foo} to the path: /somePath/{foo} 
        '''

        parsed = yaml.load(content)
        self.parsed_oas['paths'][path][operation]['parameters'].append(parsed)


    def dump(self):
        "This returns itself as a yaml"

        return yaml.dump(self.parsed_oas)
