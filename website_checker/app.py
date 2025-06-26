print("WEBSITE URL CHECKER")
url = input("\n Enter a website URL: ")

if url.startswith("https://"):
    print("This website uses HTTPS (secure)")
elif url.startswith("http://"):
    print("This website uses HTTP (Not secure)")
else:
    print("This doesn't look like a complete URL")
