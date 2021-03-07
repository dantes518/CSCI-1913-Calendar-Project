"""
Project 1

Class: CSCI 1913, Spring 2021, Section 10
Professor: Jerald Thomas
Student: Dante Schroeder (schr1684)
"""
from project1_dotw import get_dotw, get_doomsday_dotw, dotw_index, month_index
from project1_events import get_events_binary_search

def validate_input(date_string):
    """This function takes in a user's input of a date. The date is passed in and split using the .split method.
    Using some casting functions, the if statements sort out the inputted date by month, date, and year and sees if the input is a valid date.
    If the input is a valid date, it will return a tuple of the date. If the input is not a valid date, it will return None."""
    #I decided to make sure the input was valid by checking each individual piece. I did this by splitting the input string by the dashes.
    #I checked first that the month value was between 1 and 12. I then checked depending on the month if the day value was valid.
    #I also made sure to check that the year was greater than 1000.
    #For February, I made a specific check for if it was a leap year or not. If the year inputted is not a leap year and the user entered
    #29 as the day value, it throws an error. Finally, once all values are checked and are valid, they are put into a tuple.
    splitdate = date_string.split("-")
    if splitdate[0] != '' and splitdate[1] != '' and splitdate[2] != '':
        if int(splitdate[0]) >= 1 and int(splitdate[0]) <= 12:
            if int(splitdate[0]) == 1 or int(splitdate[0]) == 3 or int(splitdate[0]) == 5 or int(splitdate[0]) == 7 or int(splitdate[0]) == 8 or int(splitdate[0]) == 10 or int(splitdate[0]) == 12:
                if int(splitdate[1]) >= 1 and int(splitdate[1]) <= 31:
                    if int(splitdate[2]) >= 1000:
                        date = (int(splitdate[0]), int(splitdate[1]), int(splitdate[2]))
                        return date
            elif int(splitdate[0]) == 4 or int(splitdate[0]) == 6 or int(splitdate[0]) == 9 or int(splitdate[0]) == 11:
                if int(splitdate[1]) >= 1 and int(splitdate[1]) <= 30:
                    if int(splitdate[2]) >= 1000:
                        date = (int(splitdate[0]), int(splitdate[1]), int(splitdate[2]))
                        return date
            elif int(splitdate[0]) == 2:
                if int(splitdate[2]) % 4 == 0 or int(splitdate[2]) % 1000 == 0:
                    if int(splitdate[1]) >= 1 and int(splitdate[1]) <= 29:
                        if int(splitdate[2]) >= 1000:
                            date = (int(splitdate[0]), int(splitdate[1]), int(splitdate[2]))
                            return date
                elif int(splitdate[1]) >= 1 and int(splitdate[1]) <= 28:
                    if int(splitdate[2]) >= 1000:
                        date = (int(splitdate[0]), int(splitdate[1]), int(splitdate[2]))
                        return date
    return None


def next_date(date):
    """This function takes in a date tuple, increments the day (whether it be a new month or year), and returns the next day, also in tuple form."""
    #For this function, I just created as many if else statements as I could to cover every situation I could think of.
    #Most of these if else statements are distinct edge cases where I add 1 in a different spot each time.
    if date[0] == 1 or date[0] == 3 or date[0] == 5 or date[0] == 7 or date[0] == 8 or date[0] == 10:
        if date[1] < 31:
            nextday = (date[0], date[1] + 1, date[2])
            return nextday
        elif date[1] == 31:
            nextday = (date[0] + 1, 1, date[2])
            return nextday
    elif date[0] == 12:
        if date[1] < 31:
            nextday = (date[0], date[1] + 1, date[2])
            return nextday
        elif date[1] == 31:
            nextday = (1, 1, date[2] + 1)
            return nextday
    elif date[0] == 4 or date[0] == 6 or date[0] == 9 or date[0] == 11:
        if date[1] < 30:
            nextday = (date[0], date[1] + 1, date[2])
            return nextday
        elif date[1] == 30:
            nextday = (date[0] + 1, 1, date[2])
            return nextday
    elif date[0] == 2:
        if date[2] % 4 == 0 or date[2] % 1000 == 0:
            if date[1] < 29:
                nextday = (date[0], date[1] + 1, date[2])
                return nextday
            elif date[1] == 29:
                nextday = (date[0] + 1, 1, date[2])
                return nextday
        elif date[1] < 28:
            nextday = (date[0], date[1] + 1, date[2])
            return nextday
        elif date[1] == 28:
            nextday = (date[0] + 1, 1, date[2])
            return nextday

