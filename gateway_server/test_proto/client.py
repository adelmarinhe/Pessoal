from time import sleep
import requests
from ticket import Ticket, Medicamento, MedicamentoType, RobotAPIStatus


class RobotAPI:
    def __int__(self):
        self.port = 'http://127.0.0.1:5001/robot-api'

    def post_message(self, message):
        requests.post('http://127.0.0.1:5001/robot-api/ticket', data=message)

    def set_pause(self):
        ret = requests.post('http://127.0.0.1:5001/robot-api//pause')
        status = RobotAPIStatus.FromString(ret.content)
        print(status)

    def set_resume(self):
        ret = requests.post('http://127.0.0.1:5001/robot-api//resume')
        status = RobotAPIStatus.FromString(ret.content)
        print(status)

    def set_emergency_stop(self):
        ret = requests.post('http://127.0.0.1:5001/robot-api//emergency-stop')
        status = RobotAPIStatus.FromString(ret.content)
        print(status)


if __name__ == '__main__':
    ticket = Ticket()
    medicine_1 = Medicamento()
    medicine_2 = Medicamento()

    medicine_1.name = 'Paracetamol'
    medicine_1.quantidade = 2
    medicine_1.tipo = MedicamentoType.PACOTE

    medicine_2.name = 'Dipirona'
    medicine_2.quantidade = 1
    medicine_2.tipo = MedicamentoType.AMPOLA

    ticket.medicamentos.append(medicine_1)
    ticket.medicamentos.append(medicine_2)

    robot = RobotAPI()

    robot.post_message(ticket.SerializeToString())

    input("Pressione ENTER para o pause")
    robot.set_pause()

    input("Pressione ENTER para o resume")
    robot.set_resume()

    input("Pressione ENTER para o emergency stop")
    robot.set_emergency_stop()
