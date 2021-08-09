import PySimpleGUI as sg
import time
global driver
global wtaf
wtaf = '0'
sg.theme('DarkBlue')   # Add a touch of color
# All the stuff inside your window.
layout1 = [  [sg.Text('Welcome to the AQI Reporter!')],
			[sg.Text('Please press the "AQI" button')],
#            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('AQI'), sg.Button('Cancel')] ]


# Create the Window
reporter_window = sg.Window('The AQI Reporter', layout1)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = reporter_window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
    	
    	break
    from selenium import webdriver
    from selenium.webdriver.firefox.options import Options
    #PATH = r"C:\Users\Noah\Desktop\Coding\Data\chromedriver_win32\chromedriver.exe"
    #PATH= r"C:\Users\Noah\Desktop\Coding\Data\firefox driver\geckodriver-v0.29.1-win64\geckodriver.exe"
    firefox_options = Options()
    firefox_options.headless= True
    firefox_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Firefox(executable_path=r"C:\Users\Noah\Desktop\Coding\Data\firefox_driver\geckodriver.exe", options=firefox_options)
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--window-size=1920,1080")
    # chrome_options.headless = True # also works
    #driver = webdriver.Chrome(PATH, options=chrome_options)
    #driver = webdriver.Chrome(PATH)
    driver.get("https://www.accuweather.com/en/ca/brudenell-lyndoch-and-raglan/k0j/air-quality-index/3554654")
    time.sleep(10)
    search = driver.find_element_by_class_name('aq-number')
    #time.sleep(10)
    wtaf= search.text
    layout2 = [	[sg.Text('The reported AQI is...')],
    			[sg.Text(wtaf)],
    			[sg.Button("Cancel")]]
    result_window = sg.Window('The AQI Reported', layout2)
    print(wtaf)
    driver.quit()
    while True:
    	event, values = result_window.read()
    	if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
    	
    		break
#    print('You entered ', values[0])
    print("HOLY SHIT BITCH", wtaf)

reporter_window.close()


#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
#this allows for the sleep command
#import time
#these build the path to the webdriver
#PATH = r"C:\Users\Noah\Desktop\Coding\Data\chromedriver_win32\chromedriver.exe"
#driver = webdriver.Chrome(PATH)
#this tells the driver to open a chrome window
#driver.get("https://www.accuweather.com/en/ca/brudenell-lyndoch-and-raglan/k0j/air-quality-index/3554654")
#time.sleep(5)
#search = driver.find_element_by_class_name('aq-number')
#search_text= search.text
#print(search_text)
#driver.quit()