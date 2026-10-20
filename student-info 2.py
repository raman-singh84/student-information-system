import getpass
import platform

print("\nSystem information")
print("student Current user:", getpass.getuser())
print("student Operating system:", platform.system())
print("student Computer name:", platform.node())