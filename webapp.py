from datetime import datetime
from pytz import timezone
from flask import Flask
    
app = Flask(__name__)


@app.route("/")
def home():
    return "hello world"
@app.route("/time")
def time():
    date = datetime.now(timezone("Asia/Kolkata"))
    return str(date)

if __name__ == "__main__":
    app.run(debug=True)