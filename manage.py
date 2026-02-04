import sys
import os
import shutil
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QDialog, QFileDialog

global source_directory
global destination_directory
source_directory = ""
destination_directory = ""

def main():
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main_window.setWindowTitle("FileManager")
    main_window.setGeometry(0, 0, 800, 600)
    main_window.setStyleSheet("background-color: lightgray;")

    titleLabel = QLabel("FileManager", main_window)
    titleLabel.setGeometry(350, 50, 200, 50)
    titleLabel.setStyleSheet("font-size: 24px; font-weight: bold;")

    def require_dirs(action):
        def wrapper():
            src = sourceDirectoryInput.text().strip()
            dst = destinationDirectoryInput.text().strip()
            print(f"require_dirs: src={src!r}, dst={dst!r}")
            if not src or not dst:
                warning = QDialog(main_window)
                warning.setWindowTitle("ERROR: No Directory Set")
                warning.setGeometry(200, 200, 400, 200)
                warningLabel = QLabel("Please set both source and destination directories before proceeding.", warning)
                warningLabel.setGeometry(20, 50, 360, 100)
                warning.exec_()
                return
            if not os.path.isdir(src):
                warning = QDialog(main_window)
                warning.setWindowTitle("ERROR: Source Missing")
                warning.setGeometry(200, 200, 400, 200)
                warningLabel = QLabel("Source directory does not exist. Please check the path.", warning)
                warningLabel.setGeometry(20, 50, 360, 100)
                warning.exec_()
                return
            if not os.path.isdir(dst):
                warning = QDialog(main_window)
                warning.setWindowTitle("ERROR: Destination Missing")
                warning.setGeometry(200, 200, 400, 200)
                warningLabel = QLabel("Destination directory does not exist. Please check the path.", warning)
                warningLabel.setGeometry(20, 50, 360, 100)
                warning.exec_()
                return
            # Update global paths so action uses current values
            setSourceDirectory(src)
            setDestinationDirectory(dst)
            try:
                action()
            except Exception as e:
                print("Action error:", e)
                err = QDialog(main_window)
                err.setWindowTitle("ERROR: Operation Failed")
                err.setGeometry(200, 200, 400, 200)
                errLabel = QLabel(str(e), err)
                errLabel.setGeometry(20, 50, 360, 100)
                err.exec_()
        return wrapper

    pdfButton = QPushButton("Move PDFs", main_window)
    pdfButton.setGeometry(175, 300, 100, 60)
    pdfButton.clicked.connect(require_dirs(pdfManage))

    imgButton = QPushButton("Move Images", main_window)
    imgButton.setGeometry(275, 300, 100, 60)
    imgButton.clicked.connect(require_dirs(imgManage))

    vidButton = QPushButton("Move Videos", main_window)
    vidButton.setGeometry(375, 300, 100, 60)
    vidButton.clicked.connect(require_dirs(vidManage))

    musicButton = QPushButton("Move Music", main_window)
    musicButton.setGeometry(475, 300, 100, 60)
    musicButton.clicked.connect(require_dirs(musicManage))

    appButton = QPushButton("Move Apps", main_window)
    appButton.setGeometry(575, 300, 100, 60)
    appButton.clicked.connect(require_dirs(appManage))

    def browseSourceSourceDirectory():
        selected = QFileDialog.getExistingDirectory(main_window, "Select Source Directory")
        if selected:
            setSourceDirectory(selected)
            sourceDirectoryInput.setText(selected)
    def browseDestinationDestinationDirectory():
        selected = QFileDialog.getExistingDirectory(main_window, "Select Destination Directory")
        if selected:
            setDestinationDirectory(selected)
            destinationDirectoryInput.setText(selected)

    sourceDirectoryLabel = QLabel("Source Directory: ", main_window)
    sourceDirectoryLabel.setGeometry(100, 150, 150, 30)
    sourceDirectoryInput = QLineEdit(main_window)
    sourceDirectoryInput.setGeometry(220, 150, 300, 30)
    sourceDirectoryInput.setStyleSheet("background-color: #FFFFFF;")
    sourceDirectoryBrowseButton = QPushButton("Set Source Directory", main_window)
    sourceDirectoryBrowseButton.setGeometry(520, 150, 150, 30)
    sourceDirectoryBrowseButton.clicked.connect(browseSourceSourceDirectory)
    sourceDirectoryInput.textChanged.connect(lambda text: setSourceDirectory(text))

    destinationDirectoryLabel = QLabel("Destination Directory: ", main_window)
    destinationDirectoryLabel.setGeometry(100, 200, 150, 30)
    destinationDirectoryInput = QLineEdit(main_window)
    destinationDirectoryInput.setGeometry(220, 200, 300, 30)
    destinationDirectoryInput.setStyleSheet("background-color: #FFFFFF;")
    destinationDirectoryBrowseButton = QPushButton("Set Destination Directory", main_window)
    destinationDirectoryBrowseButton.setGeometry(520, 200, 150, 30)
    destinationDirectoryBrowseButton.clicked.connect(browseDestinationDestinationDirectory)
    destinationDirectoryInput.textChanged.connect(lambda text: setDestinationDirectory(text))

    main_window.show()
    sys.exit(app.exec_())


def setSourceDirectory(text):
    global source_directory
    global destination_directory
    source_directory = text
    destination_directory = text
    
def setDestinationDirectory(text):
    global destination_directory
    destination_directory = text


def pdfManage():
    print("MANAGING PDFs")
    for filename in os.listdir(source_directory):
        if filename.endswith('.pdf'):
            source_path = os.path.join(source_directory, filename)
            destination_path = os.path.join(destination_directory, filename)
            
            if os.path.isfile(source_path):
                shutil.move(source_path, destination_path)
            print(f'Moved: {filename}')

def imgManage():
    print("MANAGING IMAGES")
    for filename in os.listdir(source_directory):
        if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg') or filename.endswith('.gif') or filename.endswith('.JPG'):
            source_path = os.path.join(source_directory, filename)
            destination_path = os.path.join(destination_directory, filename)
            
            if os.path.isfile(source_path):
                shutil.move(source_path, destination_path)
            print(f'Moved: {filename}')

def vidManage():
    print("MANAGING VIDEOS")
    for filename in os.listdir(source_directory):
        if filename.endswith('.mp4') or filename.endswith('.avi') or filename.endswith('.mov') or filename.endswith('.wmv'):
            source_path = os.path.join(source_directory, filename)
            destination_path = os.path.join(destination_directory, filename)
            
            if os.path.isfile(source_path):
                shutil.move(source_path, destination_path)
            print(f'Moved: {filename}')

def musicManage():
    print("MANAGING MUSIC")
    for filename in os.listdir(source_directory):
        if filename.endswith('.mp3') or filename.endswith('.wav') or filename.endswith('.flac') or filename.endswith('.aac') or filename.endswith('.ogg'):
            source_path = os.path.join(source_directory, filename)
            destination_path = os.path.join(destination_directory, filename)
            
            if os.path.isfile(source_path):
                shutil.move(source_path, destination_path)
            print(f'Moved: {filename}')

def appManage():
    print("MANAGING APPS")
    for filename in os.listdir(source_directory):
        if filename.endswith('.exe') or filename.endswith('.msi') or filename.endswith('.dmg') or filename.endswith('.pkg'):
            source_path = os.path.join(source_directory, filename)
            destination_path = os.path.join(destination_directory, filename)
            
            if os.path.isfile(source_path):
                shutil.move(source_path, destination_path)
            print(f'Moved: {filename}')

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        PyQt5.show_fatal_error(e)
