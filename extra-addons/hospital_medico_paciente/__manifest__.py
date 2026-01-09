# -*- coding: utf-8 -*-
{
    'name': "hospital_medico_paciente",

    'summary': "Módulo que permite gestionar la relación entre médicos y pacientes",

    'description': """
        Módulo para gestionar la relación entre médicos y pacientes en un entorno hospitalario.
    """,

    'author': "Daniel Figueroa Vidal",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/paciente_views.xml',
        'views/medico_views.xml',
        'views/diagnostico_views.xml',
        'views/views.xml',
        'views/templates.xml',
        'demo/demo.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

