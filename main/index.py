import pkgutil

if pkgutil.find_loader("flask") is not None:
    print("Flask is installed.")
else:
    print("Flask is not installed.")
