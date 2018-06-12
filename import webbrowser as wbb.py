import webbrowser as wbb
lwbb=['BackgroundBrowser', 'BaseBrowser', 'Chrome', 'Chromium', 'Elinks', 'Error', 'Galeon', 'GenericBrowser', 'Grail', 'Konqueror', 'Mozilla', 'Netscape', 'Opera', 'UnixBrowser', 'WindowsDefault', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_browsers', '_synthesize', '_tryorder', 'browser', 'get', 'iexplore', 'main', 'open', 'open_new', 'open_new_tab', 'os', 'register', 'register_X_browsers', 'shlex', 'shutil', 'subprocess', 'sys']


x=wbb.__file__()
q=wbb.__spec__
w=wbb.__cached__
print(x)
print(q)
print(w)
t=wbb._browsers
print(t)


'''
x=wbb.Mozilla() 
print(x)

x=wbb.__name__
print(x)

#x=wbb.open_new("https://elbuhost.blogspot.com/") 
#x=wbb.open_new("https://ss64.com/")
#print(x)

x=wbb.shutil
print(x)

x=wbb.get() 
print(x)

x=wbb.Elinks() 
print(x)

#x=wbb.netscape
#print(x)

#x=wbb.browser() 
#print(x)

x=wbb.open("https://elbuhost.blogspot.com/") 
print(x)

'''