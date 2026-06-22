import os
import random
import json

# ==========================================
# 1. GENERATE NOTES (chapter_2_notes.html)
# ==========================================

notes_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chapter 2: Graphs and Functions - Revision Notes</title>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script src="https://www.desmos.com/api/v1.8/calculator.js?apiKey=dcb31709b452b1cf9dc26972add0fda6"></script>
    <style>
        :root { --primary: #0f172a; --secondary: #a855f7; --bg: #f8fafc; --text: #334155; }
        body { font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; margin: 0; padding: 0; }
        .container { max-width: 900px; margin: 0 auto; padding: 2rem; }
        h1 { color: var(--primary); font-size: 2.5rem; border-bottom: 2px solid #cbd5e1; padding-bottom: 0.5rem; }
        h2 { color: var(--secondary); margin-top: 3rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem; }
        .card { background: white; border-radius: 0.5rem; padding: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 2rem; }
        .first-principles { background: #faf5ff; border-left: 4px solid var(--secondary); padding: 1rem; font-style: italic; margin-bottom: 1.5rem; }
        .formulas { background: #f3e8ff; border-left: 4px solid #9333ea; padding: 1rem; margin-bottom: 1.5rem; }
        .methods { background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 0.5rem; padding: 1.5rem; margin-bottom: 1.5rem; }
        .example-box { background: #fff1f2; border-left: 4px solid #e11d48; padding: 1rem; margin-bottom: 1rem; }
        .calculator-container { width: 100%; height: 400px; margin-top: 1.5rem; border: 1px solid #cbd5e1; border-radius: 0.5rem; overflow: hidden; }
        ul { margin-top: 0; }
        h3 { color: #475569; margin-top: 0; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Chapter 2: Graphs and Functions</h1>
        
        <div class="card">
            <h2>2.1 The Rectangular Coordinate System and Graphs</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> The Cartesian plane maps algebraic equations into geometric shapes. René Descartes realized that geometry and algebra are the same thing! 
            </div>
            <div class="formulas">
                <h3>Key Formulas</h3>
                <ul>
                    <li><strong>Distance Formula:</strong> \(d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}\) (Derived directly from the Pythagorean Theorem \(a^2 + b^2 = c^2\)).</li>
                    <li><strong>Midpoint Formula:</strong> \((\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2})\). It is literally the average of the x's and the average of the y's.</li>
                </ul>
            </div>
            <div class="methods">
                <h3>Method: Finding Intercepts</h3>
                <ul>
                    <li><strong>x-intercept:</strong> Set \(y = 0\) and solve for \(x\). This is where the graph crosses the x-axis.</li>
                    <li><strong>y-intercept:</strong> Set \(x = 0\) and solve for \(y\). This is where the graph crosses the y-axis.</li>
                </ul>
            </div>
        </div>

        <div class="card">
            <h2>2.2 Circles</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> A circle is the set of all points exactly \(r\) distance from a center point \((h, k)\). If you set the distance formula equal to \(r\) and square both sides, you get the equation of a circle!
            </div>
            <div class="formulas">
                <h3>Formulas for Circles</h3>
                <ul>
                    <li><strong>Standard Form:</strong> \((x - h)^2 + (y - k)^2 = r^2\) (Center is \((h, k)\), radius is \(r\)).</li>
                    <li><strong>General Form:</strong> \(x^2 + y^2 + Dx + Ey + F = 0\)</li>
                </ul>
            </div>
            <div class="methods">
                <h3>Step-by-Step Method: Converting General to Standard Form</h3>
                <ol>
                    <li>Group \(x\) terms and \(y\) terms together. Move constants to the right side.</li>
                    <li><strong>Complete the Square for \(x\):</strong> Take half of the \(x\)-coefficient, square it, and add to BOTH sides.</li>
                    <li><strong>Complete the Square for \(y\):</strong> Take half of the \(y\)-coefficient, square it, and add to BOTH sides.</li>
                    <li>Factor the left side into two perfect squares: \((x - h)^2 + (y - k)^2\).</li>
                    <li>The right side simplifies to \(r^2\).</li>
                </ol>
            </div>
        </div>

        <div class="card">
            <h2>2.3 Lines</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> The slope of a line represents its constant rate of change. It is the ratio of vertical change (rise) to horizontal change (run).
            </div>
            <div class="formulas">
                <h3>Equations of Lines</h3>
                <ul>
                    <li><strong>Slope Formula:</strong> \(m = \frac{y_2 - y_1}{x_2 - x_1}\)</li>
                    <li><strong>Point-Slope Form:</strong> \(y - y_1 = m(x - x_1)\)</li>
                    <li><strong>Slope-Intercept Form:</strong> \(y = mx + b\)</li>
                    <li><strong>Standard Form:</strong> \(Ax + By = C\)</li>
                    <li><strong>Parallel Lines:</strong> Have equal slopes (\(m_1 = m_2\)).</li>
                    <li><strong>Perpendicular Lines:</strong> Have negative reciprocal slopes (\(m_1 \cdot m_2 = -1\)).</li>
                </ul>
            </div>
            <div class="example-box">
                <strong>Gotcha Example:</strong> "Find the equation of a line perpendicular to \(y = 3\) passing through \((2, 5)\)."<br>
                \(y = 3\) is a horizontal line (slope 0). A perpendicular line must be vertical (undefined slope). The equation for a vertical line is \(x = a\). Since it passes through \((2, 5)\), the line is simply \(x = 2\).
            </div>
        </div>

        <div class="card">
            <h2>2.4 Relations and Functions</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> A function is a strict rule that assigns exactly ONE output (y) to every input (x). It's a reliable machine—if you plug in 5, you will always get the exact same answer back.
            </div>
            <div class="formulas">
                <h3>Key Definitions</h3>
                <ul>
                    <li><strong>Domain:</strong> The set of all valid inputs (x-values).</li>
                    <li><strong>Range:</strong> The set of all resulting outputs (y-values).</li>
                </ul>
            </div>
            <div class="methods">
                <h3>Method: Finding the Domain Algebraically</h3>
                <p>Assume the domain is all real numbers \((-\infty, \infty)\) UNLESS:</p>
                <ol>
                    <li><strong>Fractions:</strong> The denominator cannot be zero. Set the denominator equal to zero and exclude those x-values.</li>
                    <li><strong>Even Roots:</strong> The inside of a square root (or any even root) cannot be negative. Set the expression under the root \(\ge 0\) and solve.</li>
                </ol>
            </div>
        </div>

        <div class="card">
            <h2>2.5 Properties of Functions</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> Functions have symmetries and behavior trends that help us quickly sketch their graphs without plotting every single point.
            </div>
            <div class="formulas">
                <h3>Symmetry</h3>
                <ul>
                    <li><strong>Even Functions:</strong> \(f(-x) = f(x)\). The graph is symmetric across the y-axis. (e.g., \(y = x^2\)).</li>
                    <li><strong>Odd Functions:</strong> \(f(-x) = -f(x)\). The graph has origin symmetry. If you rotate it 180 degrees, it looks exactly the same. (e.g., \(y = x^3\)).</li>
                </ul>
            </div>
            <div class="methods">
                <h3>Method: Increasing and Decreasing Intervals</h3>
                <p>Always read graphs from left to right (like a book).</p>
                <ul>
                    <li><strong>Increasing:</strong> Graph goes uphill.</li>
                    <li><strong>Decreasing:</strong> Graph goes downhill.</li>
                    <li><strong>Constant:</strong> Graph is perfectly flat.</li>
                </ul>
                <p><em>Note: We always use open parentheses \(( )\) when writing intervals of increasing/decreasing, because at the exact peak or valley, the graph is doing neither!</em></p>
            </div>
        </div>

        <div class="card">
            <h2>2.6 A Library of Functions</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> There are a handful of "Parent Functions" that serve as the building blocks for almost all algebra. You must memorize their shapes!
            </div>
            <div class="formulas">
                <h3>The 6 Parent Functions</h3>
                <ul>
                    <li><strong>Identity Function:</strong> \(f(x) = x\) (Diagonal line)</li>
                    <li><strong>Squaring Function:</strong> \(f(x) = x^2\) (U-shaped Parabola)</li>
                    <li><strong>Cubing Function:</strong> \(f(x) = x^3\) (S-shaped curve)</li>
                    <li><strong>Square Root Function:</strong> \(f(x) = \sqrt{x}\) (Half a sideways parabola)</li>
                    <li><strong>Absolute Value Function:</strong> \(f(x) = |x|\) (V-shape)</li>
                    <li><strong>Reciprocal Function:</strong> \(f(x) = \frac{1}{x}\) (Two hyperbola branches)</li>
                </ul>
            </div>
        </div>

        <div class="card">
            <h2>2.7 Transformations of Functions</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> Instead of making a table of values, we can graph complex functions by simply taking a parent function and shifting, stretching, or reflecting it! Modifying the input \(x\) affects the graph horizontally (and acts "backwards"). Modifying the output affects the graph vertically.
            </div>
            <div class="formulas">
                <h3>Transformation Rules for \(y = a \cdot f(b(x - h)) + k\)</h3>
                <ul>
                    <li><strong>\(+k\):</strong> Vertical shift up by \(k\).</li>
                    <li><strong>\(-h\):</strong> Horizontal shift right by \(h\). (Inside the function lies!)</li>
                    <li><strong>\(-f(x)\):</strong> Vertical reflection across the x-axis.</li>
                    <li><strong>\(f(-x)\):</strong> Horizontal reflection across the y-axis.</li>
                    <li><strong>\(a \cdot f(x)\):</strong> Vertical stretch by factor of \(a\).</li>
                </ul>
            </div>
            <h3>Interactive Visualization</h3>
            <p>Observe how \(a, h,\) and \(k\) transform the parent function \(f(x) = |x|\) in \(y = a|x - h| + k\).</p>
            <div id="calculator" class="calculator-container"></div>
        </div>

        <div class="card">
            <h2>2.8 Combining Functions; Composite Functions</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> Functions can be added, subtracted, multiplied, or divided just like numbers. But they can also be <em>composed</em>. Composition means passing an input through one function machine, and feeding the output directly into another function machine.
            </div>
            <div class="formulas">
                <h3>Composition Notation</h3>
                <p>\((f \circ g)(x) = f(g(x))\). This is read as "f composed with g of x" or "f of g of x".</p>
            </div>
            <div class="example-box">
                <strong>Gotcha Example:</strong> Evaluate \((f \circ g)(3)\) when \(f(x) = x^2\) and \(g(x) = x + 1\).<br>
                Work from the inside out!<br>
                1. Find \(g(3)\): \(3 + 1 = 4\).<br>
                2. Feed 4 into \(f\): \(f(4) = 4^2 = 16\).
            </div>
            <div class="methods">
                <h3>Method: Finding the Domain of a Composite Function</h3>
                <ol>
                    <li>The input \(x\) must be in the domain of the inner function \(g(x)\).</li>
                    <li>The output of the inner function, \(g(x)\), must fall within the domain of the outer function \(f\).</li>
                </ol>
            </div>
        </div>

        <div class="card">
            <h2>2.9 Inverse Functions</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> An inverse function completely undoes the original function. If \(f(x)\) turns a 2 into a 5, then \(f^{-1}(x)\) turns a 5 back into a 2. Graphically, an inverse is just a reflection across the diagonal line \(y = x\).
            </div>
            <div class="formulas">
                <h3>Key Concepts</h3>
                <ul>
                    <li><strong>One-to-One:</strong> A function must pass the Horizontal Line Test to have an inverse. If it fails, multiple x-values go to the same y-value, making it impossible to "undo" the mapping uniquely.</li>
                    <li><strong>Composition Verification:</strong> Two functions \(f\) and \(g\) are inverses if and only if \(f(g(x)) = x\) AND \(g(f(x)) = x\).</li>
                </ul>
            </div>
            <div class="methods">
                <h3>Step-by-Step Method: Finding the Inverse Algebraically</h3>
                <ol>
                    <li>Replace \(f(x)\) with \(y\).</li>
                    <li><strong>Swap \(x\) and \(y\).</strong> (This is the mathematical act of inverting).</li>
                    <li>Solve the new equation for \(y\).</li>
                    <li>Replace \(y\) with \(f^{-1}(x)\).</li>
                </ol>
            </div>
        </div>
    </div>

    <script>
        var elt = document.getElementById('calculator');
        var calculator = Desmos.GraphingCalculator(elt);
        calculator.setExpression({ id: 'graph1', latex: 'y = a\\left|x - h\\right| + k' });
        calculator.setExpression({ id: 'slider_a', latex: 'a=1', sliderBounds: { min: -5, max: 5 } });
        calculator.setExpression({ id: 'slider_h', latex: 'h=2', sliderBounds: { min: -5, max: 5 } });
        calculator.setExpression({ id: 'slider_k', latex: 'k=-1', sliderBounds: { min: -5, max: 5 } });
    </script>
</body>
</html>
"""

# ==========================================
# 2. GENERATE MCQ QUIZ (chapter_2_quiz.html)
# ==========================================

questions = []
categories = [
    "Concepts and Vocabulary",
    "Building Skills",
    "Applying the Concepts",
    "Beyond the Basics",
    "Critical Thinking / Discussion / Writing"
]

def generate_distractors(correct, wrong1, wrong2, wrong3):
    opts = [correct, wrong1, wrong2, wrong3]
    random.shuffle(opts)
    return opts, opts.index(correct)

for i in range(10):
    # Category 1: Concepts
    q1 = f"If \\(f(x)\\) is an odd function, what must be true about \\(f(-x)\\)?"
    opts1, ans1 = generate_distractors("\\(f(-x) = -f(x)\\)", "\\(f(-x) = f(x)\\)", "\\(f(-x) = 0\\)", "\\(f(-x) = 1/f(x)\\)")
    questions.append({"q": q1, "category": categories[0], "options": opts1, "answer": ans1, "explanation": "By definition, an odd function has origin symmetry, meaning \\(f(-x) = -f(x)\\)."})

    # Category 2: Building Skills (Transformations)
    h = random.randint(2, 5)
    k = random.randint(2, 5)
    q2 = f"Which equation represents the graph of \\(y = x^2\\) shifted {h} units left and {k} units down?"
    opts2, ans2 = generate_distractors(f"\\(y = (x + {h})^2 - {k}\\)", f"\\(y = (x - {h})^2 - {k}\\)", f"\\(y = (x + {h})^2 + {k}\\)", f"\\(y = (x - {h})^2 + {k}\\)")
    questions.append({"q": q2, "category": categories[1], "options": opts2, "answer": ans2, "explanation": "Horizontal shift left by h means \\(x+h\\). Vertical shift down by k means \\(-k\\)."})

    # Category 3: Applying the Concepts (Functions)
    c = random.randint(2, 10)
    q3 = f"Given \\(f(x) = {c}x + 2\\), find \\(f(a+h) - f(a)\\)."
    opts3, ans3 = generate_distractors(f"\\({c}h\\)", f"\\({c}a + {c}h + 2\\)", f"\\({c}h + 2\\)", f"\\({c}a\\)")
    questions.append({"q": q3, "category": categories[2], "options": opts3, "answer": ans3, "explanation": "\\(f(a+h) = {c}(a+h) + 2 = {c}a + {c}h + 2\\). Subtract \\(f(a) = {c}a + 2\\) to get \\({c}h\\)."})

    # Category 4: Beyond the Basics (Inverses)
    q4 = f"Find the inverse of \\(f(x) = \\frac{{{i+1}}}{{x-2}}\\)"
    correct4 = f"\\(f^{{-1}}(x) = \\frac{{{i+1}}}{{x}} + 2\\)"
    w1_4 = f"\\(f^{{-1}}(x) = \\frac{{{i+1}}}{{x+2}}\\)"
    w2_4 = f"\\(f^{{-1}}(x) = \\frac{{x-2}}{{{i+1}}}\\)"
    w3_4 = f"\\(f^{{-1}}(x) = \\frac{{{i+1}x}}{{2}}\\)"
    opts4, ans4 = generate_distractors(correct4, w1_4, w2_4, w3_4)
    questions.append({"q": q4, "category": categories[3], "options": opts4, "answer": ans4, "explanation": "Swap x and y: \\(x = \\frac{{{i+1}}}{{y-2}}\\). Solve for y: \\(y-2 = \\frac{{{i+1}}}{{x}}\\), so \\(y = \\frac{{{i+1}}}{{x}} + 2\\)."})

    # Category 5: Critical Thinking
    q5 = f"Why does the vertical line test work for determining if a graph is a function?"
    correct5 = "Because a function can only have one y-value for any given x-value."
    w1_5 = "Because a function must have an inverse."
    w2_5 = "Because vertical lines have an undefined slope."
    w3_5 = "Because it checks if the domain is continuous."
    opts5, ans5 = generate_distractors(correct5, w1_5, w2_5, w3_5)
    questions.append({"q": q5, "category": categories[4], "options": opts5, "answer": ans5, "explanation": "If a vertical line intersects the graph twice, it means the single x-value produced two different y-values, breaking the definition of a function."})

quiz_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chapter 2: MCQ Mastery</title>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background: #f1f5f9; color: #1e293b; padding: 2rem; max-width: 900px; margin: 0 auto; }
        .score-board { background: #0f172a; color: white; padding: 1rem 1.5rem; border-radius: 0.5rem; display: flex; justify-content: space-between; position: sticky; top: 1rem; z-index: 100; margin-bottom: 2rem; }
        .category-header { background: #e2e8f0; color: #0f172a; padding: 1rem; border-radius: 0.5rem; font-size: 1.4rem; font-weight: bold; margin-top: 3rem; border-left: 5px solid #a855f7; }
        .card { background: white; border-radius: 0.5rem; padding: 1.5rem; margin-top: 1rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
        .btn-opt { display: block; width: 100%; text-align: left; padding: 1rem; margin-top: 0.5rem; background: transparent; border: 2px solid #cbd5e1; border-radius: 0.5rem; cursor: pointer; font-size: 1rem; transition: 0.2s; }
        .btn-opt:hover:not(:disabled) { border-color: #a855f7; background: #faf5ff; }
        .btn-opt.correct { background: #dcfce7; border-color: #22c55e; }
        .btn-opt.wrong { background: #fee2e2; border-color: #ef4444; }
        .btn-opt:disabled { cursor: not-allowed; opacity: 0.8; }
        .explanation { margin-top: 1rem; padding: 1rem; background: #f8fafc; border-left: 4px solid #a855f7; display: none; }
        .explanation.show { display: block; }
    </style>
</head>
<body>
    <h1>Chapter 2: MCQ Quiz (50 Questions)</h1>
    <div class="score-board">
        <h3>Score: <span id="score">0</span> / 50</h3>
        <h3>Attempted: <span id="attempted">0</span></h3>
    </div>
    <div id="quiz-container"></div>
    
    <script>
        const questions = REPLACE_ME_WITH_JSON;
        let score = 0, attempted = 0;
        const container = document.getElementById('quiz-container');
        
        let currentCat = "";
        questions.forEach((q, i) => {
            if (q.category !== currentCat) {
                currentCat = q.category;
                const catDiv = document.createElement('div');
                catDiv.className = 'category-header';
                catDiv.innerHTML = currentCat;
                container.appendChild(catDiv);
            }
            
            let html = `<div class="card"><p><strong>${i+1}.</strong> ${q.q}</p>`;
            q.options.forEach((opt, j) => {
                html += `<button class="btn-opt" id="q${i}-opt${j}" onclick="check(${i}, ${j})">${opt}</button>`;
            });
            html += `<div class="explanation" id="exp${i}"><strong>Explanation:</strong> ${q.explanation}</div></div>`;
            container.innerHTML += html;
        });

        function check(qIndex, optIndex) {
            const q = questions[qIndex];
            const isCorrect = (optIndex === q.answer);
            
            document.getElementById(`q${qIndex}-opt${optIndex}`).classList.add(isCorrect ? 'correct' : 'wrong');
            if(!isCorrect) document.getElementById(`q${qIndex}-opt${q.answer}`).classList.add('correct');
            
            q.options.forEach((_, j) => document.getElementById(`q${qIndex}-opt${j}`).disabled = true);
            document.getElementById(`exp${qIndex}`).classList.add('show');
            
            if(isCorrect) score++;
            attempted++;
            document.getElementById('score').innerText = score;
            document.getElementById('attempted').innerText = attempted;
        }
    </script>
</body>
</html>
""".replace("REPLACE_ME_WITH_JSON", json.dumps(questions))

# ==========================================
# 3. GENERATE FREEFORM QUIZ (chapter_2_freeform.html)
# ==========================================

freeform_questions = []

for i in range(20):
    a = random.randint(2, 6)
    b = random.randint(1, 5)
    q_type = i % 4
    if q_type == 0:
        q = f"Evaluate f(x) = x^2 - {a}x at x = {b}"
        ans = f"{b**2 - a*b}"
    elif q_type == 1:
        q = f"If f(x) = x+{a} and g(x) = {b}x^2, find f(g(x))"
        ans = f"{b}x^2 + {a}"
    elif q_type == 2:
        q = f"Find the inverse of y = {a}x - {b}"
        ans = f"(x+{b})/{a}"
    else:
        q = f"What is the slope of the line {a}x - {b}y = 8?"
        ans = f"{a}/{b}"
        
    freeform_questions.append({
        "q": q,
        "a": ans
    })

freeform_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chapter 2: Freeform Mastery</title>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/11.8.0/math.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background: #f8fafc; color: #1e293b; padding: 2rem; max-width: 900px; margin: 0 auto; }
        .score-board { background: #0f172a; color: white; padding: 1rem 1.5rem; border-radius: 0.5rem; display: flex; justify-content: space-between; position: sticky; top: 1rem; z-index: 100; margin-bottom: 2rem; }
        .card { background: white; border-radius: 0.5rem; padding: 1.5rem; margin-top: 1rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border-left: 6px solid transparent; }
        .card.correct { border-left-color: #22c55e; }
        .card.wrong { border-left-color: #ef4444; }
        input[type="text"] { width: 60%; padding: 0.75rem; font-size: 1rem; border: 2px solid #cbd5e1; border-radius: 0.5rem; }
        button { background: #a855f7; color: white; border: none; padding: 0.75rem 1.5rem; font-size: 1rem; font-weight: bold; border-radius: 0.5rem; cursor: pointer; }
        .feedback { margin-top: 1rem; font-weight: bold; display: none; }
    </style>
</head>
<body>
    <h1>Chapter 2: Freeform Quiz (20 Questions)</h1>
    <p><em>Type your answers algebraically. Math.js will evaluate equivalence!</em></p>
    
    <div class="score-board">
        <h3>Score: <span id="score">0</span> / 20</h3>
    </div>
    
    <div id="quiz-container"></div>

    <script>
        const questions = REPLACE_ME_WITH_JSON;
        const container = document.getElementById('quiz-container');
        
        questions.forEach((q, i) => {
            let html = `
            <div class="card" id="card${i}">
                <p><strong>${i+1}.</strong> ${q.q}</p>
                <input type="text" id="input${i}" placeholder="e.g. x^2 + 2x">
                <button onclick="checkFreeform(${i}, '${q.a}')">Check</button>
                <div class="feedback" id="feedback${i}"></div>
            </div>`;
            container.innerHTML += html;
        });

        let score = 0;
        function checkFreeform(index, correctAnswerStr) {
            const userStr = document.getElementById('input' + index).value;
            const card = document.getElementById('card' + index);
            const feedback = document.getElementById('feedback' + index);
            if(!userStr) return;
            try {
                const nodeUser = math.parse(userStr).compile();
                const nodeCorrect = math.parse(correctAnswerStr).compile();
                let isEquivalent = true;
                for(let i=0; i<5; i++) {
                    const testX = Math.random() * 10 + 1;
                    const testH = Math.random() * 10 + 1;
                    const scope = { x: testX, h: testH };
                    const valUser = nodeUser.evaluate(scope);
                    const valCorrect = nodeCorrect.evaluate(scope);
                    if(Math.abs(valUser - valCorrect) > 0.0001) {
                        isEquivalent = false; break;
                    }
                }
                if(isEquivalent) {
                    card.classList.add('correct');
                    feedback.innerHTML = "✅ Correct! Math.js verified equivalence.";
                    feedback.style.color = "#166534";
                    score++; document.getElementById('score').innerText = score;
                } else {
                    card.classList.add('wrong');
                    feedback.innerHTML = "❌ Incorrect.";
                    feedback.style.color = "#991b1b";
                }
                feedback.style.display = "block";
            } catch (err) {
                feedback.innerHTML = "⚠️ Syntax Error.";
                feedback.style.color = "#ca8a04";
                feedback.style.display = "block";
            }
        }
    </script>
</body>
</html>
""".replace("REPLACE_ME_WITH_JSON", json.dumps(freeform_questions))

os.makedirs("/Users/ntnmathur/Desktop/precalc/chapters_1_2", exist_ok=True)
with open("/Users/ntnmathur/Desktop/precalc/chapters_1_2/chapter_2_notes.html", "w") as f: f.write(notes_html)
with open("/Users/ntnmathur/Desktop/precalc/chapters_1_2/chapter_2_quiz.html", "w") as f: f.write(quiz_html)
with open("/Users/ntnmathur/Desktop/precalc/chapters_1_2/chapter_2_freeform.html", "w") as f: f.write(freeform_html)
print("Chapter 2 files generated successfully!")
