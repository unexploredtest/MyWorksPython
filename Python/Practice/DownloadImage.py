# First, import the package
import urllib.request

# Then, we need the file url and a name for the file:

address = input("Enter the address of the desired picture:")
file_name = input("Choose a name for your image:")

# Next, we define a function which will download the image:

def download_image(address, location, filename):
    Cpath = location + filename + ".png"
    urllib.request.urlretrieve(address, Cpath)

# We use the function to download the image:

download_image(address, "Images/", file_name)

print(f"The picture was seccussfuly downloaded, you can see it by going to the C:/Users/aliPMPAINT/Programs/Python/Practice/Images/{file_name}")
