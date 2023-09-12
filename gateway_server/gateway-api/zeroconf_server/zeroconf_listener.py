from zeroconf import ServiceBrowser, ServiceListener, Zeroconf
import requests
import time
import socket


class MyListener(ServiceListener):
    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        print(f"Service {name} updated\n")

    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        print(f"Service {name} removed\n")
        info = zc.get_service_info(type_, name)
        if info:
            requests.get(
                f'http://localhost:5000/saiu')  # TODO: Esse evento tem que ser disparado para o front-end quando o serviço é removido

    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        info = zc.get_service_info(type_, name)
        print(info)
        # print(f"Service {name} added, service info: {info}\n")
        print(f"\nService name: {name} added,\nIP address: {socket.inet_ntoa(info.addresses[0])}\n")


if __name__ == "__main__":
    zeroconf = Zeroconf()
    listener = MyListener()

    browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)

    try:
        input("Press enter to exit...\n\n")
        time.sleep(1)
    finally:
        zeroconf.close()
