# JavaScript - Web Scraping
***

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

&nbsp;
&nbsp;

## File Manipulation in JS
***

## The `fs` Module

The fs module contains methods to interact with the file system. 
It contains methods to read, write, and delete files.

## Functions in the `fs` Module
The following are methods that the fs module uses to interact with the file system. Assume that all functions have defined fs as a const variable to store the module `fs`

### `readFile`
**Syntax: `fs.readFile(path[, options], callback)`**

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
encoding, and the callback function is called when the file has been read. The callback function in this example is `(err, data) => {...}`. If an error occurs during the reading, the error object is passed to the callback function. Otherwise, the data is passed to the callback function. The callback function contains the `console.log` and the `console.error` statements to be executed when the function is called.

### Whats a callback function?
Callback functions are passed as an argument to another function and executed after the first function has finished. Theyre used to control the flow of the program, and allow certain code to be executed only after other code has finished.
```
{
  object.function(parameter1, parameter2, (callbackParameter) => {
    //code to execute in callback function
    });
}
```

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

&nbsp;
***

## HTTP Requests Using `request`

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
&nbsp;
The **callback function** for this example takes an `err` object for an error that occurs during the request, the `res` object for information about the response, and `body` - the response body that is usually a string. If any errors occurs, they will be logged to the console and the function will exit. If not, the body is converted to a **JavaScript** object with`JSON.parse`, that object is logged to the console, and the function completes.

&nbsp;
***

## Misc. Functions Used

### `console`
The console object is a global object in **JavaScript**, meaning it can be accessed from anywhere in your code without needing to be imported. It provides a set of methods that are used to output information to the console. This [post](https://developer.mozilla.org/en-US/docs/Web/API/console) explains more on console and the different methods it has to offer.

#### `console.log()`
This is a method in JavaScript that is used to print any kind of variables defined before or inside of it, or just to print any message that needs to be displayed to the user.

#### `console.error()`
This is a method in JavaScript that is used to print error messages to the console. similar to console.log, but it includes a stack trace to help you find where the error occured. The data passed to `console.error()` can be any type, but is commonly a string or error object.

>For more information on error handling in JavaScript, Craig Buckler has more information in this [blog post](https://www.sitepoint.com/javascript-error-handling/). 

&nbsp;
&nbsp;

## `process`
The process object is also a global object in **JS**. It provides information about, and control over, the current **Node.js** process. It can be used to read command line arguments, get environment variables, access the current working directory, and more.

#### `process.argv[]`
This is an array containing the command-line arguments passed when the **Node.js** process was launched. The first element [0] will be `node`, and the second element [1]will be the name of the **JavaScript** file. Any other elements will be command-line arguments passed from the user.

#### `process.exit([code])`
This method instructs **Node.js** to terminate the process synchronously [(what does that mean?)](https://stackoverflow.com/questions/748175/asynchronous-vs-synchronous-execution-what-is-the-difference) with an exit status of `code`. If the `code` is omitted, it either uses the success code of `0` or the value of `process.exitCode` if it has been set. **Node.js** will force the process the exit as quickly as possible, even if there are other operations pending that have not completed. 

&nbsp;
&nbsp;

## `includes()`
This method is used to check if an array or string includes a certain element or substring. it takes the element or substring to search for as an argument and returns a boolean indicating whether or not it was found. It can be used by tacking it onto an array 
&nbsp;
&nbsp;

## `forEach`
This method is used to execute a provided function once for each element in an array. It takes a **callback function** as an argument, which is called for each element in the array. It can only be used on arrays, maps, or sets. 
> For more information on JavaScript data types, [w3schools](https://www.w3schools.com/js/js_datatypes.asp) has great cheat sheets!

&nbsp;
***
&nbsp;

This README was made with :heart: by [Allison Binger](https://github.com/allisonabinger/holbertonschool-higher_level_programming/commits?author=allisonabinger), Holberton Tulsa Student.
