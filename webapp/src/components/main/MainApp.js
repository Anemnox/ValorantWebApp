import React, { useState } from "react";

import "./mainapp.css";
import NavBar from "../navbar/NavBar.js";

const sio = require("socket.io-client")("http://localhost:4000");

const MainApp = (props) => {
  const [message, setMsg] = useState("Hello World!");

  sio.on("Message", (msg) => {
    setMsg(msg);
  });

  return (
    <div className="mainapp">
      <NavBar />
      {message}
    </div>
  );
}

export default MainApp;
