from api import db


class WordSearch(db.Model):
    """Model for word_search table
    Args:
        Param1(object) : to create model of table

    """
    __tablename__ = "word_search"

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), unique=True, nullable=False)
    frequency = db.Column(db.String(100), nullable=False)

    def __init__(self, word, frequency):
        self.word = word
        self.frequency = frequency

    def __repr__(self):
        """Create string representation of object
        Args:
            Param1(object) : self - return string representation of object

        Returns:
            Param1(str) : string representation

        """
        return "User('{}','{}','{}')".format(self.id, self.word, self.frequency)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'word': self.word,
            'frequency': self.frequency,
        }
