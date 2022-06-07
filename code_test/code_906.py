import re
def extract_date(url):
        """
        Write a function to extract year, month and date from a url by using regex.
        """
        return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)
