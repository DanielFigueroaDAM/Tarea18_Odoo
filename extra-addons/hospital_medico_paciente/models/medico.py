from odoo import models, fields, api

class Medico(models.Model):
    _name = "hospital.medico"
    _description = "Gestion de Médicos"
    _rec_name = "nombre"

    name = fields.Char(string="Nombre Completo(Nombre y apellidos)", required=True)
    numero_colegiado = fields.Char(string="Número de Colegiado", required=True)

    ids_diagnostico = fields.One2many( "hospital.diagnostico", "medico_id", string="Diagnósticos Realizados")