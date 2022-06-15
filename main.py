import bs4 as bs

import sys
import json
import time
import os.path
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl, QDate, QTime, QDateTime, Qt, QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView


def save_to_json(s_date, s_time, wait_time):
    json_data = {}
    file_name = "wait_data/" + s_date + ".json"

    if os.path.isfile(file_name):
        with open(file_name) as json_file:
            json_data = json.load(json_file)
    else:
        json_data = {}

    json_data[s_time] = wait_time

    with open(file_name, 'w') as outfile:
        json.dump(json_data, outfile)



def parse_tree(html):
    soup = bs.BeautifulSoup(html, "lxml")
    #print("SOUP", soup)
    main = soup.find("main")
    if not main:
        print("Main not found!")
        return
    standard_content = main.find("div", {"id": "StandardPageContent"})

    vantetider = standard_content.find("div", {"id": "vantetider", "class": "queuetimeblock"})

    nowaittime = vantetider.find("div", {"class":  "no-waiting-time"})

    sample_date = QDate.currentDate().toString(Qt.ISODate)
    sample_time = QTime.currentTime().toString(Qt.ISODate)

    wait_time = {}
    if nowaittime:
        wait_time = {"Terminal 2": 45,
                     "Terminal 5D": 45,
                     "Terminal 5F": 45}
    else:
        terminal_entries = vantetider.findAll("div", {"class": "terminalEntry"})
        for entry in terminal_entries:
            label = entry.find("div", {"class": "terminalLabel"}).text
            queue = entry.find("div", {"class": "terminalQueueTime"}).text

            queue = queue.split(" ")[-1]
            if "-" in queue:
                queue = queue.split("-")[-1]

            wait_time[label] = int(queue)

    print("Wait_time: ", wait_time)
    save_to_json(sample_date, sample_time, wait_time)

    #print("HTML", vantetider)


def _on_render_complete(html):
    parse_tree(html)
    print("render complete")
    web.loadFinished.disconnect(_load_finished)


def _load_finished():
    print("Finished")
    web.page().runJavaScript(
        "document.getElementsByTagName('html')[0].innerHTML", _on_render_complete
    )

def _load_site():

    web.load(QUrl(site))
    web.show()
    web.loadFinished.connect(_load_finished)

site = "https://www.swedavia.se/arlanda/sakerhetskontroll"

app = QApplication(sys.argv)
web = QWebEngineView()

timer = QTimer()
timer.timeout.connect(_load_site)
timer.setInterval(1000 * 60 * 1)
timer.start(1000 * 60 * 1)

sys.exit(app.exec_())

