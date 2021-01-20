import sqlite3
from sqlite3 import Error
import pandas as pd
import re


class SQLiteCon:
    
    def __init__(self,database):
        self.create_connection(database)
        self.createTables("test","Symbol VARCHAR(8) NOT NULL UNIQUE, Price FLOAT NOT NULL")
        #out = self.select_all("test")
        #print(out)

    def create_connection(self, db_file):
        """ create a database connection to a SQLite database """
        self.conn = None
        try:
            #self.conn = sqlite3.connect('file:' + db_file +'?mode=memory&cache=shared')
            self.conn = sqlite3.connect(':memory:')

            print(sqlite3.version)
        except Error as e:
            print(e)




    def createTables(self,table_name, columns):


        cur = self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS test ( Symbol VARCHAR(8) NOT NULL UNIQUE, price VARCHAR(32) NOT NULL);")
        self.conn.commit()

    def select_all(self, table_name):
        #cur = self.conn.cursor()
        #cur.execute('SELECT * FROM ?' , (table_name,))
        #rows = cur.fetchall()
        df = pd.read_sql_query("""select * from """ + table_name, self.conn)
        return df

    def select_Where(self, table_name, whereType, whereValue):
        #cur = self.conn.cursor()
        #cur.execute("SELECT * FROM ? WHERE ?=?", (table_name, whereType,whereValue))
        #rows = cur.fetchall()
        df = pd.read_sql_query("""SELECT * FROM test WHERE Symbol=?""", self.conn, params=(whereValue,))
        return df

    def insert(self,values):
        cur = self.conn.cursor()
        cur.execute("""INSERT INTO test values (?,?)""",values)
        self.conn.commit()

    def createTableOfSymbols(self,data):
        cur = self.conn.cursor()
        cur.execute('CREATE TABLE symbols (Symbol text, Name text, LastSale text, NetChange text, Change text, MarketCap text, Country text, IPOYear text, Volume text, Sector text, Industry text)')
        self.conn.commit()
        data.to_sql("symbols", self.conn, if_exists='replace', index = False)


if __name__ == "__main__":
    sq = SQLiteCon("testDB")

    nasdaqData = pd.read_csv("nasdaq.csv")
    #print(nasdaqData)
    columns = []

    for column in nasdaqData.columns:
        columns = columns + [column.replace('%','').replace(' ','')]
    nasdaqData.columns = columns
    print(nasdaqData.columns)
    sq.createTableOfSymbols(nasdaqData)
    print(sq.select_all("symbols"))

