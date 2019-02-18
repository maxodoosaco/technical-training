# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Session(models.Model):
    _description = 'Session class'
    _name = 'openacademy.session'
    
    name = fields.Char(string="Session Name", required=True)
    teacher_id = fields.Many2one('openacademy.partner', required=True)
    course_id = fields.Many2one('openacademy.course', required=True, ondelete='restrict')
    state = fields.Selection([('draft', 'Draft'), ('final', 'Final')], default='draft')
    