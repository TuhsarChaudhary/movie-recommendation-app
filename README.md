# Movie Recommendation System

This project is a Movie Recommendation System that suggests movies based on user preferences such as genre, duration, and mood. The application uses Flask for the backend and HTML, CSS, and JavaScript for the frontend.

## Features

- Users can select their preferred genre, movie duration, and mood.
- The application provides personalized movie recommendations based on user input.
- The recommendation includes movie details such as title, director, IMDb rating, and a brief description.
- The movie poster is displayed as the background of the recommendation container.
- The site is responsive and works well on both desktop and mobile devices.

## Technologies Used

- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: CSS with Flexbox and Media Queries
- **Hosting**: Vercel

## Setup and Installation

### Prerequisites

- Python 3.x
- Flask
- Git 

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/movie-recommendation.git
    cd movie-recommendation
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `Procfile` (if not already created) with the following content:

    ```plaintext
    web: gunicorn app:app
    ```

4. Create a `runtime.txt` (if not already created) with the desired Python version:

    ```plaintext
    python-3.9.7
    ```

### Running the Application Locally

1. Start the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

### Deployment

#### Deploying to Vercel

1. Sign up for Vercel at [Vercel](https://vercel.com).

2. Create a new project and link your GitHub repository containing your Flask app.

3. Configure the build and start commands:
    - Build Command: `pip install -r requirements.txt`
    - Start Command: `gunicorn app:app`

4. Deploy the project on Vercel.

5. Visit your live application at `https://movie-recommendation-app-ashy.vercel.app/recommend`.

## Usage

1. Open the application in your web browser.
2. Select your preferred genre, movie duration, and mood from the dropdown menus.
3. Click the "Get Recommendation" button.
4. View the personalized movie recommendation and details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss any changes or improvements.

## Acknowledgments

- Thanks to the Flask, HTML, CSS, and JavaScript communities for their invaluable resources and support.
