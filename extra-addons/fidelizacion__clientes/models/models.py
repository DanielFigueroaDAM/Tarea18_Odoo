# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    codigo_socio = fields.Char(string='Código de Socio')

    nivel_fidelidad = fields.Char(
        string='Nivel de Fidelidad',
        compute='_calcular_nivel_fidelidad',
        store=True,
        readonly=True
    )

    @api.depends('codigo_socio')
    def _calcular_nivel_fidelidad(self):
        for record in self:
            if not record.codigo_socio:
                record.nivel_fidelidad = "ESTANDAR"
            elif record.codigo_socio.startswith('G'):
                record.nivel_fidelidad = "GOLD"
            else:
                record.nivel_fidelidad = "PREMIUM"

