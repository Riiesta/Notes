from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Article

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///articles.db'
app.config['SECRET_KEY'] = 'mysecretkey'
db.init_app(app)

@app.route('/')
def index():
    articles = Article.query.all()
    return render_template('index.html', articles=articles)

@app.route('/add', methods=['POST', 'GET'])
def add_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_article = Article(title=title, content=content)
        db.session.add(new_article)
        db.session.commit()
        flash('Article Added Successfully')
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:id>')
def delete_article(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    flash('Article Deleted Successfully')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

