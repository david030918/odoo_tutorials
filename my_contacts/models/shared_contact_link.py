from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SharedContactLink(models.Model):
    """带属性的多对多关系：Client(res.partner) ↔ Shared Contact(shared.contact)

    需求：关系表上需要额外字段（Primary、职位等），因此不能用纯 Many2many。
    """

    _name = "shared.contact.link"
    _description = "Shared Contact / Client Link"
    _order = "partner_id, is_primary desc, id"

    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Client",
        required=True,
        index=True,
        ondelete="cascade",
    )
    contact_id = fields.Many2one(
        comodel_name="shared.contact",
        string="Contact",
        required=True,
        index=True,
        ondelete="cascade",
    )

    is_primary = fields.Boolean(string="Primary", default=False)
    role_title = fields.Char(string="Position")
    note = fields.Text(string="Note")

    # 方便在 Client 页面直接看到 Contact 的基础信息（只读）
    contact_phone = fields.Char(related="contact_id.phone", readonly=True)
    contact_mobile = fields.Char(related="contact_id.mobile", readonly=True)
    contact_email = fields.Char(related="contact_id.email", readonly=True)
    # contact_note = fields.Char(related="contact_id.note", readonly=True)

    _sql_constraints = [
        (
            "uniq_partner_contact",
            "unique(partner_id, contact_id)",
            "This contact is already linked to this client.",
        ),
    ]

    @api.constrains("is_primary", "partner_id")
    def _check_one_primary_per_client(self):
        """同一个 Client 只能有一个 Primary Contact。

        如果你允许多个 primary，把这个方法删掉即可。
        """
        for rec in self.filtered(lambda r: r.is_primary and r.partner_id):
            exists = self.search_count(
                [
                    ("partner_id", "=", rec.partner_id.id),
                    ("is_primary", "=", True),
                    ("id", "!=", rec.id),
                ]
            )
            if exists:
                raise ValidationError("Only one primary contact is allowed per client.")
