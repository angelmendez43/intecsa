# -*- coding: utf-8 -*-

{
    'name': 'Intecsa',
    'version': '1.0',
    'category': 'Hidden',
    'sequence': 6,
    'summary': 'Módulo para Intecsa',
    'description': """

""",
    'depends': ['base','sale','purchase', 'project', 'web_studio', 'industry_fsm_report','stock','account','account_reports','account_gt'],
    'data': [
        'views/res_partner_views.xml',
        'views/report_financial.xml',
        'views/account_journal_views.xml',
        'report/cotizacion_sale_order.xml',
        'report/report_hoja_servicios.xml',
        'report/report_entrada_ajustes.xml',
        'report/report_salida_ajustes.xml',
        'report/report_nota_entrega.xml',
        'report/pago_entrada.xml',
        'report/pago_efectuado.xml',
        'report/comprobante_pago.xml',
        'report/pos_session_report.xml',
        'security/groups.xml',
        'views/report.xml',
        'data/globatronics_report_data.xml',
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
        'views/res_bank_views.xml'
    ],
    'assets': {
        'account_reports.assets_financial_report': [
            'intecsa/static/src/scss/account_report_print.scss',
        ]
    },
    'installable': True,
    'auto_install': False,
}
