# -*- coding: utf-8 -*-
{
    'name': "Purchase Order Line Wizard",

    'summary': """
        Wizard Purchase Order Line
    """,

    'author': "Aloh",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

    # always loaded
    'data': [
        # 'views/views.xml',
        # 'views/product_view.xml'
        'views/purchase_order_line_wizard_view.xml'
    ],
    'installable': True,
    'application': True,
    # only loaded in demonstration mode

}
