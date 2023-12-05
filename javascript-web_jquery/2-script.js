/**
 * Script that updates the text color of the <header> element to red (#FF0000)
 * whenever a user clicks on the tag DIV#red_header
 * Uses jQuery API
 */
$('#red_header').click(function () {
  $('header').css('color', '#FF0000');
});
