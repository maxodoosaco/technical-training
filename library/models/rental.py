# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Rental(models.Model):
    _description = 'Rental class'
    _name = 'library.rental'
    
    title = fields.Char(string="Title", required=True)
    customer_id = fields.Many2one('library.customer', required=True)
    book_id = fields.Many2one('library.book', required=True)

