from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Livre de la bibliotheque'

    name = fields.Char(string='Titre', required=True)
    author = fields.Char(string='Auteur (texte libre)')
    isbn = fields.Char(string='ISBN')
    publication_date = fields.Date(string='Date de publication')
    available = fields.Boolean(string='Disponible', default=True)
    author_id = fields.Many2one('library.author', string='Auteur')
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('available', 'Disponible'),
        ('borrowed', 'Emprunte'),
        ('lost', 'Perdu'),
    ], string='Etat', default='draft')