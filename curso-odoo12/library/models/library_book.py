# -*- coding: utf-8 -*-

from odoo import api, models, fields, exceptions


class LibraryBook(models.Model):
    _name = "library.book"

    name = fields.Char(string="Book", default="Novo")
    description = fields.Text(string="Description")
    isbn = fields.Char("ISBN")

    category_ids = fields.One2many(comodel_name="library.category", inverse_name="book_id", string="Categoría")
    _sql_constraints = [
        ('name_uniq', 'unique (name)', '¡Nombre repetido!')
    ]
    @api.constrains("isbn")
    def check_isbn(self):
        isbn = self.search([]).mapped("isbn")
        if self.isbn and self.isbn in isbn:
            raise exceptions.ValidationError("ISBN REPETIDO")


