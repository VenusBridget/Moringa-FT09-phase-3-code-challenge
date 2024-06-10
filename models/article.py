from database.connection import get_db_connection

class Article:
    # def __init__(self, id, title, content, author_id, magazine_id):
    #     self.id = id
    #     self.title = title if title else "Untitled"
    #     self.content = content
    #     self.author_id = author_id
    #     self.magazine_id = magazine_id

    # def __repr__(self):
    #     return f'<Article {self.title}>'
    
    # @property
    # def title(self):
    #     return self._title
    
    # @title.setter
    # def title(self, title):
    #     if hasattr(self, title):
    #         raise TypeError("Title cannot be changed")
    #     elif isinstance(title, str) and (5<= len(title) <=50):
    #         self._title = title
    #     else:
    #         raise TypeError("title must be a non-empty string")

    # @property
    # def content(self):
    #     return self._content
    
    # @content.setter
    # def content(self, content):
    #     if isinstance(content, str) and len(content):
    #         self._content = content
    #     else:
    #         raise ValueError(
    #             "Content must be a non-empty string"
    #         )
        
    # @property
    # def author_id(self):
    #     return self._author_id
    
    # @author_id.setter
    # def author_id(self, author_id):
    #     from models.author import Author
    #     if isinstance(author_id, int) and Author.find_by_id(author_id):
    #         self._author_id = author_id
    #     else:
    #         raise ValueError(
    #             "Author ID must reference an author in the database")
        
    # @property
    # def magazine_id(self):
    #     return self._magazine_id
    
    # @magazine_id.setter
    # def magazine_id(self, magazine_id):
    #     from models.magazine import Magazine
    #     if type(magazine_id) is int and Magazine.find_by_id(magazine_id):
    #         self._magazine_id = magazine_id
    #     else:
    #         raise ValueError("Magazine ID must reference a magazine in the database")
    # def author(self):
    #     from models.author import Author
    #     conn = get_db_connection()
    #     CURSOR = conn.cursor()
    #     """retrieves and returns the author who wrote this article"""
    #     sql = """
    #         SELECT a.*
    #         FROM authors a
    #         INNER JOIN articles ar ON ar.author = a.id
    #         WHERE ar.id = ?
    #     """
    #     CURSOR.execute(sql, (self.id))
    #     author_data = CURSOR.fetchone()

    #     if author_data:
    #         return Author(*author_data)
    #     else:
    #         return None

    # def magazine(self):
    #     from models.magazine import Magazine
    #     conn = get_db_connection()
    #     CURSOR = conn.cursor()
    #     """retrieves and returns the magazine in which this article is published"""
    #     sql = """
    #         SELECT m.*
    #         FROM magazines m
    #         INNER JOIN articles ar ON ar.magazine = m.id
    #         WHERE ar.id = ?
    #     """
    #     CURSOR.execute(sql, (self.id))
    #     magazine_data = CURSOR.fetchone()

    #     if magazine_data:
    #         return Magazine(*magazine_data)
    #     else:
    #         return None
        
    # @classmethod
    # def create(cls, author, magazine, title):
    #     with get_db_connection() as conn:
    #         cursor = conn.cursor()
    #         cursor.execute('''
    #             INSERT INTO articles (author_id, magazine_id, title)
    #             VALUES (?,?,?)
    #         ''', (author.id, magazine.id, title))
    #         conn.commit()

    # @classmethod
    # def fetch_by_id(cls, id):
    #     with get_db_connection() as conn:
    #         cursor = conn.cursor()
    #         cursor.execute('SELECT * FROM articles WHERE id =?', (id,))
    #         article = cursor.fetchone()
    #         return cls(*article) if article else None

    def _init_(self, id, author_id, magazine_id, title, content, conn):
        self.id = id
        self.author_id = author_id
        self.magazine = magazine_id
        self.title = title
        self.content = content
        self.conn = conn


    def _repr_(self):
        return f'<Article {self.title}>'

    def get_title(self):
        return self._title

    def set_title(self, title):
        if type(title) is not str:
            raise ValueError("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = title

    title = property(get_title, set_title)

    @classmethod
    def create(cls, author, magazine, title):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO articles (author_id, magazine_id, title)
                VALUES (?,?,?)
            ''', (author.id, magazine.id, title))
            conn.commit()

    @classmethod
    def fetch_all(cls):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM articles')
            articles = cursor.fetchall()
            return [cls(*article) for article in articles]

    @classmethod
    def fetch_by_id(cls, id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM articles WHERE id =?', (id,))
            article = cursor.fetchone()
            return cls(*article) if article else None
        
    @classmethod
    def get_author(cls, id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT a.name
                FROM authors a
                JOIN articles ar ON a.id = ar.author_id
                WHERE ar.id = ?
            ''', (id,))
            return cursor.fetchone()[0]

    @classmethod
    def get_magazine(cls, id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT m.name
                FROM magazines m
                JOIN articles ar ON m.id = ar.magazine_id
                WHERE ar.id = ?
            ''', (id,))
            return cursor.fetchone()[0]