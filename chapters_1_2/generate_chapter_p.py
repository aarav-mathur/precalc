import os
import random
import json

# ==========================================
# 1. GENERATE NOTES (chapter_p_notes.html)
# ==========================================

notes_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chapter P: Prerequisites - Revision Notes</title>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script src="https://www.desmos.com/api/v1.8/calculator.js?apiKey=dcb31709b452b1cf9dc26972add0fda6"></script>
    <style>
        :root { --primary: #0f172a; --secondary: #3b82f6; --bg: #f8fafc; --text: #334155; }
        body { font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; margin: 0; padding: 0; }
        .container { max-width: 900px; margin: 0 auto; padding: 2rem; }
        h1 { color: var(--primary); font-size: 2.5rem; border-bottom: 2px solid #cbd5e1; padding-bottom: 0.5rem; }
        h2 { color: var(--secondary); margin-top: 3rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem; }
        .card { background: white; border-radius: 0.5rem; padding: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 2rem; }
        .first-principles { background: #eff6ff; border-left: 4px solid var(--secondary); padding: 1rem; font-style: italic; margin-bottom: 1.5rem; }
        .formulas { background: #f8fafc; border-left: 4px solid #64748b; padding: 1rem; margin-bottom: 1.5rem; }
        .methods { background: #f1f5f9; border: 1px solid #cbd5e1; border-radius: 0.5rem; padding: 1.5rem; margin-bottom: 1.5rem; }
        .example-box { background: #fff1f2; border-left: 4px solid #e11d48; padding: 1rem; margin-bottom: 1rem; }
        .calculator-container { width: 100%; height: 400px; margin-top: 1.5rem; border: 1px solid #cbd5e1; border-radius: 0.5rem; overflow: hidden; }
        ul { margin-top: 0; }
        h3 { color: #475569; margin-top: 0; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Chapter P: Prerequisites</h1>
        
        <div class="card">
            <h2>P.1 The Real Numbers and Their Properties</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> The real number system \(\mathbb{R}\) forms a continuous line. It contains both rational numbers (fractions) and irrational numbers (numbers with non-repeating, non-terminating decimals).
            </div>
            <div class="formulas">
                <h3>Key Definitions & Properties</h3>
                <ul>
                    <li><strong>Natural Numbers \(\mathbb{N}\):</strong> \(\{1, 2, 3, \dots\}\)</li>
                    <li><strong>Integers \(\mathbb{Z}\):</strong> \(\{\dots, -2, -1, 0, 1, 2, \dots\}\)</li>
                    <li><strong>Rational Numbers \(\mathbb{Q}\):</strong> Any number that can be expressed as \(\frac{p}{q}\).</li>
                    <li><strong>Commutative Property:</strong> \(a + b = b + a\) and \(ab = ba\). (Order doesn't matter).</li>
                    <li><strong>Associative Property:</strong> \((a+b)+c = a+(b+c)\). (Grouping doesn't matter).</li>
                    <li><strong>Distributive Property:</strong> \(a(b+c) = ab + ac\).</li>
                </ul>
            </div>
            <div class="methods">
                <h3>Absolute Value Distance</h3>
                <p>The distance between any two points \(a\) and \(b\) on the real number line is exactly \(|a - b|\) or \(|b - a|\).</p>
            </div>
        </div>

        <div class="card">
            <h2>P.2 Integer Exponents and Scientific Notation</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> Exponents are just a shorthand for repeated multiplication. A negative exponent is the inverse of multiplication—it means repeated division (the reciprocal).
            </div>
            <div class="formulas">
                <h3>Rules of Exponents</h3>
                <ul>
                    <li><strong>Product Rule:</strong> \(b^m \cdot b^n = b^{m+n}\)</li>
                    <li><strong>Quotient Rule:</strong> \(\frac{b^m}{b^n} = b^{m-n}\)</li>
                    <li><strong>Power Rule:</strong> \((b^m)^n = b^{m \cdot n}\)</li>
                    <li><strong>Negative Exponent Rule:</strong> \(b^{-n} = \frac{1}{b^n}\) and \(\frac{1}{b^{-n}} = b^n\)</li>
                    <li><strong>Zero Exponent Rule:</strong> \(b^0 = 1\) (for \(b \neq 0\))</li>
                </ul>
            </div>
            <div class="example-box">
                <strong>Gotcha Example:</strong> Simplify \((-3x^4)^2\).<br>
                Many students forget to square the negative sign or the 3. They write \(-3x^8\).<br>
                <strong>Correct:</strong> \((-3)^2(x^4)^2 = 9x^8\).
            </div>
        </div>

        <div class="card">
            <h2>P.3 Polynomials</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> A polynomial is an algebraic expression consisting of variables and coefficients, involving only addition, subtraction, multiplication, and non-negative integer exponents.
            </div>
            <div class="formulas">
                <h3>Special Products</h3>
                <ul>
                    <li><strong>Sum and Difference of Same Terms:</strong> \((A + B)(A - B) = A^2 - B^2\)</li>
                    <li><strong>Squaring a Binomial:</strong> \((A + B)^2 = A^2 + 2AB + B^2\)</li>
                    <li><strong>Cubing a Binomial:</strong> \((A + B)^3 = A^3 + 3A^2B + 3AB^2 + B^3\)</li>
                </ul>
            </div>
            <div class="methods">
                <h3>Method: FOIL (First, Outer, Inner, Last)</h3>
                <p>To multiply two binomials \((ax+b)(cx+d)\):</p>
                <ol>
                    <li>Multiply First terms: \((ax)(cx)\)</li>
                    <li>Multiply Outer terms: \((ax)(d)\)</li>
                    <li>Multiply Inner terms: \((b)(cx)\)</li>
                    <li>Multiply Last terms: \((b)(d)\)</li>
                    <li>Combine like terms.</li>
                </ol>
            </div>
        </div>

        <div class="card">
            <h2>P.4 Factoring Polynomials</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> Factoring is the inverse of polynomial multiplication. We break a polynomial down into its irreducible "prime" pieces. This is critical for solving equations because of the Zero-Product Property.
            </div>
            <div class="formulas">
                <h3>Factoring Formulas</h3>
                <ul>
                    <li><strong>Difference of Squares:</strong> \(A^2 - B^2 = (A - B)(A + B)\)</li>
                    <li><strong>Difference of Cubes:</strong> \(A^3 - B^3 = (A - B)(A^2 + AB + B^2)\)</li>
                    <li><strong>Sum of Cubes:</strong> \(A^3 + B^3 = (A + B)(A^2 - AB + B^2)\)</li>
                </ul>
            </div>
            <div class="methods">
                <h3>General Strategy for Factoring</h3>
                <ol>
                    <li>Factor out the Greatest Common Factor (GCF) first.</li>
                    <li>If it has 2 terms, check for difference of squares or sum/difference of cubes.</li>
                    <li>If it has 3 terms, check for perfect square trinomials, or factor by grouping/ac-method.</li>
                    <li>If it has 4 terms, try factoring by grouping.</li>
                </ol>
            </div>
            <h3>Interactive Visualization</h3>
            <p>Factored forms reveal the roots (x-intercepts) of a polynomial graph! Move the sliders to change the roots.</p>
            <div id="calculator" class="calculator-container"></div>
        </div>

        <div class="card">
            <h2>P.5 Rational Expressions</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> A rational expression is the quotient of two polynomials. It behaves exactly like numerical fractions, meaning you must find common denominators to add/subtract, and you can only cancel common <strong>factors</strong>, not terms.
            </div>
            <div class="methods">
                <h3>Method: Adding/Subtracting Rational Expressions</h3>
                <ol>
                    <li>Factor the denominators completely.</li>
                    <li>Find the Least Common Denominator (LCD).</li>
                    <li>Multiply the numerator and denominator of each fraction by whatever factors they are missing from the LCD.</li>
                    <li>Add/subtract the numerators over the common LCD.</li>
                    <li>Factor the new numerator to see if anything can cancel with the denominator.</li>
                </ol>
            </div>
            <div class="example-box">
                <strong>Gotcha Example:</strong> Simplify \(\frac{x^2 + 5}{x}\).<br>
                Many students illegally "cancel" the \(x\) to get \(x + 5\). You CANNOT cancel parts of an addition expression!<br>
                <strong>Correct:</strong> This expression cannot be simplified by factoring. It is already simplified. (Or split into \(\frac{x^2}{x} + \frac{5}{x} = x + \frac{5}{x}\)).
            </div>
        </div>

        <div class="card">
            <h2>P.6 Rational Exponents and Radicals</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> A rational (fractional) exponent is just a compact way of writing a radical. The denominator of the exponent is the index of the root, and the numerator is the power.
            </div>
            <div class="formulas">
                <h3>Key Formulas</h3>
                <ul>
                    <li><strong>Definition:</strong> \(a^{m/n} = (\sqrt[n]{a})^m = \sqrt[n]{a^m}\)</li>
                    <li><strong>Product Property of Radicals:</strong> \(\sqrt[n]{ab} = \sqrt[n]{a}\sqrt[n]{b}\)</li>
                    <li><strong>Quotient Property of Radicals:</strong> \(\sqrt[n]{\frac{a}{b}} = \frac{\sqrt[n]{a}}{\sqrt[n]{b}}\)</li>
                </ul>
            </div>
            <div class="methods">
                <h3>Method: Rationalizing Denominators</h3>
                <p>When you have a radical in the denominator (like \(\frac{5}{\sqrt{3}}\) or \(\frac{2}{\sqrt{x} - 1}\)), you must eliminate it.</p>
                <ul>
                    <li><strong>Single Radical:</strong> Multiply numerator and denominator by the radical. \(\frac{5}{\sqrt{3}} \cdot \frac{\sqrt{3}}{\sqrt{3}} = \frac{5\sqrt{3}}{3}\).</li>
                    <li><strong>Binomial Radical:</strong> Multiply by the <em>conjugate</em>. For \(\frac{2}{\sqrt{x} - 1}\), multiply top and bottom by \((\sqrt{x} + 1)\). The denominator becomes \((\sqrt{x})^2 - 1^2 = x - 1\).</li>
                </ul>
            </div>
        </div>
    </div>

    <script>
        var elt = document.getElementById('calculator');
        var calculator = Desmos.GraphingCalculator(elt);
        calculator.setExpression({ id: 'graph1', latex: 'y = (x-a)(x-b)(x-c)' });
        calculator.setExpression({ id: 'slider_a', latex: 'a=1', sliderBounds: { min: -5, max: 5 } });
        calculator.setExpression({ id: 'slider_b', latex: 'b=-2', sliderBounds: { min: -5, max: 5 } });
        calculator.setExpression({ id: 'slider_c', latex: 'c=3', sliderBounds: { min: -5, max: 5 } });
    </script>
</body>
</html>
"""

# ==========================================
# 2. GENERATE MCQ QUIZ (chapter_p_quiz.html)
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
    q1 = f"Which property justifies the statement: If \\({i+2}x = {i+5}\\), then \\({i+5} = {i+2}x\\)?"
    opts1, ans1 = generate_distractors("Symmetric Property", "Reflexive Property", "Transitive Property", "Commutative Property")
    questions.append({"q": q1, "category": categories[0], "options": opts1, "answer": ans1, "explanation": "The Symmetric Property states that if a=b, then b=a."})

    # Category 2: Building Skills
    a = random.randint(2, 9)
    q2 = f"Factor completely: \\({a**2}x^2 - 81\\)"
    correct2 = f"\\(({a}x - 9)({a}x + 9)\\)"
    opts2, ans2 = generate_distractors(correct2, f"\\(({a}x - 9)^2\\)", f"\\(({a**2}x - 9)({a**2}x + 9)\\)", f"\\(({a}x - 81)({a}x + 81)\\)")
    questions.append({"q": q2, "category": categories[1], "options": opts2, "answer": ans2, "explanation": "Difference of squares."})

    # Category 3: Applying the Concepts
    b = random.randint(2, 5)
    c = random.randint(2, 4)
    q3 = "Simplify the expression using exponent rules: \\( (\\frac{x^" + str(b) + "}{y^{-" + str(c) + "}})^{-2} \\)"
    correct3 = f"\\( \\frac{{1}}{{x^{b*2}y^{c*2}}} \\)"
    opts3, ans3 = generate_distractors(correct3, f"\\( \\frac{{y^{c*2}}}{{x^{b*2}}} \\)", f"\\( \\frac{{x^{b*2}}}{{y^{c*2}}} \\)", f"\\( \\frac{{1}}{{x^{b+2}y^{c+2}}} \\)")
    questions.append({"q": q3, "category": categories[2], "options": opts3, "answer": ans3, "explanation": "Flip the fraction and multiply exponents."})

    # Category 4: Beyond the Basics
    d = random.randint(2, 5)
    q4 = f"Rationalize the denominator: \\( \\frac{{{d}}}{{ \\sqrt{{x}} - {d} }} \\)"
    correct4 = f"\\( \\frac{{{d}\\sqrt{{x}} + {d**2}}}{{x - {d**2}}} \\)"
    opts4, ans4 = generate_distractors(correct4, f"\\( \\frac{{{d}\\sqrt{{x}} - {d**2}}}{{x - {d**2}}} \\)", f"\\( \\frac{{{d}\\sqrt{{x}} + {d**2}}}{{x + {d**2}}} \\)", f"\\( \\frac{{{d}\\sqrt{{x}} + {d}}}{{x - {d**2}}} \\)")
    questions.append({"q": q4, "category": categories[3], "options": opts4, "answer": ans4, "explanation": "Multiply numerator and denominator by conjugate."})

    # Category 5: Critical Thinking
    q5 = f"Why is the domain of \\( \\frac{{1}}{{\\sqrt{{x - {i+1}}}}} \\) restricted to \\( x &gt; {i+1} \\) instead of \\( x \\ge {i+1} \\)?"
    correct5 = f"Because \\(x = {i+1}\\) causes division by zero."
    opts5, ans5 = generate_distractors(correct5, f"Because the square root of {i+1} is irrational.", "Because you cannot take the square root of a negative number.", "Because fractions cannot have a positive denominator.")
    questions.append({"q": q5, "category": categories[4], "options": opts5, "answer": ans5, "explanation": "Division by zero is undefined."})

quiz_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chapter P: MCQ Mastery</title>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background: #f1f5f9; color: #1e293b; padding: 2rem; max-width: 900px; margin: 0 auto; }
        .score-board { background: #0f172a; color: white; padding: 1rem 1.5rem; border-radius: 0.5rem; display: flex; justify-content: space-between; position: sticky; top: 1rem; z-index: 100; margin-bottom: 2rem; }
        .category-header { background: #e2e8f0; color: #0f172a; padding: 1rem; border-radius: 0.5rem; font-size: 1.4rem; font-weight: bold; margin-top: 3rem; border-left: 5px solid #3b82f6; }
        .card { background: white; border-radius: 0.5rem; padding: 1.5rem; margin-top: 1rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
        .btn-opt { display: block; width: 100%; text-align: left; padding: 1rem; margin-top: 0.5rem; background: transparent; border: 2px solid #cbd5e1; border-radius: 0.5rem; cursor: pointer; font-size: 1rem; transition: 0.2s; }
        .btn-opt:hover:not(:disabled) { border-color: #3b82f6; background: #eff6ff; }
        .btn-opt.correct { background: #dcfce7; border-color: #22c55e; }
        .btn-opt.wrong { background: #fee2e2; border-color: #ef4444; }
        .btn-opt:disabled { cursor: not-allowed; opacity: 0.8; }
        .explanation { margin-top: 1rem; padding: 1rem; background: #f8fafc; border-left: 4px solid #3b82f6; display: none; }
        .explanation.show { display: block; }
    </style>
</head>
<body>
    <h1>Chapter P: MCQ Quiz (50 Questions)</h1>
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
# 3. GENERATE FREEFORM QUIZ (chapter_p_freeform.html)
# ==========================================

freeform_questions = []

for i in range(20):
    a = random.randint(2, 6)
    b = random.randint(1, 5)
    q_type = i % 4
    if q_type == 0:
        q = f"Expand and simplify: (x - {a})(x + {b})"
        ans = f"x^2 + {b-a}x - {a*b}"
    elif q_type == 1:
        q = f"Factor completely: x^2 - {a**2}"
        ans = f"(x-{a})(x+{a})"
    elif q_type == 2:
        q = f"Simplify the rational expression: (x^2 - {a**2}) / (x - {a})"
        ans = f"x+{a}"
    else:
        q = f"Expand the perfect square: (x + {b})^2"
        ans = f"x^2 + {2*b}x + {b**2}"
        
    freeform_questions.append({
        "q": q,
        "a": ans
    })

freeform_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chapter P: Freeform Mastery</title>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/11.8.0/math.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background: #f8fafc; color: #1e293b; padding: 2rem; max-width: 900px; margin: 0 auto; }
        .score-board { background: #0f172a; color: white; padding: 1rem 1.5rem; border-radius: 0.5rem; display: flex; justify-content: space-between; position: sticky; top: 1rem; z-index: 100; margin-bottom: 2rem; }
        .card { background: white; border-radius: 0.5rem; padding: 1.5rem; margin-top: 1rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border-left: 6px solid transparent; }
        .card.correct { border-left-color: #22c55e; }
        .card.wrong { border-left-color: #ef4444; }
        input[type="text"] { width: 60%; padding: 0.75rem; font-size: 1rem; border: 2px solid #cbd5e1; border-radius: 0.5rem; }
        button { background: #3b82f6; color: white; border: none; padding: 0.75rem 1.5rem; font-size: 1rem; font-weight: bold; border-radius: 0.5rem; cursor: pointer; }
        .feedback { margin-top: 1rem; font-weight: bold; display: none; }
    </style>
</head>
<body>
    <h1>Chapter P: Freeform Quiz (20 Questions)</h1>
    <p><em>Type your answers using standard math notation. Math.js will evaluate your answer algebraically!</em></p>
    
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
                    const scope = { x: testX };
                    const valUser = nodeUser.evaluate(scope);
                    const valCorrect = nodeCorrect.evaluate(scope);
                    if(Math.abs(valUser - valCorrect) > 0.0001) {
                        isEquivalent = false; break;
                    }
                }
                if(isEquivalent) {
                    card.classList.add('correct');
                    feedback.innerHTML = "✅ Correct! Math.js verified the algebraic equivalence.";
                    feedback.style.color = "#166534";
                    score++; document.getElementById('score').innerText = score;
                } else {
                    card.classList.add('wrong');
                    feedback.innerHTML = "❌ Incorrect. Try again!";
                    feedback.style.color = "#991b1b";
                }
                feedback.style.display = "block";
            } catch (err) {
                feedback.innerHTML = "⚠️ Math Syntax Error. Use standard notation like x^2, *(multiply).";
                feedback.style.color = "#ca8a04";
                feedback.style.display = "block";
            }
        }
    </script>
</body>
</html>
""".replace("REPLACE_ME_WITH_JSON", json.dumps(freeform_questions))

os.makedirs("/Users/ntnmathur/Desktop/precalc/chapters_1_2", exist_ok=True)
with open("/Users/ntnmathur/Desktop/precalc/chapters_1_2/chapter_p_notes.html", "w") as f: f.write(notes_html)
with open("/Users/ntnmathur/Desktop/precalc/chapters_1_2/chapter_p_quiz.html", "w") as f: f.write(quiz_html)
with open("/Users/ntnmathur/Desktop/precalc/chapters_1_2/chapter_p_freeform.html", "w") as f: f.write(freeform_html)

print("Chapter P files generated successfully!")
