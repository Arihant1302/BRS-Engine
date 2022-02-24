from flask import Flask, render_template, request
import recommender

app = Flask(__name__)

@app.route('/') # To render Homepage
def home_page():
    return render_template('index.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
     #Taking inputs from html page to python code;
     if (request.method=='POST'):
         operation =request.form['operation']
         n_books = int(request.form["books_count"])
         if(operation == 'comic'):
             name = "comic"
             result = recommender.contents_based_recommender(name, n_books)
         if (operation == 'datascience'):
             name = "datascience"
             result = recommender.contents_based_recommender(name, n_books)
         if (operation == 'computerscience'):
             name = "computerscience"
             result = recommender.contents_based_recommender(name, n_books)
         if (operation == 'fiction'):
             name = "fiction"
             result = recommender.contents_based_recommender(name, n_books)
         if (operation == 'nonfiction'):
             name = "nonfiction"
             result = recommender.contents_based_recommender(name, n_books)
         if (operation == 'philosophy'):
             name = "philosophy"
             result = recommender.contents_based_recommender(name, n_books)
         if (operation == 'psychology'):
             name = "psychology"
             result = recommender.contents_based_recommender(name, n_books)
         if (operation == 'history'):
             name = "history"
             result = recommender.contents_based_recommender(name, n_books)
         if (operation == 'signalprocessing'):
             name = "signalprocessing"
             result = recommender.contents_based_recommender(name, n_books)
         if (operation == 'science'):
             name = "science"
             result = recommender.contents_based_recommender(name, n_books)
         if (operation == 'mathematics'):
             name = "mathematics"
             result = recommender.contents_based_recommender(name, n_books)
         if (operation == 'economics'):
             name = "economics"
             result = recommender.contents_based_recommender(name, n_books)
        #returning values to html page
         return render_template('submit.html',mk = result)

if __name__ == '__main__':
    app.run()