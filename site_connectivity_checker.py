import urllib.request as urlib 

def connections(url):
    print("checking URL code")
    
    response = urlib.urlopen(url)
    print(f"Connected to {url} Successfuly")
    print(f"response code is :  {response.getcode()}")


iUrl=input("Enter The Url ")
connections(iUrl)