def previous_date(date):
    """This function takes in a date tuple, decrements the day (whether it be a new month or year), and returns the previous day, also in tuple form."""
    #This function is basically the same as the next_date function, except I subtracted 1 instead of adding 1.
    #The main difference was figuring out what to do when transitioning to a different month with a different amount of days.
    #This is why August, for example, is in it's own if else statement; most 31 day months go backwards into a 30 day month.
    #August, however, transitions into July, which is another 31 day month. Because of this, I needed to create a case just for August.
    #I used the same thought process for the other monthly transitions, as well as the year transition (1-1-XXXX -> 12-31-XXX(X-1))
    if date[0] == 5 or date[0] == 7 or date[0] == 10 or date[0] == 12:
        if date[1] > 1:
            prevday = (date[0], date[1] - 1, date[2])
            return prevday
        elif date[1] == 1:
            prevday = (date[0] - 1, 30, date[2])
            return prevday
    elif date[0] == 8:
        if date[1] > 1:
            prevday = (date[0], date[1] - 1, date[2])
            return prevday
        elif date[1] == 1:
            prevday = (date[0] - 1, 31, date[2])
            return prevday
    elif date[0] == 1:
        if date[1] > 1:
            prevday = (date[0], date[1] - 1, date[2])
            return prevday
        elif date[1] == 1:
            prevday = (12, 31, date[2] - 1)
            return prevday
    elif date[0] == 4 or date[0] == 6 or date[0] == 9 or date[0] == 11:
        if date[1] > 1:
            prevday = (date[0], date[1] - 1, date[2])
            return prevday
        elif date[1] == 1:
            prevday = (date[0] - 1, 31, date[2])
            return prevday
    elif date[0] == 3:
        if date[2] % 4 == 0 or date[2] % 1000 == 0:
            if date[1] > 1:
                prevday = (date[0], date[1] - 1, date[2])
                return prevday
            elif date[1] == 1:
                prevday = (2, 29, date[2])
                return prevday
        elif date[1] > 1:
            prevday = (date[0], date[1] - 1, date[2])
            return prevday
        elif date[1] == 1:
            prevday = (date[0] - 1, 28, date[2])
            return prevday
    elif date[0] == 2:
        if date[1] > 1:
            prevday = (date[0], date[1] - 1, date[2])
            return prevday
        elif date[1] == 1:
            prevday = (date[0] - 1, 31, date[2])
            return prevday

