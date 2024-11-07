import os
import requests
from urllib.parse import urlparse

def generate_sitemap(domain_url):
    # Simple implementation of sitemap generation
    # You can expand this logic to crawl and fetch URLs dynamically
    print("Generating sitemap for:", domain_url)
    
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        <url>
            <loc>{domain_url}</loc>
            <lastmod>2024-11-07</lastmod>
            <changefreq>daily</changefreq>
            <priority>1.0</priority>
        </url>
    </urlset>"""
    
    # Save the generated sitemap.xml file
    with open("sitemap.xml", "w") as f:
        f.write(sitemap)
    print("Sitemap saved as sitemap.xml")

if __name__ == "__main__":
    url = "http://example.com"  # Replace with dynamic URL input in real case
    generate_sitemap(url)