import asyncio
from proxybroker import Broker
import warnings

class ProxyRouter():

    def __init__(self):
        
        self.proxy_data = ''

    def FindProxsy(self):

        with warnings.catch_warnings():

            warnings.simplefilter("ignore")
            warnings.warn("deprecated", DeprecationWarning)

            async def check(proxies):
                while True:
                    proxy = await proxies.get()
                    if proxy is None: 
                        break
                    else:
                        self.proxy_data = (str(proxy))
                        

            proxies = asyncio.Queue()
            broker = Broker(proxies)
            tasks = asyncio.gather(
                broker.find(types=['HTTP', 'HTTPS'], limit=1),
                check(proxies))

            loop = asyncio.get_event_loop()
            loop.run_until_complete(tasks)


            #<Proxy BG 1.83s [HTTPS] 77.238.79.111:8080>
            #Found proxy: <Proxy HU 2.47s [HTTP: Transparent] 79.120.177.106:8080>

            #O boyda eziyet cek proxleri tapmagn yoln tap gel indi gijdillax kimi bunun filtrofkasiynan elles

            sing_index = self.proxy_data[0:-1].index("]") # position of ] sign
            
            proxy_return = self.proxy_data[sing_index + 2:-1] # final pxory variable with cutted extra strings

            if 'http' in self.proxy_data.lower():
                self.protocol = 'http'

            elif 'https' in self.proxy_data.lower():
                self.protocol = 'https'

            proxy = '{}://{}'.format(self.protocol, proxy_return)

            return proxy

if __name__ == '__main__':
    
    print(ProxyRouter().FindProxsy())
