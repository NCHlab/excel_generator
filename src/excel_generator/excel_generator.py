#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import requests
import openpyxl
from openpyxl.styles import NamedStyle, PatternFill, Border, Side, Alignment, Protection, Font, colors
# from openpyxl import load_workbook
from datetime import datetime
from constant import filepath

fill = PatternFill(fill_type="solid",
                    start_color='FFFFFFFF',
                    end_color='FF000000')

# {'lightDown', 'solid', 'darkDown', 'darkTrellis',
# 'gray0625', 'darkGray', 'darkGrid', 'lightHorizontal',
# 'lightGray', 'lightUp', 'darkHorizontal', 'mediumGray',
# 'darkUp', 'lightTrellis', 'darkVertical', 'lightGrid', 'lightVertical', 'gray125'}

# highlight = NamedStyle(name="Accent1")
# highlight.font = Font(bold=True, size=20)
# bd = Side(style='thick', color="3480eb")

thin = Side(border_style="thin", color="000000")

# black.font = Font(color='00FF0000', italic=True

# highlight.border = Border(left=Side(border_style=None,
#                               color='FF000000'),
#                     right=Side(border_style=None,
#                                color='FF000000'),
#                     top=Side(border_style=None,
#                              color='FF000000'),
#                     bottom=Side(border_style=None,
#                                 color='FF000000')
#                    )
# highlight.border = Border(left=thin, top=thin, right=thin, bottom=thin)

def get_headers(columns):
    basic_alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    excel_cols = []
    # columns = 26
    for i in range(columns):

        if i <= 25:
            excel_cols.append(basic_alpha[i])

        if i > 25:
            for j in range(len(basic_alpha)):
                for k in range(len(basic_alpha)):

                    if len(excel_cols) >= columns:
                        break

                    excel_cols.append(basic_alpha[j]+basic_alpha[k])

    return str(excel_cols[0]),str(excel_cols[-1])
            
# print(get_headers(310))


# print(excel_cols)

# exit()

def generate_xlsx(custom_header, rows=4, columns=5, force_columns=False):

    wb = openpyxl.load_workbook(filepath)
    ws = wb["Sheet1"]
    # red_font = Font(color='00FF0000', italic=True)
    # for cell in ws["2:5"]:
    #     cell.style = "Accent1"
    if force_columns:
        cols = columns
    else:
        cols = len(custom_header) or columns


    for row in ws.iter_rows(min_row=0, min_col=0, max_row=rows, max_col=cols):
        for cell in row:

            if cell.row is 1:
                cell.style = "60 % - Accent1"
            else:
                cell.style = "20 % - Accent1"

            cell.border = Border(left=thin, top=thin, right=thin, bottom=thin)
            cell.font = Font(color=colors.BLACK)
            # cell.border = Border(left=thin, top=thin, right=thin, bottom=thin)
            # print(dir(cell))
            # # print(cell.coordinate)
            # print(cell.style)
            # print(cell.column)
            # cell.value="test"
            # wb.save("D:\\User.ADMIN\\Desktop\\Projects\\excel_generator\\excelfile.xlsx")
            # exit()
    if custom_header:
        first_col, last_col = get_headers(cols) # column numbers
        for row in ws[f"{first_col}1:{last_col}1"]:
            for i,cell in enumerate(row):
                # print(i)
                cell.value = custom_header[i]
                cell.font = Font(color=colors.BLACK)



    # # filepath = input("Enter Filepath")
    # wb = openpyxl.Workbook()
    # # wb.add_named_style(highlight)

    # ws1 = wb['Sheet']
    # ws1.title = 'TITLE'

    # # ws1['A1'].fill = fill
    # ws1['A1'].style = highlight
    # # ws1['A1'].style = "Accent1"
    # # ws1['A1'].border = Border(left=thin, top=thin, right=thin, bottom=thin)
    # ws1['A2'].style = "20 % - Accent1"
    # ws1['A3'].style = "40 % - Accent1"
    # ws1['A4'].style = "60 % - Accent1"
    # # ws1.save("file.xlsx")

    # # ws1 = wb.create_sheet("TITLE")
    # # ws1.title = "Title_A"






    wb.save(filepath)




if __name__ == "__main__":
    data = ["House", "Location", "Price", "Bedrooms"]
    generate_xlsx(custom_header=data)

















# from PySide2 import QtCore, QtWidgets, QtGui


# Form, Window = uic.loadUiType("dialog.ui")

# app = QApplication([])
# window = Window()
# form = Form()
# form.setupUi(window)
# window.show()
# app.exec_()

# import sys
# import random
# from PySide2 import QtCore, QtWidgets, QtGui

# class MyWidget(QtWidgets.QWidget):
#     def __init__(self):
#         QtWidgets.QWidget.__init__(self)
        
#         self.hello = ["Hallo Welt", "你好，世界", "Hei maailma",
#             "Hola Mundo", "Привет мир"]

#         self.button = QtWidgets.QPushButton("Click me!")
#         self.text = QtWidgets.QLabel("Hello World")
#         self.text.setAlignment(QtCore.Qt.AlignCenter)

#         self.layout = QtWidgets.QVBoxLayout()
#         self.layout.addWidget(self.text)
#         self.layout.addWidget(self.button)
#         self.setLayout(self.layout)

#         self.button.clicked.connect(self.magic)


#     def magic(self):
#         self.text.setText(random.choice(self.hello))


# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)

#     widget = MyWidget()
#     widget.show()

#     sys.exit(app.exec_())