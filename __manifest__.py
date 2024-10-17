{
    'name': 'Pesantren',
    'version': '1.0',
    'summary': 'Pesantren',
    'description': """
        oke.
    """,
    'category': 'Pesantren',
    'author': 'Dil',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/guru_views.xml',
        'views/santri_views.xml',
        'views/room_views.xml',
    ],
    'sequence': -2,
    'installable': True,
    'application': True,
}
