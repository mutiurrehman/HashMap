from hashmap import Hashmap


mp = Hashmap()


if __name__ == '__main__':
    mp.put("7452037218", "Mutiur")
    print(mp.get("7452037218"))
    mp.print_hash_map()