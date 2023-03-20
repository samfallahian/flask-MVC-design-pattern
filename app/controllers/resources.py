from flask import render_template, request, url_for, redirect, flash
from app.controllers import bp_resources
from app import database
from app.models.resources import Resource

db = next(database.get_db())


@bp_resources.route('/')
def index():
    data = db.query(Resource).all()
    return render_template("resources/list.html", resources=data)


@bp_resources.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        if not request.form['item'] or not request.form['amount']:
            flash('Please enter all the fields', 'error')
        else:
            resource = Resource(item=request.form['item'], amount=request.form['amount'])

            db.add(resource)
            db.commit()

            flash('Record was successfully added')
            return redirect(url_for('resources.index'))
    return render_template('resources/add.html')


@bp_resources.route('/update/<int:item_id>/', methods=['GET', 'POST'])
def update(item_id):
    if request.method == 'POST':
        if not request.form['item'] or not request.form['amount']:
            flash('Please enter all the fields', 'error')
        else:
            resource = db.query(Resource).filter_by(id=item_id).first()
            resource.item = request.form['item']
            resource.amount = request.form['amount']
            db.commit()

            flash('Record was successfully updated')
            return redirect(url_for('resources.index'))
    data = db.query(Resource).filter_by(id=item_id).first()
    return render_template("resources/update.html", data=data)


@bp_resources.route('/delete/<int:item_id>/', methods=['GET', 'POST'])
def delete(item_id):
    if request.method == 'POST':
        resource = db.query(Resource).filter_by(id=item_id).first()
        db.delete(resource)
        db.commit()

        flash('Record was successfully deleted')
        return redirect(url_for('resources.index'))
    data = db.query(Resource).filter_by(id=item_id).first()
    return render_template("resources/delete.html", data=data)
