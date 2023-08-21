# -*- coding: utf-8 -*-

{
    'name': 'Intecsa',
    'version': '1.0',
    'category': 'Hidden',
    'sequence': 6,
    'summary': 'Módulo para Intecsa',
    'description': """

""",
    'depends': ['base','sale','purchase','project','industry_fsm_report'],
    'data': [
        'views/res_partner_views.xml',
        'report/cotizacion_sale_order.xml',
        'report/report_hoja_servicios.xml',
        'data/globatronics_report_data.xml',
        'views/report.xml',
    ],
    'assets':{},
    'installable': True,
    'auto_install': False,
}
