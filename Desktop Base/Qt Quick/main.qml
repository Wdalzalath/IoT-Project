import QtQuick 2.15
import QtQuick.Controls 2.15


ApplicationWindow {
    visible: true
    width: 400
    height: 200
    title: qsTr("PySide6: Home Automation System")

    property variant data: iotDatabase.read_inserted_data

    Component.onCompleted: {
        // set default room status
        if(data[0][1]==1)
        {
            btnOn1.enabled = false;
            btnOff1.enabled = true;
        }
        else
        {
            btnOn1.enabled = true;
            btnOff1.enabled = false;
        }
        if(data[1][1]==1)
        {
            btnOn2.enabled = false;
            btnOff2.enabled = true;
        }
        else
        {
            btnOn2.enabled = true;
            btnOff2.enabled = false;
        }
    }

    // a form to iot data to update records
    Column {
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        spacing: 10

        // button to on and off bed room
        Row {
            spacing: 10
            Text {
                text: qsTr("Bed Room")
                font.pointSize: 12
                font.family: "Arial"
                font.bold: true
            }
            Button {
                id: btnOn1
                text: qsTr('ON')
                width: 100
                height: 28
                font.pointSize: 12
                font.family: "Arial"
                font.bold: true
                onClicked: {
                    iotDatabase.update_table('Room_1', 1)
                    btnOn1.enabled = false
                    btnOff1.enabled = true
                }
            }
            Button {
                id: btnOff1
                text: qsTr('OFF')
                width: 100
                height: 28
                font.pointSize: 12
                font.family: "Arial"
                font.bold: true
                onClicked: {
                    iotDatabase.update_table('Room_1', 0)
                    btnOn1.enabled = true
                    btnOff1.enabled = false
                }
            }
        }
        // button to on and off kitchen
        Row {
            spacing: 10
            Text {
                text: qsTr("Kitchen")
                font.pointSize: 14
                font.family: "Arial"
                font.bold: true
                width: 80
            }
            Button {
                id: btnOn2
                text: qsTr('ON')
                width: 100
                height: 28
                font.pointSize: 12
                font.family: "Arial"
                font.bold: true
                onClicked: {
                    iotDatabase.update_table('Room_2', 1)
                    btnOn2.enabled = false
                    btnOff2.enabled = true
                }
            }
            Button {
                id: btnOff2
                text: qsTr('OFF')
                width: 100
                height: 28
                font.pointSize: 12
                font.family: "Arial"
                font.bold: true
                onClicked: {
                    iotDatabase.update_table('Room_2', 0)
                    btnOn2.enabled = true
                    btnOff2.enabled = false
                }
            }
        }
    }
}
