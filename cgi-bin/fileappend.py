# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
file_append = form.getvalue('fileappend')

print("""
<html>
<body>
<h1>""")
# %s is the string placeholder, and the variables are in parenthesis
print("The file path and name is %s" % (file_append,))
print("""
</h1>
</body>
</html>
""")
f = open(file_append, "a")
f.write("\nNow the file has more content!")
f.close()

#open and read the file after the appending:
f = open(file_append, "r")
print(f.read())
f.close()