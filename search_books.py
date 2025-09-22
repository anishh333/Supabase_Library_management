from connect_db import sb
def search_books(title=None, author=None, category=None):
    query = sb.table("books").select("*")

    if title:
        query = query.ilike("title", f"%{title}%")
    if author:
        query = query.ilike("author", f"%{author}%")
    if category:
        query = query.ilike("category", f"%{category}%")

    resp = query.execute()
    return resp.data


if __name__ == "__main__":
    while True:
        print("\n=== Book Search Menu ===")
        print("1. Search by Title")
        print("2. Search by Author")
        print("3. Search by Category")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            t = input("Enter title: ").strip()
            results = search_books(title=t)
        elif choice == "2":
            a = input("Enter author: ").strip()
            results = search_books(author=a)
        elif choice == "3":
            c = input("Enter category: ").strip()
            results = search_books(category=c)
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            continue

        if results:
            print("\nSearch Results:")
            for r in results:
                print(f"ID: {r['id']} | Title: {r['title']} | Author: {r['author']} | "
                      f"Category: {r['category']} | Stock: {r['stock']}")
        else:
            print("No books found.")
