from selenium import webdriver
import time




def loginBOT(usr, pas,name1):

    br = webdriver.Chrome()
    br.maximize_window()
    br.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin/")

    user = br.find_element_by_css_selector("#identifierId")
    user.clear()
    user.send_keys(usr)   

    btn = br.find_element_by_css_selector("#identifierNext")
    btn.click()
    time.sleep(2)
    
    passwd = br.find_element_by_name("password")
    passwd.clear()
    passwd.send_keys(pas)
    
    
    btn1 = br.find_element_by_css_selector("#passwordNext")
    btn1.click()
    time.sleep(2)
    
        
    
    btn1 = br.find_element_by_css_selector(" .aic .z0 div")
    btn1.click()
    time.sleep(2)
    
    
    user = br.find_element_by_css_selector(".oj div textarea  ")
    user.clear()
    user.send_keys(name1) 
    
    user = br.find_element_by_css_selector(".aoD.az6  input ")
    user.clear()
    user.send_keys("BOT Mail")    
    
    user = br.find_element_by_css_selector(".Ar.Au div ")
    user.clear()
    user.send_keys("Hello, its my first BOT!!!")  
    
    btn1 = br.find_element_by_css_selector("tr.btC td:nth-of-type(1) div div:nth-of-type(2) ")
    btn1.click()
    time.sleep(2)
        
if __name__ == "__main__":
	loginBOT('raghavbang2012@gmail.com', '705Raghav$','raghavbang2012@gmail.com')