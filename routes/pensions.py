from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from models import db, Pension, Payment

pensions_bp = Blueprint('pensions', __name__, url_prefix='/pensions')

@pensions_bp.route('/')
def index():
    pensions = Pension.query.all()
    return render_template('pensions/index.html', pensions=pensions)

@pensions_bp.route('/<int:id>')
def show(id):
    pension = Pension.query.get_or_404(id)
    payments = Payment.query.filter_by(pension_code=id).all()
    return render_template('pensions/show.html', pension=pension, payments=payments)

@pensions_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            pension = Pension(
                pension_code=request.form['pension_code'],
                pension_name=request.form['pension_name']
            )
            db.session.add(pension)
            db.session.commit()
            flash('Вид пенсії успішно створено', 'success')
            return redirect(url_for('pensions.index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Помилка при створенні виду пенсії: {str(e)}', 'danger')
    return render_template('pensions/form.html')

@pensions_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    pension = Pension.query.get_or_404(id)
    if request.method == 'POST':
        try:
            pension.pension_name = request.form['pension_name']
            db.session.commit()
            flash('Вид пенсії успішно оновлено', 'success')
            return redirect(url_for('pensions.show', id=id))
        except Exception as e:
            db.session.rollback()
            flash(f'Помилка при оновленні виду пенсії: {str(e)}', 'danger')
    return render_template('pensions/form.html', pension=pension)

@pensions_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    pension = Pension.query.get_or_404(id)
    try:
        db.session.delete(pension)
        db.session.commit()
        flash('Вид пенсії успішно видалено', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Помилка при видаленні виду пенсії: {str(e)}', 'danger')
    return redirect(url_for('pensions.index'))

# API endpoints
@pensions_bp.route('/api')
def api_index():
    pensions = Pension.query.all()
    return jsonify([{
        'pension_code': p.pension_code,
        'pension_name': p.pension_name
    } for p in pensions])