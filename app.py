from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

# Load preprocessed data
popular_df = pickle.load(open('popular.pkl', 'rb'))
siml_table = pickle.load(open('siml_table.pkl', 'rb'))
table = pickle.load(open('table.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    ratings_rounded = popular_df['Book-Rating'].apply(lambda x: round(x, 2))
    return render_template(
        'index.html',
        book_name=popular_df['Book-Title'].to_list(),
        author=popular_df['Book-Author'].to_list(),
        image=popular_df['Image-URL-M'].to_list(),
        votes=popular_df['numberofratings'].to_list(),
        rating=ratings_rounded.to_list()
    )

@app.route('/recommend')
def ui():
    return render_template('recommend.html')

@app.route('/recommend_books', methods=['POST'])
def suggest():
    user_input = str(request.form.get('user_input'))  # Typecast to string
    data = []

    try:
        index = np.where(table.index == user_input)[0][0]  # Ensure book exists
        recommended_books = sorted(
            list(enumerate(siml_table[index])),
            key=lambda x: x[1],
            reverse=True
        )[1:9]

        for i in recommended_books:
            item = []
            temp_df = books[books['Book-Title'] == table.index[i[0]]]
            temp_df = temp_df.drop_duplicates('Book-Title')  # Correct spelling
            item.extend(temp_df['Book-Title'].to_list())
            item.extend(temp_df['Book-Author'].to_list())
            item.extend(temp_df['Image-URL-M'].to_list())
            data.append(item)

    except IndexError:
        data = ["Book not found. Please try another title."]

    return render_template('recommend.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
