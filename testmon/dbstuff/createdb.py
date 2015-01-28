#!/usr/bin/python3.2

# Library to create the data base if it doesn't exists

import sqlite3
conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()

# Create the tables
# Unit table
c.execute('''CREATE TABLE units (
      unitid INTEGER PRIMARY KEY ,
      unit TEXT,
      unitL TEXT,
      dimension TEXT,
      dimensionL TEXT,
      scale INTEGER)''')

# Sensor table
c.execute('''CREATE TABLE sensors (
      sensorid INTEGER PRIMARY KEY AUTOINCREMENT,
      type TEXT,
      name TEXT,
      description TEXT,
      scale INTEGER,
      idlemax INTEGER,
      unit TEXT, FOREIGN KEY(unit) REFERENCES units(unitid) )''')

# Measurement table
c.execute('''CREATE TABLE sensordata (
      sensor INTEGER,
      meas INTEGER, 
      time INTEGER,
      FOREIGN KEY(sensor) REFERENCES sensors(sensorid))''')


#insert the units
c.execute("INSERT INTO units VALUES (1, 'mA', 'milli Ampere', 'I', 'Electric Current', -3)");
c.execute("INSERT INTO units VALUES (2, 'A',  'Ampere'      , 'I', 'Electric Current',  1)");
c.execute("INSERT INTO units VALUES (3, 'mV', 'milli Volt'  , 'V', 'Electric Potential', -3)");
c.execute("INSERT INTO units VALUES (4, 'V',  'Volt'        , 'V', 'Electric Potential',  1)");
c.execute("INSERT INTO units VALUES (5, 'C',  'degree Celsius'    , 'T', 'Temperature',  1)");
c.execute("INSERT INTO units VALUES (6, 'F',  'degree Farenheit'  , 'T', 'Temperature',  1)");
c.execute("INSERT INTO units VALUES (7, '%',  'percentage'  , 'CPUload', 'CPU Load',  1)");

#insert the sensors
c.execute("INSERT INTO sensors VALUES (null,'current1', 'main', 'first sensor', 10, 0.1,  1)")
c.execute("INSERT INTO sensors VALUES (null,'cpuload1', 'cpuload', 'first test', 1, 4,    7)")

# Save the changes
conn.commit()

conn.close()
