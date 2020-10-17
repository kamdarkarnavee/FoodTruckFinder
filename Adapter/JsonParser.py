from .ResponseParser import ResponseParser


# parses JSON response, formats and outputs the columns to display
class JsonParser(ResponseParser):

    def parse(self, response, columns, main_config):
        response_length = len(response)

        for response_index in range(0, response_length, main_config['limit_per_page']):
            for index in range(len(response[response_index: response_index + main_config['limit_per_page']])):
                index += response_index
                formatted_response = ' '.join([response[index][column_name] for column_name in columns])
                print(formatted_response)
            input('Press Enter to view more:')
