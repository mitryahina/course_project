import trend as td
import headline as hd
import compare
import datetime
import API_trial as at
import twitter_geo as tg

now = datetime.datetime.now()


def get_data(location=1):
    global now

    with open("data/news_{}_{}_{}.txt".format(now.day, now.month, now.year),
              'w', errors='ignore') as file:
            file.write(str(at.get_headlines()))

    with open("data/trends_{}_{}_{}.txt".format(now.day, now.month, now.year),
              'w', errors='ignore') as file:
            file.write(str(tg.api.trends_place(location)))


def create_headlines_obj(day=None, month=None, year=None):
    global now
    if not day or not month or not year:
        day = now.day
        month = now.month
        year = now.year
    return hd.DayHeadlines('data/news_{}_{}_{}.txt'.
                           format(day, month, year),
                           '{}.{}.{}'.format(day, month, year))


def get_trends_obj(day=None, month=None, year=None):
    global now
    if not day or not month or not year:
        day = now.day
        month = now.month
        year = now.year
    return td.DayTrends('data/trends_{}_{}_{}.txt'.
                        format(day, month, year),
                        '{}.{}.{}'.format(day, month, year))


def compare_daily(day=None, month=None, year=None):
    headlines = create_headlines_obj(day, month, year)
    trends = get_trends_obj(day, month, year)
    similar = []

    for trend in trends.DAY_TRENDS:
        print('Comparing...')
        for headline in headlines.headlines:
            k = compare.compare(headline, trend)
            print(k)
            if k > 0.4:
                similar.append((headline, trend, k))
    return similar


def write_results(day=None, month=None, year=None):
    global now
    if not day or not month or not year:
        day = now.day
        month = now.month
        year = now.year
    with open('result_{}_{}_{}.txt'.format(day, month, year),
              'w', encoding='UTF-8', errors='ignore') as f:
        res = compare_daily(day, month, year)
        for i in res:
            s = i[0].title + i[1].name + str(i[2]) + '\n'
            f.write(s)


# get_data()

def menu():
    print("Choose options: \n1) get today's data\n2) analyze today's data\n"
          "3) show analysis results\n4) exit")
    action = input()
    while action not in ['1', '2', '3', '4']:
        action = input('Wrong option! Try again: ')

    if action == '1':
        print('Retrieving results...')
        get_data()

    if action == '2':
        print('Analyzing files. This might take a while')
        write_results()

    if action == '3':
        day, month, year = input('Enter the date separated by a'
                                 ' whitespaces(dd mm yyyy): ').split()
        with open('results/result_{}_{}_{}.txt'.format(day, month, year)) as f:
            for line in f:
                print(line)

    if action == '4':
        return False


if __name__ == '__main__':
    while True:
        menu()
