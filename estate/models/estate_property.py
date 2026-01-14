from odoo import fields, models


class TestModel(models.Model):
    _name = "estate.property"

    # id = fields.Integer('Plan Name', required=True, translate=True)
    # create_uid = fields.Integer('Create Uid', translate=True)
    # create_date = fields.Datetime('Create Date', translate=True)
    # write_uid = fields.Integer('Write Uid', translate=True)
    # write_date = fields.Datetime('Write Date', translate=True)
    name = fields.Char('Plan Name', translate=True)
    description = fields.Text('Description', translate=True)
    postcode = fields.Char('postcode', translate=True)
    date_availability = fields.Date('date availability', translate=True)
    expected_price=fields.Float('expected price', translate=True)
    selling_price=fields.Float('selling price', translate=True)
    bedrooms=fields.Integer('bedrooms', translate=True)
    living_area=fields.Integer('living area', translate=True)
    facades=fields.Integer('facades', translate=True)
    garage=fields.Boolean('garage', translate=True)
    garden=fields.Boolean('garden', translate=True)
    garden_area=fields.Integer('garden area', translate=True)
    garden_orientation = fields.Selection(
        [
            ('east', 'East'),
            ('south', 'South'),
            ('west', 'West'),
            ('north', 'North')
        ],
        string='Garden Orientation'
    )