import sqlite3
from project import create_db_tables
from project import copy_client_personal_info_from_excel_and_insert_into_db
from project import create_not_added_clients_msg
from openpyxl import Workbook

def test_create_db_tables():
     # Create a database in memory
    conn = sqlite3.connect(':memory:') 
    cursor = conn.cursor()
    create_db_tables(cursor)

    # Check if the table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Client_info';")
    assert cursor.fetchone() is not None
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Dyno_measurments';")
    assert cursor.fetchone() is not None
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Caliper_measurments';")
    assert cursor.fetchone() is not None
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Branch';")
    assert cursor.fetchone() is not None
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Trainer_info';")
    assert cursor.fetchone() is not None
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Trainers';")
    assert cursor.fetchone() is not None
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='_3BTrainersOfClients_';")
    
    conn.close()


def test_copy_client_personal_info_from_excel():
    # Create a workbook and worksheet with some test data
    wb = Workbook()
    ws = wb.active
    ws.append(["Date", "Name", "Phone", "Age", "Height", "Weight", "Activity"])
    ws.append(["2023-10-27", "SKIP_row", "1234567890", "30", "180", "80", "Active"])
    ws.append(["2023-10-27", "SKIP_row", "12345673490", "30", "180", "80", "Active"])
    ws.append(["2023-10-27", "SKIP_row", "12342367890", "30", "180", "80", "Active"])
    ws.append(["2023-10-27", "BEBE Doe", "1243567890", "30", "180", "80", "Active"])
    ws.append(["2023-10-27", "SESE Doe", "12324567890", "30", "180", "80", "Active"])
    ws.append(["2023-10-27", "DEDE Doe", "1234327890", "30", "180", "80", "Active"])
    ws.append(["2023-10-27", "EFE Doe", "1235467890", "30", "180", "80", "Active"])
    ws.append(["2023-10-27", "NENE Doe", None, "25", "170", "60", "Inactive"])

    # Create a database in memory
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Create the tablew
    create_db_tables(cursor)

    # Call the function with the tesst data
    date, listOfClientsWithoutPhoneNumbers = copy_client_personal_info_from_excel_and_insert_into_db(ws, cursor)

    # Check the return values
    assert date == "2023-10-27"
    assert listOfClientsWithoutPhoneNumbers == ["NENE Doe"]

    # Checc the data in the database
    cursor.execute("SELECT Name, Phone_no FROM Client_info;")
    data = cursor.fetchall()
    print(data)
    assert data == [('BEBE Doe', '1243567890'), ('SESE Doe', '12324567890'), ('DEDE Doe', '1234327890'), ('EFE Doe', '1235467890'), ('NENE Doe', None)]

    conn.close()

def test_create_not_added_clients_msg():
    listOfClientsWithoutPhoneNumbers = ["Tairq", "Michael"]
    assert create_not_added_clients_msg(listOfClientsWithoutPhoneNumbers) == f"Error: The Following Clients (['Tairq', 'Michael']) couldn't be found in database, and didnot got inserted into it !.\nExiting system..."
