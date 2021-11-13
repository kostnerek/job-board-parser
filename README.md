# Job board parser
I written simple app to get me data from popular pages with job offers, because I wanted to knew immidietly if there is some new offer that suits me. Then I found out about subscribe button on those sites **¯\\_(ツ)_/¯** .
### What does it make exactly
Scraps data from popular polish job boards: [justjoin.it](http://justjoin.it "justjoin.it"), [nofluffjobs.com](http://nofluffjobs.com "nofluffjobs.com"), [solid.jobs](http://solid.jobs "solid.jobs") using selenium, and puts them in json file.
### TODO
I am planning to deploy this app to RaspberryPi, and add some notification using propably Flask
### Config
- go ahead and download [geckodriver](http://https://github.com/mozilla/geckodriver/releases "geckodriver") and put it in main directory of app
- go on and get links to sites from which you want to scrap data
- put those links in **conf.json** format them as shown below


| | site |
| ------------ | ------------ |
|  nfj  |  [NoFluffJobs](http://nofluffjobs.com "nofluffjobs.com")  |
|  jjit  |  [justjoin.it](http://justjoin.it "justjoin.it")  |
|  sj  |  [solid.jobs](http://solid.jobs "solid.jobs")  |

``` 
{
    "nfj":{
        "0":"https://nofluffjobs.com/pl/praca-it/praca-zdalna/python?criteria=city%3Dkrakow%20seniority%3Dtrainee&page=1"
    },
    "jjit": {
        "0": "https://justjoin.it/krakow/python/junior",
        "1": "https://justjoin.it/remote-poland/python/junior"
    },
    "sj":{
        "0":"https://solid.jobs/offers/it;experiences=Sta%C5%BC;cities=Krak%C3%B3w;subcategories=Python",
        "1":"https://solid.jobs/offers/it;experiences=Junior;cities=Krak%C3%B3w;subcategories=Python"
    }
}
```
- just run **main.py**
