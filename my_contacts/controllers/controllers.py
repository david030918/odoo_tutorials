from odoo import http


class MyContacts(http.Controller):
    @http.route('/my_contacts/my_contacts', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/my_contacts/my_contacts/objects', auth='public')
    def list(self, **kw):
        return http.request.render('my_contacts.listing', {
            'root': '/my_contacts/my_contacts',
            'objects': http.request.env['my_contacts.my_contacts'].search([]),
        })

    @http.route('/my_contacts/my_contacts/objects/<model("my_contacts.my_contacts"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('my_contacts.object', {
            'object': obj
        })

