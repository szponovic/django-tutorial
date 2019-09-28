from django.test import TestCase
from example.models import Movie, Genre
from example.forms import MovieForm

class SimpleTestCase(TestCase):
    def setUp(self):
        self.genre = Genre.objects.create(name='horror')
        self.movie = Movie.objects.create(
            name='Dracula',
            year=1987,
            relased='02-11-1987',
            genre=self.genre,
        )

    def tearDown(self):
        self.movie.delete()
        self.genre.delete()

    def test_max_length(self):
        form = MovieForm(data={'name': 'X' * 200})
        self.assertFalse(form.is_valid())

    def test_str_year(self):
        form = MovieForm(data={'year': 'X' * 200})
        self.assertFalse(form.is_valid())

    def test_initial(self):
        form = MovieForm(instance=self.movie)
        self.assertEqual(form.initial['name'], self.movie.name)
        self.assertEqual(form.initial['year'], self.movie.year)
        self.assertEqual(form.initial['relased'], self.movie.relased)
        self.assertEqual(form.initial['genre'], self.movie.genre.id)

    def test_correct_form(self):
        form = MovieForm(data={'year': 2010, 'name': 'Scary Movie', 'relased': '01-01-2010', 'genre': self.genre.id})
        self.assertTrue(form.is_valid())