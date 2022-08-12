from flask import (
    render_template, Blueprint, flash, g, redirect, request,url_for)

    from werkzeug.exceptions import abort 

    from exfabrica.models.post import post
    from exfabrica,models.user import user 

    from exfabrica.views.auth import login_required

    from exfabrica import db

    exfabrica = Blueprint('exfabrica', __name__)
#obtener un usuario 
    def get_user(id):
        user = user.query.get_or-404(id)
        return user 

@exfabrica.route("/")
def index ():
    post = post.query.all()
    db.session.commit()
    return render_template('exfabrica/index.html', posts = posts)

#registrar un post
@exfabrica.route('/create', methods=('GET', 'POST'))
@login_required
def register():
    if request ():
        if request.method =='POST':
            title = request.form.get('title')
            body = request.form.get('body')
            
            post = post(g.user.id, title, body )

            error = None 
            if not title
                error ='se queriere un titulo'
            
            if error is not none
                flash(error)
            else: 
            user_name = user.query.filter_by(username = username).first()
            if user_name == None
                db.session.add(user)
                db.session.commit()
                 return redirect(url_for ('exfabrica.index'))

            flash(error)
        return render_template('exfabrica/create.html')    

    
