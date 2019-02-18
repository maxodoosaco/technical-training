# -*- coding: utf-8 -*-

from odoo import api, fields, models

class Course(models.Model):
    _description = 'Course class'
    _name = 'openacademy.course'
    
    name = fields.Char(string="Course Name", required=True)
    level = fields.Integer(required=True)
    