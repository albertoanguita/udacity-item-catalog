###############################################################################
# This script checks the initialization parameters and starts the server      #
###############################################################################

from itemcatalog import app
import sys

if len(sys.argv) != 2:
    print 'Usage: "python.exe runserver.py <port>"'
    sys.exit(1)

try:
    port = int(sys.argv[1])
    if port < 0 or port > 65535:
        raise ValueError()
except ValueError:
    print 'argument must be an integer between 0 and 65535'
    sys.exit(1)

app.secret_key = 'super_secret_key'
app.debug = True
app.run(host='0.0.0.0', port=int(sys.argv[1]))
