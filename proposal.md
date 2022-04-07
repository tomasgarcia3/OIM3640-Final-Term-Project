# Project Proposal

## 1. The Big Data
My idea for this project is to build a trading bot to automate cryptocurrency trading. Essentially the bot will fetch live data from an exchange, then apply a trading algorithm on the data and finally execute the trade (buy or sell position). Some of the concepts I will explore would be to use an exchange with an open API which I could use to fetch data, then be able to process the desired data through an algorithm represented by one or multiple functions. Finally, I would use the API and key I have from the exchange to place an order with my account. The minimum viable product would be to have everything running with a simple algorithm that uses a few technical indicators. If time allows, I would potentially want to make this algorithm more complex and even implement trading factors that go beyond technical analysis. I know that some traders have built bots to trade based on social media trends and that could potentially be interesting to implement getting data from social media platforms like tweeter. However, this is taking the project to a stretch and my first objective is to just build a program that trades using a simple algorithm.

## 2. Learning Goal
As I work on this project individually, I hope to make a lot of progress in my python programming skills through the development of this project. Essentially I believe this project would let me understand better the concept of APIs as I will be fetching a lot of live data and also interacting with the site through the API. Furthermore, I also think I will improve my ability to create models to analyze data and translate trading strategies into python code. Overall I think it will be a great learning experience that would shape my logical skills when writing python code. 

## 3. Implementing Plan
I have already looked at different trading bots that are connected to exchanges to fetch the data. As of now, I have looked into a crypto exchange trading library called CCXT and Binance exchange to collect the price data of the desired cryptocurrency. So the plan starts with the data collection, after that the desired measures will go through the function analyzing the data and a trading recommendation will be returned. If the algorithm recommends buying it will then buy or keep holding if the currency is already in the portfolio. If the recommendation is negative, then the currency will be sold or stay sold if it was not in the portfolio already. For this, I need to find the exchange that I will use to trade the currencies.

## 4. Project Schedule
As of this week, I have roughly 3.5 weeks to complete this project. I have divided the project into three main stems: Step one is to connect to exchange and fetch the data. Step two is to apply a trading algorithm to the data. Finally, step three is to execute the trade. With these steps defined, I will plan to accomplish one step every week. In the end, having roughly half a week to a week left for final tests and debugging. Potentially being able to improve the algorithm used for trading and make profit. 

## 5. Collaboration Plan
I am working on this assignment by myself so I do not need a collaboration plan. In terms of time management, I do not plan to use a software. I will work on my weekly tasks during my free time starting at the beginning of each week and trying not to leave too much work for the weekend. This will give me time to spread and stress less when the weekend is approaching since I know I will have time to keep working and will be able to ask for help in office hours if needed. 

## 6. Risks
My biggest risk for the success of this project falls into how well I can develop the trading algorithm. My goal is to build a trading bot that is profitable, but I understand how challenging that could be. I want to take this as a learning experience and try my best to build the best algorithm to the best of my ability in the time I have to work on this project. Regarding the steps, I believe I will be able to achieve them even if I need to ask for help. Overall I think the tasks and goals I have proposed are feasible and I'm excited to see what would be the outcome of this project. 

## 7. Additional Course Content
I think we have already covered most of the topics I need to develop this project. I will apply all my learnings from the exercises and assignments we have done in class. I understand well how APIs work and how the data is structured, and the ways to read and analyze that data. The only thing I might be asking for help or self-teaching is how to use the API to send buy or sell signals to the exchange platform in order to execute my trade. 