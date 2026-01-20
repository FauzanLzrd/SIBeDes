from odoo import models, fields

class HelloModel(models.Model):
    _name = "hello.model"
    _description = "Hello Model"

    name = fields.Char(required=True)
