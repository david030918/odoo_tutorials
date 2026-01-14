from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    shared_contact_link_ids = fields.One2many(
        comodel_name="shared.contact.link",
        inverse_name="partner_id",
        string="Shared Contacts",
    )

    # 为了方便做筛选/标签展示，这里提供一个“只读的多对多视图”。
    # 真实关系（包含 primary/职位等）以 shared_contact_link_ids 为准。
    shared_contact_ids = fields.Many2many(
        comodel_name="shared.contact",
        compute="_compute_shared_contact_ids",
        string="Shared Contacts (computed)",
        store=False,
    )

    @api.depends("shared_contact_link_ids.contact_id")
    def _compute_shared_contact_ids(self):
        for partner in self:
            partner.shared_contact_ids = partner.shared_contact_link_ids.mapped("contact_id")
