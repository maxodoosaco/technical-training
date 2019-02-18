# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Task(models.Model):
    _description = 'Task class'
    _name = 'coopplanning.task'
    
    task_id = fields.Many2one('coopplanning.task_template', required=True)
    partner_id = fields.Many2many('coopplanning.partner', required=True)
    recurring = fields.Boolean()
    date = fields.Date()
    