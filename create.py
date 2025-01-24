# create.py

# File path for the banned books text file
input_file = "banned_books.txt"

# HTML template with updated links for Rutherford County Library
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rutherford County Schools BANNED BOOKS</title>
</head>
<body>
    <h1>Rutherford County TENNESSEE - Schools BANNED BOOKS</h1>
    
    <div id="info">
        <h2>This page is not affiliated with Rutherford County Schools nor Rutherford County Library District.</h2>
        <h2>Access Books Digitally</h2>
        <p>
            A small minority of "adults" have chosen to restrict the freedom of students in Rutherford County School system by banning certain books. These actions limit the availability of important literature that could help expand your knowledge and understanding.
        </p>
        <p>
            However, there is a way to still access these books! With a library card from the Rutherford County Library District, you can borrow books and audiobooks digitally for free. If a book is not available on overdrive, ask your friendly librarian about digital copies!
        </p>
        <p>
            The Libby app allows you to borrow these books on your phone. It's available for download on both Android and iOS devices:
        </p>
        <ul>
            <li><a href="https://play.google.com/store/apps/details?id=com.overdrive.mobile.android.libby&hl=en-US" target="_blank">Libby for Android</a></li>
            <li><a href="https://apps.apple.com/us/app/libby-the-library-app/id1076402606" target="_blank">Libby for iOS</a></li>
        </ul>
        <p>For more information, including library locations and hours, visit the Rutherford County Library's website:</p>
        <p><a href="https://rclstn.org/locations/" target="_blank">Rutherford County Library Locations & Hours</a></p>
    </div>

    <p>Below are links to search for banned books on the Rutherford County Library website:</p>
    
    <ul id="books-list">
        <!-- Links will be dynamically added here -->
    </ul>

    <script>
        const books = [
            {books_list}
        ];

        const rclSearchUrl = "https://explore.rclstn.org/Union/Search?view=list&lookfor=";
        const storyGraphBaseUrl = "https://app.thestorygraph.com/browse?search_term=";
        const overdriveBaseUrl = "https://www.overdrive.com/search?q=";

        function generateLinks() {
            const booksList = document.getElementById("books-list");

            books.forEach((book, index) => {
                const searchQuery = encodeURIComponent(book);

                const listItem = document.createElement("li");

                // Add the book number to the list item
                listItem.textContent = `${index + 1}. `;

                // Create Overdrive link with book name and author clickable
                const overdriveLink = document.createElement("a");
                overdriveLink.href = `${overdriveBaseUrl}${searchQuery}`;
                overdriveLink.textContent = `${book} (Overdrive)`;
                overdriveLink.target = "_blank";
                listItem.appendChild(overdriveLink);

                // Add a separator between links
                listItem.appendChild(document.createTextNode(" | "));

                // Create StoryGraph link
                const storyGraphLink = document.createElement("a");
                storyGraphLink.href = `${storyGraphBaseUrl}${searchQuery}`;
                storyGraphLink.textContent = "(Storygraph)";
                storyGraphLink.target = "_blank";
                listItem.appendChild(storyGraphLink);

                booksList.appendChild(listItem);
            });
        }

        generateLinks();
    </script>
</body>
</html>
"""

def create_bundle(input_file):
    try:
        # Read books from banned_books.txt
        with open(input_file, "r") as file:
            books = file.readlines()

        # Clean up each book name and format it as a JavaScript array element
        books = [f'"{book.strip()}"' for book in books]

        # Join all book entries into a single string for inclusion in the HTML
        books_js_array = ',\n            '.join(books)

        # Generate the final HTML content by replacing the placeholder
        html_content = html_template.replace("{books_list}", books_js_array)

        # Write the generated HTML to a file
        output_file = "index.html"
        with open(output_file, "w") as out_file:
            out_file.write(html_content)

        print(f"HTML page created successfully: {output_file}")

    except Exception as e:
        print(f"Error reading the banned books file: {e}")

# Run the script
create_bundle(input_file)
