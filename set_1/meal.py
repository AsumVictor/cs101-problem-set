# Convert function

# Convert every time to total hours eg 7:30 --> 7.5 hours


def main():
    time = convert('18:59')

    if time >= 7.0 and time <= 8.0:
        print("Breakfast")
    if time >= 12.0 and time <= 12.0:
        print("Lunch")
    if time >= 18.0 and time <= 19.0:
        print("Dinner")

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
    return float(minute) / 60 + int(hour)


main()
