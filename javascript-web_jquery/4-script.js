/**
 * Script that toggles the class of the <header> element to red or green
 * when a user clicks on the tag DIV#toggle_header.
 * Uses jQuery API
 * Based on 4-main.html
 */
$('#toggle_header').click(function () {
  $('header').toggleClass('red green');
});
