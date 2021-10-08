# -*- coding: utf-8 -*-
{
    'name': 'ERP Siglo 21 Reportes',
    'version': '0.4',
    'license': 'AGPL-3',
    'summary': 'Reporteria de ERP Siglo 21',
    'author': u'ERP Siglo 21',
    'depends': ['stock','l10n_cl_edi'],
    'data': [
        'reports/paper_format.xml',
        'reports/report_picking.xml',
        'views/account_move_views'
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}
