# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Partner(models.Model):
    _description = 'Partner class'
    _name = 'openacademy.partner'
    
    name = fields.Char(string="Partner Name", required=True)
    is_teacher = fields.Boolean()
    