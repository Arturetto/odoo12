# -*- coding: utf-8 -*-
{
    'name': "Report invoice testt",

    'summary': """
        Library Management
    """,

    'author': "Aloha",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        'data/paperformat.xml',
        'report/reports.xml',
        'report/account_invoice_report.xml',


    ],
    'installable': True,
    'application': True,
    # only loaded in demonstration mode

}
