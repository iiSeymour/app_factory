from datetime import datetime

from flask import render_template_string

from . import blog


@blog.route('/latest')
def today():
    dt = datetime.now()
    return render_template_string('Today is - {{ dt | int_date }}', dt=dt)
