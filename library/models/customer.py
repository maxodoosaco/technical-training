# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Customer(models.Model):
    _description = 'Customer class'
    _name = 'library.customer'
    
    name = fields.Char(string="Name", required=True)
    rental_ids = fields.One2many('library.rental', 'customer_id', required=True)


