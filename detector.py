import re
import whois
from datetime import datetime

def get_risk_score(url):
    score = 0
    
    # Rule 1: IP Address Check (40 points)
    # Agar URL mein IP address hai, toh woh bahut risky hai
    if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', url):
        score += 40
        
    # Rule 2: Suspicious Keywords Check (30 points)
    # Agar ye words URL mein hain, toh phishing ka khatra hai
    suspicious_keywords = ['login', 'verify', 'account', 'banking', 'secure', 'update']
    if any(word in url.lower() for word in suspicious_keywords):
        score += 30
        
    # Rule 3: Domain Age Check (30 points)
    # Agar domain 30 din se kam purana hai, toh woh phishing ho sakta hai
    try:
        domain = url.split("//")[-1].split("/")[0]
        domain_info = whois.whois(domain)
        creation_date = domain_info.creation_date
        
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
            
        if creation_date:
            age = (datetime.now() - creation_date).days
            if age < 30:
                score += 30
    except:
        # Agar WHOIS info nahi mili, toh hum thoda risk badha dete hain
        score += 10
        
    return min(score, 100) # Maximum score 100 limit kiya hai