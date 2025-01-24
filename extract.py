import re, requests
from bs4 import BeautifulSoup

# URL of the banned books page
url = "https://www.rcschools.net/apps/pages/index.jsp?uREC_ID=525032&type=d&pREC_ID=2636708"

# File to save the list of books
output_file = "banned_books.txt"

def extract_banned_books():
    try:
        # Fetch the page content
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text

        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(html_content, "html.parser")

        # Find all rows in the table
        rows = soup.select("table tbody tr")
        books = []

        for row in rows:
            # Extract the first cell (Material) which contains the book name and author
            material_cell = row.find("td")
            if material_cell:
                book_info = material_cell.get_text(strip=True)
                if book_info:
                    books.append(book_info)

        # Save the books to a file
        with open(output_file, "w") as f:
            for book in books:
                f.write(book + "\n")

        print(f"Extracted {len(books)} books and saved to {output_file}")

    except Exception as e:
        print("An error occurred:", e)

def clean_book_list(input_file, output_file):
    with open(input_file, "r") as file:
        lines = file.readlines()

    cleaned_lines = []
    for line in lines:
        line = line.strip()
        # Match lines with " by " (correct format)
        if re.search(r"\sby\s", line):
            cleaned_lines.append(line)
        # Fix lines with "*by" (missing space before "by")
        elif re.search(r"\Sby\s", line):  # Matches "<word>by "
            fixed_line = re.sub(r"(\S)by\s", r"\1 by ", line)
            cleaned_lines.append(fixed_line)
        # Skip lines without " by " or "*by"
        else:
            continue
    
    # sort lines alphebeticallly
    cleaned_lines.sort()

    # Write the cleaned lines to the output file
    with open(output_file, "w") as file:
        for line in cleaned_lines:
            file.write(line + "\n")

if __name__ == "__main__":
    extract_banned_books()
    clean_book_list(output_file, output_file)
