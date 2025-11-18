import sqlite3
from bottle import run, get


# create api file for read data from database
# you can also read data from local database
# connect your web or server database
conn = sqlite3.connect('iot_data.db')
c = conn.cursor()

# read data from database
def read_table_data():
        _list = []
        c.execute('select [Room No], [Room Status] from room_info')
        for r in c.fetchall():
                _list.append([r[0], r[1]])
        return _list

# get data from user and send data to local or server database
# @route('/data')
@get('/data')
def get_data():
    data_list = read_table_data()
    data = [{'Room No': data_list[0][0], 'Room Status': data_list[0][1]},
            {'Room No': data_list[1][0], 'Room Status': data_list[1][1]}]
    # response.content_type = 'application/json'
    # return dumps(data)
    return {'data' : data}

# change your host address or port number
run(host='localhost', reloader=True, port=9990, debug=True)