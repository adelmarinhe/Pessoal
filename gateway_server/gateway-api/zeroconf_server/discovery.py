from time import sleep
from threading import Thread
from zeroconf import ServiceBrowser, Zeroconf, ServiceStateChange

import requests


class InvalidServiceAddedException(Exception):
    pass


class InvalidServiceRemovedException(Exception):
    pass


class ZeroConfDiscovery(Thread):
    def __init__(self):
        super().__init__()
        self.services = {}
        self.zeroconf = Zeroconf()

    def on_service_change(self, zeroconf, service_type, name, state_change):
        print(f"Service {name} of type {service_type} State Changed: {state_change}")

        try:
            service_name = name.split(".")[0]
            if state_change is ServiceStateChange.Added:
                info = self.zeroconf.get_service_info(service_type, name)
                service_port = info.port
                self.services[service_name] = f"{service_name}:{service_port}"

            elif state_change is ServiceStateChange.Removed:
                found = self.services.pop(service_name, None)

                requests.get(f'http://localhost:5000/saiu')

                if found is None:
                    raise InvalidServiceRemovedException(f"The service removed is not valid.")

        except (Exception, KeyError) as e:
            raise InvalidServiceAddedException(f"The name or properties of the service added are not valid: {e}")

    def run(self):
        _ = ServiceBrowser(self.zeroconf, "_http._tcp.local.", handlers=[self.on_service_change])

        try:
            input("Press enter to exit...\n\n")
            sleep(1)
        except (KeyboardInterrupt, InvalidServiceAddedException):
            print("Exiting...")
        finally:
            self.zeroconf.close()
