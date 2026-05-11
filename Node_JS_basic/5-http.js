const http = require('http');
const countStudents = require('./3-read_file_async');

const port = 1245;

const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    countStudents(process.argv[2])
      .then((response) => {
        res.statusCode = 200;
        res.end(`This is the list of our students\n${response}`);
      })
      .catch((error) => {
        res.statusCode = 500;
        res.end(`This is the list of our students\n${error.message}`);
      });
  } else {
    res.statusCode = 404;
    res.end('Not found.');
  }
});

app.listen(port);

module.exports = app;
