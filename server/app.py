from flask import Flask, Response
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)  # 允许跨域

@app.route('/events')
def stream():
    def event_stream():
        while True:
            time.sleep(1)
            yield f'data: Server time is {time.strftime("%Y-%m-%d %H:%M:%S")}\n\n'
    return Response(event_stream(), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)

