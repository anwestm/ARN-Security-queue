import bs4 as bs

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl, QDate, QTime, QDateTime, Qt, QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView

import scraper



def _on_render_complete(html):
    scraper.parse_tree(html)
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
timer.setInterval(1000 * 60 * 5)
timer.start(1000 * 60 * 5)

sys.exit(app.exec_())

