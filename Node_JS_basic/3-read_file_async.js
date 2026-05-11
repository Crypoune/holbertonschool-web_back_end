// 3-read_file_async.js
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const fields = {};
      const students = data
        .split('\n')
        .filter((student) => student.trim() !== '');

      students.shift();

      let response = `Number of students: ${students.length}`;
      console.log(response);

      for (const student of students) {
        const cols = student.split(',');
        const field = cols[3];

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(cols[0]);
      }

      for (const field of Object.keys(fields)) {
        const responseField = `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;

        console.log(responseField);
        response += `\n${responseField}`;
      }

      resolve(response);
    });
  });
}

module.exports = countStudents;
