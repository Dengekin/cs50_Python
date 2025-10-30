answer = input("File name: ").strip().lower()

#extension = answer.split(".")[-1]
#extension = answer.rsplit(".",1)[-1]

"""
if answer.endswith(".gif"):
    print("image/gif")
elif answer.endswith(".jpg"):
    print("image/jpeg")
elif answer.endswith(".jpeg"):
    print("image/jpeg")
elif answer.endswith(".png"):
    print("image/png")
elif answer.endswith("pdf"):
    print("application/pdf")
elif answer.endswith("txt"):
    print("application/pdf")
elif answer.endswith("zip"):
    print("application/zip")
else:
    print("application/octet-stream")
"""

ext = answer.rsplit(".",1)[-1] if "." in answer else ""

mimes = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}

print (mimes.get(ext,"application/octet-stream"))
