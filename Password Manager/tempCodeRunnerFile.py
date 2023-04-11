    if is_ok:
            with open(f"./Password Manager/bimil.txt", 'a') as file:
                content = f"{website} | {email}  | {pw} \n"
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                file.write(content)
