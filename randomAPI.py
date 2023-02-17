import requests

number_of_users = 100
gender = 'male'


url =  f'https://randomuser.me/api/?page=3&results={number_of_users}&gender={gender}'

response = requests.get(url)

data = response.json()
for x in range(100):
    userDetails = data['results'][x]

    print(x+1, 'Name', userDetails['name']['first'],'Gender',userDetails['gender'],'Country',userDetails['location']['country'],'Email',userDetails['email'])
    print('--------------------------------------------------------------------------')