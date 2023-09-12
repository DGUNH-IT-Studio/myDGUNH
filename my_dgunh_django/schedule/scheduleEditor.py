
class Weekday:
    """
    Class for getting the name of the day of the week by it's number.
    >>> example = Weekday()
    >>> i = 1
    >>> example[i]
    output: "Monday"
    """

    def __init__(self):
        self.daysoftheweek = (
            "Monday", "Tuesday", "Wednsday", "Thurday",
            "Friday", "Saturday", "Sunday"
        )
    
    def __getitem__(self, daynum):
        try:
            weekday = self.daysoftheweek[daynum]
        except IndexError:
            weekday = 'null'
        return weekday


class Schedule:
    """
    """


    def __get_schedule(self):
        # when this module will be finished -> TODO: take schedule from db
        # users table, schedule field
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

            return 0 if (delta % 2) else 1
            
        
        def __eventsparser(self, schedule:dict, iso_format_date:str = None):
            """
            Функция для получения списка всех событий расписания на 
            определенную дату, в определенный день недели для
            соответствующей недели. 
            """

            from datetime import datetime
            events = list()
            current_date = None

            if iso_format_date == None:
                current_date = datetime.today()
            else:
                current_date = datetime.fromisoformat(iso_format_date)

            weeknum = self.__weekcalc()
            weekday = Weekday()[current_date.weekday()]

            events = schedule[weeknum][weekday]

            return events
        

        def __init__(self, schedule=None, event=dict()) -> None:
            self.event = event
            if schedule:
                self.event_list = self.__eventsparser(schedule)
            else:
                self.event_list = [event]

        def filtration(self, event:dict, reqs:dict):
            for i in reqs.keys:
                if type(i) == dict:
                    self.filtration(event[i], reqs[i])
                elif (event[i] != reqs[i]):
                    return False
            return True

        def create(self, **kwargs):
            parameters = dict(kwargs)
            event = self.__init__(event=parameters)


        def delete(self, event:dict):
            self.__init__(event={})


        def update(self, new_values:dict, **filterchoose) -> None:
            filter = dict(filterchoose)
            for i in self.event_list:
                if self.filtration(i, filter):
                    for e in new_values.keys:
                        i[e] = new_values[e]
                    self.event_list[self.event_list.index(i)] = i
            return


    def __getitem__(self):
        return 0
    
    def makedayfree(self, isoformatdate:str):
        return 0

    def addEvent(self):
        return 0

    def replaceEvent(self):
        return 0

    def removeEvent(self):
        return 0
    
    def savechanges(self):
        return 0

    def __dict__(self):
        return {}


def main():
    a = Schedule()
    return 0


if __name__ == '__main__':
    main()
