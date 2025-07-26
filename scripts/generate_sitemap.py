import os
from urllib.parse import urljoin
from xml.etree.ElementTree import Element, SubElement, ElementTree

# Konfiguration
base_url = "https://teemulis.github.io"
site_dir = "."  # Root deines Repos
sitemap_path = "sitemap.xml"

# HTML-Seiten finden
urls = set()
for root, _, files in os.walk(site_dir):
    for file in files:
        if file.endswith(".html"):
            rel_path = os.path.relpath(os.path.join(root, file), site_dir)
            rel_url = rel_path.replace("\\", "/")
            if rel_url.startswith("_site") or rel_url.startswith(".git") or "node_modules" in rel_url:
                continue
            url = "/" if rel_url == "index.html" else "/" + rel_url
            full_url = urljoin(base_url, url)
            urls.add(full_url)

# Sitemap XML erzeugen
urlset = Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

for url in sorted(urls):
    url_elem = SubElement(urlset, "url")
    loc = SubElement(url_elem, "loc")
    loc.text = url

# In Datei schreiben
tree = ElementTree(urlset)
tree.write(sitemap_path, encoding="utf-8", xml_declaration=True)

print(f"✅ Neue sitemap.xml mit {len(urls)} Seiten erzeugt.")
