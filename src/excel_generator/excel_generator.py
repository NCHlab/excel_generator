#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
import openpyxl
import os
from openpyxl.styles import NamedStyle, PatternFill, Border, Side, Alignment, Protection, Font, colors
from datetime import datetime
# from constant import filepath


def get_headers(columns):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    excel_cols = []

    if columns <= len(alphabet):
        excel_cols += alphabet[:columns]

    elif columns > len(alphabet):
        excel_cols += alphabet

        for j in range(len(alphabet)):
            for k in range(len(alphabet)):
                if len(excel_cols) >= columns:
                    return str(excel_cols[0]),str(excel_cols[-1])

                excel_cols.append(alphabet[j]+alphabet[k])

    return str(excel_cols[0]),str(excel_cols[-1])


def modify_sheet_title(wb, sheetname):
    ws = wb["Sheet"]
    ws.title = sheetname

    return ws


def get_columns(table_header, columns, force_columns, quick_create):
    if force_columns or quick_create:
        cols = columns
    else:
        cols = len(table_header) or columns
    return cols


def format_sheet(ws, rows, cols, accent_type):

    thin = Side(border_style="thin", color="000000")

    for row in ws.iter_rows(min_row=0, min_col=0, max_row=rows, max_col=cols):
        for cell in row:

            if cell.row is 1:
                cell.style = f"60 % - {accent_type}"
            else:
                cell.style = f"20 % - {accent_type}"

            cell.border = Border(left=thin, top=thin, right=thin, bottom=thin)
            cell.font = Font(color=colors.BLACK)

    return ws


def create_table_header(ws, cols, table_header):
    first_col, last_col = get_headers(cols) # column numbers
    for row in ws[f"{first_col}1:{last_col}1"]:
        for i,cell in enumerate(row):
            if i >= len(table_header):
                return ws
            cell.value = table_header[i]
            cell.font = Font(color=colors.BLACK)

    return ws


# Force_columns, incase user wants to input some column names and leave formatted table space for more
def generate_xlsx(table_header, filename, filepath=None, sheetname="Sheet1", rows=4, columns=5, AccentType="Accent1", force_columns=False, quick_create=False):

    wb = openpyxl.Workbook()
    ws = modify_sheet_title(wb, sheetname)
    cols = get_columns(table_header, columns, force_columns, quick_create)
    ws = format_sheet(ws, rows, cols, AccentType)

    if quick_create:
        wb.save(filepath)
        return

    if table_header:
        ws = create_table_header(ws, cols, table_header)

    wb.save(filepath)


@click.command()
@click.option("--table_header", "-th")
@click.option("--filename", "-f", default="excel_gen")
@click.option("--filepath", "-p", default=None)
@click.option("--quick_create", "-qc")
@click.option("--sheetname", "-s", default="Sheet1")
@click.option("--rows", "-r", default=4)
@click.option("--columns", "-c", default=5)
@click.option("--accent_type", "-ac", default="Accent1")
@click.option("--force_columns", "-fc", default=False)
def click_generate_xlsx(table_header, filename, filepath=None, sheetname="Sheet1", rows=4, columns=5, accent_type="Accent1", force_columns=False, quick_create=False):

    if filename:
        if "xlsx" not in filename:
            filename += ".xlsx"

    if not filepath:
        filepath = os.path.join(os.getcwd())

    if type(table_header) == str:
        table_header = table_header.split(",")
        table_header = list(map(lambda x: x.strip(), table_header))

    wb = openpyxl.Workbook()
    ws = modify_sheet_title(wb, sheetname)
    cols = get_columns(table_header, columns, force_columns, quick_create)
    ws = format_sheet(ws, rows, cols, accent_type)

    if quick_create:
        wb.save(f"{filepath}/{filename}")
        return

    if table_header:
        ws = create_table_header(ws, cols, table_header)

    wb.save(f"{filepath}/{filename}")


if __name__ == "__main__":
    data = ["House", "Location", "Price", "Bedrooms"]
    click_generate_xlsx()