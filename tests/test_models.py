import unittest
from database.connection import get_db_connection
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_author_init(self):
        conn = get_db_connection()
        self.author = Author(1, 'John Doe')
        self.assertEqual(self.author.id, 1)
        self.assertEqual(self.author.name, 'John Doe')

    def test_author_add_author(self):
        author1 = Author(id=1, name="John Doe")
        author2 = Author(id=2, name="Jane Doe")
        self.assertEqual(author1.name, "John Doe")
        self.assertEqual(author2.name, "Jane Doe")

    def test_author_id_property(self):
        author = Author(id=1, name="John Doe")
        self.assertEqual(author.id, 1) 

    def test_author_name_property(self):
        author = Author(id=1, name="John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_author_repr(self):
        author = Author(1, "John Doe")
        self.assertEqual(str(author), "<Author John Doe>") 

    def test_get_author_id(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.get_author_id(), 1)  

    def test_id_setter(self):
        obj = Author(123, "John Doe")
        obj.id = 123
        self.assertEqual(obj.id, 123)

    def test_name_setter(self):
        obj = Author(123, "John Doe")
        self.assertEqual(obj.name, "John Doe")        
        
    def test_article_author_property(self):
        author = Author(name="John Doe", id=1)
        
    def test_magazine_creation(self):
        magazine = Magazine(id= 1, name="Tech Weekly", category="Technology")
        self.assertEqual(magazine.name, "Tech Weekly")

    def test_magazine_init(self):
        magazine = Magazine(1, "Tech Weekly", "Tech")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Tech")

    def test_id_property(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.id, 1)

    def test_name_property(self):
        magazine = Magazine(1, "Tech Weekly", "Technology")
        self.assertEqual(magazine.name, "Tech Weekly")

    def test_magazine_category_property(self):
        magazine = Magazine(1, "Tech Weekly", "Tech")
        self.assertEqual(magazine.id, 1)
        self.assertEqual(magazine.name, "Tech Weekly")   
        self.assertEqual(magazine.category, "Tech")

if __name__ == "__main__":
    unittest.main()
