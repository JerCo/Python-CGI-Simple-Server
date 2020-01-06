# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
first_name = form.getvalue('firstname')

print("""
<html>
<body>
<h1>""")
# %s is the string placeholder, and the variables are in parenthesis
print("Hello %s" % (first_name,))
print("""
</h1>
</body>
</html>
""")