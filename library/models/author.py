# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Author(models.Model):
    _description = 'Author class'
    _name = 'library.author'
    
    name = fields.Char(string="Name", required=True)
    #book_ids = fields.Many2many('library.book')


