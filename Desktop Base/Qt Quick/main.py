import sys, os
from PySide6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PySide6.QtCore import QUrl, Slot, QObject, Property
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine


# method #1
'''import psycopg2

con = psycopg2.connect(database="iot_data", user="postgres", password="postgres", host="localhost", port= '5432')
cur_obj = con.cursor()

# create database table
cur_obj.execute('create table if not exists room_info([Room No] text, [Room Status] integer)')

# read data from table
cur_obj.execute('select [Room No], [Room Status] from room_info')
data = cur_obj.fetchall()
print(data)'''


# method #2
# root class
class DatabaseManager(QObject):
    __data = []
    def __init__(self):
        super().__init__()
        self.db = QSqlDatabase.addDatabase("QSQLITE") # QPSQL driver for PostgreSQL
        # self.db.setHostName("localhost")  # set the hostname of the database server
        # self.db.setPort(5432)  # set the port of the database server
        self.db.setDatabaseName("iot_data.db")  # set the name of the database
        # self.db.setUserName("postgres")  # set the username to access the database
        # self.db.setPassword("postgres")  # set the password for the database user

        if not self.db.open():
            print("Failed to connect to database")
            sys.exit(1)

        # create database query object
        self.query = QSqlQuery()
        # create database table model object
        self.model = QSqlTableModel()
        
        self.create_table()
        
        self.model.setTable('room_info')
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.select()
        
    # data store into list
    def data_store(self):
        data = []
        for r in range(self.model.rowCount()):
            li = []
            for c in range(self.model.columnCount()):
                d = self.model.index(r, c).data()
                li.append(d)
            data.append(li)
        return data
            
    # create database table if not exists
    def create_table(self):
        self.query.prepare('create table if not exists room_info([Room No] text, [Room Status] integer)')
        self.query.exec()
        
    # insert default data or read data for action from database
    @Property(list, constant=True)
    def read_inserted_data(self):
        default_data = {'Room_1' : 0, 'Room_2' : 0}
        self.query.prepare('select [Room No], [Room Status] from room_info')
        self.query.exec()
        if self.query.next():
            self.__data = self.data_store()
        else:
            for k, v in default_data.items():
                self.query.prepare("insert into room_info([Room No], [Room Status]) values (:no, :status)")
                self.query.bindValue(":no", k)
                self.query.bindValue(":status", v)
                self.query.exec()
            self.model.select()
            self.query.prepare('select [Room No], [Room Status] from room_info')
            self.query.exec()
            self.__data = self.data_store()
        return self.__data

    # update database for set action or status
    @Slot(str, int)
    def update_table(self, rm_no, rm_status):
        self.query.prepare('update room_info set [Room Status]=:status where [Room No]=:no')
        self.query.bindValue(':no', rm_no)
        self.query.bindValue(':status', rm_status)
        self.query.exec()

# root
if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # create an instance of the databaseManager class
    iotDatabase = DatabaseManager()

    # expose the databaseManager instance to QML
    engine.rootContext().setContextProperty("iotDatabase", iotDatabase)

    # find the current file path
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    # load the QML file
    qmlfile = os.path.join(CURRENT_DIR, "main.qml")
    engine.load(QUrl.fromLocalFile(qmlfile))

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())