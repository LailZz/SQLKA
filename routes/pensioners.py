from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Pensioner, District
from sqlalchemy.orm import joinedload
from datetime import datetime

pensioners_bp = Blueprint('pensioners', __name__, url_prefix='/pensioners')

@pensioners_bp.route('/')
def index():
    pensioners = Pensioner.query.options(joinedload(Pensioner.district)).all()
    return render_template('pensioners/index.html', pensioners=pensioners)

@pensioners_bp.route('/<int:id>')
def show(id):
    pensioner = Pensioner.query.options(
        joinedload(Pensioner.district),
        joinedload(Pensioner.payments)
    ).get_or_404(id)
    return render_template('pensioners/show.html', pensioner=pensioner)

@pensioners_bp.route('/create', methods=['GET', 'POST'])
def create():
    districts = District.query.all()
    if request.method == 'POST':
        try:
            birth_date = datetime.strptime(request.form['birth_date'], '%Y-%m-%d').date()
            pensioner = Pensioner(
                pensioner_id=request.form['pensioner_id'],
                last_name=request.form['last_name'],
                first_name=request.form['first_name'],
                middle_name=request.form['middle_name'],
                birth_date=birth_date,
                district_code=request.form['district_code'],
                address=request.form['address']
            )
            db.session.add(pensioner)
            db.session.commit()
            flash('Пенсіонера успішно створено', 'success')
            return redirect(url_for('pensioners.index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Помилка при створенні пенсіонера: {str(e)}', 'danger')
    return render_template('pensioners/form.html', districts=districts)

@pensioners_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    pensioner = Pensioner.query.get_or_404(id)
    districts = District.query.all()
    if request.method == 'POST':
        try:
            pensioner.last_name = request.form['last_name']
            pensioner.first_name = request.form['first_name']
            pensioner.middle_name = request.form['middle_name']
            pensioner.birth_date = datetime.strptime(request.form['birth_date'], '%Y-%m-%d').date()
            pensioner.district_code = request.form['district_code']
            pensioner.address = request.form['address']
            db.session.commit()
            flash('Дані пенсіонера успішно оновлено', 'success')
            return redirect(url_for('pensioners.show', id=id))
        except Exception as e:
            db.session.rollback()
            flash(f'Помилка при оновленні даних пенсіонера: {str(e)}', 'danger')
    return render_template('pensioners/form.html', pensioner=pensioner, districts=districts)

@pensioners_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    pensioner = Pensioner.query.get_or_404(id)
    try:
        db.session.delete(pensioner)
        db.session.commit()
        flash('Пенсіонера успішно видалено', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Помилка при видаленні пенсіонера: {str(e)}', 'danger')
    return redirect(url_for('pensioners.index'))