try:
    with open('proxies.txt', 'r') as file:
        proxy = [ line.rstrip() for line in file.readlines()]
except FileNotFoundError:
    raise Exception('Proxies.txt not found.')