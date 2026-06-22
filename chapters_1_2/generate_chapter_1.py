import os
import random
import json

# ==========================================
# 1. GENERATE NOTES (chapter_1_notes.html)
# ==========================================

notes_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chapter 1: Equations & Inequalities - Revision Notes</title>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script src="https://www.desmos.com/api/v1.8/calculator.js?apiKey=dcb31709b452b1cf9dc26972add0fda6"></script>
    <style>
        :root { --primary: #0f172a; --secondary: #10b981; --bg: #f8fafc; --text: #334155; }
        body { font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; margin: 0; padding: 0; }
        .container { max-width: 900px; margin: 0 auto; padding: 2rem; }
        h1 { color: var(--primary); font-size: 2.5rem; border-bottom: 2px solid #cbd5e1; padding-bottom: 0.5rem; }
        h2 { color: var(--secondary); margin-top: 3rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem; }
        .card { background: white; border-radius: 0.5rem; padding: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 2rem; }
        .first-principles { background: #ecfdf5; border-left: 4px solid var(--secondary); padding: 1rem; font-style: italic; margin-bottom: 1.5rem; }
        .formulas { background: #eff6ff; border-left: 4px solid #3b82f6; padding: 1rem; margin-bottom: 1.5rem; }
        .methods { background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 0.5rem; padding: 1.5rem; margin-bottom: 1.5rem; }
        .example-box { background: #fff1f2; border-left: 4px solid #e11d48; padding: 1rem; margin-bottom: 1rem; }
        .calculator-container { width: 100%; height: 400px; margin-top: 1.5rem; border: 1px solid #cbd5e1; border-radius: 0.5rem; overflow: hidden; }
        ul { margin-top: 0; }
        h3 { color: #475569; margin-top: 0; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Chapter 1: Equations and Inequalities</h1>
        
        <div class="card">
            <h2>1.1 Linear Equations in One Variable</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> A linear equation represents a constant rate of change. Solving an equation like \(ax + b = 0\) geometrically means finding the single point where the line crosses the x-axis.
            </div>
            <div class="formulas">
                <h3>Key Definitions</h3>
                <ul>
                    <li><strong>Linear Equation:</strong> An equation that can be written in the form \(ax + b = 0\), where \(a \neq 0\).</li>
                    <li><strong>Identity:</strong> An equation that is true for all real numbers (e.g., \(x + 1 = x + 1\)). Solution set: \((-\infty, \infty)\).</li>
                    <li><strong>Conditional Equation:</strong> An equation true for at least one real number but not all (e.g., \(2x = 4\)).</li>
                    <li><strong>Inconsistent Equation:</strong> An equation with no solution (e.g., \(x = x + 1\)). Solution set: \(\emptyset\).</li>
                </ul>
            </div>
            <div class="methods">
                <h3>Step-by-Step Method: Solving Linear Equations</h3>
                <ol>
                    <li><strong>Clear fractions:</strong> Multiply both sides by the Least Common Denominator (LCD).</li>
                    <li><strong>Simplify:</strong> Use the distributive property to remove parentheses. Combine like terms on each side.</li>
                    <li><strong>Isolate the variable:</strong> Use addition/subtraction to move all variable terms to one side and constants to the other.</li>
                    <li><strong>Solve:</strong> Divide or multiply to get the variable by itself.</li>
                </ol>
            </div>
            <div class="example-box">
                <strong>Gotcha Example:</strong> When clearing fractions involving negative signs, like \( \frac{x}{2} - \frac{x-1}{3} = 1\), students often forget to distribute the negative sign to the \(-1\).<br>
                Correct algebraic step after multiplying by 6: \(3x - 2(x - 1) = 6 \implies 3x - 2x + 2 = 6\).
            </div>
        </div>

        <div class="card">
            <h2>1.2 Applications of Linear Equations</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> Word problems map real-world scenarios to algebraic structures. The goal is to translate English keywords into mathematical operations and define a single unknown variable.
            </div>
            <div class="formulas">
                <h3>Common Formulas</h3>
                <ul>
                    <li><strong>Simple Interest:</strong> \(I = Prt\) (Interest = Principal &times; rate &times; time)</li>
                    <li><strong>Distance-Rate-Time:</strong> \(d = rt\)</li>
                </ul>
            </div>
            <div class="methods">
                <h3>Step-by-Step Method: Mixture Problems</h3>
                <ol>
                    <li>Define \(x\) as the unknown amount of the first substance.</li>
                    <li>Express the second substance's amount in terms of \(x\) (e.g., \(100 - x\)).</li>
                    <li>Set up the concentration equation: \((\text{Concentration}_1)(\text{Volume}_1) + (\text{Concentration}_2)(\text{Volume}_2) = (\text{Final Concentration})(\text{Total Volume})\).</li>
                </ol>
            </div>
        </div>

        <div class="card">
            <h2>1.3 Quadratic Equations</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> A quadratic equation forms a parabola. Solving \(ax^2+bx+c=0\) means finding exactly where this parabola crosses the x-axis. Because parabolas curve back on themselves, they can cross the axis twice, once, or never!
            </div>
            <div class="formulas">
                <h3>Key Formulas</h3>
                <ul>
                    <li><strong>Standard Form:</strong> \(ax^2 + bx + c = 0\)</li>
                    <li><strong>Quadratic Formula:</strong> \(x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}\)</li>
                    <li><strong>Discriminant (\(\Delta\)):</strong> \(b^2 - 4ac\)
                        <ul>
                            <li>If \(\Delta &gt; 0\): Two distinct real roots.</li>
                            <li>If \(\Delta = 0\): One repeated real root.</li>
                            <li>If \(\Delta &lt; 0\): Two complex conjugate roots (no real x-intercepts).</li>
                        </ul>
                    </li>
                </ul>
            </div>
            <div class="methods">
                <h3>Step-by-Step Method: Completing the Square</h3>
                <ol>
                    <li>Divide by \(a\) so the coefficient of \(x^2\) is 1.</li>
                    <li>Move the constant term to the right side: \(x^2 + \frac{b}{a}x = -\frac{c}{a}\).</li>
                    <li>Take half of the \(x\) coefficient, square it, and add it to BOTH sides.</li>
                    <li>Factor the left side into a perfect square binomial: \((x + \frac{b}{2a})^2\).</li>
                    <li>Use the Square Root Property to solve for \(x\).</li>
                </ol>
            </div>
            <h3>Interactive Visualization</h3>
            <p>Use the sliders to see how \(a\), \(b\), and \(c\) shift the parabola. Watch the roots (x-intercepts) change!</p>
            <div id="calculator" class="calculator-container"></div>
        </div>

        <div class="card">
            <h2>1.4 Complex Numbers</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> When a parabola doesn't cross the x-axis, its roots are imaginary. We define \(i = \sqrt{-1}\), meaning \(i^2 = -1\). This expands our number system to handle all algebraic equations.
            </div>
            <div class="formulas">
                <h3>Key Definitions</h3>
                <ul>
                    <li><strong>Standard Form:</strong> \(a + bi\), where \(a\) is the real part and \(bi\) is the imaginary part.</li>
                    <li><strong>Complex Conjugate:</strong> The conjugate of \(a + bi\) is \(a - bi\). Their product is always a real number: \((a+bi)(a-bi) = a^2 + b^2\).</li>
                </ul>
            </div>
            <div class="methods">
                <h3>Step-by-Step Method: Dividing Complex Numbers</h3>
                <ol>
                    <li>Set up the division as a fraction: \(\frac{a+bi}{c+di}\).</li>
                    <li>Multiply both the numerator and the denominator by the <strong>complex conjugate of the denominator</strong>, which is \(c-di\).</li>
                    <li>Expand both using FOIL. Remember to replace any \(i^2\) with \(-1\).</li>
                    <li>Separate the result back into standard \(A + Bi\) form.</li>
                </ol>
            </div>
        </div>

        <div class="card">
            <h2>1.5 Other Types of Equations</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> Many higher-degree, radical, or rational equations can be converted into quadratic equations using algebraic manipulation or \(u\)-substitution.
            </div>
            <div class="methods">
                <h3>Method 1: Solving Radical Equations</h3>
                <ol>
                    <li>Isolate the radical on one side of the equation.</li>
                    <li>Raise both sides to the power of the index (e.g., square both sides for a square root).</li>
                    <li>Solve the resulting equation.</li>
                    <li><strong>CRITICAL:</strong> You MUST check for extraneous solutions by plugging answers back into the original equation. Squaring both sides can introduce false roots.</li>
                </ol>
                <h3>Method 2: Equations Quadratic in Form</h3>
                <p>If an equation looks like \(ax^{2n} + bx^n + c = 0\), use substitution:</p>
                <ol>
                    <li>Let \(u = x^n\).</li>
                    <li>Rewrite the equation as \(au^2 + bu + c = 0\).</li>
                    <li>Solve for \(u\) using factoring or the quadratic formula.</li>
                    <li>Substitute back (\(x^n = u\)) and solve for \(x\).</li>
                </ol>
            </div>
        </div>

        <div class="card">
            <h2>1.6 Inequalities</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> Inequalities represent an infinite continuous range of values (intervals) rather than specific points.
            </div>
            <div class="formulas">
                <h3>Interval Notation</h3>
                <ul>
                    <li><strong>Parentheses \(( )\) :</strong> Excludes the endpoint (used for \(&lt;\) or \(&gt;\), and always for \(\infty\) or \(-\infty\)).</li>
                    <li><strong>Brackets \([ ]\) :</strong> Includes the endpoint (used for \(\le\) or \(\ge\)).</li>
                </ul>
            </div>
            <div class="example-box">
                <strong>Gotcha Example:</strong> Solve \(-3x &gt; 12\).<br>
                Many students incorrectly divide by -3 and write \(x &gt; -4\).<br>
                <strong>The Golden Rule of Inequalities:</strong> When you multiply or divide both sides of an inequality by a negative number, YOU MUST FLIP THE INEQUALITY SIGN!<br>
                Result: \(x &lt; -4\), or in interval notation: \((-\infty, -4)\).
            </div>
        </div>

        <div class="card">
            <h2>1.7 Absolute Value Equations and Inequalities</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> Absolute value geometrically means "distance from zero." The equation \(|x| = 5\) asks: "What numbers are exactly 5 units away from zero?" The answers are 5 and -5.
            </div>
            <div class="formulas">
                <h3>Absolute Value Inequality Rules</h3>
                <ul>
                    <li><strong>"Less thAND" rule:</strong> \(|X| &lt; c \implies -c &lt; X &lt; c\). The distance is less than \(c\), so \(X\) is trapped between \(-c\) and \(c\).</li>
                    <li><strong>"GreatOR" rule:</strong> \(|X| &gt; c \implies X &gt; c \text{ OR } X &lt; -c\). The distance is greater than \(c\), so \(X\) is pushed outwards away from zero.</li>
                </ul>
            </div>
            <div class="methods">
                <h3>Step-by-Step Method</h3>
                <ol>
                    <li>Isolate the absolute value expression completely: \(|ax+b| = c\).</li>
                    <li>If \(c &lt; 0\), an equation or a "less than" inequality has <strong>No Solution</strong>. An absolute value cannot be negative!</li>
                    <li>Split into two separate equations/inequalities based on the rules above.</li>
                    <li>Solve each separately.</li>
                </ol>
            </div>
        </div>
    </div>

    <script>
        var elt = document.getElementById('calculator');
        var calculator = Desmos.GraphingCalculator(elt);
        calculator.setExpression({ id: 'graph1', latex: 'y = ax^2 + bx + c' });
        calculator.setExpression({ id: 'slider_a', latex: 'a=1', sliderBounds: { min: -5, max: 5 } });
        calculator.setExpression({ id: 'slider_b', latex: 'b=0', sliderBounds: { min: -5, max: 5 } });
        calculator.setExpression({ id: 'slider_c', latex: 'c=-4', sliderBounds: { min: -5, max: 5 } });
    </script>
</body>
</html>
"""

# ==========================================
# 2. GENERATE MCQ QUIZ (chapter_1_quiz.html)
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
    q1 = f"What does a discriminant of {-random.randint(1, 10)} indicate about a quadratic equation?"
    opts1, ans1 = generate_distractors("Two complex conjugate roots", "Two distinct real roots", "One repeated real root", "No roots exist at all")
    questions.append({"q": q1, "category": categories[0], "options": opts1, "answer": ans1, "explanation": "A negative discriminant means the roots involve the square root of a negative number, resulting in two complex conjugate roots."})

    # Category 2: Building Skills (Linear Inequalities)
    a = random.randint(2, 5)
    q2 = f"Solve the inequality: \\(-{a}x &gt; {a*3}\\)"
    opts2, ans2 = generate_distractors(f"\\(x &lt; -3\\)", f"\\(x &gt; -3\\)", f"\\(x &lt; 3\\)", f"\\(x &gt; 3\\)")
    questions.append({"q": q2, "category": categories[1], "options": opts2, "answer": ans2, "explanation": "When dividing by a negative number, you must flip the inequality symbol. So \\(x &lt; -3\\)."})

    # Category 3: Applying the Concepts (Mixture problem)
    b = random.randint(10, 20)
    q3 = f"If you have {b}L of a 10% acid solution, how many liters of pure (100%) acid must be added to create a 50% solution?"
    correct_amount = (0.5 * b - 0.1 * b) / 0.5
    correct3 = f"{correct_amount:.1f} L"
    opts3, ans3 = generate_distractors(correct3, f"{correct_amount*2:.1f} L", f"{correct_amount/2:.1f} L", f"{b} L")
    questions.append({"q": q3, "category": categories[2], "options": opts3, "answer": ans3, "explanation": "\\(0.10({b}) + 1.0(x) = 0.50({b} + x)\\). Solving for x gives the amount of pure acid to add."})

    # Category 4: Beyond the Basics (Quadratic in form)
    q4 = f"Find all real solutions: \\(x^4 - {i+5}x^2 + 4 = 0\\). Note: use substitution \\(u = x^2\\)."
    opts4, ans4 = generate_distractors("Varies based on roots", "No real solutions", "x = 2", "x = -2")
    questions.append({"q": q4, "category": categories[3], "options": opts4, "answer": ans4, "explanation": "This is quadratic in form. Substitute u = x^2, solve for u, then take the square root (if positive) to find x."})

    # Category 5: Critical Thinking
    q5 = f"Why is squaring both sides of \\(\\sqrt{{x}} = -{i+1}\\) considered a dangerous algebraic move?"
    correct5 = "It introduces extraneous solutions by discarding the negative sign."
    w1_5 = "Because you cannot square an unknown variable."
    w2_5 = "Because it makes the equation non-linear."
    w3_5 = "It is actually perfectly safe."
    opts5, ans5 = generate_distractors(correct5, w1_5, w2_5, w3_5)
    questions.append({"q": q5, "category": categories[4], "options": opts5, "answer": ans5, "explanation": "Squaring both sides makes \\(x = {(i+1)**2}\\). But plugging it back in gives \\({i+1} = -{i+1}\\), which is false. Squaring removes sign information."})

quiz_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chapter 1: MCQ Mastery</title>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background: #f1f5f9; color: #1e293b; padding: 2rem; max-width: 900px; margin: 0 auto; }
        .score-board { background: #0f172a; color: white; padding: 1rem 1.5rem; border-radius: 0.5rem; display: flex; justify-content: space-between; position: sticky; top: 1rem; z-index: 100; margin-bottom: 2rem; }
        .category-header { background: #e2e8f0; color: #0f172a; padding: 1rem; border-radius: 0.5rem; font-size: 1.4rem; font-weight: bold; margin-top: 3rem; border-left: 5px solid #10b981; }
        .card { background: white; border-radius: 0.5rem; padding: 1.5rem; margin-top: 1rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
        .btn-opt { display: block; width: 100%; text-align: left; padding: 1rem; margin-top: 0.5rem; background: transparent; border: 2px solid #cbd5e1; border-radius: 0.5rem; cursor: pointer; font-size: 1rem; transition: 0.2s; }
        .btn-opt:hover:not(:disabled) { border-color: #10b981; background: #ecfdf5; }
        .btn-opt.correct { background: #dcfce7; border-color: #22c55e; }
        .btn-opt.wrong { background: #fee2e2; border-color: #ef4444; }
        .btn-opt:disabled { cursor: not-allowed; opacity: 0.8; }
        .explanation { margin-top: 1rem; padding: 1rem; background: #f8fafc; border-left: 4px solid #10b981; display: none; }
        .explanation.show { display: block; }
    </style>
</head>
<body>
    <h1>Chapter 1: MCQ Quiz (50 Questions)</h1>
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
# 3. GENERATE FREEFORM QUIZ (chapter_1_freeform.html)
# ==========================================

freeform_questions = []

for i in range(20):
    a = random.randint(2, 6)
    b = random.randint(1, 5)
    q_type = i % 4
    if q_type == 0:
        q = f"Expand the quadratic: (x + {a})^2 - {b}"
        ans = f"x^2 + {2*a}x + {a**2 - b}"
    elif q_type == 1:
        q = f"Multiply complex numbers: ({a} + {b}i)({a} - {b}i). Treat 'i' as a variable."
        ans = f"{a**2} - {b**2}*(i^2)"
    elif q_type == 2:
        q = f"Solve for expression equal to 0: {a}x - {b} = x + 10"
        ans = f"{(a-1)}x - {b+10}"
    else:
        q = f"What is the discriminant of x^2 + {a}x + {b}?"
        ans = f"{a**2 - 4*b}"
        
    freeform_questions.append({
        "q": q,
        "a": ans
    })

freeform_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chapter 1: Freeform Mastery</title>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/11.8.0/math.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background: #f8fafc; color: #1e293b; padding: 2rem; max-width: 900px; margin: 0 auto; }
        .score-board { background: #0f172a; color: white; padding: 1rem 1.5rem; border-radius: 0.5rem; display: flex; justify-content: space-between; position: sticky; top: 1rem; z-index: 100; margin-bottom: 2rem; }
        .card { background: white; border-radius: 0.5rem; padding: 1.5rem; margin-top: 1rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border-left: 6px solid transparent; }
        .card.correct { border-left-color: #22c55e; }
        .card.wrong { border-left-color: #ef4444; }
        input[type="text"] { width: 60%; padding: 0.75rem; font-size: 1rem; border: 2px solid #cbd5e1; border-radius: 0.5rem; }
        button { background: #10b981; color: white; border: none; padding: 0.75rem 1.5rem; font-size: 1rem; font-weight: bold; border-radius: 0.5rem; cursor: pointer; }
        .feedback { margin-top: 1rem; font-weight: bold; display: none; }
    </style>
</head>
<body>
    <h1>Chapter 1: Freeform Quiz (20 Questions)</h1>
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
                    const testI = Math.sqrt(-1);
                    const scope = { x: testX, i: testI };
                    const valUser = nodeUser.evaluate(scope);
                    const valCorrect = nodeCorrect.evaluate(scope);
                    let diff;
                    if(valUser.re !== undefined && valCorrect.re !== undefined) {
                       diff = Math.abs(valUser.re - valCorrect.re);
                    } else {
                       diff = Math.abs(valUser - valCorrect);
                    }
                    if(diff > 0.0001) {
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
with open("/Users/ntnmathur/Desktop/precalc/chapters_1_2/chapter_1_notes.html", "w") as f: f.write(notes_html)
with open("/Users/ntnmathur/Desktop/precalc/chapters_1_2/chapter_1_quiz.html", "w") as f: f.write(quiz_html)
with open("/Users/ntnmathur/Desktop/precalc/chapters_1_2/chapter_1_freeform.html", "w") as f: f.write(freeform_html)
print("Chapter 1 files generated successfully!")
