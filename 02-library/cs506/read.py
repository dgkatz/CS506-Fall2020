import csv


class ReadCSVError(Exception):
    """Raised when read_csv() fails to parse csv file."""


def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    csv_rows = []
    try:
        with open(csv_file_path) as csv_file:
            csv_reader = csv.reader(csv_file)
            for csv_row in csv_reader:
                csv_row = [parse_string(val) for val in csv_row]
                csv_rows.append(csv_row)
    except Exception as exc:
        raise ReadCSVError(exc)
    
    return csv_rows


def parse_string(s: str):
    if s.isnumeric():
        try:
            return int(s)
        except ValueError:
            return float(s)
    return s
