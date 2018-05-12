def get_trends(path):
    """
    Read file with trends
    """
    with open(path, 'r', encoding='UTF-8') as f:
        data = f.read()[14:-4]
        trends = data.split('}, {')
        return trends


def parse(trend):
    """
    Form a dictionary of trend's attributes
    """
    splitted = trend.split(",")
    res = {}
    for i in range(len(splitted)):
        res[splitted[i].split(': ')[0]] = splitted[i].split(': ')[1]
    return res


class Trend:
    """
    Represents Trend with its name, url and volume
    """
    def __init__(self, trend_dict):
        self.name = trend_dict.get("'name'")[1:-1]
        self.url = trend_dict.get(" 'url'")[1:-1]
        self.volume = trend_dict.get(" 'tweet_volume'")[1:-1]


class DayTrends:
    """
    Contains trends for a given day
    """
    DAY_TRENDS = []

    def __init__(self, lst, date):
        self.date = date
        for i in lst:
            self.DAY_TRENDS.append(Trend(parse(i)))

    def __str__(self):
        res = self.date + '\n'
        for i in self.DAY_TRENDS:
            res += 'name: {}\nurl: {}\nvolume: {}\n\n'\
                .format(i.name, i.url, i.volume)
        return res
