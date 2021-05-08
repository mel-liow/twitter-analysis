import time

from api import app

@app.route('/twitter', methods=['POST'])
def get_data():
	return {'time': time.time()}

