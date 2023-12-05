/**
 * Fetches the character name from api and displays name
 * inside the DIV#character tag.
 * Uses jQuery AJAX API, based on 7-main.html
 */
$.ajax({
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  method: 'GET',
  dataType: 'json',
  success: function (data) {
    $('#character').text(`${data.name}`);
  },
  error: function (error) {
    console.error('Error fetching character name', error);
  }
});
