from asyncio.windows_events import NULL


class Contact:
    vorname = NULL
    nachname = NULL
    email = NULL
    send = False

    def __init__(self, vorname, nachname, email) -> None:
        self.vorname = vorname
        self.nachname = nachname
        self.email = email

    def getVorname(self):
        return self.vorname

    def getNachname(self):
        return self.nachname

    def getMail(self):
        return self.email

    def getSend(self):
        return self.send

    def setSend(self):
        self.send = True
