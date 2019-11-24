import csv
from flask import Flask, abort, render_template, url_for

app = Flask(__name__)

def get_csv():
    csv_file = open('hittakuri_data.csv', 'r', encoding='utf-8')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

@app.route("/")
def index():
    template = 'home.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)

@app.route('/<row_id>/')
def detail(row_id):
    template = 'detail.html'
    object_list = get_csv()
    for row in object_list:
        if row['id'] == row_id:  
            return render_template(template, object=row)
    abort(404)

if __name__ == '__main__':
    app.run(debug=True)