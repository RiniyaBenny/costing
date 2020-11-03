# -*- coding: utf-8 -*-
from odoo import fields, models

class Pricelist(models.Model):
    _inherit = 'res.currency'

    # Add a new column to the res.currency model, by default pricelist does not
    # exist
    pricelist = fields.Char(string='Pricelist')