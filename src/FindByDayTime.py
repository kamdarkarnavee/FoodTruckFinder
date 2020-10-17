from FoodTruckFinder.utils.DateTime import DateTime
from FoodTruckFinder.utils.DayOrder import DayOrder
from FoodTruckFinder.src.FindByX import FindByX
from datetime import datetime
from functools import lru_cache


# To get all open food trucks open today and at current time
class FindByDayTime(FindByX):
    def __init__(self):
        super().__init__()

    # Fetches all the open food trucks at the moment and caches the response for further use
    # The response is cached for at max for 1 hour before the value of current hour changes
    # The current_date is solely used to ensure that the cache is updated at least once every time the date changes
    @lru_cache(maxsize=1)
    def fetch_all_open_food_trucks(self, request_url: str, current_date: datetime.date):
        return super().execute_request(request_url)

    # Generates API query URL for FindByDayTime
    def generate_url(self, domain, config):
        # Get current day of the week
        day = DayOrder().get_day_order()
        dayorder = f"dayorder={day}"

        # Used to fetch all the available food trucks open at present
        start_hour = DateTime().get_current_time().hour
        end_hour = start_hour + 1
        where = f"$where=start24 between '00:00' and '{start_hour}:00' and end24 between '{end_hour}:00' and '24:00'"

        url = super().generate_url(domain, config)
        url = url + '&' + dayorder
        url = url + '&' + where
        return url

    # Fetches columns to display from config file
    def get_columns_to_display(self, config):
        try:
            select = config[self.class_name]['$select']
            preprocessed_select = select.replace('distinct', '').replace(' ', '')
            columns_to_display = preprocessed_select.split(',')
            return columns_to_display
        except Exception as error:
            print(error)
            exit(0)
