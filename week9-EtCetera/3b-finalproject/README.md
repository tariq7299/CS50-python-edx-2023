# YOUR PROJECT TITLE
#### Video Demo:  <https://youtu.be/u8fkw6ZgKUs>
#### Description:

A note about the excell file I have attached *members_data.xlsx* --> This is a excel file to test my program

This prorgram copies the content of excell files and then insert it into a sqlite data base  

I created it becasue as i needed to store data of customers of my company into somthing more relieble and effiencitnt than a axcell sheet so. (I work at health center, and the data I want to copy represents some fintenss and body measuruments info for our members)

First I have stored all the customers info in an excell sheet.

Then I used `openpyxl` to copy excell data from the sheets to my program.

**The following are steps I took in my code**
First I loaded the excell file, and created an instance of the workbook using `openpyxl.load_workbook('excell_file')`

Then I have created an instance of the sheet that contains the data

Then I have created the sqlite tables of my database using create_db_tables() function

the schema is :

```

    CREATE TABLE Client_info (
                        Client_id INTEGER NOT NULL,
                        Name TEXT,
                        Phone_no TEXT UNIQUE,
                        AGE TEXT,
                        Height REAL,
                        Weight REAL,
                        Activity TEXT,
                        ID_card_no TEXT UNIQUE,
                        PRIMARY KEY (Client_id)
                        );
CREATE TABLE Dyno_measurments (
                        Dyno_id INTEGER NOT NULL,
                        Client_id INTEGER,
                        Date NUMERIC, 
                        Energy_src_from_protein__percent TEXT,
                        Energy_src_from_carbs__percent TEXT,
                        Energy_src_from_fat__percent TEXT,
                        BMR_analysis_value__kcal TEXT,
                        BMR_ruleOfThumb__kcal TEXT,
                        BMR_calorie_requirment__kcal TEXT,
                        Combustion_perDay__kcal TEXT,
                        Calorie_consumption_through_activities__kcal TEXT,
                        PRIMARY KEY (Dyno_id),
                        FOREIGN KEY (Client_id) REFERENCES Client_info(Client_id)
                        );
CREATE TABLE Caliper_measurments (
                        Caliper_id INTEGER NOT NULL,
                        Client_id INTEGER,
                        Date NUMERIC, 
                        Chest__mm TEXT,
                        Scapula__mm TEXT,
                        Axilla__mm TEXT,
                        Triceps__mm TEXT,
                        Abdominal__mm TEXT,
                        Suprailiac__mm TEXT,
                        Thigh__mm TEXT,
                        Body_fat__percent TEXT,
                        Max_preferred_level__percent TEXT,
                        LBM__Lean_body_mass__kg TEXT,
                        FBM__Fat_body_mass__kg TEXT,
                        BMI__Body_mass_index__kg TEXT,
                        BMR__Bascal_metabolic_rate__kcal TEXT,
                        PRIMARY KEY (Caliper_id),
                        FOREIGN KEY (Client_id) REFERENCES Client_info(Client_id)
                        );
CREATE TABLE Branch (
                        Client_id INTEGER,
                        Branch_name TEXT,
                        FOREIGN KEY (Client_id) REFERENCES Client_info(Client_id)
                        );
CREATE TABLE Trainer_info (
                        Trainer_id INTEGER NOT NULL,
                        Trainer_system_name TEXT UNIQUE,
                        branchOfTrainer TEXT,
                        PRIMARY KEY (Trainer_id)
                        );
CREATE TABLE Trainers (
                        Trainer_id INTEGER,
                        Client_id INTEGER,
                        FOREIGN KEY (Trainer_id) REFERENCES Trainer_info(Trainer_id),
                        FOREIGN KEY (Client_id) REFERENCES Client_info(Client_id)
                        PRIMARY KEY (Trainer_id, Client_id)
                );
CREATE TABLE _3BTrainersOfClients_ (
                        Client_id INTEGER NOT NULL,
                        Trainer_system_name TEXT,
                        branchOfTrainer TEXT,
                        FOREIGN KEY (Client_id) REFERENCES Client_info(Client_id)
                        );
```

Then I copied the excell cells which contains the customers personal info into variables, then inserted those varibles into my database using the function `copy_client_personal_info_from_excel_and_insert_into_db()`

Then copied the excel cells which contains the measuruments of the client into varibles then I inserted it into the db using the function `copy_measurements_from_excel_and_insert()`

Throght out the previous code i tracked every client that didn't got inserted into db (any client that doesno't have a phone number will not be inserted into the db), and store all of them into a list [].

Then I print the `listOfClientsWithoutPhoneNumbers` if it contains data

Finally I populate the tables rest of database tables that did'n't got pou;lated `Trainer_info`, `Trainers`

