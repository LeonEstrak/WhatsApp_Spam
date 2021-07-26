# WhatsApp_Spam

A Whatsapp Spam program made using Python and Selenium.

- Send Messages to either a specific person or a group
- Send just a single message over and over or spam a series of messages in a particular order

## How it Works

- It finds the target user from your list of contacts by using `xpath`
- After the target user is found, a synthetic mouse click event is dispatched which opens the chat message box of the target
- Another synthetic mouse click event is dispatched to click on the input box of the chat
- Then the file which contains the list of messages is read
- Using the ActionChains provided by Selenium, it reads a single line from the `.txt` file and types it into the Input Box and clicks on the send button
- It awaits for the specified `waitTime` and then sends the next line message in the file
- After every iteration of sending a line of message from the file and waiting, it checks if the recipient has replied with the `safeWord`
- This process repeats itself until the program is manually stopped or the recipient replies using the `safeWord` that has been defined

> **Drawback:** For the safeWord mechanism to work, it needs to updated with every compilation updated that Whatsapp Web pushes. The safeWord search is done using getting the list of all the messages that has been sent using the `className` as the identifier for the message list, this className is probably generated using a bundler or something similar of the type which causes the `classname` to update if any dependencies have changed. 

# Usage
- Install Selenium using pip 
- Download and Extract ChromeDriver in the following way
        
        Go to Settings->About Chrome, and check your Chrome Version and download accordingly from
        https://sites.google.com/chromium.org/driver/

        After downloading, extract the chromedriver and add the file to the same directory as the main.py.

        Or alternatively, you can add the path of chromedriver.exe manually in the code.

        Look for the following line in the code.

        > driver = webdriver.Chrome("//Add Path Here")


- Run the `main.py` using Python 3.X 
- A Chrome Instance would be launched in incognito mode using the `chromedriver` where you'd need to sign-in using your mobile device
- Allow whatsapp to use your microphone if it keeps popping up because otherwise it may disturb the normal functioning of the program 
