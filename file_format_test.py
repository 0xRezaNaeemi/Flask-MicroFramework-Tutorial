allowed_formats = {"txt", "jpg", "png"}

file_format_is_not_allowed = "index.php"
file_format_is_allowed = "index.jpg"
file_format_is_allowed_2 = "i.m.a.g.e.jpg"

def checkFileFormat(fileName):
    return "." in fileName and fileName.rsplit(".", 1)[1] in allowed_formats

print("file format is not allowed: ", checkFileFormat(file_format_is_not_allowed))
print("file format is allowed: ", checkFileFormat(file_format_is_allowed))
print("file format is allowed: ", checkFileFormat(file_format_is_allowed_2))