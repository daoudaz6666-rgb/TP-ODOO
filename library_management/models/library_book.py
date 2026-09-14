from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Livre de la bibliothèque'

    name = fields.Char(string='Titre', required=True)
    author = fields.Char(string='Auteur')
    isbn = fields.Char(string='ISBN')
    publication_date = fields.Date(string='Date de publication')
    available = fields.Boolean(string='Disponible', default=True)