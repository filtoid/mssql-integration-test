import pyodbc

class MsSql():
    def __init__(self, host, db_name, driver, username=None, password=None, port=1433):
        if host is None:
            raise ValueError("Host cannot be None")
        
        if db_name is None:
            raise ValueError("Database Name cannot be None")

        if driver is None:
            raise ValueError("Driver cannot be None")

        self.host = host
        self.port = port
        self.db_name = db_name
        self.username = username
        self.password = password
        self.driver = driver

        self.__engine__ = None
        self.__conn__ = None

    def connect(self):
        if self.__conn__ is None:
            conn_str  = f"DRIVER={{{self.driver}}};SERVER={self.host},{self.port};" \
                        f"DATABASE={self.db_name};"
            if self.username is not None and self.password is not None:
                conn_str = f"{conn_str}UID={self.username};PWD={self.password};" \
                            "TrustServerCertificate=yes;"
            else:
                conn_str = f"{conn_str}Trusted_Connection=yes;" \
                            "TrustServerCertificate=yes;INTEGRATED " \
                            "SECURITY=yes;ENCRYPT=no;"
            self.__conn__ = pyodbc.connect(conn_str)
        return self.__conn__
