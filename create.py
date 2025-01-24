# create.py

# File path for the banned books text file
input_file = "banned_books.txt"

# HTML template with updated table and sorting functionality
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rutherford County Schools BANNED BOOKS</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 10px;
            text-align: left;
            border: 1px solid #ddd;
        }
        th {
            cursor: pointer;
        }
        .sorted-asc::after {
            content: " ↓";
        }
        .sorted-desc::after {
            content: " ↑";
        }
    </style>
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

    <h2>List of Banned Books</h2>
    <table id="books-table">
        <thead>
            <tr>
                <th id="title-header" onclick="sortTable(0)">Title</th>
                <th id="author-header" onclick="sortTable(1)">Author</th>
                <th>Overdrive</th>
                <th>StoryGraph</th>
            </tr>
        </thead>
        <tbody>
            <!-- Book data will be dynamically inserted here -->
        </tbody>
    </table>

    <script>
        const books = [
            {books_list}
        ];

        const overdriveBaseUrl = "https://explore.rclstn.org/Union/Search?view=list&lookfor=";
        const storyGraphBaseUrl = "https://app.thestorygraph.com/browse?search_term=";

        let sortDirection = {
            0: true,  // Title column: true means ascending by default
            1: null  // Author column: null means no sort initially
        };

        function generateTable() {
            const tableBody = document.getElementById("books-table").getElementsByTagName("tbody")[0];

            books.forEach((book) => {
                const [author, title] = book.split(" by ").reverse(); // Split from the last " by " and reverse to correct order
                const row = tableBody.insertRow();
                row.insertCell(0).innerHTML = `<a href="${overdriveBaseUrl}${encodeURIComponent(title)}" target="_blank">${title}</a>`;
                row.insertCell(1).innerHTML = `<a href="${overdriveBaseUrl}${encodeURIComponent(author)}" target="_blank">${author}</a>`;
                row.insertCell(2).innerHTML = `<a href="${overdriveBaseUrl}${encodeURIComponent(title)}" target="_blank">Overdrive</a>`;
                row.insertCell(3).innerHTML = `<a href="${storyGraphBaseUrl}${encodeURIComponent(title)}" target="_blank">StoryGraph</a>`;
            });
        }

        function sortTable(columnIndex) {
            const table = document.getElementById("books-table");
            let rows = Array.from(table.rows).slice(1);
            let sortedRows;

            // Toggle sort direction
            if (sortDirection[columnIndex] === null || sortDirection[columnIndex] === false) {
                sortDirection[columnIndex] = true; // Set to ascending
            } else {
                sortDirection[columnIndex] = false; // Set to descending
            }

            if (columnIndex === 0) {  // Sort by Title
                sortedRows = rows.sort((a, b) => {
                    const titleA = a.cells[columnIndex].textContent.trim().toLowerCase();
                    const titleB = b.cells[columnIndex].textContent.trim().toLowerCase();
                    return sortDirection[columnIndex] ? (titleA < titleB ? -1 : 1) : (titleA < titleB ? 1 : -1);
                });
            } else if (columnIndex === 1) {  // Sort by Author
                sortedRows = rows.sort((a, b) => {
                    const authorA = a.cells[columnIndex].textContent.trim().toLowerCase();
                    const authorB = b.cells[columnIndex].textContent.trim().toLowerCase();
                    return sortDirection[columnIndex] ? (authorA < authorB ? -1 : 1) : (authorA < authorB ? 1 : -1);
                });
            }

            table.tBodies[0].append(...sortedRows);
            updateSortArrows(columnIndex);
        }

        function updateSortArrows(sortedColumn) {
            // Reset all arrows
            document.getElementById("title-header").classList.remove("sorted-asc", "sorted-desc");
            document.getElementById("author-header").classList.remove("sorted-asc", "sorted-desc");

            // Update the sorted column's arrow
            if (sortedColumn === 0) {
                document.getElementById("title-header").classList.add(sortDirection[0] ? "sorted-asc" : "sorted-desc");
            } else if (sortedColumn === 1) {
                document.getElementById("author-header").classList.add(sortDirection[1] ? "sorted-asc" : "sorted-desc");
            }
        }

        // Ensure that the title column is marked as sorted-asc when the page loads
        window.onload = function() {
            document.getElementById("title-header").classList.add("sorted-asc");
        };

        generateTable();
    </script>
</body>
</html>
"""

def create_bundle(input_file):
    try:
        # Read books from banned_books.txt
        with open(input_file, "r") as file:
            books = file.readlines()

        # Clean up each book name and format it as a JavaScript array element (title by author)
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
