##Create records
- book = Book.objects.create(title='1984',author='George Orwell', publication_year =1984)
- 
- book.save()

- This line of code create a book instance and saves it to the sqlite3 database