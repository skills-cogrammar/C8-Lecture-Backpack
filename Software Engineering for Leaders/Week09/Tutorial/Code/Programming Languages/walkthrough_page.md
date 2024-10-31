### Exercise: Programming Languages Page

**Objective:**  
Create an interactive "Programming Languages" page that displays information about four popular programming languages. The page will introduce basic HTML structure, styling with CSS, and Bootstrap components for layout and interactivity.

---

### Step-by-Step Guide

---

#### Step 1: Set Up the HTML Structure

1. **Create the HTML File:**  
   Start by creating a file named `index.html`.

2. **Basic HTML Boilerplate:**  
   Open `index.html` and add the basic HTML structure, including the `<!DOCTYPE html>`, `<html>`, `<head>`, and `<body>` tags.

3. **Page Title and Header:**  
   Inside the `<head>`, set the page title with `<title>Programming Languages</title>`.
   Then, add a `<header>` in the `<body>` for the main title:
   ```html
   <header>
     <h1>Popular Programming Languages</h1>
   </header>
   ```

4. **Programming Language Sections:**  
   Underneath the header, create a `<section>` with `class="languages-container"` for your language cards:
   ```html
   <section class="languages-container">
     <!-- Language cards will go here -->
   </section>
   ```

5. **Individual Language Cards:**  
   Inside the `<section>`, add divs for each language card. Each card should contain:
   - An `<img>` for the language’s logo.
   - A `<h2>` heading for the language’s name.
   - A `<p>` paragraph for the language description.
   
   Example of a card for Python:
   ```html
   <div class="language-card">
     <img src="images/python-logo.png" alt="Python Logo">
     <h2>Python</h2>
     <p>Python is known for its readability and versatility, making it popular in fields such as web development, data science, and automation.</p>
   </div>
   ```

6. **Repeat for Other Languages:**  
   Duplicate the card structure for each language (JavaScript, Java, and C#), replacing the text and image paths accordingly.

---

#### Step 2: Add Basic CSS for Layout and Styling

1. **Create a CSS File:**  
   Create a new file named `styles.css` in the same folder as `index.html`.

2. **Link the CSS to HTML:**  
   Inside the `<head>` of `index.html`, add a link to `styles.css`:
   ```html
   <link rel="stylesheet" href="styles.css">
   ```

3. **CSS for Basic Styling:**  
   In `styles.css`, add some global styles:
   ```css
   body {
     font-family: Arial, sans-serif;
     background-color: #f4f4f4;
     color: #333;
     text-align: center;
     margin: 0;
   }

   header {
     background-color: #0073e6;
     color: white;
     padding: 1rem;
   }

   .languages-container {
     display: flex;
     justify-content: center;
     flex-wrap: wrap;
     gap: 1rem;
     padding: 2rem;
   }
   ```

4. **Language Card Styling:**  
   Add styles for `.language-card` to define its width and layout:
   ```css
   .language-card {
     width: 150px;
     border: 1px solid #ddd;
     border-radius: 8px;
     background-color: #fff;
     padding: 1rem;
     text-align: center;
     box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
     transition: transform 0.3s ease;
   }

   .language-card:hover {
     transform: scale(1.05);
   }
   ```

5. **Image Styling:**  
   Make sure each image fills the width of the card and has rounded corners:
   ```css
   .language-card img {
     width: 100%;
     border-radius: 8px;
   }
   ```

---

#### Step 3: Integrate Bootstrap for Interactivity

1. **Link to Bootstrap:**  
   Add the Bootstrap CDN link in the `<head>` section of `index.html` for Bootstrap’s CSS:
   ```html
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
   ```

2. **Convert Language Cards to Bootstrap Cards:**  
   Update each `.language-card` to use Bootstrap’s `card` class structure. Wrap content in `<div class="card-body">` and add a button to each card. Here’s an example for Python:
   ```html
   <div class="language-card card text-center">
     <img src="images/python-logo.png" class="card-img-top" alt="Python Logo">
     <div class="card-body">
       <h2 class="card-title">Python</h2>
       <p class="card-text">Python is known for its readability and versatility, making it popular in fields such as web development, data science, and automation.</p>
       <a href="https://www.python.org/" class="btn btn-primary" target="_blank">Learn More</a>
     </div>
   </div>
   ```

3. **Add Buttons for Other Languages:**  
   Repeat the button addition for JavaScript, Java, and C# cards, updating each button’s link and text accordingly.

4. **Add Bootstrap’s JavaScript for Full Support (Optional):**  
   At the end of `<body>`, include Bootstrap’s JavaScript bundle:
   ```html
   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
   ```

---

#### Step 4: Final Touches and Testing

1. **Preview the Page:**  
   Open `index.html` in a web browser to view your work. Ensure that:
   - The layout displays cards horizontally and wraps if there are too many.
   - Hovering over a card slightly enlarges it.
   - The "Learn More" button for each language links to a relevant resource.

2. **Adjust CSS as Needed:**  
   Modify styles in `styles.css` if you want to change card spacing, text alignment, or background colors.
