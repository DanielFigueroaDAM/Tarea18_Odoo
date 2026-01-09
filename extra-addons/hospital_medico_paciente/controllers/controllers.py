# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalMedicoPaciente(http.Controller):
#     @http.route('/hospital_medico_paciente/hospital_medico_paciente', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_medico_paciente/hospital_medico_paciente/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_medico_paciente.listing', {
#             'root': '/hospital_medico_paciente/hospital_medico_paciente',
#             'objects': http.request.env['hospital_medico_paciente.hospital_medico_paciente'].search([]),
#         })

#     @http.route('/hospital_medico_paciente/hospital_medico_paciente/objects/<model("hospital_medico_paciente.hospital_medico_paciente"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_medico_paciente.object', {
#             'object': obj
#         })

