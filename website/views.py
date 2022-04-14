from flask import Blueprint,render_template,request,jsonify
from flask_login import login_required,current_user
from .models import List
from . import db
import json
views = Blueprint('views',__name__)


@views.route('/',methods=['GET','POST'])
@login_required
def home():
    return render_template('home.html',user=current_user)


@views.route('/add',methods=['POST'])
@login_required
def add():
    job = json.loads(request.data)
    title = job['text']
    new_job = List(title=title, user_id=current_user.id)
    db.session.add(new_job)
    db.session.commit()
    return jsonify({})

@views.route('/delete',methods=['POST'])
@login_required
def delete():
    job = json.loads(request.data)
    id = job['id']
    job = List.query.get(id)
    if job:
        if job.user_id == current_user.id:
            db.session.delete(job)
            db.session.commit()
    return jsonify({})