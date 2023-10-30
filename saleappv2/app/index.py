from flask import Flask, render_template
import dao

app = Flask(__name__)

@app.route("/")
def index():
    cates = dao.get_categories()
    produs = dao.get_categories()
    return render_template('index.html', categories=cates, product=produs)

if __name__ == '__main__':
    app.run(debug=True)