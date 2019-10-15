from flask import render_template, Blueprint
main = Blueprint(
    'main',
    __name__,
    template_folder='templates/main',
    url_prefix='/'
)


@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main/index.html')
