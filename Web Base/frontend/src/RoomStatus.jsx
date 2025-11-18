import React, { useEffect, useState } from "react";
import axios from "axios";

export default function RoomStatus() {
  const [rooms, setRooms] = useState([]);

  // fetch room data
  const fetchRooms = async () => {
    try {
      const response = await axios.get("http://127.0.0.1:8000/room_info/");
      setRooms(response.data);
    } catch (error) {
      console.error("Error fetching rooms:", error);
    }
  };

  // update room status
  const updateRoomStatus = async (roomId, status) => {
    try {
      await axios.put(`http://127.0.0.1:8000/room_info/${roomId}/`, {
        room_status: status,
      });
      fetchRooms(); // fefresh data
    } catch (error) {
      console.error("Error updating room:", error);
    }
  };

  // load rooms on page load
  useEffect(() => {
    fetchRooms();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Room Now</h2>

      {rooms.map((room) => (
        <div
          key={room.id}
          style={{
            padding: "15px",
            marginBottom: "10px",
            border: "1px solid #ccc",
            borderRadius: "8px",
            width: "300px",
          }}
        >
          <h3>{room.room_no}</h3>

          <button
            onClick={() => updateRoomStatus(room.id, 1)}
            disabled={room.room_status === 1}
            style={{
              marginRight: "10px",
              padding: "8px 15px",
              backgroundColor: room.room_status === 1 ? "#ccc" : "green",
              color: "#fff",
              border: "none",
              borderRadius: "5px",
              cursor: room.room_status === 1 ? "not-allowed" : "pointer",
            }}
          >
            ON
          </button>

          <button
            onClick={() => updateRoomStatus(room.id, 0)}
            disabled={room.room_status === 0}
            style={{
              padding: "8px 15px",
              backgroundColor: room.room_status === 0 ? "#ccc" : "red",
              color: "#fff",
              border: "none",
              borderRadius: "5px",
              cursor: room.room_status === 0 ? "not-allowed" : "pointer",
            }}
          >
            OFF
          </button>
        </div>
      ))}
    </div>
  );
}