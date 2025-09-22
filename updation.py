from connect_db import sb

def update_member_email(member_id, new_email):
    resp = (
        sb.table("members")
        .update({"email": new_email})
        .eq("member_id", member_id)
        .execute()
    )
    return resp.data
def update_book_stock(book_id,new_stock):
    resp=(
        sb.table("books")
        .update({"stock":new_stock})
        .eq("book_id",book_id)
        .execute()
    )
    return resp.data


if __name__ == "__main__":
    member_id = int(input("Enter Member ID: "))
    new_email = input("Enter new email: ").strip()

    updated = update_member_email(member_id, new_email)
    if updated:
        print("Updated:", updated)
    else:
        print("No record updated.")

    book_id=int(input("Enter a book id"))
    new_stock=input("Enter a new Stock").strip()

    updated=update_book_stock(book_id,new_stock)
    if updated:
        print("Updated :",updated)
    else:
        print("NO record Updated")
        
