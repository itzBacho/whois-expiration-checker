import threading
import requests
from bs4 import BeautifulSoup

def check_domain(domain):
    try:
        url = f"https://www.whois.com/whois/{domain}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            expires_on_label = soup.find("div", text="Expires On:")
            if expires_on_label:
                expiration_date_element = expires_on_label.find_next_sibling("div", {"class": "df-value"})
                if expiration_date_element:
                    expiration_date = expiration_date_element.text.strip()
                    print(f"Domain: {domain}, Expiration Date: {expiration_date}")

                    # UPWORK B.KOKAIA
                    with open("SavedDates.txt", "a") as exp_file:
                        exp_file.write(f"Domain: {domain}, Expiration Date: {expiration_date}\n")
                else:
                    print(f"Not Found {domain}")
            else:
                print(f"Not Found Expiration Date {domain}")
        else:
            print(f"Failed to retrieve expire date for domain {domain}")
    except Exception as e:
        print(f"domain error {domain}: {e}")

def main():
    print("WHOIS EXPIRATION DATE TOOL")

    # UPWORK B.KOKAIA
    file_name = input("put file name(domains.txt): ")

    try:
        with open(file_name, "r") as file:
            domains = file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        return

    # UPWORK B.KOKAIA
    try:
        num_threads = int(input("Enter the number of threads: "))
    except ValueError:
        print("Invalid input. Please provide an integer for the number of threads.")
        return

    domain_chunks = [domains[i:i + len(domains) // num_threads] for i in range(0, len(domains), len(domains) // num_threads)]

    threads = []

    for chunk in domain_chunks:
        thread = threading.Thread(target=lambda chunk=chunk: [check_domain(domain) for domain in chunk])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # UPWORK B.KOKAIA
    total_domains_detected = sum(1 for line in open("SavedDates.txt") if line.startswith("Domain:"))
    print(f"Total Domains Detected: {total_domains_detected}")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
