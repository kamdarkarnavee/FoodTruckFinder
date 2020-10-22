from FoodTruckFinder.Adapter.JsonParser import JsonParser
from FoodTruckFinder.src.FindByDayTime import FindByDayTime
from FoodTruckFinder.utils.DateTime import DateTime
import json


def main():
    # Reading must-have configurations file, else exit program
    try:
        with open('FoodTruckFinder/config.json') as config_file:
            config_dictionary = json.load(config_file)
        main_config = config_dictionary['__main__']
    except Exception as error:
        print('Error with config.json:', error)
        exit(0)

    # Creating object of FindByDayTime to get all open food trucks open today and at current time
    food_truck_finder_object = FindByDayTime()
    domain = "https://data.sfgov.org/resource/jjew-r69b.json?"

    # Generate URL to access Socrata API data without need of Access Token
    request_url = food_truck_finder_object.generate_url(domain=domain, config=config_dictionary)

    current_request_url = request_url
    current_date = DateTime().get_date()
    print('Food Trucks open at:', DateTime().get_current_time())

    # To parse respone in JSON format
    response_parser = JsonParser()
    food_truck_display_columns = food_truck_finder_object.get_columns_to_display(config_dictionary)

    # The program keeps running until user enters exit or an exception occurs resulting in termination of program
    while True:
        response = food_truck_finder_object.fetch_all_open_food_trucks(current_request_url, current_date)

        # parse response and display output in desired format
        response_parser.parse(response, food_truck_display_columns, main_config)
        response_length = len(response)

        # If all the open food trucks are displayed for the current time
        if 0 <= response_length < main_config['$limit']:
            print('-' * 50)
            print('Displayed all the open food trucks for current time!')
            print('-' * 50)
            input_ = input('Type Exit to exit or press enter to find the latest food trucks open:')
            if input_ == 'exit':
                exit(0)
            print('\nFood Trucks open at:', DateTime().get_current_time())
            current_request_url = food_truck_finder_object.generate_url(domain=domain, config=config_dictionary)
        # Else, increment the offset and fetch the next batch of open food trucks
        else:
            main_config['$offset'] += response_length
            current_request_url = request_url + f"&$offset={main_config['$offset']}"

        # Deleting response -> to free up memory
        del response


if __name__ == '__main__':
    main()
