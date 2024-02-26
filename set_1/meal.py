# Convert function

# Convert every time to total hours eg 7:30 --> 7.5 hours


def main():
    print(convert('12:30'))


def convert(time):
    # @input formatr '##:##' or '#:##'
    # Split the input according to the ':'
    # result would be [##, ##] or [#, ##]
    # hour == first elemet ## or #
    # minute = second half ##

    # convert the minute to hours ##/50 --> converted hour
    # add to the hours to get total hours hour + converted hour --> total hour
    # return total hour
    hour, minute = time.split(':')
    minute_hours = (float(minute) / 60)
    total_hours = minute_hours + int(hour)
    return total_hours

    return splitted_string


main()
