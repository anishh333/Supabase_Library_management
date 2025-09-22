from connect_db import sb 
def add_member(name, email):
    payload = {"name": name, "email":email}
    resp = sb.table("members").insert(payload).execute()
    return resp.data
 
if __name__ == "__main__":
    name = input("Enter product name: ").strip()
    email = input("Enter email : ").strip()
 
    created = add_member(name, email)
    print("Inserted:", created)