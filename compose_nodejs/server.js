'use strict';

// Imports
const express = require('express');
const os = require("os");

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// get host name
const hostName = os.hostname();

// App
const app = express();
app.get('/', (req, res) => {
  res.setHeader('content-type', 'text/html');
  res.send(`<h2>Hello World from hostname <code>${hostName}</code>(using NodeJS)</h2>`);
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
