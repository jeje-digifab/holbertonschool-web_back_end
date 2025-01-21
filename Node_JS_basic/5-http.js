const http = require('http');
const url = require('url');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
    const parsedUrl = url.parse(req.url, true);
    const {
        pathname
    } = parsedUrl;

    if (pathname === '/students') {
        if (process.argv.length > 2) {
            const csvFile = process.argv[2];
            const output = 'This is the list of our students\n';

            const originalLog = console.log;
            let capturedOutput = '';
            console.log = (message) => {
                capturedOutput += `${message}\n`;
            };

            countStudents(csvFile)
                .then(() => {
                    console.log = originalLog;

                    res.writeHead(200, {
                        'Content-Type': 'text/plain',
                    });
                    res.write(output);
                    res.write(capturedOutput.trim());
                    res.end();
                });
        } else {
            res.writeHead(200, {
                'Content-Type': 'text/plain',
            });
            res.end('Hello Holberton School!');
        }
    } else {
        res.writeHead(200, {
            'Content-Type': 'text/plain',
        });
        res.end('Hello Holberton School!');
    }
});

app.listen(1245);

module.exports = app;
