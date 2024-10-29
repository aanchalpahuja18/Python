## Magic methods in Python

class Book:
    def __init__(self,title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title or self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return f"Total pages: {self.num_pages + other.num_pages}"
    
    def __contains__(self, keyword):
        if keyword in self.title:
            return f"'{keyword}' is in {self.title}"
        
        elif keyword in self.author:
            return f"{keyword} is in {self.author}"
        
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"'{key}' is not found!"


book1 = Book("Aanchal's story", "Aanchal", 300)
book2 = Book("The Magical World", "P Pahuja", 500)
book3 = Book("The sky is pink", "C Bhagat", 200)

print(book3)
print(book1 == book2)
print(book2 > book3)
print(book3 < book1)
print(book1 + book2)
print("Aanchal" in book2)
print(book2["num_pages"])