# -*- coding: utf-8 -*-

{
    'name': 'Intecsa',
    'version': '1.0',
    'category': 'Hidden',
    'sequence': 6,
    'summary': 'Módulo para Intecsa',
    'description': """

""",
    'depends': ['base','sale','purchase'],
    'data': [
        'views/sale_report.xml',
        'views/res_partner_views.xml',
        'report/cotizacion_sale_order.xml'
    ],
    'assets':{},
    'installable': True,
    'auto_install': False,
}
