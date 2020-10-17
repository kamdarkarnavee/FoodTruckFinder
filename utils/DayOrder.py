from datetime import datetime


class DayOrder:
    # Mapping day of week 0=Sunday, 1=Monday, etc. as per the Socrata API specifications
    days_mapping = {
        0: 1,
        1: 2,
        2: 3,
        3: 4,
        4: 5,
        5: 6,
        6: 0
    }

    def get_day_order(self) -> int:
        return self.days_mapping[datetime.now().weekday()]
