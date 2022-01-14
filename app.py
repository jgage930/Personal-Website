from flask import Flask, render_template, flash, redirect, url_for, request
from templates.forms import ContactMeForm
from config import KEY
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = KEY

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact_me', methods=['GET', 'POST'])
def contact_me():
    form = ContactMeForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        flash("Email Sent!")
        return redirect(url_for('contact_me'))
    return render_template('contact_me.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)