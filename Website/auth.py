from flask import Blueprint, render_template, request, flash, redirect, url_for, session, g
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email_address=email).first()
        if user:
            if user.is_active:
                if check_password_hash(user.password, password):
                    flash('Logged in successfully', category='success')
                    login_user(user)
                    #session.permanent = True
                    return redirect(url_for('views.home'))
                else:
                    flash('Your email or password is incorrect. Please try again', category='error')
            flash('Unable to log in. Your account is locked', category='error')
        else:
            flash('Your email or password is incorrect. Please try again', category='error')
    
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        surname = request.form.get('surname')
        password = request.form.get('password')
        confirm_password = request.form.get('confirmPassword')

        user = User.query.filter_by(email_address=email).first()

        if user:
            flash('This email is already registered to an account', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(first_name) < 2:
            flash('First Name must be greater than 1 characters', category='error')
        elif len(surname) < 2:
            flash('Surname must be greater than 1 characters', category='error')
        elif password != confirm_password:
            flash('Passwords must match', category='error')
        elif len(password) < 4:
            flash('Password must be greater than 3 characters', category='error')
        else:
            # Add User
            new_user = User(email_address = email, first_name = first_name, surname = surname, password = generate_password_hash(password, method='sha256'), is_active = True, is_admin = False)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash('User account added', category='success')
            
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)