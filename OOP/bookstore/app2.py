from app import Database

if __name__ == "__main__":
    db = Database("OOP/bookstore/books.db")
    print(db.view())