# -*- coding: utf-8 -*-

from odoo import models, fields


class LibraryBook2(models.Model):
    _name = "library.book"

    name = fields.Char(string="Book")
    description = fields.Text(string="Description")
