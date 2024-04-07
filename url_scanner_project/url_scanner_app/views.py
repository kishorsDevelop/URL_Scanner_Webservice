from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ScanResult
from playwright.sync_api import sync_playwright
import socket
import ssl
import json
import random
import base64
from urllib.parse import urlparse
from bs4 import BeautifulSoup
@csrf_exempt
def scan_url(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        print(url)
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.goto(url)
            screenshot_path = f'screenshots/screenshot_{random.randint(1, 1000)}.png'
            page.screenshot(path=screenshot_path)
            ip_address = socket.gethostbyname(urlparse(url).hostname)
            source_url = page.url
            destination_url = page.evaluate('''() => {
                return window.location.href;
            }''')
            asn_information = socket.gethostbyaddr(ip_address)
           
            try:
                cert = ssl.get_server_certificate((urlparse(url).hostname, 443))
                ssl_certificate_details = base64.b64encode(ssl.PEM_cert_to_DER_cert(cert)).decode('utf-8')
            except Exception as e:
                ssl_certificate_details = str(e)
           
            page_source = page.content()
            
            soup = BeautifulSoup(page_source, 'html.parser')
            natural_language_content = soup.get_text()
          
            browser.close()

        extracted_information = {
            'url': url,
            'screenshot': screenshot_path,
            'ip_address': ip_address,
            'source_url': source_url,
            'destination_url': destination_url,
            'asn_information': asn_information,
            'ssl_certificate_details': ssl_certificate_details,
            'page_source': page_source,
            'natural_language_content': natural_language_content,
        }
        scan_result = ScanResult.objects.create(
            url=url,
            screenshot=screenshot_path,
            ip_address=ip_address,
            source_url=source_url,
            destination_url=destination_url,
            asn_information=json.dumps(asn_information),
            ssl_certificate_details=ssl_certificate_details,
            page_source=page_source,
            natural_language_content=natural_language_content,
            extracted_information=extracted_information,    
        )
        return JsonResponse({'status': 'success', 'scan_id': scan_result.id})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)