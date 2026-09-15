{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Gestion de bibliotheque - TP Odoo',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_author_views.xml',
        'views/library_menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}