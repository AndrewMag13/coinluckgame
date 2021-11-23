import hashlib
import time

secret='Y[wUkLSn7W,U>wZ'
merchant_id='1159'

print(time.time())

opl = hashlib.md5(f'{merchant_id}:{100}:{secret}:RUB:{123123123}'.encode('utf-8')).hexdigest()
urrl = f'https://pay.freekassa.ru/?m={merchant_id}&oa={100}&o={123123123}&s={opl}&currency=RUB'