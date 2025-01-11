function getRecommendation() {
    const genre = document.getElementById('genre').value;
    const duration = document.getElementById('duration').value;
    const mood = document.getElementById('mood').value;

    fetch('https://movie-recommendation-il9ixouex.vercel.app/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ genre, duration, mood })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('recommendation').innerHTML = data.recommendation;
        document.getElementById('recommendation-container').style.display = 'block'; // Show the recommendation container
    });
}
