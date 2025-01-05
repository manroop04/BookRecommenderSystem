```markdown
# 📚 Book Recommender System

A web application that recommends books based on user preferences using collaborative filtering and popularity based filtering. This project leverages Python, Flask, and various data processing libraries to create a robust recommendation system.

## 🚀 Features

- Displays a list of popular books with their ratings and authors.
- Accepts user input to suggest similar books.
- Provides detailed book information, including titles, authors, and cover images.
- Interactive UI built with Bootstrap for a responsive design.
- Recommendations are generated using a precomputed similarity matrix.

## 🛠️ Technologies Used

- **Backend**: Flask, Python
- **Frontend**: HTML, CSS, Bootstrap
- **Data Processing**: Pandas, NumPy
- **Libraries for ML/Recommendations**: Precomputed similarity matrix
- **Data Storage**: Pickle files for loading preprocessed data


## 🖥️ How to Run

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/manroop04/BookRecommenderSystem.git
   cd BookRecommenderSystem
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Start the Flask development server:
   ```bash
   python app.py
   ```

## 🖼️ Screenshots


## 🧠 How It Works

1. **Popular Books**:
   The homepage displays a list of popular books based on predefined data (`popular.pkl`).

2. **Recommendations**:
   When a user inputs a book title:
   - The app looks up the book in the similarity matrix (`siml_table.pkl`).
   - It retrieves similar books based on collaborative filtering.
   - The results are displayed with their titles, authors, and cover images.

3. **Preprocessed Data**:
   - All the data is preprocessed and stored in `.pkl` 

## 📄 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as per the license terms.

---
