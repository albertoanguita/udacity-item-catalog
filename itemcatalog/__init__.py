###############################################################################
# This script initializes the application                                     #
###############################################################################

from flask import Flask

app = Flask(__name__)

import itemcatalog.views
