''' Class representing a oas/swagger file

todo:
- remove items related to headers: e.g. security definitions and security
  within the operation itself
'''

import yaml

class OpenAPISpec:

    def __init__(self, file):

        self.parsed_oas = yaml.load(file)

        file.close

    def delete_parameter(self, name, type):
        "This deletes parameter of given name and type"

        for path in self.parsed_oas['paths']:

            valid_ops = ['get','put', 'post', 'delete', 'options', 'head', 'patch', 'trace']

            for ops in self.parsed_oas['paths'][path]:
                if ops in valid_ops:
                    parameters = self.parsed_oas['paths'][path][ops]['parameters']
                    
                    for i, val in enumerate(parameters):
                        if ( ( parameters[i]['name'] == name ) & ( parameters[i]['in'] == type ) ) :
                            del self.parsed_oas['paths'][path][ops]['parameters'][i]

    def add_parameter(self, path, operation, content):
        "This adds a parameter in a given location"

        currentparams = self.parsed_oas['paths'][path][operation]['parameters']
        #print(currentparams)
        
        self.parsed_oas['paths'][path][operation]['parameters'].append(content.read())


    def dump(self):
        "This returns itself as a yaml"

        return yaml.dump(self.parsed_oas)
