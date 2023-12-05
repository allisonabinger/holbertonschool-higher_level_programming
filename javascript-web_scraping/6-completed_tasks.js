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
  todoList.forEach((task) => {
    if (task.completed) {
      completedList[task.userId] = (
        completedList[task.userId] || 0) + 1;
      }
    });
    console.log(completedList);
