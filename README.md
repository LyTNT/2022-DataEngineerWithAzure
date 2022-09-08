# 2022-DataEngineerWithAzure
Take note the process of PROJECT execution

STEP1: Set up virtual env on cmd
1. Transfer to folder of Project
pip install virtualenv 

python -m venv virtualenv # open virtual env
pip install virtualenv[all] # install dependency

2. Open pycharm, open virtual env to process data
Syntax:
cd virtualenv/Scripts
activate

3. Issue solved: appear 2 virtual environments in the same time Or Pycharm open wrong vir env
Reason: maybe cause by Anaconda
Solution: 
	Ctrl +alt+S
	Choose your Python Intepreter instead of Anaconda
	refresh and access the virtual env again
STEP2: PROCESS DATA
There are 2 Data Collection: Tweets in Json Format and Satelite images
Assuming the have relaton

2.1 Source of data:
Hurricane Harvey Tweets: https://www.kaggle.com/dan195/hurricaneharvey 
Satellite Images of Hurricane Damage from Kaggle: https://www.kaggle.com/kmader/satellite-images-of-hurricane-damage

2.2 prepocess_tweet
Purpose: Grouping tweets by Days
Detail: tweets_batch = ['2017-8-26', '2017-8-27', '2017-8-24', '2017-8-28',
                    '2017-8-29', '2017-8-23', '2017-6-1', '2017-6-21', '2017-8-17',
                    '2017-8-18', '2017-8-14', '2017-8-22', '2017-2-19', '2017-3-28',
                    '2017-8-19', '2017-8-13', '2017-5-21', '2017-5-26', '2017-4-19',
                    '2017-8-16', '2017-8-15', '2017-6-9', '2017-8-21', '2017-6-2',
                    '2017-2-21', '2017-5-25', '2017-4-20', '2017-8-4', '2017-3-21',
                    '2017-8-20', '2017-1-11', '2017-2-10']
File: src/preprocess_twitter.py
2.3 preprocess img
Purpose: change img format to base64 format
File: src/preprocess_images.py

2.4 Merge 2 dataset
Purpose: Distribute images metadata to every tweets
File:src/merge_tweets_images.py

2.5 Transfer data from Json Format to Requests having header and schema

Syntax: python src/push_tweets.py send_tweets_to_rest_api 5
Purpose: 

- Tạo JSON file chứa MESSAGES- là các tweets và img đã merged
- Viết Python program gửi OBJECTS IN JSON as Messages
qua HTTP Request
tới Azure API Mangement (APIM) endpoint - emulation of source of streaming data (mô phỏng nguồn dữ liệu trực tuyến)

STEP3: TAO AZURE FUNCTION HTTPREQUESTTWEETTOBLOBANDEVENTHUB

3.1 In VSC. install 
- install extension Azure Function
- install extension Python

3.1.2 HOW TO SIGN IN TO AZURE via VSCode
VIEW=> COMMAND PALLTE=> AZURE:Sign in

3.2 Open pallete
View=> pallete=> azure function: create func
- create local azure func- http trigger- type: anonymous
- on terminal: func start
copy link and test in Postman=> ok
Ctrl + C to exist
- install requirements.txt for virtual venv, test lại chạy okay vs sample function
 
3.3 Create new function app in azure via vs code
- vs code, sign in azure=> create function app (advanced)
- name: noreur-dev-dataeng-FA (PS: need to create global unique name)
- Southeast asia
- new storage account: noreur-dev-dataeng-config
- create new app insight: noreur-dev-dataeng-ins

3.4 Adjust function.json and init.py

3.5 Deploy to cloud
3.6 test with Postman
Azure=> function app=> Function HTTPREQUESTTWEETTOBLOBANDEVENTHUB=> Monitor=> logs

STEP4: BIND FUNCTION OUTPUT WITH AZURE BLOB STORAGE
-Azure function: binding => out => name: outputBlob
-dat ten cho outcontainer: tweets/{rand-guid}.json
-create new local app setting => create new storage account : tweetssa
-resourse group
tao moi...
southest asia
 
4.1 Result:
file Function.json adjusted automatically
4.2 In appilcation setting, VS code=> Upload local setting
4.3 func start 
copy link and test with POST
RESULT: There are file in Container, tab Edit will see content

4.4 deploy to cloud again

STEP5 WORK WITH AZURE API MANAGEMENT

1. Create Azure API INSTANCE (empty gateway)
2. Thêm API vào APIM để mà Bảo vệ và triển khai Azure Function as Backend
3. Test
4. (Theo cach hieu cua misa) them vào default subscription key va add Basic authentication policy
5. test

STEP6: CREATE AND COMBINE EVENT HUBS, AZURE FUNCTION AND COSMOS DB
1. tạo Event hubs namespace- Standard tier
2. create event hubs
gồm 2 partitions và 1 day message retention ( giữ mess trong 1 day)
3. capture events- lưu event vĩnh viễn, thay vì lưu trong Blob storage đang có
mô tả: azure event hubs capture cho phép mình TỰ ĐỘNG chuyển DỮ LIỆU STREAMING từ EVENT HUB đến AZ Blob Storage, hoặc là AZ Data lake 
azure event hubs cho phép mình linh động về thời gian
4. Create Function EventHubTriggerToCosmosDB and deploy to Cloud

STEP7: CONNECT POWER BI DESKTOP VIA CONNECTOR, AND CREATE A DASHBOARD FROM DATASET
