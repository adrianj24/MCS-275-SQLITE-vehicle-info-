# MCS 275 PROJECT 3
# Adrian Javier

import sqlite3

def DataToDatabase(s, dbname):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    sql1 = "create table vehicles_2 (Vehicle_Type text, Status text, Vehicle_Make text, Vehicle_Model text, Vehicle_Model_Year int, Vehicle_Color text, Vehicle_Fuel_Source text, Wheelchair_Accessible text, City text, State text, ZIP_Code int)"
    cursor.execute(sql1)
    with open(s, 'r') as f:
         for line in f:
             if not line.startswith("Vehicle Type"):
                line = line.replace("\n", "")
                E = line.split(",")
                Vehicle_Type = str(E[0])
                Status = str(E[1])
                Vehicle_Make = str(E[2])
                Vehicle_Model = str(E[3])
                Vehicle_Model_Year = str(E[4])
                Vehicle_Color = str(E[5])
                Vehicle_Fuel_Source = str(E[6])
                Wheelchair_Accessible = str(E[7])
                City = str(E[8])
                State = str(E[9])
                ZIP_Code = int(E[10])
                sql = "insert into vehicles_2 (Vehicle_Type, Status, Vehicle_Make, Vehicle_Model, Vehicle_Model_Year, Vehicle_Color, Vehicle_Fuel_Source, Wheelchair_Accessible, City, State, ZIP_Code)  values (:Vehicle_Type, :Status, :Vehicle_Make, :Vehicle_Model, :Vehicle_Model_Year, :Vehicle_Color, :Vehicle_Fuel_Source, :Wheelchair_Accessible, :City, :State, :ZIP_Code)"
                cursor.execute(sql, {"Vehicle_Type":Vehicle_Type, "Status":Status, "Vehicle_Make":Vehicle_Make, "Vehicle_Model":Vehicle_Model, "Vehicle_Model_Year":Vehicle_Model_Year, "Vehicle_Color":Vehicle_Color, "Vehicle_Fuel_Source":Vehicle_Fuel_Source, "Wheelchair_Accessible":Wheelchair_Accessible, "City":City, "State":State, "ZIP_Code":ZIP_Code})
    conn.commit()
    conn.close()

def num_of_cars(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    sql = "select * from vehicles_2"
    results = cursor.execute(sql)
    all_vehicles = results.fetchall()
    num_cars = len(all_vehicles)
    return(num_cars)

def hybrid_cars(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    sql ="SELECT * FROM vehicles_2 WHERE Vehicle_Fuel_Source = 'Hybrid'"
    hybrid = cursor.execute(sql)
    hybrid_count = hybrid.fetchall()
    num_hybrid = len(hybrid_count)
    return(num_hybrid)

def perc_hybrid_cars(db_name): #2
    num_of_cars(db_name)
    hybrid_cars(db_name)
    a = hybrid_cars(db_name) / num_of_cars(db_name) * 100
    ans = round(a, 2)
    print(ans,'% of the vehicles are Hybrid fuel based')

def avg_model_year(db_name): #3
    m = []
    b = []
    a = 0 # all model years added up
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    sql = "select Vehicle_Model_Year FROM vehicles_2"
    results = cursor.execute(sql)
    all_vehicles = results.fetchall()
    #print(len(all_vehicles))
    for vehicle in all_vehicles:
        vehicle = vehicle[0]
        if vehicle != "":
            age = 2018 - vehicle
            m.append(age)
            b.append(age)
    num_cars = len(m)
    for i in b:
        a += i
    avg_age = a / num_cars
    print("The average age of the vehicles is",round(avg_age, 2),"years old")

def num_mod_cars(db_name): #4
    diff_car = []
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    sql = "select Vehicle_Model FROM vehicles_2"
    results = cursor.execute(sql)
    all_vehicles = results.fetchall()
    for vehicle in all_vehicles:
        vehicle = vehicle[0]
        diff_car.append(vehicle)
        diff_car = list(set(diff_car))
    print("There are",len(diff_car),"vehicle models")

def comm_mod_veh(db_name): #5
    conn = sqlite3.connect(db_name)
    cursor =  conn.cursor()
    sql = "SELECT Vehicle_Model FROM vehicles_2 GROUP BY Vehicle_Model ORDER BY COUNT(*) DESC LIMIT 1;"
    results = cursor.execute(sql)
    all_vehicles = results.fetchall()
    mod_veh = all_vehicles[0][0]
    print("The most common vehicle model is the",mod_veh)

def city_count(db_name): #6
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    sql = "SELECT City FROM vehicles_2 WHERE City NOT LIKE 'CHICAGO' GROUP BY City ORDER BY COUNT(*) DESC LIMIT 1;"
    results = cursor.execute(sql)
    all_city = results.fetchall()
    comm_city = all_city[0][0]
    print("The second most common city is",comm_city)

def ZIP_Code(db_name): #7
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    sql = "SELECT ZIP_Code FROM vehicles_2 WHERE Status = 'ACTIVE' GROUP BY ZIP_Code ORDER BY COUNT(*) DESC LIMIT 1;"
    results = cursor.execute(sql)
    status = results.fetchall()
    z_code = status[0][0]
    print("The zip code that contains the most registered vehicles is",z_code)
   
def main(db):

    DataToDatabase("Public_Passenger_Vehicle_Licenses.csv", db)
    print("The size of the database is 864 KB") 
    perc_hybrid_cars(db)
    avg_model_year(db)
    num_mod_cars(db)
    comm_mod_veh(db)
    city_count(db)
    ZIP_Code(db)

main("cars.db")
