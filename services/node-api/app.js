const express = require('express');
const app = express();
const port = 8001; // Node.js API runs on port 8001

app.get('/', (req, res) => {
  res.json({ message: 'Hello Docker API' });
});

app.get('/health', (req, res) => {
  res.json({ status: 'ok' });
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Node.js API listening at http://0.0.0.0:${port}`);
});
