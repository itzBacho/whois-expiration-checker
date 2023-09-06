# DOMAIN-EXPIRYDATE-SCRAPE
This Python script is a WHOIS expiration date retrieval tool. It utilizes multiple threads to efficiently check and retrieve the expiration dates of a list of domains provided in a file

Here's a brief description of its functionality:

The script takes user input for the filename containing the list of domains to be checked.

It also allows the user to specify the number of threads to use for concurrent processing, which can help speed up the WHOIS checks for a large number of domains.

The script reads the list of domains from the input file and splits them into chunks based on the number of threads specified.

Each thread independently checks the WHOIS information for a chunk of domains using the "requests" library to access the 'whois.com' website. It parses the HTML response using BeautifulSoup to extract the expiration date.

If an expiration date is found, it prints the domain name and expiration date to the console and appends this information to a file called "SavedDates.txt."

After all threads have completed their tasks, the script calculates and displays the total number of domains for which expiration dates were successfully detected.

Finally, it waits for user input to exit the program.

This script is useful for individuals or organizations managing multiple domains and needing a quick way to check their expiration dates in parallel, making it a more efficient and time-saving tool for domain management.
