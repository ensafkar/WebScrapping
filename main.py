import requests
from bs4 import BeautifulSoup

# Hedef web sitesi
url = 'https://www.avis.com.tr/kiralik-araba'

# Web sitesinden HTML içeriğini çekme
response = requests.get(url)
html_content = response.content

# HTML içeriğini parse etme
soup = BeautifulSoup(html_content, 'html.parser')

# Araç bilgilerini çekme
arac_bilgileri = soup.find_all('div', class_='primary-vehicle-card')
for arac in arac_bilgileri:
    arac_modeli = arac.find('h4', class_='car-model')
    if arac_modeli:  # arac_modeli None değilse
        print(f"Araç Modeli: {arac_modeli.text}")
    else:
        print("Araç modeli bulunamadı.")