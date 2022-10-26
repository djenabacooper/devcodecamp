from alarmclock import AlarmClock

alarm_one = AlarmClock(alarm_on_passed= True, alarm_time_passed= 12, current_time_passed= 10)

print(alarm_one.alarm_on)
print(alarm_one.alarm_time)

alarm_one.alarm_active()
alarm_one.change_time()

print(alarm_one.alarm_active)
print(alarm_one.change_time)