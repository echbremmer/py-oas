''' Class representing a oas/swagger file

todo: 
- else statements for all if
- maybe remove first if (no code is executed anyway)
- double check doc standards
- make listlen > 0 part of the main elif
- in 'delete_parameter' include a check for the 'type' (i.e "in" == type)
- how to handle security definitions (e.g. give error or remove them)
- remove items related to headers: e.g. security definitions and security
  within the operation itself
- make it support other stuff then just headers; e.g. start with similar stuff
  like path, body
- ability to add headers
- ability to add other stuff
'''

import yaml

class OpenAPISpec:
    
    def __init__(self, file):
    
        self.parsed_oas = yaml.load(file)
    
        file.close

    def delete_parameter(self, oas, name, type):
        
        for k in oas:
            
            if isinstance(oas[k], str):
                pass
            
            elif isinstance(oas[k], dict):
                self.delete_parameter(oas[k], name, type)
                pass

            elif ( isinstance(oas[k], list) ):
                listlen = len(oas[k])
                if listlen > 0:
                    # make sure elements are dictionaries
                    if isinstance(oas[k][0], dict):
                        for i in oas[k]:
                            if "name" in i.keys():
                                if (i['name'] == name):
                                    oas[k].remove(i)

        self.parsed_oas = oas
    
    def dump(self):

        return yaml.dump(self.parsed_oas)
