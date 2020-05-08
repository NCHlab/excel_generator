import os
import sys
from PySide2 import QtCore, QtWidgets, QtGui
import webbrowser

from datetime import datetime

from gui import main
from excel_generator import generate_xlsx


class MyQtApplication(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApplication, self).__init__()
        self.setupUi(self)
        self.setup_icon()
        self.setWindowTitle("Excel Generator - v1.1")
        self.populate_cols()
        self.populate_rows()
        self.filename_form()

        # Buttons
        self.filepath_TB.clicked.connect(self.filepath_selector)
        self.create_PB.clicked.connect(self.create_excel)
        self.quickcreate_PB.clicked.connect(self.quick_create_excel)
        self.cancel_PB.clicked.connect(lambda x: sys.exit(0))

        # File Menu
        self.create_ACTION.triggered.connect(self.create_excel)
        self.quickcreate_ACTION.triggered.connect(self.quick_create_excel)
        self.exit_ACTION.triggered.connect(lambda x: sys.exit(0))

        self.clearfields_ACTION.triggered.connect(self.clear_fields)

    def setup_icon(self):
        app_icon = QtGui.QIcon()
        app_icon.addFile("gui/xcel_gen.png", QtCore.QSize(256, 256))
        app.setWindowIcon(app_icon)

    def clear_fields(self):
        self.filename_LE.clear()
        self.filepath_LE.clear()
        self.sheetname_LE.clear()
        self.headers_LE.clear()

    def populate_cols(self):
        self.cols_CB.clear()

        for num in range(1, 101):
            self.cols_CB.addItem(str(num))

    def populate_rows(self):
        self.rows_CB.clear()

        for num in range(2, 101):
            self.rows_CB.addItem(str(num))

    def filename_form(self):
        text = self.filename_LE.text()
        return str(text)

    def sheetname_form(self):
        text = self.sheetname_LE.text()
        if not text:
            text = "Sheet1"
        return str(text)

    def filepath_form(self):
        text = self.filepath_LE.text()
        return str(text)

    def headers_form(self):
        text = self.headers_LE.text()
        return str(text)

    def rows_form(self):
        text = self.rows_CB.currentText()
        return int(text)

    def cols_form(self):
        text = self.cols_CB.currentText()
        return int(text)

    def accent_form(self):
        text = self.accenttype_CB.currentText()
        return str(text)

    def filepath_selector(self):
        filepath = QtWidgets.QFileDialog.getExistingDirectory(self, "Select directory")
        if filepath:
            self.filepath_LE.setText(filepath)

    def force_cols_checkbox(self):
        checked = self.checkBox.isChecked()
        return checked

    def create_excel(self):
        filename = self.filename_form()
        if not filename:
            QtWidgets.QMessageBox.critical(
                self, "Filename Required", "Filename was not provided"
            )
            return

        sheetname = self.sheetname_form()

        filepath = self.filepath_form()
        if not filepath:
            QtWidgets.QMessageBox.critical(
                self,
                "Filepath Required",
                "Filepath was not provided.\nPlease select the location for the save file",
            )
            return

        headers = self.headers_form()

        force_columns = self.force_cols_checkbox()
        if not headers:
            force_columns = True

        rows = self.rows_form()
        cols = self.cols_form()
        accept_type = self.accent_form()

        generate_xlsx(
            headers,
            filename,
            filepath=filepath,
            sheetname=sheetname,
            rows=rows,
            columns=cols,
            accent_type=accept_type,
            force_columns=force_columns,
            quick_create=False,
        )

        openfilepath = QtWidgets.QMessageBox.question(
            self,
            "Created",
            f"Excel File Created: {filename}.xlsx\nLocation: {filepath}\n\nOpen location of file?",
        )

        if openfilepath == (QtWidgets.QMessageBox.Yes):
            webbrowser.open("file:///" + filepath)

    def quick_create_excel(self):

        filepath = self.filepath_form()
        if not filepath:
            filepath = os.path.join(os.getcwd())

        now = datetime.now()
        current_time = now.strftime("%d_%m_%Y %H_%M_%S")

        filename = f"Excel_Sheet_{current_time}"

        accept_type = self.accent_form()

        generate_xlsx(
            table_header="",
            filename=filename,
            filepath=filepath,
            accent_type=accept_type,
            force_columns=True,
            quick_create=True,
        )

        openfilepath = QtWidgets.QMessageBox.question(
            self,
            "Created",
            f"Excel File Created: {filename}.xlsx\nLocation: {filepath}\n\nOpen location of file?",
        )

        if openfilepath == (QtWidgets.QMessageBox.Yes):
            webbrowser.open("file:///" + filepath)


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    qt_app = MyQtApplication()
    qt_app.show()

    app.exec_()