def printweek(date):
    '''This function takes in a date tuple and prints out each day of that week, including events that occur on any day of that week.'''
    #This function took forever to work out the kinks. It involves a lot of messy lines using next_date and previous_date.
    #There 100% is a better way to go about this function, but this was the first thing that came to mind and I just wanted to make it work.
    #Keeping track of everything in this function was really difficult, but I ended up finding a quick and easy way to make every case work.
    dotw = get_dotw(date)
    if dotw == 0:
        print(dotw_index[dotw] + ",", month_index[date[0]], date[1])
        if len(get_events_binary_search(date)) == 0:
            print(" - No events")
        elif len(get_events_binary_search(date)) > 1:
            for event in get_events_binary_search(date):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(date)[0])

        print(dotw_index[dotw + 1] + ",", month_index[next_date(date)[0]], next_date(date)[1])
        if len(get_events_binary_search(next_date(date))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(next_date(date))) > 1:
            for event in get_events_binary_search(next_date(date)):
                print(" - " + event)
        else:
            print(" - " + get_events_binary_search(next_date(date))[0])

        print(dotw_index[dotw + 2] + ",", month_index[next_date(next_date(date))[0]], next_date(next_date(date))[1])
        if len(get_events_binary_search(next_date(next_date(date)))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(next_date(next_date(date)))) > 1:
            for event in get_events_binary_search(next_date(next_date(date))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(next_date(next_date(date)))[0])

        print(dotw_index[dotw + 3] + ",", month_index[next_date(next_date(next_date(date)))[0]], next_date(next_date(next_date(date)))[1])
        if len(get_events_binary_search(next_date(next_date(next_date(date))))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(next_date(next_date(next_date(date))))) > 1:
            for event in get_events_binary_search(next_date(next_date(next_date(date)))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(next_date(next_date(next_date(date))))[0])

        print(dotw_index[dotw + 4] + ",", month_index[next_date(next_date(next_date(next_date(date))))[0]], next_date(next_date(next_date(next_date(date))))[1])
        if len(get_events_binary_search(next_date(next_date(next_date(next_date(date)))))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(next_date(next_date(next_date(next_date(date)))))) > 1:
            for event in get_events_binary_search(next_date(next_date(next_date(next_date(date))))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(next_date(next_date(next_date(next_date(date)))))[0])

        print(dotw_index[dotw + 5] + ",", month_index[next_date(next_date(next_date(next_date(next_date(date)))))[0]], next_date(next_date(next_date(next_date(next_date(date)))))[1])
        if len(get_events_binary_search(next_date(next_date(next_date(next_date(next_date(date))))))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(next_date(next_date(next_date(next_date(next_date(date))))))) > 1:
            for event in get_events_binary_search(next_date(next_date(next_date(next_date(next_date(date)))))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(next_date(next_date(next_date(next_date(next_date(date))))))[0])

        print(dotw_index[dotw + 6] + ",", month_index[next_date(next_date(next_date(next_date(next_date(next_date(date))))))[0]], next_date(next_date(next_date(next_date(next_date(next_date(date))))))[1])
        if len(get_events_binary_search(next_date(next_date(next_date(next_date(next_date(next_date(date)))))))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(next_date(next_date(next_date(next_date(next_date(next_date(date)))))))) > 1:
            for event in get_events_binary_search(next_date(next_date(next_date(next_date(next_date(next_date(date))))))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(next_date(next_date(next_date(next_date(next_date(next_date(date)))))))[0])

    if dotw == 1:
        print(dotw_index[dotw - 1] + ",", month_index[previous_date(date)[0]], previous_date(date)[1])
        if len(get_events_binary_search(previous_date(date))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(previous_date(date))) > 1:
            for event in get_events_binary_search(previous_date(date)):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(previous_date(date))[0])

        print(dotw_index[dotw] + ",", month_index[date[0]], date[1])
        if len(get_events_binary_search(date)) == 0:
            print(" - No events")
        elif len(get_events_binary_search(date)) > 1:
            for event in get_events_binary_search(date):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(date)[0])

        print(dotw_index[dotw + 1] + ",", month_index[next_date(date)[0]], next_date(date)[1])
        if len(get_events_binary_search(next_date(date))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(next_date(date))) > 1:
            for event in get_events_binary_search(next_date(date)):
                print(" - " + event)
        else:
            print(" - " + get_events_binary_search(next_date(date))[0])

        print(dotw_index[dotw + 2] + ",", month_index[next_date(next_date(date))[0]], next_date(next_date(date))[1])
        if len(get_events_binary_search(next_date(next_date(date)))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(next_date(next_date(date)))) > 1:
            for event in get_events_binary_search(next_date(next_date(date))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(next_date(next_date(date)))[0])

        print(dotw_index[dotw + 3] + ",", month_index[next_date(next_date(next_date(date)))[0]], next_date(next_date(next_date(date)))[1])
        if len(get_events_binary_search(next_date(next_date(next_date(date))))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(next_date(next_date(next_date(date))))) > 1:
            for event in get_events_binary_search(next_date(next_date(next_date(date)))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(next_date(next_date(next_date(date))))[0])

        print(dotw_index[dotw + 4] + ",", month_index[next_date(next_date(next_date(next_date(date))))[0]], next_date(next_date(next_date(next_date(date))))[1])
        if len(get_events_binary_search(next_date(next_date(next_date(next_date(date)))))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(next_date(next_date(next_date(next_date(date)))))) > 1:
            for event in get_events_binary_search(next_date(next_date(next_date(next_date(date))))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(next_date(next_date(next_date(next_date(date)))))[0])

        print(dotw_index[dotw + 5] + ",", month_index[next_date(next_date(next_date(next_date(next_date(date)))))[0]], next_date(next_date(next_date(next_date(next_date(date)))))[1])
        if len(get_events_binary_search(next_date(next_date(next_date(next_date(next_date(date))))))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(next_date(next_date(next_date(next_date(next_date(date))))))) > 1:
            for event in get_events_binary_search(next_date(next_date(next_date(next_date(next_date(date)))))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(next_date(next_date(next_date(next_date(next_date(date))))))[0])

    if dotw == 2:
        print(dotw_index[dotw - 2] + ",", month_index[previous_date(previous_date(date))[0]], previous_date(previous_date(date))[1])
        if len(get_events_binary_search(previous_date(previous_date(date)))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(previous_date(previous_date(date)))) > 1:
            for event in get_events_binary_search(previous_date(previous_date(date))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(previous_date(previous_date(date)))[0])

        print(dotw_index[dotw - 1] + ",", month_index[previous_date(date)[0]], previous_date(date)[1])
        if len(get_events_binary_search(previous_date(date))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(previous_date(date))) > 1:
            for event in get_events_binary_search(previous_date(date)):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(previous_date(date))[0])

        print(dotw_index[dotw] + ",", month_index[date[0]], date[1])
        if len(get_events_binary_search(date)) == 0:
            print(" - No events")
        elif len(get_events_binary_search(date)) > 1:
            for event in get_events_binary_search(date):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(date)[0])

        print(dotw_index[dotw + 1] + ",", month_index[next_date(date)[0]], next_date(date)[1])
        if len(get_events_binary_search(next_date(date))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(next_date(date))) > 1:
            for event in get_events_binary_search(next_date(date)):
                print(" - " + event)
        else:
            print(" - " + get_events_binary_search(next_date(date))[0])

        print(dotw_index[dotw + 2] + ",", month_index[next_date(next_date(date))[0]], next_date(next_date(date))[1])
        if len(get_events_binary_search(next_date(next_date(date)))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(next_date(next_date(date)))) > 1:
            for event in get_events_binary_search(next_date(next_date(date))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(next_date(next_date(date)))[0])

        print(dotw_index[dotw + 3] + ",", month_index[next_date(next_date(next_date(date)))[0]], next_date(next_date(next_date(date)))[1])
        if len(get_events_binary_search(next_date(next_date(next_date(date))))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(next_date(next_date(next_date(date))))) > 1:
            for event in get_events_binary_search(next_date(next_date(next_date(date)))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(next_date(next_date(next_date(date))))[0])

        print(dotw_index[dotw + 4] + ",", month_index[next_date(next_date(next_date(next_date(date))))[0]], next_date(next_date(next_date(next_date(date))))[1])
        if len(get_events_binary_search(next_date(next_date(next_date(next_date(date)))))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(next_date(next_date(next_date(next_date(date)))))) > 1:
            for event in get_events_binary_search(next_date(next_date(next_date(next_date(date))))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(next_date(next_date(next_date(next_date(date)))))[0])

    if dotw == 3:
        print(dotw_index[dotw - 3] + ",", month_index[previous_date(previous_date(previous_date(date)))[0]], previous_date(previous_date(previous_date(date)))[1])
        if len(get_events_binary_search(previous_date(previous_date(previous_date(date))))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(previous_date(previous_date(previous_date(date))))) > 1:
            for event in get_events_binary_search(previous_date(previous_date(previous_date(date)))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(previous_date(previous_date(previous_date(date))))[0])

        print(dotw_index[dotw - 2] + ",", month_index[previous_date(previous_date(date))[0]], previous_date(previous_date(date))[1])
        if len(get_events_binary_search(previous_date(previous_date(date)))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(previous_date(previous_date(date)))) > 1:
            for event in get_events_binary_search(previous_date(previous_date(date))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(previous_date(previous_date(date)))[0])

        print(dotw_index[dotw - 1] + ",", month_index[previous_date(date)[0]], previous_date(date)[1])
        if len(get_events_binary_search(previous_date(date))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(previous_date(date))) > 1:
            for event in get_events_binary_search(previous_date(date)):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(previous_date(date))[0])

        print(dotw_index[dotw] + ",", month_index[date[0]], date[1])
        if len(get_events_binary_search(date)) == 0:
            print(" - No events")
        elif len(get_events_binary_search(date)) > 1:
            for event in get_events_binary_search(date):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(date)[0])

        print(dotw_index[dotw + 1] + ",", month_index[next_date(date)[0]], next_date(date)[1])
        if len(get_events_binary_search(next_date(date))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(next_date(date))) > 1:
            for event in get_events_binary_search(next_date(date)):
                print(" - " + event)
        else:
            print(" - " + get_events_binary_search(next_date(date))[0])

        print(dotw_index[dotw + 2] + ",", month_index[next_date(next_date(date))[0]], next_date(next_date(date))[1])
        if len(get_events_binary_search(next_date(next_date(date)))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(next_date(next_date(date)))) > 1:
            for event in get_events_binary_search(next_date(next_date(date))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(next_date(next_date(date)))[0])

        print(dotw_index[dotw + 3] + ",", month_index[next_date(next_date(next_date(date)))[0]], next_date(next_date(next_date(date)))[1])
        if len(get_events_binary_search(next_date(next_date(next_date(date))))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(next_date(next_date(next_date(date))))) > 1:
            for event in get_events_binary_search(next_date(next_date(next_date(date)))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(next_date(next_date(next_date(date))))[0])

    if dotw == 4:
        print(dotw_index[dotw - 4] + ",", month_index[previous_date(previous_date(previous_date(previous_date(date))))[0]], previous_date(previous_date(previous_date(previous_date(date))))[1])
        if len(get_events_binary_search(previous_date(previous_date(previous_date(previous_date(date)))))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(previous_date(previous_date(previous_date(previous_date(date)))))) > 1:
            for event in get_events_binary_search(previous_date(previous_date(previous_date(previous_date(date))))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(previous_date(previous_date(previous_date(previous_date(date)))))[0])

        print(dotw_index[dotw - 3] + ",", month_index[previous_date(previous_date(previous_date(date)))[0]], previous_date(previous_date(previous_date(date)))[1])
        if len(get_events_binary_search(previous_date(previous_date(previous_date(date))))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(previous_date(previous_date(previous_date(date))))) > 1:
            for event in get_events_binary_search(previous_date(previous_date(previous_date(date)))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(previous_date(previous_date(previous_date(date))))[0])

        print(dotw_index[dotw - 2] + ",", month_index[previous_date(previous_date(date))[0]], previous_date(previous_date(date))[1])
        if len(get_events_binary_search(previous_date(previous_date(date)))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(previous_date(previous_date(date)))) > 1:
            for event in get_events_binary_search(previous_date(previous_date(date))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(previous_date(previous_date(date)))[0])

        print(dotw_index[dotw - 1] + ",", month_index[previous_date(date)[0]], previous_date(date)[1])
        if len(get_events_binary_search(previous_date(date))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(previous_date(date))) > 1:
            for event in get_events_binary_search(previous_date(date)):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(previous_date(date))[0])

        print(dotw_index[dotw] + ",", month_index[date[0]], date[1])
        if len(get_events_binary_search(date)) == 0:
            print(" - No events")
        elif len(get_events_binary_search(date)) > 1:
            for event in get_events_binary_search(date):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(date)[0])

        print(dotw_index[dotw + 1] + ",", month_index[next_date(date)[0]], next_date(date)[1])
        if len(get_events_binary_search(next_date(date))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(next_date(date))) > 1:
            for event in get_events_binary_search(next_date(date)):
                print(" - " + event)
        else:
            print(" - " + get_events_binary_search(next_date(date))[0])

        print(dotw_index[dotw + 2] + ",", month_index[next_date(next_date(date))[0]], next_date(next_date(date))[1])
        if len(get_events_binary_search(next_date(next_date(date)))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(next_date(next_date(date)))) > 1:
            for event in get_events_binary_search(next_date(next_date(date))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(next_date(next_date(date)))[0])

    if dotw == 5:
        print(dotw_index[dotw - 5] + ",", month_index[previous_date(previous_date(previous_date(previous_date(previous_date(date)))))[0]], previous_date(previous_date(previous_date(previous_date(previous_date(date)))))[1])
        if len(get_events_binary_search(previous_date(previous_date(previous_date(previous_date(previous_date(date))))))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(previous_date(previous_date(previous_date(previous_date(previous_date(date))))))) > 1:
            for event in get_events_binary_search(previous_date(previous_date(previous_date(previous_date(previous_date(date)))))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(previous_date(previous_date(previous_date(previous_date(previous_date(date))))))[0])

        print(dotw_index[dotw - 4] + ",", month_index[previous_date(previous_date(previous_date(previous_date(date))))[0]], previous_date(previous_date(previous_date(previous_date(date))))[1])
        if len(get_events_binary_search(previous_date(previous_date(previous_date(previous_date(date)))))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(previous_date(previous_date(previous_date(previous_date(date)))))) > 1:
            for event in get_events_binary_search(previous_date(previous_date(previous_date(previous_date(date))))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(previous_date(previous_date(previous_date(previous_date(date)))))[0])

        print(dotw_index[dotw - 3] + ",", month_index[previous_date(previous_date(previous_date(date)))[0]], previous_date(previous_date(previous_date(date)))[1])
        if len(get_events_binary_search(previous_date(previous_date(previous_date(date))))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(previous_date(previous_date(previous_date(date))))) > 1:
            for event in get_events_binary_search(previous_date(previous_date(previous_date(date)))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(previous_date(previous_date(previous_date(date))))[0])

        print(dotw_index[dotw - 2] + ",", month_index[previous_date(previous_date(date))[0]], previous_date(previous_date(date))[1])
        if len(get_events_binary_search(previous_date(previous_date(date)))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(previous_date(previous_date(date)))) > 1:
            for event in get_events_binary_search(previous_date(previous_date(date))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(previous_date(previous_date(date)))[0])

        print(dotw_index[dotw - 1] + ",", month_index[previous_date(date)[0]], previous_date(date)[1])
        if len(get_events_binary_search(previous_date(date))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(previous_date(date))) > 1:
            for event in get_events_binary_search(previous_date(date)):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(previous_date(date))[0])

        print(dotw_index[dotw] + ",", month_index[date[0]], date[1])
        if len(get_events_binary_search(date)) == 0:
            print(" - No events")
        elif len(get_events_binary_search(date)) > 1:
            for event in get_events_binary_search(date):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(date)[0])

        print(dotw_index[dotw + 1] + ",", month_index[next_date(date)[0]], next_date(date)[1])
        if len(get_events_binary_search(next_date(date))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(next_date(date))) > 1:
            for event in get_events_binary_search(next_date(date)):
                print(" - " + event)
        else:
            print(" - " + get_events_binary_search(next_date(date))[0])

    if dotw == 6:
        print(dotw_index[dotw - 6] + ",", month_index[previous_date(previous_date(previous_date(previous_date(previous_date(previous_date(date))))))[0]], previous_date(previous_date(previous_date(previous_date(previous_date(previous_date(date))))))[1])
        if len(get_events_binary_search(previous_date(previous_date(previous_date(previous_date(previous_date(previous_date(date)))))))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(previous_date(previous_date(previous_date(previous_date(previous_date(previous_date(date)))))))) > 1:
            for event in get_events_binary_search(previous_date(previous_date(previous_date(previous_date(previous_date(previous_date(date))))))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(previous_date(previous_date(previous_date(previous_date(previous_date(previous_date(date)))))))[0])

        print(dotw_index[dotw - 5] + ",", month_index[previous_date(previous_date(previous_date(previous_date(previous_date(date)))))[0]], previous_date(previous_date(previous_date(previous_date(previous_date(date)))))[1])
        if len(get_events_binary_search(previous_date(previous_date(previous_date(previous_date(previous_date(date))))))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(previous_date(previous_date(previous_date(previous_date(previous_date(date))))))) > 1:
            for event in get_events_binary_search(previous_date(previous_date(previous_date(previous_date(previous_date(date)))))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(previous_date(previous_date(previous_date(previous_date(previous_date(date))))))[0])

        print(dotw_index[dotw - 4] + ",", month_index[previous_date(previous_date(previous_date(previous_date(date))))[0]], previous_date(previous_date(previous_date(previous_date(date))))[1])
        if len(get_events_binary_search(previous_date(previous_date(previous_date(previous_date(date)))))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(previous_date(previous_date(previous_date(previous_date(date)))))) > 1:
            for event in get_events_binary_search(previous_date(previous_date(previous_date(previous_date(date))))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(previous_date(previous_date(previous_date(previous_date(date)))))[0])

        print(dotw_index[dotw - 3] + ",", month_index[previous_date(previous_date(previous_date(date)))[0]], previous_date(previous_date(previous_date(date)))[1])
        if len(get_events_binary_search(previous_date(previous_date(previous_date(date))))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(previous_date(previous_date(previous_date(date))))) > 1:
            for event in get_events_binary_search(previous_date(previous_date(previous_date(date)))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(previous_date(previous_date(previous_date(date))))[0])

        print(dotw_index[dotw - 2] + ",", month_index[previous_date(previous_date(date))[0]], previous_date(previous_date(date))[1])
        if len(get_events_binary_search(previous_date(previous_date(date)))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(previous_date(previous_date(date)))) > 1:
            for event in get_events_binary_search(previous_date(previous_date(date))):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(previous_date(previous_date(date)))[0])

        print(dotw_index[dotw - 1] + ",", month_index[previous_date(date)[0]], previous_date(date)[1])
        if len(get_events_binary_search(previous_date(date))) == 0:
            print(" - No events")
        elif len(get_events_binary_search(previous_date(date))) > 1:
            for event in get_events_binary_search(previous_date(date)):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(previous_date(date))[0])

        print(dotw_index[dotw] + ",", month_index[date[0]], date[1])
        if len(get_events_binary_search(date)) == 0:
            print(" - No events")
        elif len(get_events_binary_search(date)) > 1:
            for event in get_events_binary_search(date):
                print(" _ " + event)
        else:
            print(" - " + get_events_binary_search(date)[0])

#Main function, just ensures that the input isn't taken when the file is imported elsewhere.
if __name__ == '__main__':
    inputdate = input("Enter a date: ")
    inputdate = validate_input(inputdate)
    printweek(inputdate)