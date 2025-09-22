from connect_db import sb
def get_member_with_borrowed_books(member_id):
    resp = (
        sb.table("members")
        .select("*, borrowed_books(*)")
        .eq("member_id", member_id)
        .execute()
    )
    return resp.data    
if __name__ == "__main__":
    member_id = int(input("Enter Member ID: "))
    member_info = get_member_with_borrowed_books(member_id)
    if member_info:
        member = member_info[0]
        print(f"Member ID: {member['member_id']}, Name: {member['name']}, Email: {member['email']}")
        borrowed_books = member.get("borrowed_books", [])
        if borrowed_books:
            print("Borrowed Books:")
            for book in borrowed_books:
                print(f"- Book ID: {book['book_id']}, Title: {book['title']}, Author: {book['author']}")
        else:
            print("No borrowed books.")
    else:
        print("Member not found.")
