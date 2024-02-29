from classes.Drug import Drug
from utils.database_connector import database_connector

while True:
    Drug(database_connector, "Honey Bunny", "Death", "None")