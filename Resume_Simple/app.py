import oyaml as yaml
from flask import Flask
from flask import render_template


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def index():
    #with open('_config.yaml', 'r') as f:
    #    website_data = yaml.full_load(stream=f)
    website_data = yaml.full_load(open('_config.yaml'))

    return render_template('index.html', data=website_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
