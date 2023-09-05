
class WeekInfo:


    def __init__(self):
        pass


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
        
        def __schedule_parser(self, schedule:dict, iso_format_date:str = None, week_num:int = None, day_of_the_week:int = None):
            from datetime import datetime
            events = list()
            date = datetime.fromisoformat(iso_format_date) 

            

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
