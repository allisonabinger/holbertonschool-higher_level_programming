/**
 * Adds a <li> element to a list when the user clicks on the tag DIV#add_item
 * Uses jQuery, based on 5-main.html
 */
$('#add_item').click(function () {
  $('.my_list').append('<li>Item</li>');
});
