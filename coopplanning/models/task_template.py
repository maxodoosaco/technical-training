# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Task_template(models.Model):
    _description = 'Task template class'
    _name = 'coopplanning.task_template'
    
    name = fields.Char(string="Name", required=True)
    people_no = fields.Integer(string="No of people", default='1')
    