# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Book(models.Model):
    _description = 'Book class'
    _name = 'library.book'
    
    title = fields.Char(string="Title", required=True)
    author_ids = fields.Many2many('library.author', required=True)
    editor = fields.Char(required=True)
    year = fields.Integer()
    rental_ids = fields.One2many('library.rental', 'book_id')
