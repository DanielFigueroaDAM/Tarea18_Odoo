from odoo import models, fields, api

class Paciente(models.Model):
    _name = "hospital.paciente"
    _description = "Gestión de Pacientes"
    _rec_name = "nombre"

    _name = fields.Char(string="Nombre Completo(Nombre y apellidos)", required=True)
    sintomas = fields.Text(string="Síntomas del paciente", required=True)

    ids_diagnosticos = fields.One2many( "hospital.diagnostico", "paciente_id", string="Diagnósticos Recibidos")