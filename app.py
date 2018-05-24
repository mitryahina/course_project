from flask import Flask, render_template
import json


app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/word_cloud', methods=['GET'])
def word_cloud():
    with open('results/result_5_17_2018.txt', encoding='UTF-8', errors='ignore') as f:
        data = f.readlines()
        res = []
        for i in data:
            i = i.strip()
            try:
                headline = i.split('#')[0]
                k = i.split('.')[0][-1] + '.' + i.split('.')[1]
                trend = i[i.index('#'): i.index('.') - 1]
                res.append((headline, int(float(k) * 100)))
                res.append((trend, int(float(k) * 200)))
            except Exception as e:
                print(e)
                continue
    res = {item[0]: item[1] for item in res}
    res_json = []
    for text, weight in res.items():
        res_json.append({'text': text, 'weight': weight})
    print(res_json)
    return json.dumps(res_json)


if __name__ == '__main__':
    app.run()
