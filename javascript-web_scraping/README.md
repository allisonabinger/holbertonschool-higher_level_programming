# JavaScript - Web Scraping

## The `fs` Module

The fs module contains methods to interact with the file system. 
It contains methods to read, write, and delete files.

## `require`
The require function is used to import modules in node.js. when you call require,
it loads the given module and returns an object that contains
all the methods and properties. 

For example:

> `const fs = require('fs');`
>
> This line of codes defines a variable `fs`, then uses `require` to load
> the fs module, and stores it as an object in the `fs` module. It can then
> be used to call functions like `fs.readFile` or `fs.writeFile`.

## Functions in the fs module
The following are methods that the fs module uses to interact with the file system. Assume that all functions have defined fs as a const variable to store the module `fs`

### `readFile`
##### Syntax: `fs.readFile(path[, options], callback)`

Example:
```

  fs.readFile('path_to_file', 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });

```

This example would read the file 'path_to_file', using utf-8 character
encoding, and the callback function is called when the file has been read.

> The callback function in this example is `(err, data) => {...}`

The callback function takes two parameters: err and data. The function is everything inside of the {} and uses the => syntax to define the function body.
If an error occurs during the reading, the error object is passed to the callback function. Otherwise, the data is passed to the callback function. The callback function contains the `console.log` and the `console.error` statements to be executed when the function is called.

### `writeFile`
##### Syntax: `fs.writeFile(path, data[, options], callback)`

Example:

```

  fs.writeFile('path_to_file, 'data_to_write', 'utf-8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log('File has been written to');
  });

```
This example is similar to `readFile`, except it will use the data provided and write it to the file given.

## The `request` Module

The `request` module is a popular library for making HTTP requests in Node.js. After establishing a request object using `require`, you can use it to make `GET`, `POST`, `PUT`, `DELETE`, and more HTTP requests. It provides a flexible API and handles responses, and supports **JSON** parsing, form data, and timeouts.

#### Syntax: `request(url, (error, response, body) => {...});`

Example:
```
{
  const request = require('request');
  const options = {
    url: 'https://apiurl.in/api/users',
    method: 'GET'
  };
  request(options, (err, res, body) => {
    if (err) {
      return console.error('Error occured: ', err);
    }
    console.log(JSON.parse(body));
  })
}
```
This example establishes a request object to import the request module, and then initializes an object called options that will be used to specify the details of the **HTTP** request. It then calls the `request` function using the options object as the first argument, and uses the callback for the second argument to execute after the request is complete. 
The **callback function** for this example takes an `err` object for an error that occurs during the request, the `res` object for information about the response, and `body` - the response body that is usually a string. If any errors occurs, they will be logged to the console and the function will exit. If not, the body is converted to a **JavaScript** object with`JSON.parse`, that object is logged to the console, and the function completes.


## Misc. Functions used in this project

### console.error
