/**
 * Fetches and lists the title for all movies from api and displays
 * each name in the list_movies UL tag
 * Uses jQuery AJAX API, based on 8-main.html
 */
$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  method: 'GET',
  dataType: 'json',
  success: function (data) {
    data.results.forEach(function (film) {
      /* Iterates through the results to get each title */
      $('#list_movies').append('<li>' + film.title + '</li>');
    });
  },
  error: function (error) {
    console.error('Error fetching movies: ', error);
  }
});
