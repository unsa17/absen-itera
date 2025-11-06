import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

url = "https://api.itera.ac.id/v2/presensi/kelas"

print("Manual Absen System")
token= input('masukkan token absen: ')
nim = input('masukkan nim: ')
payload = {
  'token': token,
  'nim': nim
}

headers = {
  'User-Agent': "Dart/3.5 (dart:io)",
  'Accept': "application/json",
  'Accept-Encoding': "gzip"
}

response = requests.post(url, verify=False, data=payload, headers=headers)

print(response.text)
