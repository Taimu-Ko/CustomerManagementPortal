from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, current_app
from flask_login import login_required, current_user
from .models import Card, Invoice, InvoiceLineItem, User
from . import db
import json
from sqlalchemy.sql import func
import string
import random
from datetime import datetime, timedelta, date

views = Blueprint('views', __name__)

#region Home
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():      
    user = User.query.get(current_user.id)  
    return render_template("home.html", user=user)
#endregion

#region Card Views
@views.route('/cards')
@login_required
def cards():
    return render_template("cards.html", user=current_user)

@views.route('/cards/id=<int:id>&canEdit=<string:canEdit>', methods=['GET', 'POST'])
@login_required
def view_card(id, canEdit):    
    if request.method == 'GET':
        card = Card.query.get(id)
        if current_user.id == card.user_id:
            return render_template("card_info.html", user=current_user, card=card, canEdit=canEdit)
        else:
            flash('Card does not exist', category='error')
            current_app.logger.warning('User tried tried to view a card that doesnt exist or doesnt belong to them.')
            return redirect(url_for('views.cards'))
                  
    if request.method == 'POST':
        card = Card.query.filter_by(id=id).first()
        if card:
            card_name = request.form.get('cardName')

            if current_user.id == card.user_id:
                card.card_name = card_name
                db.session.commit()
                flash('Successfully updated card details', category='success')
                current_app.logger.info('User successfully updated a card.')
                
                return redirect(url_for('views.cards'))
       
    return render_template("card_info.html", user=current_user, card=card, canEdit=canEdit)

@views.route('/cards/add', methods=['GET', 'POST'])
@login_required
def add_card():
    if request.method == 'POST':
        card_number = request.form.get('cardNumber')
        card_name = request.form.get('cardName')
        card_status = request.form.get('status')
        expiry_date = datetime.now().date() + timedelta(weeks=216)
        
        card = Card.query.filter_by(card_number = card_number).first()

        if len(card_name) > 30:
            flash('Card name must be 30 characters or less', category='error')
            current_app.logger.warning('User supplied invalid card name.')
        elif card_status != 'Pending':
            flash('Card status must be \'Pending\' for new cards', category='error')
            current_app.logger.warning('User supplied incorrect card status.')
        elif card:
            flash('Card number already exists', category='error')
            current_app.logger.warning('User supplied incorrect card number.')
        else:
            # Add Card
            new_card = Card(card_number = card_number, status = card_status, card_name = card_name, expiry_date = expiry_date, user_id = current_user.id)
            db.session.add(new_card)
            db.session.commit()
            flash('Card added', category='success')
            current_app.logger.warning('User successfully added a new card.')
            return redirect(url_for('views.cards'))
        
    card_number = getAndCheckCardNumber(11)
        
    return render_template("card_info.html", user=current_user, newCard = 'Y', cardNumber = card_number)

@views.route('/cards/delete', methods = ['POST'])
def delete_card():
    card = json.loads(request.data)
    cardId = card['cardId']
    card = Card.query.get(cardId)
    
    if card:
        if card.user_id == current_user.id:
            db.session.delete(card)
            db.session.commit()
            flash('Card deleted', category='success')
            current_app.logger.info('User successfully deleted a card.')
        
    return jsonify({})
#endregion

#region Invoice Views
@views.route('/invoices')
@login_required
def invoices():
    return render_template("invoices.html", user=current_user)

@views.route('/invoices/id=<int:id>')
@login_required
def view_invoice(id):    
    if request.method == 'GET':
        invoice = Invoice.query.get(id)
        if invoice:
            if invoice.user_id != current_user.id:
                flash("Invoice does not exist", category="error")
                current_app.logger.warning('User tried to view an invoice that doesnt exist or doesnt belong to them.')
                return redirect(url_for('views.invoices'))          
        
            return render_template("invoice_info.html", user=current_user, invoice=invoice)
#endregion

#region Admin
@views.route('/admin')
@login_required
def admin():
    logged_in_user = User.query.get(current_user.id)
    if(logged_in_user.is_admin):
        users = User.query.all()
        return render_template("admin.html", user=current_user, users=users)
    return redirect(url_for('views.home'))

@views.route('/admin/delete', methods = ['POST'])
def delete_user():
    user = json.loads(request.data)
    userId = user['userId']
    delete_user = User.query.get(userId)
    
    if delete_user:
        if current_user.is_admin:
            # Delete Invoice and Invoice Line Items
            invoices = Invoice.query.filter_by(user_id = userId).all()
            for i in invoices:
                line_items = InvoiceLineItem.query.filter_by(invoice_id = i.id).all()
                for ili in line_items:
                    db.session.delete(ili)
                # Delete Invoice
                db.session.delete(i)           
            # Delete Cards
            cards = Card.query.filter_by(user_id = userId).all()
            for c in cards:
                db.session.delete(c)
            # Delete User
            db.session.delete(delete_user)
            db.session.commit()
            flash('User deleted', category='success')
            current_app.logger.info('All users data has been deleted.')
    return jsonify({})  

@views.route('/admin/lock', methods = ['POST'])
def lock_user():
    user = json.loads(request.data)
    userId = user['userId']
    lock_user = User.query.get(userId)
    
    if lock_user:
        if current_user.is_admin:
            if lock_user.is_active:
                lock_user.is_active = False
                flash('User account unlocked', category='success')
                current_app.logger.info('User has been unlocked.')
            else:
                lock_user.is_active = True
                flash('User account locked', category='success')
                current_app.logger.info('User has been locked.')
            db.session.commit()
 
    return jsonify({})
#endregion

#region Private Functions
def getAndCheckCardNumber(length):
    card_number = '63562900' + get_random_card_number(11)
    card = Card.query.filter_by(card_number = card_number).first()
    if card:
        getAndCheckCardNumber(length)
    else:
        return card_number

def get_random_card_number(length):
    numbers = string.digits
    result_number = ''.join(random.choice(numbers) for i in range(length))
    return result_number
#endregion