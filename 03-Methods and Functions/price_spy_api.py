import requests
from pprint import pprint
from time import sleep


def main():

    sleep_rate = 0.05

    all_prices = []
    toll_free_countries = []
    most_expensive_lvn = 0

    for country in get_country_codes():
        request = requests.get("https://rest.nexmo.com/pricing/messaging/{}/jsonp?".format(country))

        if request.status_code != 200:
            print("ERROR")
            print(request.status_code)
            break

        request_data = request.json()

        print('Processing country {}'.format(country))

        if 'flatMobilePrice' in request_data['messaging']['outbound']:
            all_prices.append(float(request_data['messaging']['outbound']['flatMobilePrice']))

        if 'tollFreePrice' in request_data['messaging']['inbound']:
            toll_free_countries.append(country)
        

        if 'numbers' in request_data['messaging']['inbound']:
            for number in request_data['messaging']['inbound']['numbers']:
                monthlyFee = float(number['monthlyFee'])

                if 'tollfree' in number['type']:
                    toll_free_countries.append(country)


                if most_expensive_lvn < monthlyFee:
                    most_expensive_lvn = monthlyFee

        sleep(sleep_rate)


    avg_all_prices = sum(all_prices) / len(all_prices)

    print(avg_all_prices)
    print(toll_free_countries)
    print(most_expensive_lvn)


def get_country_codes():
    return ["AC", "AD", "AE", "AF", "AG", "AI", "AL", "AM", "AO", "AR", "AS", "AT", "AU", "AW", "AZ", "BA", "BB", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BM","BN", "BO", "BQ", "BR", "BS", "BT", "BW", "BY", "BZ", "CA", "CD", "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR", "CU", "CV", "CW", "CY", "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "ER", "ES", "ET", "FI", "FJ", "FM", "FO", "FR", "GA", "GB", "GD", "GE", "GF", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GT", "GU", "GW", "GY", "HK", "HN", "HR", "HT", "HU", "ID", "IE", "IL", "IN", "IQ", "IR", "IS", "IT", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NG", "NI", "NL", "NO", "NP", "NR", "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SG", "SI", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV", "SX", "SY", "SZ", "TC", "TD", "TG", "TH", "TJ", "TL", "TM", "TN", "TO", "TR", "TT", "TW", "TZ", "UA", "UG", "US", "UY", "UZ", "VC", "VE", "VG", "VI", "VN", "VU", "WS", "XK", "YE", "YT", "ZA", "ZM", "ZW"]


main()