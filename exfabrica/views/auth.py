from os import error
    render_template, Blueprint, flash, g, redirect, request, session, url_for
    )

from werkzeug.security import check_password_hash, generate_password_hash

from exfabrica.models.user import User

from exfabrica import db

auth = Blueprint('auth', __name__, url_prefix='/auth')

#registrar un usuario 
@auth.route('/register', methods=('GET', 'POST'))
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
                 #return redirect(url_for ('auth.login'))

            else:
                error = f'El usuario {username} ya esta registrado'
            flash (error)
        return render_template('auth/register.html')

#Iniciar sesion
@auth.route('login', methods=('GET', 'POST'))
def login():
    if request ():
        if request.method =='POST':
            username = request.form.get('username')
            password = request.form.get('password')
            
            error = None 

            user = user.query.filter_by(username = username).first()

            if user  = None 
                error 'Nombre de usuario incorrecto'
            elif not check_password_hash(user.password, password):
                error = 'contraseña incorrecta'

            if error is None:
                session.clear()
                session.commit()
                return redirect(url_for ('index'))
            
            flash (error)

            return render_template('auth/login.html')

#verificacion ususrio bugeado
@auth.before_app_request
 def load_logger_in_user():
     user_id = session.get('user_id')

       if user_id is None:
            g.user = None
       else:
                g.user = User.query.get_or_404(user_id)
#cerrar sesion
@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('exfabrica.index'))

def login required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view