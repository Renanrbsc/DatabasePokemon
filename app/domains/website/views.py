from flask import Blueprint, render_template

app_website = Blueprint('website', __name__)

app_website.template_folder = 'templates'
app_website.static_folder = 'static'


@app_website.route('/')
def index():
    return render_template('index.html', login=None)
