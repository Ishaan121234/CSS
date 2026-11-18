
books = ["Alice in Wonderland", "Harry Potter and the gambler", "Geronimo Stilton", "Harry Potter"]

print("Books:", len(books), books)
print("First:", books[0], "| Last:", books[-1])               # (given) B

shelves = ["C1", "H2", "M1", "W3"]


shelf_of = {}
print("Shelf map:", shelf_of)


def where_is(book):
    """Return the shelf code, or a message if the library does not have the book."""
    
    return "?" 


for title in ["Holes", "Dune"]:                                
    print(title, "->", where_is(title))

librarian = {"name": "Ms. Manioelaa", "desk": "Front"}            
