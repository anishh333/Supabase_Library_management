from connect_db import sb 
 
def add_books(title, author, category, stock):
    payload = {"title": title, "author": author, "category": category, "stock": stock}
    resp = sb.table("books").insert(payload).execute()
    return resp.data
 
if __name__ == "__main__":
    title = input("Enter product name: ").strip()
    author = input("Enter author: ").strip()
    category = input("Enter category : ").strip()
    stock = int(input("Enter stock: ").strip())
 
    created = add_books(title,author,category ,stock)
    print("Inserted:", created)