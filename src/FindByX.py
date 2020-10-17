import requests
import inspect


# Designed to be the Parent class for all the FindBySomething classes
class FindByX:

    def __init__(self):
        stack = inspect.stack()
        # Storing the child class name when its object is created
        self.class_name = stack[1][0].f_locals["self"].__class__.__name__

    # Generates url to query the API
    # NOTE: the calling function's Class must be present as key in the config.json to generate corresponding URL
    def generate_url(self, domain, config):
        url = domain
        try:
            class_name = self.class_name

            if class_name in config:
                config = config[class_name]
                url = url + '&'.join([f"{key}={value}" for key, value in config.items()])
                return url

        except Exception as error:
            print('No information found for ' + class_name)
            print('Exiting program to avoid over information sharing.')
            exit(0)

    # Used to get data from the API
    def execute_request(self, request_url):
        try:
            response = requests.get(request_url)
            if response.status_code == requests.codes.ok:
                response_json = response.json()
                return response_json
            else:
                print('Response Status Code:', response.status_code)
                print(response.text)
                raise Exception(response)
        except Exception as error:
            print(error)
            exit(0)
