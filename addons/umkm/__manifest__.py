{
    'name': 'UMKM',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Module for managing UMKM 11 Desa Binaan',
    'description': 'This module allows managing profiles for Micro, Small, and Medium Enterprises (UMKM).',
    'author': 'Fauzan',
    'depends': ['base', 'mail', 'hr'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/pelaku_umkm_views.xml',
        'views/products_views.xml',
        'views/umkm_profile_views.xml',
        'views/expert_classes_views.xml',
    ],
    'installable': True,
    'application': True,
    'category': 'Custom'
}