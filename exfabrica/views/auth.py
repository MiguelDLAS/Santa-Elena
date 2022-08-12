from flask import(
    render_template, Blueprint, flash, g, redirect, request, session, url_for
    )

from werkzeug.security import check_password_hash, generate_password_hash

from exfabrica.models.user import User

from exfabrica import db

auth = Blueprint('auth', __name__, url_prefix='/auth')

    #registrar un usuario 
@auth.route('/register', methods=['POST'])
def register():
    if request ():
        if request.method =='POST':
            username = request.form.get('username')
            password = request.form.get('password')
            
            user = User (username, generate_password_hash(password))

            error = None 
            if not username
            error 'se queriere nombre de usuario'
            elif not password:
                error = 'se requiere contraseña '

            user_name = user.query.filter_by(username = username).first()
            if user_name == None
                db.session.add(user)
                db.session.commit()
            else:
                error = f 'el usuario {username} ya esta registrado'
            flash (error)
        return render_template('auth/register.html')