from connect_db import sb 
def list_books():
    resp = sb.table("books").select("*").order("book_id", desc=False).execute()
    return resp.data
 
if __name__ == "__main__":
    books = list_books()
    if books:
        print("Products:")
        for b in books:
            if b["stock"] > 0:
                print(f"{b['book_id']}: {b['title']} (author:{b['author']}) — {b['category']} — stock: {b['stock']}")
    else:
        print("No products found.")
 
 