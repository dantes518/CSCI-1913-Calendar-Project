"""
Project 1

Class: CSCI 1913, Spring 2021, Section 10
Professor: Jerald Thomas
Student: Dante Schroeder (schr1684)
"""

dotw_index = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}

#I added a month index to help clean up some other functions.
month_index = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

def get_doomsday_dotw(year):
    """This function takes in a year and returns the index of the doomsday day of the week for that year."""
    #This function follows the exact steps given in the readme. I split everything up to make it easier to understand, but I'm sure you could do most of this in just a few lines.
    century = year - (year % 100)
    if century % 400 == 0:
        #tuesday
        centuryindex = 2
    if century % 400 == 100:
        #sunday
        centuryindex = 0
    if century % 400 == 200:
        #friday
        centuryindex = 5
    if century % 400 == 300:
        #wednesday
        centuryindex = 3

    lastdigits = year % 100
    divisbytwelve = lastdigits // 12
    remaindertwelve = lastdigits % 12
    remainderfour = remaindertwelve // 4
    sum = (centuryindex + divisbytwelve + remaindertwelve + remainderfour) % 7
    return sum

def get_dotw(date):
    """This function takes in a date tuple and returns which day of the week that date is using the doomsday of each month."""
    #Jan. 3rd (or 4th if leap year)
    #Feb. 28th (or 29th if leap year)
    #March 14th
    #April 4th
    #May 9th
    #June 6th
    #July 11th
    #Aug. 8th
    #Sept. 5th
    #Oct. 10th
    #Nov. 7th
    #Dec. 12th
    #This function took me a long time to understand, but all it took was simplifying what I was trying to do.
    #I was originally taking into account the sign of the difference, but I found out that the sign doesn't matter because the modulo operation doesn't care about the sign of either number.
    #Once I figured that out, this function essentially wrote itself.
    if date[0] == 1:
        if date[2] % 4 == 0 or date[2] % 1000 == 0:
            diff = date[1] - 4
        else:
            diff = date[1] - 3
    elif date[0] == 2:
        if date[2] % 4 == 0 or date[2] % 1000 == 0:
            diff = date[1] - 29
        else:
            diff = date[1] - 28
    elif date[0] == 3:
        diff = date[1] - 14
    elif date[0] == 4:
        diff = date[1] - 4
    elif date[0] == 5:
        diff = date[1] - 9
    elif date[0] == 6:
        diff = date[1] - 6
    elif date[0] == 7:
        diff = date[1] - 11
    elif date[0] == 8:
        diff = date[1] - 8
    elif date[0] == 9:
        diff = date[1] - 5
    elif date[0] == 10:
        diff = date[1] - 10
    elif date[0] == 11:
        diff = date[1] - 7
    elif date[0] == 12:
        diff = date[1] - 12
    sum = diff + get_doomsday_dotw(date[2])
    return sum % 7