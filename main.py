import json
import ujson
import orjson

from time import time


def main(func_name: str, dumps, loads):
    data: str = open('data.json').read()
    start_d: time = time()
    dumps(data)
    end_d: time = time()

    start_l: time = time()
    loads(data)
    end_l: time = time()
    print(f"{func_name}        {end_d - start_d}s      {end_l - start_l}s")


if __name__ == '__main__':
    print("Nomi          dumps                     loads")
    main(func_name="json  ", dumps=json.dumps, loads=json.loads)
    main(func_name="ujson ", dumps=ujson.dumps, loads=ujson.loads)
    main(func_name="orjson", dumps=orjson.dumps, loads=orjson.loads)
