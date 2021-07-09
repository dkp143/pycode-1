email = input("Enter Your Email : ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format = (f"Your Username is '{username}' and Your Domain name is '{domain_name}'")
print(format)