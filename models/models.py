# -*- coding: utf-8 -*-

from odoo import models, fields, api
class Costing(models.Model):
    _name = 'costing.costing'
    _description = 'Costing'

    customer = fields.Many2one('res.users',
                                  ondelete='set null', string="Customer", index=True)
    season = fields.Char(default='Winter Season 2020-T24B11 Costing', string="Season")
    style_ref_name = fields.Char(default='PANTALOON', string="Style/Ref Name")
    prod_concept = fields.Char(string='Product Concept')
    type = fields.Selection([('prelimnary', 'Prelimnary Costing'), ('buyer_approved', 'Buyer Approved Costing'),
                             ('factory_approved', 'Factory Approved Costing')])
    company = fields.Char(string='Company')
    pricelist = fields.Many2one('res.currency', string='Pricelist')
    currency = fields.Many2one('res.currency', string='Currency')
    stage = fields.Selection([('new', 'New'), ('progress', 'Progress'),
                             ('approved', 'Approved'), ('effective', 'Effective')])
    board = fields.Char(string='Board')
    order_qty = fields.Integer(string='Order Quantity', required=True, default=0)
    size_range = fields.Char(string='Size/Range', required=True, default='OBA')
    sample_size = fields.Char(string='Sample Size', required=True, default='OBA')
    merch_div = fields.Char(string='Merch of Division')
    merch_fabric = fields.Char(string='Merch of Fabrication')
    merch_size = fields.Char(string='Merch Size Offerings')
    spec_pattern = fields.Char(string='Spec/Pattern')
    costsheetlines = fields.Many2many('costing.costsheetlines')


    class CostSheetLines(models.Model):
        _name = 'costing.costsheetlines'
        _description = 'Cost Sheet Lines'

        particulars = fields.Char(string='Particulars')
        desc = fields.Char(string='Description')
        placement = fields.Char(string='Placement')
        supplier = fields.Char(string='Supplier')
        cut_width = fields.Float(string='Cuttable Width')
        consump = fields.Float(string='Consumption')
        uom = fields.Char(string='UOM')
        curr = fields.Many2one('res.currency', string='Currency')
        cost_item = fields.Float(string='Cost of Item(Ex-works/CIF/CFR)')
        costing = fields.Selection([('fabric', 'Fabric Cost'), ('accessories', 'Accessories Cost'),
                             ('packing', 'Packing Materials Cost')])


    class CostingTypes(models.Model):
        _name = 'costing.costingtypes'
        _description = 'Costing Types'

        name = fields.Char(string="Name")
        costing_types = fields.Selection([('prelimnary', 'Prelimnary Costing'), ('buyer_approved', 'Buyer Approved Costing'),
                                 ('factory_approved', 'Factory Approved Costing')])
        prelim_costing = fields.Float(string="Prelimnary Costing")
        buyer_approved = fields.Float(string="Buyer Approved Costing")
        factory_approved = fields.Float(string="Factory Approved Costing")


    class CostingStages(models.Model):
        _name = 'costing.costingstages'
        _description = 'Costing Stages'