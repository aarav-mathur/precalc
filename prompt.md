# Prompt Template for Future Chapters

*Copy and paste the following prompt when you want to generate revision materials for upcoming chapters in the textbook.*

---

Please read the next chapters (specify page range, e.g., pages 300 to 500) from the PDF in this folder and generate the following three self-contained HTML artifacts:

**1. Revision Notes (`revision_notes.html`)**
- A self-contained HTML file containing comprehensive notes for all topics covered in the chapters.
- Ensure you extract and cover *every single section and subtopic* from the Table of Contents. Do not skip any topic; this must serve as an exhaustive study guide.
- For each topic, include: a high-level summary, important formulas, first principles explanation (simple, intuitive terms), a worked-out example, and a Q&A example.
- Use MathJax via CDN for beautifully rendered mathematical equations.
- Include basic diagrams (using CSS/HTML/SVG) where appropriate.
- Style the page with a clean, modern CSS layout (e.g., sidebar navigation, distinct cards for each topic).

**2. Interactive MCQ Quiz (`quiz.html`)**
- A self-contained HTML file with multiple-choice questions spanning the topics in these chapters.
- **Difficulty**: Questions must be of "ultrathink" difficulty, requiring deep conceptual understanding, multi-step problem solving, and analytical thinking (collegiate/advanced high-school level).
- **Categorization**: You MUST categorize the questions strictly into these 5 textbook sections:
  1. Concepts and Vocabulary
  2. Building Skills
  3. Applying the Concepts
  4. Beyond the Basics
  5. Critical Thinking / Discussion / Writing
- Group the questions visually by these categories in the HTML layout.
- Ensure an interactive experience using vanilla Javascript: when a user clicks an option, immediately show whether it was correct or wrong and reveal a detailed explanation block.
- Keep a real-time score tracker.
- Provide a "Finish Quiz" button to display the final score and a "Restart Quiz" button to try again.
- Use MathJax for all formulas in questions and answers.
- Apply modern, responsive CSS styling.

**3. Interactive Freeform Quiz (`freeform_quiz.html`)**
- A self-contained HTML file with freeform questions spanning the topics in these chapters.
- Instead of multiple choice, use a freeform text input (`<input type="text">`) for the answers.
- **Difficulty**: "Ultrathink" difficulty level, similar to the MCQs.
- **Categorization**: You MUST categorize the questions strictly into the same 5 sections as above (Concepts and Vocabulary, Building Skills, Applying the Concepts, Beyond the Basics, Critical Thinking / Discussion / Writing), and display these categories in the UI.
- Implement robust Javascript grading that normalizes the user's input (e.g., removing spaces and making it lowercase) and compares it against a list of acceptable answers.
- Provide an interactive "Check" button. Upon clicking or hitting Enter, highlight the question as correct or incorrect, and reveal the accepted answers and a detailed explanation.
- Keep a real-time score tracker, a "Finish Quiz" summary modal, and a "Restart Quiz" button.
- Use MathJax for all formulas in questions and answers.
- Apply modern, responsive CSS styling.
