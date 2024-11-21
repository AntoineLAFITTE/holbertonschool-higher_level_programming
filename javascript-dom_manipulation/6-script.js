fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json()) // Parse la response en JSON
  .then(data => {
    document.getElementById('character').textContent = data.name; // Display le character's name
  })
  .catch(error => console.error('Error fetching character:', error)); // Handle any errors
