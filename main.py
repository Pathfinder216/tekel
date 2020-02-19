import os
import sys

from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.load(os.path.join("tekel", "main.qml"))

    # QML failed to load, so exit to prevent the app from hanging
    if not engine.rootObjects():
        sys.exit(1)

    sys.exit(app.exec_())
