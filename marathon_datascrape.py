import requests
from bs4 import BeautifulSoup
import csv
import xml.etree.ElementTree as ET
import sys
import os
#python file 1
def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        sys.exit(1)

def parse_html(html, tag, class_name=None):
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.find_all(tag, class_=class_name)
    data = []
    for element in elements:
        row = [text.strip() for text in element.stripped_strings]
        data.append(row)
    return data

def save_to_csv(data, filename="output.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f"Data saved to {filename}")

def save_to_xml(data, filename="output.xml"):
    root = ET.Element("data")
    for row_index, row in enumerate(data, start=1):
        item = ET.SubElement(root, f"item{row_index}")
        for col_index, value in enumerate(row, start=1):
            ET.SubElement(item, f"column{col_index}").text = value
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)
    print(f"Data saved to {filename}")

def main():
    if len(sys.argv) < 4:
        print("Usage: python webscrape.py <url> <html_tag> <output_format> [<class_name>]")
        sys.exit(1)

    url = sys.argv[1]
    html_tag = sys.argv[2]
    output_format = sys.argv[3].lower()
    class_name = sys.argv[4] if len(sys.argv) > 4 else None

    html = fetch_html(url)
    data = parse_html(html, html_tag, class_name)

    if output_format == "csv":
        save_to_csv(data)
    elif output_format == "xml":
        save_to_xml(data)
    else:
        print("Invalid output format. Choose 'csv' or 'xml'.")

if __name__ == "__main__":
    main()
