{
    'name': 'Doggo Hotel',
    'version': '1.0',
    'sequence': 0,
    'depends': ['mail', 'product'],
    'summary': "Doggo Hotel",
    'description': """
    Dog hotel for your little friends to stay when you go abroad.
    """,
    'category': 'Hotel',
    'demo': [],
    'data': ['security/ir.model.access.csv',
             'data/doggo_tag.xml',
             'data/doggo.tag.csv',
             'data/sequence_data.xml',
             'wizard/cancel_reservation_view.xml',
             'views/menu.xml',
             'views/guest_view.xml',
             'views/female_guest_view.xml',
             'views/reservation_view.xml',
             'views/doggo_tag_view.xml',
             'views/res_config_settings_views.xml'
             ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
        'web.assets_backend': [
            'doggo_hotel/static/src/js/popup.js',
        ],
    },
    'license': 'LGPL-3',
}
