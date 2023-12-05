#!/usr/local/bin/node
/**
 * Script that computes the number of tasks completed from an API
 * API: https://jsonplaceholder.typicode.com/todos given as first argument
 * Prints by User ID, only prints completed tasks.
 */
const request = require('request');
const url = process.argv[2];

const completedList = {} /* Makes a map! Stores # of completed task by user */
/* Key = id, Value = number of tasks completed */

request(url, (error, response, body) => {
  if (error) {
    console.error('Error occured: ', error);
    process.exit(1);
  }

  const todoList = JSON.parse(body);
  /* Makes array after parsing the body of response */
  todoList.forEach((task) => {
    /* Takes each value, assigns it to `task` to execute function */
    if (task.completed) {
      /* Checks if the completed value is not null/false in the API */
      completedList[task.userId] = (
        completedList[task.userId] || 0) + 1;
        /* assigns the key/value pairs to completedList */
        /* if user was not in list, they will be added with a count of 1 */
      } 
    });
    console.log(completedList);
  });
