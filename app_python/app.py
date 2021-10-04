"""Simple python flask application"""
from flask import Flask, render_template
import pytz
import datetime

app = Flask(__name__)


@app.route("/")
def home_page():
    """
    Returns rendered index.htl as a home page
    """

    timezone = pytz.timezone("Europe/Moscow")
    server_time = datetime.datetime.now(timezone)
    # print(str(server_time))
    visits = []
    with open("visits.txt", "r", encoding="utf-8") as file:
        visits = file.readlines()
    visits = visits[:100]
    visits.insert(0, str(server_time)+'\n')
    with open("visits.txt", "w", encoding="utf-8") as file:
        file.writelines(visits)
    
    return render_template("index.html")


@app.route("/visits")
def visits_page():
    """
    Returns number of times root path was accessed
    Returns:
        int: number of times was accessed
    """
    visits = []
    with open("visits.txt", "r", encoding="utf-8") as file:
        visits = file.readlines()
    html_response = render_template(
        "visits.html", visits=visits
    )
    return html_response


if __name__ == "__main__":
    app.run("0.0.0.0", port=80, debug=True)
