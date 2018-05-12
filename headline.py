def read_file(path):
    with open(path, 'r', encoding='UTF-8', errors='ignore') as f:
        data = f.read()
        data = data[data.index("[") + 1:-2].split('}')
        print(data[1])
    return data


def parse(headline):
    source = headline[0][headline[0].find("'name':") + 9:-1]
    title = headline[1][headline[1].find("'title':") + 10:
                        headline[1].find("'description'") - 3]
    url = headline[1][headline[1].find("'url': '") + 8:
                      headline[1].find("', 'urlTo")]
    description = headline[1][headline[1].find("'description'") + 16:
                              headline[1].find("', 'url'")]
    return title, source, url, description


class Headline:
    def __init__(self, title, source, url, description):
        self.title = title
        self.source = source
        self.url = url
        self.description = description

    def __str__(self):
        return "Title: {}\nSource: {}\nUrl: {}\nDescription:{}\n\n".\
            format(self.title, self.source, self.url, self.description)


class DayHeadlines:
    def __init__(self, path, date):
        self.date = date
        self.headlines = []

        headlines = read_file(path)
        for i in range(0, len(headlines) - 1, 2):
            title, source, url, description = parse(headlines[i: i + 2])
            self.headlines.append(Headline(title, source, url, description))

    def __str__(self):
        res = "Headlines for: " + self.date + '\n'
        for headline in self.headlines:
            res += str(headline)
        return res
