from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from models import db, District, Pensioner

districts_bp = Blueprint('districts', __name__, url_prefix='/districts')

@districts_bp.route('/')
def index():
    districts = District.query.all()
    return render_template('districts/index.html', districts=districts)

@districts_bp.route('/<int:id>')
def show(id):
    district = District.query.get_or_404(id)
    pensioners = Pensioner.query.filter_by(district_code=id).all()
    return render_template('districts/show.html', district=district, pensioners=pensioners)

@districts_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            district = District(
                district_code=request.form['district_code'],
                district_name=request.form['district_name']
            )
            db.session.add(district)
            db.session.commit()
            flash('Район успішно створено', 'success')
            return redirect(url_for('districts.index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Помилка при створенні району: {str(e)}', 'danger')
    return render_template('districts/form.html')

@districts_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    district = District.query.get_or_404(id)
    if request.method == 'POST':
        try:
            district.district_name = request.form['district_name']
            db.session.commit()
            flash('Район успішно оновлено', 'success')
            return redirect(url_for('districts.show', id=id))
        except Exception as e:
            db.session.rollback()
            flash(f'Помилка при оновленні району: {str(e)}', 'danger')
    return render_template('districts/form.html', district=district)

@districts_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    district = District.query.get_or_404(id)
    try:
        db.session.delete(district)
        db.session.commit()
        flash('Район успішно видалено', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Помилка при видаленні району: {str(e)}', 'danger')
    return redirect(url_for('districts.index'))

# API endpoints
@districts_bp.route('/api')
def api_index():
    districts = District.query.all()
    return jsonify([{
        'district_code': d.district_code, 
        'district_name': d.district_name
    } for d in districts])