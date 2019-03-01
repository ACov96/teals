from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

students = {}

with open('./repls.csv', 'r') as f:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    actions = ActionChains(driver)
    line = f.readline()
    while line:
        name = line.split(',')[0]
        repl = line.split(',')[1]

        # Load the repl
        driver.get(repl)
        sleep(10)

        # Grab the run button and the terminal
        runButton = driver.find_element_by_css_selector('svg.run-icon-svg')
        term = driver.find_element_by_css_selector('canvas.xterm-cursor-layer')

        # Run the program
        runButton.click()
        sleep(5)

        # Send input to the program
        seq = actions.click(term)
        for i in range(10):
            seq.send_keys(str(i)).key_down(Keys.RETURN)
        seq.perform()
        students[name] = input('Notes on %s\'s program? ' % name)
        line = f.readline()
    driver.close()

print('Here are your notes:')
for key, val in students.items():
    print('%s - %s' % (key, val))
