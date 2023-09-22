# -*- coding: utf-8 -*-

{
    'name': 'Intecsa',
    'version': '1.0',
    'category': 'Hidden',
    'sequence': 6,
    'summary': 'Módulo para Intecsa',
    'description': """

""",
    'depends': ['base','sale','purchase', 'project', 'web_studio', 'industry_fsm_report','stock'],
    'data': [
        'views/res_partner_views.xml',
        'views/report.xml',
        'report/cotizacion_sale_order.xml',
        'report/report_hoja_servicios.xml',
        'report/report_entradas_salidas.xml',
        'report/report_entradas_salidas_general.xml',
        'report/report_nota_entrega.xml',
        'data/globatronics_report_data.xml',
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
    ],
    'assets':{},
    'installable': True,
    'auto_install': False,
}
