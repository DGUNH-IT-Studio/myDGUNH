
class Schedule:
    """
    """


    schedule = None


    def __get_schedule(self):
        import json
        f = open('static/json/schedule.json')
        schedule = json.load(f)
        f.close()
        return schedule
    

    def __init__(self):
        self.schedule = self.__get_schedule()



    class ScheduleEvent:


        # TODO: создать новый способ определения которая сейчас неделя.
        def __weekcalc(self, looking_date:str = None, start = "2023-08-27"):
            """
            looking_date:str arg must be iso format string.
            """
            from datetime import datetime
            if looking_date == None:
                looking_date = datetime.today()
            else:
                looking_date = datetime.fromisoformat(looking_date)
            
            delta = (looking_date - start).days // 7

            if delta % 2:
                # it means first week
                return 0
            else:
                # it means second week
                return 1
            
        
        def __schedule_parser(self, schedule:dict, iso_format_date:str = None):
            from datetime import datetime
            events = list()
            current_date = None

            if iso_format_date == None:
                current_date = datetime.today()
            else:
                current_date = datetime.fromisoformat(iso_format_date)

            weeknum = self.__weekcalc()
            weekday = current_date.weekday()

            events = schedule[weeknum][weekday]
                        
            return events


        def __init__(self, schedule=None, event=dict()) -> None:
            self.event = event
            if schedule:
                self.event_list = self.__schedule_parser(schedule)
            else:
                self.event_list = [event]


        def create(self):
            pass



    def __getitem__(self):
        return 0

    def addEvent(self):
        return 0

    def replaceEvent(self):
        return 0

    def removeEvent(self):
        return 0

    def __dict__(self):
        return {}


def main():
    userSchedule = Schedule
    print(userSchedule.obj)
    return 0


if __name__ == '__main__':
    main()
