from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fcrud.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Grocery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable =False)
    created_at = db.Column(db.DateTime, nullable= False, default=datetime.utcnow)

    def __repr__(self):
        return f'{self.name}'

@app.route('/',methods=['GET','POST'])
def index():
    # form handling logic
    if request.method == 'POST': # form is submitted
        name = request.form.get('name')
        item =  Grocery(name=name)
        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return "there was a problem add the new grocery item"
    else: # page is opened normally
        groceries = Grocery.query.order_by(Grocery.created_at).all()
        return render_template('index.html',groceries=groceries)
    
@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    grocery = Grocery.query.get_or_404(id)
    if request.method == 'POST':
        grocery.name = request.form.get('name')
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "there was a problem updating grocery item"
    else:
        title = 'Update Data'
        return render_template('update.html',title=title, grocery=grocery)

@app.route('/delete/<int:id>')
def delete(id):
    grocery = Grocery.query.get_or_404(id)
    try:
        db.session.delete(grocery)
        db.session.commit()
        return redirect('/')
    except:
        return "there was a problem deleting data"



if __name__ == '__main__':
    app.run(debug=True)