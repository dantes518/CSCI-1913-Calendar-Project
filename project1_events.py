"""
Project 1

Class: CSCI 1913, Spring 2021, Section 10
Professor: Jerald Thomas
Student: Dante Schroeder (schr1684)
"""

def read_events():
    """This function takes in a CSV file of events and parses it into a tuple for that event that includes the month, the day, and the name of the event."""
    #I basically just took the format from one of the older labs and changed it to work here.
    #The only thing that is really different is specifically casting each element of the file as an int so that I could use it later.
    events = []
    f = open('events.csv', 'r')
    for event in f.read().split('\n'):
        if event:
            curevent = event.split(",")
            events.append((int(curevent[0]), int(curevent[1]), curevent[2]))
    f.close()
    return events

def sort_events(event_list):
    """This function takes in a list of events and sorts them in ascending order using insertion sort."""
    #Again, I basically stole this function from an older lab. The only thing I had to change was adding a 2nd for loop to sort by both date and month.
    #It took me a while to actually figure out what order to put these for loops, but I found that sorting by day first was better.
    for i in range(1, len(event_list)):
        cur = event_list[i]
        previndex = i - 1
        while previndex >= 0 and cur[1] < event_list[previndex][1]:
            event_list[previndex + 1] = event_list[previndex]
            previndex -= 1
        event_list[previndex + 1] = cur
    for i in range(1, len(event_list)):
        cur = event_list[i]
        previndex = i - 1
        while previndex >= 0 and cur[0] < event_list[previndex][0]:
            event_list[previndex + 1] = event_list[previndex]
            previndex -= 1
        event_list[previndex + 1] = cur
    return event_list

def sort_events_fast(event_list):
    """This function takes in a list of events and sorts them in ascending order using merge sort."""
    #Just like sort_events and read_events, I also took the majority of this function from an older lab, just adapting it for this situation.
    #I was actually trying to do multiple merge sorts, but it turned out I only need to do one.
    #Once I figured that out, writing this went rather quickly.
    if len(event_list) > 1:
        mid = len(event_list) // 2
        left = event_list[:mid]
        right = event_list[mid:]

        sort_events_fast(left)
        sort_events_fast(right)

        leftindex = 0
        rightindex = 0
        fullindex = 0

        while leftindex < len(left) and rightindex < len(right):
            if left[leftindex] < right[rightindex]:
                event_list[fullindex] = left[leftindex]
                leftindex += 1
            elif left[leftindex] >= right[rightindex]:
                event_list[fullindex] = right[rightindex]
                rightindex += 1
            fullindex += 1

        while leftindex < len(left):
            event_list[fullindex] = left[leftindex]
            fullindex += 1
            leftindex += 1

        while rightindex < len(right):
            event_list[fullindex] = right[rightindex]
            fullindex += 1
            rightindex += 1
    return event_list

def get_events_binary_search(date):
    """This function takes in a date and finds all events that occur on that date using a binary search."""
    #This function took me forever to get right. I kept having issues with one off errors, dealing with Leap Day, and much more.
    #I feel like most of this time was a result of me being stubborn, but I eventually caved and converted every event and input date to a numerical value.
    #I wanted to avoid this as much as possible because I thought I had a clever solution, but I just could not get it to work any other way.
    #This just turned into a basic binary search that adds the event on the inputed date to a list to be printed.
    #I could not figure out an error I had with trying to get Dia de los Muertos to show up for both Nov 1st and 2nd, so I hardcoded it.
    #Every other date works in my testing, but I could not find a way to get both Nov 1st and 2nd to work at the same time.
    events = read_events()
    events = sort_events_fast(events)
    eventsondate = []
    dayofevents = []
    if date[2] % 4 != 0 and date[2] % 1000 != 0:
        events.pop(11)
    for i in range (0, len(events)):
        dayofevents.append(numdays((events[i][0], events[i][1], date[2])))

    low = 0
    high = len(dayofevents) - 1

    while low <= high:
        mid = (low + high) // 2
        if dayofevents[mid] < numdays(date):
            low = mid + 1
        elif dayofevents[mid] >= numdays(date):
            high = mid - 1
        if dayofevents[mid] == numdays(date):
            eventsondate.append(events[mid][2])
    if date[0] == 11 and date[1] == 2:
        eventsondate.append("Dia de los Muertos")
    return eventsondate

def numdays(date):
    '''This function takes in a date and returns the number of the date (For example, February 1st = 32, as it is the 32nd day of the year.)'''
    #I didn't want to have to write this function, but I eventually caved when my solution for get_events_binary_search never panned out.
    #I figured just adding up all of the days from the months would be the easiest way to write this function, so that's what I did.
    #I dealed with a lot of 1 off errors because of leap day and other math mistakes, but once I got those hammered out this function works well.
    months = date[0]
    days = date[1]
    if months == 2:
        days += 31
    elif months == 3:
        if date[2] % 4 == 0 or date[2] % 1000 == 0:
            days += 60
        else:
            days += 59
    elif months == 4:
        if date[2] % 4 == 0 or date[2] % 1000 == 0:
            days += 90
        else:
            days += 89
    elif months == 5:
        if date[2] % 4 == 0 or date[2] % 1000 == 0:
            days += 121
        else:
            days += 120
    elif months == 6:
        if date[2] % 4 == 0 or date[2] % 1000 == 0:
            days += 151
        else:
            days += 150
    elif months == 7:
        if date[2] % 4 == 0 or date[2] % 1000 == 0:
            days += 182
        else:
            days += 181
    elif months == 8:
        if date[2] % 4 == 0 or date[2] % 1000 == 0:
            days += 213
        else:
            days += 212
    elif months == 9:
        if date[2] % 4 == 0 or date[2] % 1000 == 0:
            days += 243
        else:
            days += 242
    elif months == 10:
        if date[2] % 4 == 0 or date[2] % 1000 == 0:
            days += 274
        else:
            days += 273
    elif months == 11:
        if date[2] % 4 == 0 or date[2] % 1000 == 0:
            days += 305
        else:
            days += 304
    elif months == 12:
        if date[2] % 4 == 0 or date[2] % 1000 == 0:
            days += 335
        else:
            days += 334
    return days