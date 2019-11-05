import uuid, sys, hashlib, random, string



if len(sys.argv) <= 1:
	print("Missing param: email")
	print("python gen.py <email> [<password>:optional]")
	exit()

email = sys.argv[1] if len(sys.argv) > 1 else "demo@improwised.com"
pw = sys.argv[2] if len(sys.argv) > 2 else "Secret#123"
un = uuid.uuid4()
salt = un.hex

hashed_password = hashlib.sha512(pw + salt).hexdigest()



def randomString(stringLength=8):
    """Generate a random string of fixed length """
    letters= string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.sample(letters,stringLength))

random_key = randomString(32)
custom_id  = randomString(6)

print("consumers:")
print("- id: " + str(un))
print("  custom_id: " + custom_id)
print("  username: " + email)
print("  keyauth_credentials:")
print("  - key: " + random_key)
print("  acls:")
print("  - group: listing-management-staging")
print("  - group: listing-management-prod")
print("  basicauth_credentials:")
print("  - username: " + email)
print("    password: " + hashed_password)


# print(sys.argv)
