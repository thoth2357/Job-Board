import requests

#get user location
def get_user_location(request) -> str:
    '''
    args: Request
    return: str
    '''
    ip = request.META.get("REMOTE_ADDR")
    if ip and ip != '127.0.0.1':
        try:
            response = requests.get(f'https://ipapi.co/{ip}/json/')
            if response.status_code == 200:
                data = response.json()
                return f"{data['city']}, {data['country']}"
        except:
            pass
    else:
        return "Localhost"