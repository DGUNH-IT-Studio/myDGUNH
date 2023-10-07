def reference_date(looking_date=None):
    # from datetime import datetime

    # get reference date from db
    return looking_date


class Week:
    from datetime import datetime

    __WEEKDAYS = (
        "Monday", "Tuesday", "Wednsday", "Thurday",
        "Friday", "Saturday", "Sunday"
    )
    __date = None
    weekday = None
    weekdaynum = None
    weeknum = None

    def __weeknum(self, lookingdate: datetime.isoformat = None, start=reference_date()):
        # TODO: создать новый способ определения которая сейчас неделя.
        # looking_date:str arg must be iso format string.

        from datetime import datetime

        self.__date = datetime.today() if lookingdate is None \
            else datetime.fromisoformat(lookingdate)

        start = datetime.fromisoformat(start)
        delta = (self.__date - start).days // 7

        self.weeknum = 0 if (delta % 2) else 1

    def __init__(self, date=None):
        from datetime import datetime

        if date is None:
            date = datetime.today()
            self.__date = date
        elif type(date) is datetime:
            self.__date = date
        elif type(date) is str:
            date = datetime.fromisoformat(date)
            self.__date = date
        else:
            self.__date = datetime.today()

        self.weekdaynum = date.weekday()
        self.weekday = self.__WEEKDAYS[self.weekdaynum]
        self.__weeknum()


def get_schedule():
    # when this module will be finished -> TODO: take schedule from db users table, schedule field
    import json

    f = open('./static/json/schedule.json')
    schedule = json.load(f)
    f.close()
    return schedule


class Schedule:
    schedule = None
    date_info = None


    def __init__(self, date, schedule:dict = None):
        if schedule is None:
            self.schedule = get_schedule()
        else:
            self.schedule = schedule
        self.date_info = Week(date)
        self.events = Events(schedule)

    def __getitem__(self, item):
        return self.schedule[item]

    def looking_schedule(self, date):
        if Week(date) is not self.date_info:
            self.date_info = Week(date)
        return self.schedule[self.date_info.weeknum][self.date_info.weekday]

    
def __init__(self, schedule: dict = None, event={}) -> None:
    self.event = event
    self.event_list = self.__eventsparser(schedule) if schedule else [event]

def delete(self, event: dict):
    self.__init__(event={})

def update(self, new_values: dict):
    for i in new_values.keys():
        self.event[i] = new_values[i]
    return
