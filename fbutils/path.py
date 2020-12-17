import re
from datetime import datetime


def get_file_dates(files: list,
                   date_exp: str = r'\d{4}_\d{2}_\d{2}_\d{4}',
                   date_format: str = '%Y_%m_%d_%H%M') -> list:
    """Get a list of all dates from date-names files in a directory.

    Args:
        path (str): Target directory.
        date_exp (str): Date regex.
        date_format (str): Date format.
        file_suffix (str): File suffix.

    Returns:
        list: List of dates extracted from file names.

    """

    # Compile date matching regex
    date_exp = re.compile(date_exp)

    # Extract date strings
    file_dates = [date_exp.search(x).group() for x in files]

    # Gxtract date values from date strings
    file_dates = [datetime.strptime(x, date_format) for x in file_dates]

    return file_dates
