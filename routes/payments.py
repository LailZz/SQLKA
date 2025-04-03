from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from models import db, Payment, Pensioner, Pension
from datetime import datetime

payments_bp = Blueprint('payments', __name__, url_prefix='/payments')

@payments_bp.route('/')
def index():
    payments = Payment.query.all()
    return render_template('payments/index.html', payments=payments)

@payments_bp.route('/<int:id>')
def show(id):
    payment = Payment.query.get_or_404(id)
    return render_template('payments/show.html', payment=payment)

@payments_bp.route('/create', methods=['GET', 'POST'])
def create():
    pensioners = Pensioner.query.all()
    pensions = Pension.query.all()
    if request.method == 'POST':
        try:
            payment_date = datetime.strptime(request.form['payment_date'], '%Y-%m-%d').date()
            payment = Payment(
                pensioner_id=request.form['pensioner_id'],
                pension_code=request.form['pension_code'],
                amount=request.form['amount'],
                payment_date=payment_date,
                additional_payment=request.form.get('additional_payment', 0.00),
                additional_info=request.form.get('additional_info', '')
            )
            db.session.add(payment)
            db.session.commit()
            flash('Виплату успішно створено', 'success')
            return redirect(url_for('payments.index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Помилка при створенні виплати: {str(e)}', 'danger')
    return render_template('payments/form.html', pensioners=pensioners, pensions=pensions)

@payments_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    payment = Payment.query.get_or_404(id)
    pensioners = Pensioner.query.all()
    pensions = Pension.query.all()
    if request.method == 'POST':
        try:
            payment.pensioner_id = request.form['pensioner_id']
            payment.pension_code = request.form['pension_code']
            payment.amount = request.form['amount']
            payment.payment_date = datetime.strptime(request.form['payment_date'], '%Y-%m-%d').date()
            payment.additional_payment = request.form.get('additional_payment', 0.00)
            payment.additional_info = request.form.get('additional_info', '')
            db.session.commit()
            flash('Виплату успішно оновлено', 'success')
            return redirect(url_for('payments.show', id=id))
        except Exception as e:
            db.session.rollback()
            flash(f'Помилка при оновленні виплати: {str(e)}', 'danger')
    return render_template('payments/form.html', payment=payment, pensioners=pensioners, pensions=pensions)

@payments_bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    payment = Payment.query.get_or_404(id)
    try:
        db.session.delete(payment)
        db.session.commit()
        flash('Виплату успішно видалено', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Помилка при видаленні виплати: {str(e)}', 'danger')
    return redirect(url_for('payments.index'))

# API endpoints
@payments_bp.route('/api')
def api_index():
    payments = Payment.query.all()
    return jsonify([{
        'payment_id': p.payment_id,
        'pensioner_id': p.pensioner_id,
        'pension_code': p.pension_code,
        'amount': float(p.amount),
        'payment_date': p.payment_date.strftime('%Y-%m-%d'),
        'additional_payment': float(p.additional_payment),
        'additional_info': p.additional_info
    } for p in payments])