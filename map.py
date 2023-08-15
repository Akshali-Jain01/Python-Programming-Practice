import webbrowser
source = input("enter source: ")
dest = input("enter destination: ")
url = 'https://www.google.com/maps/dir'
url = url +"/" + source.title()+"/"+ dest.title()
print(url)
# url = "https://www.google.com/maps/dir/Udaipur,+Rajasthan/Jaipur,+Rajasthan/data=!4m8!4m7!1m2!1m1!1s0x3967e56550a14411:0xdbd8c28455b868b0!1m2!1m1!1s0x396c4adf4c57e281:0xce1c63a0cf22e09!3e0?sa=X&ved=2ahUKEwi-36-3pN39AhVV8nMBHeOXCacQox16BAgBEBE"
webbrowser.open(url)
