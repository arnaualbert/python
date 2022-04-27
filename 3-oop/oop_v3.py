'''
Object oriented programing
'''
import sys
import pprint
from pathlib import Path
from typing import List

"""
- This is a copy of tables/2022-01-20-covid-dades/main_v6_comprehensions.py
- I added a conditional at the end 'if __name__ == "__main__"'
  in order to be able to import it from other python files.
"""

# classmethod : 

# -----------------------------------------------------------------------------
class Table:

    # Constructor
    def __init__(self, csv_file_path: str):

        self.data: list[list[str]] = self.read_table(csv_file_path)

    @classmethod
    def admit_list(cls,lista_de_listas: list[list]):
        cls.something = lista_de_listas

    def __str__(self) -> str:
        # return str(self.data)
        result: str = ""
        for row in self.data:
            row_str: str= " ".join(row)
            result = result + f"{row_str}\n"

        return result

    # 1. Read csv file
    # -----------------------------------------------------------------------------
    def read_csv(self, csv_file_path: str) -> str:
        '''Input:  The path to a .csv file.
        Output: The contents of the .csv file as a single string.'''

        raw_text:      str = Path(csv_file_path).read_text()
        stripped_text: str = raw_text.strip()

        return stripped_text


    # 2. Separate by rows
    # -----------------------------------------------------------------------------
    def separate_by_rows(self, contents: str) -> list[str]:
        '''Input:  The file contents as a single string.
            Output: A list of strings where each string is a row of the csv file.'''
        
        rows: list[str] = contents.split("\n")

        return rows


    # 3. Separate by columns
    # -----------------------------------------------------------------------------
    def separate_by_columns(self, rows: list[str]) -> list[list[str]]:
        '''Input:  A list of strings. Each string is a row of a csv file. Row fields are separated by ";".
            Output: A table where each row has been splitted into a list of fields.'''

        table: list[list[str]] = [row.split(";") for row in rows]

        return table


    # -----------------------------------------------------------------------------
    def read_table(self, csv_file_path: str) -> list[list[str]]:
        '''Input:  Path of a .csv file.
        Output: Table as a list of lists of strings with the csv contents.'''

        csv_str: str             = self.read_csv(csv_file_path)
        rows:    list[str]       = self.separate_by_rows(csv_str)
        table:   list[list[str]] = self.separate_by_columns(rows)

        return table


    # -----------------------------------------------------------------------------
    def filter_rows(self, column_name: str, search_str: str):
        '''Input:  Table, columne and search string to filter by. 
        Output: Returns table with rows whose column_name includes search_str. Includes the header.'''

        # Precondition: There is at least a header in the table
        assert len(self.data) >= 1

        # Get the header and data body
        header: list[str]       = self.data[0]
        body:   list[list[str]] = self.data[1:]

        # Precondition: column_name is in the header
        assert column_name in header

        # Find the column index
        column_index: int = header.index(column_name)

        # Filter rows
        filtered_data: list[list[str]] = [row
                                        for row in body
                                        if (search_str in row[column_index]) ]

        # Add header to result
        result: list[list[str]] = [header] + filtered_data

        # Store the data inside the object
        self.data = result


    # -----------------------------------------------------------------------------
    def get_column(self, column_name: str) -> list[str]:
        '''Input:  Column name as a string and Table as a list of lists of strings.
        Output: The column whose name is column_name WITHOUT the header.'''

        # Precondition: There is at least a header in the table
        assert len(self.data) >= 1

        # Get the header and data body
        header: list[str]       = self.data[0]
        body:   list[list[str]] = self.data[1:]

        # Precondition: column_name is in the header
        assert column_name in header

        # Find the column index
        column_index: int = header.index(column_name)

        # Return column
        result: list[str] = [row[column_index] for row in body]

        return result


# PENDING TO MOVE SOMEWHERE ELSE...
# -----------------------------------------------------------------------------
def convert_type_to_int(input_list: list) -> list[int]:
    '''Input:  A list of a certain type.
    Output: The list with all elements converted to new_type.'''

    result: list[int] = [int(elem) for elem in input_list]

    return result


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    table: Table = Table("covid-dades-simple.csv")
    table.filter_rows('NOM', 'ALT CAMP I CONCA DE BARBERÀ')

    dosi2_column_str: list[str] = table.get_column('VACUNATS_DOSI_2')
    dosi2_column_int: list[int] = convert_type_to_int(dosi2_column_str)
    print(dosi2_column_int)

    print(table)

    sys.exit()

    # table:     list[list[str]] = read_table("covid-dades-simple.csv")
    # bcn_table: list[list[str]] = filter_rows(table, 'NOM', 'ALT CAMP I CONCA DE BARBERÀ')

    # dosi1_str_list: list[str]  = get_column(bcn_table, 'VACUNATS_DOSI_1')
    # dosi1_int_list: list[int]  = convert_type_to_int(dosi1_str_list)
    # dosi2_str_list: list[str]  = get_column(bcn_table, 'VACUNATS_DOSI_2')
    # dosi2_int_list: list[int]  = convert_type_to_int(dosi2_str_list)

    # dosi1_total: int = sum(dosi1_int_list)
    # dosi2_total: int = sum(dosi2_int_list)

    # print(set(get_column(bcn_table, 'NOM')))

    # print(f"Total de dosi 1: {dosi1_total}")
    # print(f"Total de dosi 2: {dosi2_total}")

# -----------------------------------------------------------------------------
