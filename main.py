import requests,os
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)
app.config['SECRET_KEY'] = 'your_secret_key' 

# Define the form class
class BookSearchForm(FlaskForm):
    book_name = StringField("Book Name", validators=[DataRequired()])
    submit = SubmitField("Search")


api_key = os.getenv("api_key")
base_url = "https://www.googleapis.com/books/v1/volumes"
# Define routes
@app.route("/", methods=["GET", "POST"])
def home():
    form = BookSearchForm()
    if form.validate_on_submit():
        book_name = form.book_name.data
        url = f"{base_url}?q={book_name}&key={api_key}"
        response = requests.get(url)

        data = response.json()
        print(data)
        info = data["items"][0]["volumeInfo"]
        title = info["title"]
        author = info["authors"][0]
        description = info["description"]

        access_info = data["items"][0]["volumeInfo"]
        pdf_link = access_info["previewLink"]
        
        
        return render_template("index.html",form = form,title = title,author = author,description= description,link = pdf_link,search = True)  # Replace with your logic
    return render_template("index.html", form=form,search = False)



if __name__ == "__main__":
    app.run(debug=True)


