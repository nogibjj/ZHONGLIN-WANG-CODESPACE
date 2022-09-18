# ZHONGLIN-WANG-CODESPACE
Welcome to Zhonglin's project 1 repo!!!!!! The following praph presents the basic workflow of my project.
## Workflow![2017](https://user-images.githubusercontent.com/112585430/190886983-3403aefd-1f86-4a66-87b7-0f4826da8a47.jpeg)


## Aim of the project 1:
> In this project, an ETH dataset can be accessed through codespace and webservice via click script and microservice fastapi. By using the tool I provide, users can pull the recent ETH transactions information from the dataset uploaded to databricks.
## Dataset settings:
The dataset embedded is downloaded from Kaggle called Ethereum Transactions (https://www.kaggle.com/datasets/blessontomjoseph/ethereum-transactions). ETH is a cryptocurrency which uses blockchain technology and achieves a distributed transaction. Via the tool provided by me, any users can have free access to the most recent ETH transactions.
![WechatIMG18](https://user-images.githubusercontent.com/112585430/190887488-fb5fa5d7-3308-4ca9-a718-2700227e695d.jpeg)
## Connection between Codespace and Databricks
Via setting secrets of tokens and hostname, we can obtain access to databricks cluster and running the task in the back-in server.
![WechatIMG19](https://user-images.githubusercontent.com/112585430/190887549-a1889bcb-b3f2-445c-a8af-6a316730a117.jpeg)
## Query function
To get access to and search the latest ETH transactions information, I defined a query funcion to pull data from the eth database. The default will return the most recent 15 transactions including the amount, the hash, host address.

![WechatIMG20](https://user-images.githubusercontent.com/112585430/190888153-31aa4928-8c94-4086-a61a-9a935e705d34.jpeg)
## Webservice via Fastapi
first we type the following commend in the commend line in codespace:
![image](https://user-images.githubusercontent.com/112585430/190889204-cfb704b2-c01c-482a-bfe3-237a543e908a.png)
Then open the webpage:
![WechatIMG23](https://user-images.githubusercontent.com/112585430/190889169-3e4add20-2ce4-4e97-b761-e0a7390de4db.png)
Type "query" after the "dev" in the URL bar, and wait for results to pump up
![WechatIMG25](https://user-images.githubusercontent.com/112585430/190889338-a529380c-8f16-4fff-bf39-8b0e92139031.png)
# HERE WE GO!!!!!!!
