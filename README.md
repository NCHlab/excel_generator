# Excel Generator


This is a quick excel generator, GUI created using PySide2 GUI library.

This tool allows for quick generation of basic excel sheet formatted into a table.

(The primary object of this project is to learn how to use QT5 / PySide2 Library to create a GUI interface)

## CLI Tool

The CLI version allows for the program to be executed via a Terminal.

```bash
python excel_generator.py -f "Houses" -p "PATH\Where\To\Save" -th "Table, Header, names, seperated, by, a, comma" -ac Accent2
```

| Argument        | Alias | Help                                                                 | Default Value             |
|-----------------|-------|----------------------------------------------------------------------|---------------------------|
| --table_header  | -th   | Column Table Names e.g "Car Make, Model, Year, Price"                |                           |
| --filename      | -f    | Name of the file to be created                                       | Sheet1                    |
| --filepath      | -p    | Location where file should be saved                                  | Same place as file called |
| --sheetname     | -s    | Name of the Excel Sheet                                              | Sheet1                    |
| --rows          | -r    | \<Num>                                                               | 4                         |
| --columns       | -c    | \<Num>                                                               | 5                         |
| --accent_type   | -ac   | Accent Types  (Accent1 - 5 exist)                                    | Accent1                   |
| --quick_create  | -qc   | Allows for quick generation of file (uses most defaults)             | False                     |
| --force_columns | -fc   | Enables for more cols to be created than table header names provided | False                     |
