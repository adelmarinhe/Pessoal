from time import sleep
import requests
from ticket import Ticket, Medicamento, MedicamentoType, RobotAPIStatus


def get_status():
    ret = requests.get('http://127.0.0.1:5001/robot-api/execution-status')
    print(ret, ret.content)


if __name__ == '__main__':

    while True:
        input("Pressione ENTER para o status")
        get_status()