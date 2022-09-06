import re
from flask import Blueprint, render_template, request, flash, redirect, url_for, session, g
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy.sql import func
from datetime import timedelta

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email_address=email).first()
        if user:
            if user.failed_login_attempts < 3:
                if user.is_active:
                    if check_password_hash(user.password, password):
                        flash('Logged in successfully', category='success')
                        login_user(user)
                        user.failed_login_attempts = 0
                        db.session.commit()
                        #session.permanent = True
                        return redirect(url_for('views.home'))
                    else:
                        user.failed_login_attempts = user.failed_login_attempts + 1
                        db.session.commit()
                        flash('Your username or password is incorrect.', category='error')
                else:
                    flash('Unable to log in. Your account is locked.', category='error')
            else:
                user.is_active = False
                user.failed_login_attempts = 0
                db.session.commit()
                flash('Your account has been locked due to multiple failed login attempts. Please contact your administrator.', category='error')
        else:
            flash('Your username or password is incorrect.', category='error')
    
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    password_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        surname = request.form.get('surname')
        password = request.form.get('password')
        confirm_password = request.form.get('confirmPassword')

        user = User.query.filter_by(email_address=email).first()

        if user:
            flash('This email is already registered to an account', category='error')
        elif not re.search(email_regex, email):
            flash('Email does not match email pattern', category='error')
        elif len(first_name) < 1:
            flash('First Name cannot be empty', category='error')
        elif len(surname) < 1:
            flash('Surname cannot be empty', category='error')
        elif password != confirm_password:
            flash('Passwords must match', category='error')
        elif not re.search(password_regex, password):
            flash('Password must be at least 8 characters and contain at least one uppercase, one number and one special character', category='error')
        else:
            # Add User
            new_user = User(email_address = email, first_name = first_name, surname = surname, password = generate_password_hash(password, method='sha256'), is_active = True, is_admin = False)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash('User account added', category='success')
            
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)