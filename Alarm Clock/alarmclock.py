class AlarmClock:
    def __init__(self, current_time_passed, alarm_on_passed, alarm_time_passed):
        self.current_time = current_time_passed
        self.alarm_on = alarm_on_passed
        self.alarm_time = alarm_time_passed

    def change_time(self):
        self.current_time = input('What is the current time?: ')
        print(self.current_time)

    def alarm_active(self):
       self.alarm_on = input()
       print(self.alarm_on)