# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
file_name = form.getvalue('filename')

print("""
<html>
<body>
<h1>""")
# %s is the string placeholder, and the variables are in parenthesis
print("The file path and name is %s" % (file_name,))
print("""
</h1>
</body>
</html>
""")
f = open(file_name, "r")
# prints whole contents
print(f.read())
f.close()

# prints one line at a time
#for x in f:
#  print(x)

