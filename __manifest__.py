
{
    'name': 'yousentech_accounting_partners',
    'category': 'Accounting',
    'summary': """ Ensures that the partner code is unique across all partners, preventing duplication.""",
    'description':"""   
        * Enforces uniqueness of the partner code across all partners.
        * Displays a validation error message if a duplicate partner code is detected.""",
    'author': 'yousen tech Techno Solutions, Odoo SA',
    'website': "https://www.qimamhd.com",
    'company': 'yousen Techno Solutions',
    'maintainer': 'yousen Techno Solutions',
    'depends': ['base', 'account','sale','purchase','yousentech_invoicing_partners'],
    'data': [


    #    'views/sale_order.xml',     
    #    'views/purchase_order.xml',
    ],

    'license': 'LGPL-3',
    'images': ['static/description/icon.png'],
    'sequence': '-100',
    'installable': True,
    'auto_install': False,
    'application': True,
}
