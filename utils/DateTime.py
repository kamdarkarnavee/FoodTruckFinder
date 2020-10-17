from datetime import datetime


# This class is designed to be used by multiple class methods to get date and time
# Single place of change: any desired change in formatting is applicable to everywhere these functions are called
class DateTime:

    def get_current_time(self) -> datetime:
        return datetime.now()

    def get_date(self) -> datetime.date:
        return datetime.now().date()
