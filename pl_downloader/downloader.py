import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import urllib.request


class Downloader(QDialog):

    def __init__(self):
        QDialog.__init__(self)

        layout = QVBoxLayout()

        self.url = QLineEdit()
        self.save_location = QLineEdit()
        self.progress = QProgressBar()
        download = QPushButton("Download")
        browse = QPushButton("Browse")
        close_button = QPushButton("Cancel")

        self.url.setPlaceholderText("URL")
        self.save_location.setPlaceholderText("File save location")

        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(browse)
        layout.addWidget(self.progress)
        layout.addWidget(download)
        layout.addWidget(close_button)

        self.setLayout(layout)

        self.setWindowTitle("PyDownloader")
        self.setFocus()

        download.clicked.connect(self.download)
        browse.clicked.connect(self.browse_file)
        close_button.clicked.connect(self.close)

    def browse_file(self):
        save_file = QFileDialog.getSaveFileName(self, caption="Save File As", directory=".",
                                                filter='All Files (*.*)')
        self.save_location.setText(QDir.toNativeSeparators(save_file))

    def download(self):
        url = self.url.text()
        save_location = self.save_location.text()

        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception:
            QMessageBox.warning(self, "Warning", "The download failed")
            return

        QMessageBox.information(self, "information", "The download is complete")
        self.progress.setValue(0)
        self.url.setText("")
        self.save_location.setText("")

    def report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = readsofar * 100 / totalsize
            self.progress.setValue(int(percent))


app = QApplication(sys.argv)
dl = Downloader()
dl.show()
app.exec_()

'''
http://ipv4.download.thinkbroadband.com/10MB.zip

save_file = QFileDialog.QFileDialog(self, caption="Save file As:", directory=".", filter='All Files (*.*)')
self.save_location.setText(save_file)

close_button = QPushButton("Cancel")
close_button.clicked.connect(self.close)
layout.addWidget(close_button)
'''
