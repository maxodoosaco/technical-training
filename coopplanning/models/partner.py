# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Partner(models.Model):
    _description = 'Partner class'
    _name = 'coopplanning.partner'
    
    name = fields.Char(string="Name", required=True)
    recurring = fields.Boolean(string="Recurring", required=True)
    