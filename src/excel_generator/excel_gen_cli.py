#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import click
import openpyxl
from excel_generator import modify_sheet_title, get_columns, format_sheet, create_table_header

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
    click_generate_xlsx()
    