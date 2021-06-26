from datetime import datetime
import csv

# step 2a
def convert_mmddyyyy_date(date):
    '''Takes a date in the format mm/dd/yyyy and converts it to a datetime object.

    Args:
        date: string of a date in the mm/dd/yyyy format.

    Returns: a datetime object.
    '''
    return datetime.strptime(date, '%m/%d/%Y')

# step 2b
def get_month_name(date):
    '''Gets the month name from a datetime object.

    Args:
        date: a datetime object.

    Returns: the month name from the given date
        (e.g. "January", "February", etc).
    '''
    return date.strftime('%B')


def format_text(text, spaces):
    '''Formats a string to be left aligned and take up a certain number of
        characters.

    Args:
        text: a string.
        spaces: the number of spaces the string should take up.

    Returns: the formatted string.
    '''
    return f"{text:<{spaces}}"

# step 1
def read_csv_file(file_name):
    '''Reads a csv file and returns the data as a list.

    Args:
        file_name: a string representing the path and name of a csv file.

    Returns: a list.
    '''

    reading_file = []

    with open(file_name, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            #print(line)
        
            reading_file.append(line)

    return reading_file


def output_overall_statistics(monthly_data):
    '''Prints a summary of the total number of nests, hatched nests, false
        crawls, hit rocks and nest predation.

    Args:
        monthly_data: a list of lists, where each sublist contains the month
        name and total values for that month.
    '''
    pass


def output_monthly_statistics(monthly_data):
    '''Prints a summary of the total number of nests, hatched nests, false crawls,
       hit rocks and nest predation per month.

    Args:
        monthly_data: a list of lists, where each sublist contains the month
            name and total values for that month.
    '''
    pass


def output_nests_per_month_graph(monthly_data):
    '''Prints a graph of the total number of nests found per month.

    Args:
        monthly_data: a list of lists, where each sublist contains the month
            name and total values for that month.
    '''
    pass

# step 2
def transform_daily_to_monthly(data):
    '''Transform the data from daily to monthly format.

    Args:
        data: a list of lists, where each sublist represents data
            for a specific day.

    Returns: a list of lists, where each sublist represents data
        for a whole month.
    '''
    monthly = {
        'October': [],
        'November': [],
        'December': [],
        'January': [], 
        'February': [],
        'March': []
    }

    # monthly = []

    # print(monthly)
    # print(monthly["November"])

    for day in data:
        date = convert_mmddyyyy_date(day[0])
        month = get_month_name(date)
        # print(month)
        # print()
        # print(monthly)
        # print()
        # print(monthly[month])
        # new_monthly_data = 
        monthly[month] = monthly[month] + [day[1:6]]
        
        
    # print(monthly['December'])

    for month in monthly.keys():
        days = monthly[month]
        # print(days)
        nests = 0
        false_crawls = 0
        hit_rocks = 0
        hatched_nests = 0
        nest_pred = 0
        
        for day in days:
            nests += int(day[0])
            false_crawls += int(day[1])
            hit_rocks += int(day[2])
            hatched_nests += int(day[3])
            nest_pred += int(day[4])

        print(f"Monthly Statistics :")
        print([month, nests, hatched_nests, false_crawls, hit_rocks, nest_pred])
    
    return [month, nests, hatched_nests, false_crawls, hit_rocks, nest_pred]

        # total = sum([sum(int(x)) for x in days])
        # print(total)


    # test_date = "10/8/2020"
    # test_date = convert_mmddyyyy_date(test_date)
    # print(test_date)
    # print()

    # print(get_month_name(test_date))



    # october = 0
    # nests_oct = [all_data[1:12]]
    # print(nests_oct)

    # for ele in range(0, len(nests_oct)):
    #     print(nests_oct[ele])
    #     total = nests_oct + nests_oct[ele]
    # print(f"Number of Nests recorded per month (X = 5 nests):") 
    # print(f"October : {nests_oct}{total}")
    
    # monthly = []
    # for i in data:
        


if __name__ == "__main__":
    all_data = read_csv_file('data/2020_2021_turtle_data.csv')
    all_data.remove(all_data[0])
    # print(all_data)
    monthly_data = transform_daily_to_monthly(all_data)

    print('2020/2021 Flatback Turtle Migration at Cemetery Beach')
    print()
    output_nests_per_month_graph(monthly_data)
    print()
    output_monthly_statistics(monthly_data)
    print()
    output_overall_statistics(monthly_data)
    print()
