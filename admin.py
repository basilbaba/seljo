from flask import *
from database import *
admin = Blueprint('admin', __name__)

@admin.route('/adminhome',methods=['get','post'])
def home():
	return render_template('adminhome.html')

@admin.route('/manage_training', methods=['GET', 'POST'])
def manage_training():

    data = {}

    # INSERT
    if 'submit' in request.form:

        title = request.form['title']
        img = request.form['img']
        description = request.form['description']

        q = """
        insert into training
        values(
            null,
            '%s',
            '%s',
            '%s'
        )
        """ % (title, img, description)

        insert(q)

        return redirect(url_for('admin.manage_training'))

    # DELETE
    action = request.args.get('action')
    id = request.args.get('id')

    if action == "delete":

        q = "delete from training where t_id='%s'" % (id)

        delete(q)

        return redirect(url_for('admin.manage_training'))

    # VIEW
    q = "select * from training"

    data['training'] = select(q)

    return render_template(
        "managetrainig.html",
        data=data
    )






@admin.route('/manage_gallery', methods=['GET', 'POST'])
def manage_gallery():

    data = {}

    # INSERT
    if 'submit' in request.form:

        title = request.form['title']
        image = request.form['image']
        description = request.form['description']

        q = """
        insert into gallery
        values(
            null,
            '%s',
            '%s',
            '%s'
        )
        """ % (title, image, description)

        insert(q)

        return redirect(url_for('admin.manage_gallery'))

    # DELETE
    action = request.args.get('action')
    id = request.args.get('id')

    if action == "delete":

        q = "delete from gallery where gallery_id='%s'" % (id)

        delete(q)

        return redirect(url_for('admin.manage_gallery'))

    # VIEW
    q = "select * from gallery"

    data['gallery'] = select(q)

    return render_template(
        "managegalary.html",
        data=data
    )