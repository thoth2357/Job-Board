import requests

#get user location
def get_user_location(request) -> str:
    '''
    args: Request
    return: str
    '''
    ip = request.meta.get("REMOTE_ADDR")
    if ip:
        try:
            response = requests.get(f'https://ipapi.co/{ip}/json/')
            if response.status_code == 200:
                data = response.json()
                return f"{data['city']}, {data['country']}"
        except:
            pass