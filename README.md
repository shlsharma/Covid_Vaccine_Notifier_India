# Covid_Vaccine_Notifier_India
VaccineNotifier checks the cowin portal periodically to find vaccination slots available in your pin code and for your age. If found, it will send you emails every minute until the slots are available.
Steps to run the script:
1. Create new gmail account or use your existing gmail account.
2. Enable application access on your gmail with steps given [here](https://support.google.com/accounts/answer/185833?p=InvalidSecondFactor&visit_id=637554658548216477-2576856839&rd=1):\
Example:
![alt text](https://github.com/shlsharma/Covid_Vaccine_Notifier_India/blob/main/Images/less_secure_app_access.png)
3. Install the requirements using pip3
```python
pip3 install -r requirements.txt
```
4. Change the variables
```python
age = 18 #Age 18 for (18-44) group and age 45 gor (45+) group
district_id = 230 #Your District Id [Example - 230 for JAMMU]
max_search_days = 12 #Number of days - search region
to_list = ['receiver_1@gmail.com','receiver_2@gmail.com']#receiver list
gmail_user = 'sender' #Sender email account (DON'T ENTER @gmail.com)
gmail_password = '**password**' #Sender email password 
```
5. Run the main script
```python
python3 Vaccine_Notifier.py
```
6. Sample alert email fomat:\
![alt_text](https://github.com/shlsharma/Covid_Vaccine_Notifier_India/blob/main/Images/email.jpg)

NOTE:
1. Get the state id from this [public API](https://cdn-api.co-vin.in/api/v2/admin/location/states)
2. Put the state id number at the end of this link to get the district ids
```python
https://cdn-api.co-vin.in/api/v2/admin/location/districts/state_id_number
```
3. For Example State Id number is 14 then 
```python
https://cdn-api.co-vin.in/api/v2/admin/location/districts/14
```
4. Copy the above link with your state id and open on any browser to get your district id

