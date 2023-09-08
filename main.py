class Library:
  def __init__(self):
    self.nbooks = 0
    self.book = []

  def addbook(self, b):
    self.book.append(b)
    self.nbooks = len(self.book)

  def details(self):
    print(f"Number of books: {self.nbooks}. And the books are:")
    for i in self.book:
      print(i)

l = Library()
l.addbook ("English")
l.addbook ("Math")
l.addbook ("Science")
l.details()
