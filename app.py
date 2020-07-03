from random import choice

import argparse

from flask import Flask
app = Flask(__name__)


@app.route('/')
def rand_number():
    nums = [0,  2,  4,  6,  8]
    rand = choice(nums)
    return str(rand)+'\n'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='start an http server that returns numbers')
    parser.add_argument('--port', type=int, default=5000, help='port on which to serve http')
    args = parser.parse_args()
    app.run(debug=True, host='0.0.0.0', port=args.port)
