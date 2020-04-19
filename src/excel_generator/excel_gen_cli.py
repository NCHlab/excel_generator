#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import click
import openpyxl
from excel_generator import generate_xlsx

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

    generate_xlsx(table_header, filename, filepath, sheetname, rows, columns, accent_type, force_columns, quick_create)
    print(f"Generated {filename}.xlsx")


if __name__ == "__main__":
    click_generate_xlsx()
    