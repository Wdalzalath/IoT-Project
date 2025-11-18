# Tkinter User Interface

**Tkinter** is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit and is Python's de facto standard GUI.
This is a simple tkinter **_(python defalut gui)_** user interface with sqlite3 **_(python default)_** database.


## Requirements

To run this application, you will need:

* [Python3.x](https://www.python.org/downloads/) or higher
* [Sqlite3](https://sqlitebrowser.org/)

You will also need access to sqlite3 database.


## Installation

1. Clone this repository to your local machine.
2. Install the required Python modules by running the following command in your terminal.
3. Edit the config.ini file to include your PostgreSQL database credentials.

```bash
pip install -r requirements.txt
# or (Linux / MacOS)
sudo pip install -r requirements.txt
```

## Folder Structure

```bash
Qt-Quick/
│
├── screenshots/
├── iot_data.db
├── main.py
├── README.md
└── requirments.txt
```


## Usage

To run the application, simply run the following command in your terminal:

* Clone this repository to your local machine and type to run

```css
python main.py
```


## Screenshots

Here are some screenshots of the `Tkinter` project:

**Main Window**<br/>
![Main Windows](screenshots/main.png)<br/>


This will launch the Tkinter user interface. From there, you can update **_IoT(Internet of Things)_** status records in the connected Sqlite3 database by clicking button.