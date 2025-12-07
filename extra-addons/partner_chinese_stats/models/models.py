# -*- coding: utf-8 -*-

from odoo import models, fields, api


class partner_chinese_stats(models.Model):
    _inherit = 'res.partner'

    f_nac = fields.Date(string="Fecha de Nacimiento")
    edad = fields.Integer(string="Edad",readonly=True ,compute='_compute_edad',store=True)
    signo_chino = fields.Char(string="Signo Chino", readonly=True, compute='_calcular_chinada', store=True)

    @api.depends('f_nac')
    def _calcular_edad(self):
        for record in self:
            if record.f_nac:
                # Aquí se insertará el código para calcular la edad
                record.edad = 130
    @api.depends('f_nac')
    def _calcular_chinada(self):
        for record in self:
            if record.f_nac:
                record.signo_chino = "Sin signo"
