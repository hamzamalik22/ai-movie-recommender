# Movie Recommendation System 🎬

A content-based movie recommendation system built with Streamlit that uses the TMDB 5000 Movie Dataset to provide personalized movie recommendations based on movie content, including genres, cast, director, and plot overview.

## Features

- Content-based movie recommendations using TF-IDF vectorization
- Interactive web interface built with Streamlit
- Real-time similarity scoring
- Detailed movie information display including:
  - Movie title
  - Genres
  - Director
  - Cast members
  - Overview
  - User ratings
  - Similarity scores

## Website

Visit the live application here:  [Movie Flix AI](https://movie-flix-ai.streamlit.app/).

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Required Dataset

Download the following files from [TMDB 5000 Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata) on Kaggle:
- tmdb_5000_movies.csv
- tmdb_5000_credits.csv

Place both files in the project's root directory.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/hamzamalik22/ai-movie-recommender.git
cd ai-movie-recommender
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install required packages:
```bash
pip install streamlit pandas numpy scikit-learn
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

3. Use the application:
   - Select a movie from the dropdown menu
   - Click "Get Recommendations" to see similar movies
   - Explore movie details and similarity scores
   - Use the information expander to learn more about how the system works

## How It Works

The recommendation system uses the following approach:
1. Combines various movie features (genres, keywords, cast, director, overview)
2. Converts text data into numerical vectors using TF-IDF
3. Calculates similarity between movies using cosine similarity
4. Recommends movies with highest similarity scores

## Project Structure

```
movie-recommendation-system/
│
├── app.py    # Main application file
├── tmdb_5000_movies.csv    # Movie dataset (download required)
├── tmdb_5000_credits.csv   # Credits dataset (download required)
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

## Dependencies

- streamlit
- pandas
- numpy
- scikit-learn

## Performance Considerations

- The initial loading of the dataset might take a few moments
- The system uses caching to improve performance on subsequent runs
- Recommendation generation is typically fast due to pre-computed similarity matrix

## Troubleshooting

1. If you encounter a FileNotFoundError:
   - Ensure both dataset files are downloaded
   - Verify files are in the correct directory
   - Check file names match exactly

2. For memory issues:
   - Close other resource-intensive applications
   - Ensure your system meets minimum requirements
   - Consider reducing the dataset size for testing

## Future Improvements

- Add movie posters
- Implement collaborative filtering
- Add genre-based filtering
- Include release year filtering
- Add more visualization options
- Implement user ratings and feedback

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- TMDB for providing the movie dataset
- Streamlit for the web framework
- Kaggle for hosting the dataset

## Contact

For any questions or feedback, please open an issue in the repository.