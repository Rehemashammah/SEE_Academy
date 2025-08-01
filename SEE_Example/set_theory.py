admins = {"Rehema", "Shammah"}
editors = {"Shammah", "Ombeka"}

#Combine both groups
all_users = admins.union(editors)
print("All Users:", all_users)

#Who is both admin and editor?
both_roles = admins.intersection(editors)
print("Users with both roles:", both_roles)

admin_only = admins.difference(editors)
print("Admin only:", admin_only)