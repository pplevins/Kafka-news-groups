from core import DataFetcher

if __name__ == '__main__':
    interesting, not_interesting = DataFetcher().fetch_data_from_json()
    print(interesting[0])
    print(not_interesting[0])
