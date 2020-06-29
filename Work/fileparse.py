# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_error=False):
    '''
    Parse a CSV file into a list of records
    '''

    # raise exception if both select and has_headers differ from their default values
    if not has_headers and select:
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(lines, delimiter=delimiter)

    # read headers (if any)
    headers = next(rows) if has_headers else []

    # set headers to a specific selection
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):

        # skip rows without data
        if not row:
            continue

        # filter the row if specific columns were selected
        if select:
            row = [row[index] for index in indices]

        # convert to provided types
        if types:

            # try to convert values
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_error:
                    print(f"Row {rowno}: Couldn't convert {row}")
                    print(f"Row {rowno}: Reason {e}")
                continue

        # make a dictionary
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)

        records.append(record)

    return records
