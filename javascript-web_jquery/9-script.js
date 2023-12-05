/**
 * Fetches from provided API and displays the value of 'hello'
 * from that fetch inside the DIV#hello tag.
 * Uses jQuery AJAX API, based on 9-main.html
 */
$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      $('#hello').text(data.hello);
    },
    error: function (error) {
      console.error('Error in translation! Sacrebleu!', error);
    }
  })
});
