#from app.mongodb import MetadataManager
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for
health_check = Blueprint('healthcheck', __name__, url_prefix='')
zip_files = Blueprint('zipfiles', __name__, url_prefix='')

# Set the route and accepted methods
@health_check.route('/healthcheck/', methods=['GET', 'POST'])
def check_health():
    # print "debug..."
    return  render_template('healthcheck/ack.html')

@zip_files.route('/zipfiles/', methods=['GET'])
def load_zip_files():
    # vmx_zip_files = mongo.db.zipfiles.find({'vmx...': True})
    return render_template('zipfiles/zipfiles.html')
    # return render_template('zipfiles.html', zip_files=vmx_zip_files)