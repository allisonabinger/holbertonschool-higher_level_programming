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
##### Syntax: `fs.writeFile(path[, options], callback)`

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
