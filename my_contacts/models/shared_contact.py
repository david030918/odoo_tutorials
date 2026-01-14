from odoo import api, fields, models
from odoo.exceptions import ValidationError


class SharedContact(models.Model):
    _name = "shared.contact"
    _description = "Shared Contact"
    _rec_name = "name"

    name = fields.Char(required=True)
    email = fields.Char()
    phone = fields.Char()
    mobile = fields.Char()
    # 通用/默认职位（不针对某个客户）。
    # 具体到某个客户（client）的职位/主联系人等信息在 shared.contact.link 上维护。
    title = fields.Char(help="Default Position / Role")
    note = fields.Text()

    # 关系属性（Primary/客户内职位等）不能放在 Many2many 关系表里，
    # 需要通过中间模型 shared.contact.link 来表达。
    client_link_ids = fields.One2many(
        comodel_name="shared.contact.link",
        inverse_name="contact_id",
        string="Clients",
    )

    def action_open_detail(self):
        """在列表里点击“详情”按钮时打开当前 Contact 的表单页面。"""
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Shared Contact",
            "res_model": "shared.contact",
            "view_mode": "form",
            "res_id": self.id,
            "target": "current",
        }

    active = fields.Boolean(default=True)

    _sql_constraints = [
        # 你可以按业务决定是否需要“唯一”，比如同名同邮箱不允许重复
        # ("uniq_email", "unique(email)", "Email must be unique."),
    ]

    @api.constrains("email")
    def _check_email(self):
        for rec in self:
            if rec.email and "@" not in rec.email:
                raise ValidationError("Invalid email format.")