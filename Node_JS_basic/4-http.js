const http = require('http');

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html' });
  res.end('HEllo Holberton School!');
});

app.listen(1245);

module.exports = app;
