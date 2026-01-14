{
    'name': 'myContacts',
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': '\nContacts import to Clients\n    ',
    'author': 'My Company',
    'website': 'https://www.yourcompany.com',
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'contacts'],
    'data':
        [
            'security/ir.model.access.csv',
            'views/views.xml',
            'views/res_partner_views.xml',
            'views/shared_contact_views.xml'
        ],
    'demo': ['demo/demo.xml'],
    'application': True,
    'installable': True
}
