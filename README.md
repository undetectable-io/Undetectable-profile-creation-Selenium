# Undetectable-profile-creation-Selenium

How to create Undetectable profiles with API, set proxies in profiles and connect them with Selenium using Python

With that code you can create profiles in Undetectable browser and use them with Selenium.
With special argument you can set proxies to these profiles.

You can download and try Undetectable browser for free from: https://undetectable.io 

We recommend to use our webdriver that you can download from link: 
https://undetectable.io/download/chromedriver.exe
You need to save this file in folder with other files from that repository

This script will create chosen amount of Undetectable profiles one by one, set proxies in profile (optional) and open https://undetectable.io in each profile. 
You need to install and run Undetectable browser with any paid plan that can create unlimited local profiles

<h1>How to use:</h1>

1. Install Python (you can download it from https://www.python.org/)
2. run terminal with admin rules and enter: 

```
  pip install selenium
  pip install requests
```

3. download chromedriver and put it to folder with main.py
4. enter in terminal: 

```
  python main.py [--instance AMOUNT] [--use_proxy]
    optional arguments:
    --instance AMOUNT       how many profiles you want to create (default: 1)
    --use_proxy             it will take proxy from proxies_list.txt by circle. You can add only one proxy or many proxies. 
                            script will take them one by one. (default: False) 
                            
  python main.py --use_proxy --instance 3 //Create 3 profiles with proxies and make things on sites
```
