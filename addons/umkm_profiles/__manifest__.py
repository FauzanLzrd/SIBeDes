{
    'name': 'UMKM Profiles',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Module for managing UMKM profiles',
    'description': 'This module allows managing profiles for Micro, Small, and Medium Enterprises (UMKM).',
    'author': 'Fauzan',
    'depends': ['base', 'mail', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/umkm_profile_views.xml',
        'views/pelaku_umkm_views.xml',
        'views/products_views.xml',
    ],
    'installable': True,
    'application': True,
    'category': 'Custom'
}