def bus_announcements(stops):
    while True:
        for stop in stops:
            yield f'Next stop: {stop}'

stops_list = ['Central Station', 'Main Street', 'Park Avenue', 'Airport']
announcer = bus_announcements(stops_list)

# Testing the result
for bus_stop in range(6):
    print(next(announcer))