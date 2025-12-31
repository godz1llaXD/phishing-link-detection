import re
import math
from urllib.parse import urlparse

IP_REGEX = re.compile(
    r"^(http|https)://(\d{1,3}\.){3}\d{1,3}"
)

def url_entropy(url):
    probs = [url.count(c) / len(url) for c in set(url)]
    return -sum(p * math.log2(p) for p in probs)

def extract_features(url):
    parsed = urlparse(url)
    domain = parsed.netloc

    features = {
        # Lexical
        "url_length": len(url),
        "num_digits": sum(c.isdigit() for c in url),
        "num_special_chars": sum(not c.isalnum() for c in url),
        "num_dots": url.count('.'),
        "num_hyphens": url.count('-'),
        "has_at": int('@' in url),
        "has_https": int(parsed.scheme == "https"),
        "entropy": url_entropy(url),

        # Structural
        "domain_length": len(domain),
        "path_length": len(parsed.path),
        "query_length": len(parsed.query),
        "subdomain_depth": max(domain.count('.') - 1, 0),

        # Security indicators
        "num_params": parsed.query.count('&') + 1 if parsed.query else 0,
        "has_fragment": int(bool(parsed.fragment)),
        "ip_in_url": int(bool(IP_REGEX.match(url)))
    }

    return features
