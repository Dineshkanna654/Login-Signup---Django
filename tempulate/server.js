// Import the Express module
const express = require('express');

// Create an Express application
const app = express();

// Define a route that responds with an HTML page containing a hyperlink
app.get('/', (req, res) => {
    // Respond with a simple HTML page containing a hyperlink
    res.send(`
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Node.js Django</title>
        </head>
        <body>
            <a href="http://localhost:8000/signup">Click here to go to Signup</a>
        </body>
        </html>
    `);
});

// Set the port for the server to listen on
const port = 3000;

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
