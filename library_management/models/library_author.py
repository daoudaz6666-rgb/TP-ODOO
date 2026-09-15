from odoo import models, fields

<<<<<<< HEAD
class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Auteur de bibliotheque'

    name = fields.Char(string='Nom', required=True)
    biography = fields.Text(string='Biographie')
    birth_date = fields.Date(string='Date de naissance')
    book_ids = fields.One2many('library.book', 'author_id', string='Livres')
=======
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
>>>>>>> 10ec73379cb3bfc326fd7c28c6c8901fbd86c5cf
