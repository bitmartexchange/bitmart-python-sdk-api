from bitmart.api_system import APISystem

if __name__ == '__main__':

    # system api
    api = APISystem()
    print(api.get_system_time())
    print(api.get_system_service())
