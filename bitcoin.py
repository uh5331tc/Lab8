import requests

#functions ~6 

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

def main(): 
    bitcoin = get_bitcoin_amount()
    dollars = convert_b_to_d(bitcoin)
    display_results(bitcoin, dollars)


def get_bitcoin_amount():
    while True:
        try:
            bitcoin = float(input('Enter the number of bitcoin: '))
            if bitcoin >= 0:
                return bitcoin
            else:
                print(' Please enter a number greater than 0')
        except ValueError:
            print('Enter a positive number.')


def convert_b_to_d(bitcoin):
    rate_json = get_b_data()   
    exchange_rate = extract_rate(rate_json)
    
    bitcoin = exchange_rate * bitcoin
    return bitcoin

def get_b_data():
    return requests.get(url).json()

def extract_rate(rate_json):
    return rate_json['bpi']['USD']['rate_float']

def display_results(bitcoin, dollars):
    print(f'{bitcoin} bitcoin is equal to ${dollars}')



if __name__ == '__main__':
    main()
