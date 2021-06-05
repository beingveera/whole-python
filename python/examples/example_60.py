import cv2
import numpy as np
import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import QImage


class RecordVideo(QtCore.QObject):
    image_data = QtCore.pyqtSignal(np.ndarray)

    def __init__(self, camera_port, parent=None):
        super().__init__(parent)
        self.camera = cv2.VideoCapture(camera_port)
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timerEvent)
        self.timer.start(0)

    def timerEvent(self):
        read, data = self.camera.read()
        if read:
            self.image_data.emit(data)


class VideoWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image = QImage()

    def image_data_slot(self, image_data):
        if (self.width() > self.height()) != (image_data.shape[1] > image_data.shape[0]):
            # Need to rotate image data, the screen / camera is rotated
            image_data = cv2.rotate(image_data, cv2.ROTATE_90_COUNTERCLOCKWISE)
        self.image = self.get_qimage(image_data)
        self.update()

    def get_qimage(self, image):
        height, width, colors = image.shape
        image = QImage(image.data, width, height, 3 * width, QImage.Format_RGB888).rgbSwapped()
        return image

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)

        w = self.width()
        h = self.height()
        cw = self.image.width()
        ch = self.image.height()

        # Keep aspect ratio
        if ch != 0 and cw != 0:
            w = min(cw * h / ch, w)
            h = min(ch * w / cw, h)
            w, h = int(w), int(h)

        painter.drawImage(QtCore.QRect(0, 0, w, h), self.image)
        self.image = QImage()


class MainWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.video_widget = VideoWidget()
        # 0 is used for rear camera
        self.record_video = RecordVideo(0)
        self.record_video.image_data.connect(self.video_widget.image_data_slot)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.video_widget)
        self.video_widget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        options = QtWidgets.QVBoxLayout()

        af = QtWidgets.QCheckBox("Autofocus")
        af.setChecked(True)
        af.stateChanged.connect(self.onFocus)

        fslider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        fslider.valueChanged.connect(self.onSliderFocus)
        # From 0 to 10
        fslider.setRange(0, 100)
        fslider.setSingleStep(1)

        options.addWidget(af)
        options.addWidget(QtWidgets.QLabel("Manual focus"))
        options.addWidget(fslider)

        ae = QtWidgets.QCheckBox("Autoexposure")
        ae.setChecked(True)
        ae.stateChanged.connect(self.onExposure)

        eslider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        eslider.valueChanged.connect(self.onSliderExposure)
        # From 0 to 0.5 second
        eslider.setRange(0, 100)
        eslider.setSingleStep(1)

        options.addWidget(ae)
        options.addWidget(QtWidgets.QLabel("Manual exposure"))
        options.addWidget(eslider)

        torch = QtWidgets.QCheckBox("Torch")
        torch.stateChanged.connect(self.onTorch)
        options.addWidget(torch)

        layout.addLayout(options)
        self.setLayout(layout)

    def onFocus(self, state):
        self.record_video.camera.set(cv2.CAP_PROP_AUTOFOCUS, float(state == QtCore.Qt.Checked))

    def onSliderFocus(self, value):
        self.record_video.camera.set(cv2.CAP_PROP_FOCUS, value / 10.)

    def onExposure(self, state):
        self.record_video.camera.set(cv2.CAP_PROP_AUTO_EXPOSURE, float(state == QtCore.Qt.Checked))

    def onSliderExposure(self, value):
        self.record_video.camera.set(cv2.CAP_PROP_EXPOSURE, value / 200.)

    def onTorch(self, state):
        self.record_video.camera.set(cv2.CAP_PROP_ANDROID_FLASH_MODE, cv2.CAP_ANDROID_FLASH_MODE_ON if state == QtCore.Qt.Checked else cv2.CAP_ANDROID_FLASH_MODE_OFF)


app = QtWidgets.QApplication(sys.argv)
main_window = QtWidgets.QMainWindow()
main_widget = MainWidget()
main_window.setCentralWidget(main_widget)
main_window.show()
sys.exit(app.exec_())
