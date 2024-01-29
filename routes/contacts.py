from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils.db import db
from models.especialidad import Especialidad 

contacts= Blueprint('contacts',__name__)


@contacts.route('/paciente')
def paciente():
    return render_template('crearPaciente.html')

@contacts.route('/pacienteLista')
def listaPaciente():
    especialidades= Especialidad.query.all()
    return render_template('listarPaciente.html', especialidades=especialidades)

@contacts.route('/admin')
def admin():
    return render_template('profileAdmin.html')

@contacts.post('/new')
def add_contact():
    name= request.form['nombre']
    new_especialidad= Especialidad(name)
    db.session.add(new_especialidad)
    db.session.commit()

    flash("Epecialidad creada con exito!")

    return redirect(url_for('contacts.paciente'))

@contacts.route('/update/<id>', methods= ['POST','GET'])
def update_contact(id):
    especialidad= Especialidad.query.get(id)
    if request.method == "POST":
        especialidad.nombre= request.form['nombre']
        db.session.commit()
        flash("Epecialidad modificada con exito!")
        return redirect(url_for('contacts.listaPaciente'))
    return render_template('update.html', especialidad=especialidad)

@contacts.route('/delete/<id>')
def delete_contact(id):
    especialidad= Especialidad.query.get(id)
    db.session.delete(especialidad)
    db.session.commit()
    flash("Epecialidad eliminada con exito!")
    return redirect(url_for('contacts.listaPaciente'))
