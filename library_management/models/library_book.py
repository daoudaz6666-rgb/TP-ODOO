from odoo import models, fields, api
from odoo.exceptions import ValidationError

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
    loan_ids = fields.One2many('library.loan', 'book_id', string='Emprunts')

    @api.constrains('isbn')
    def _check_isbn_length(self):
        for book in self:
            if book.isbn and len(book.isbn) != 13:
                raise ValidationError("L'ISBN doit faire exactement 13 caracteres.")

    @api.onchange('author_id')
    def _onchange_author_id(self):
        if self.author_id and not self.name:
            self.name = "Nouveau livre de %s" % self.author_id.name

    def action_borrow(self):
        for book in self:
            book.state = 'borrowed'
            book.available = False
            self.env['library.loan'].create({
                'book_id': book.id,
                'borrow_date': fields.Date.today(),
            })