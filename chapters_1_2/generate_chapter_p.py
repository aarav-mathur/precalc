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
    <title>Chapter P: Basic Concepts of Algebra - Revision Notes</title>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <script src="https://www.desmos.com/api/v1.8/calculator.js?apiKey=dcb31709b452b1cf9dc26972add0fda6"></script>
    <style>
        :root { --primary: #0f172a; --secondary: #3b82f6; --bg: #f8fafc; --text: #334155; }
        body { font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; margin: 0; padding: 0; }
        .container { max-width: 900px; margin: 0 auto; padding: 2rem; }
        h1 { color: var(--primary); font-size: 2.5rem; border-bottom: 2px solid #cbd5e1; padding-bottom: 0.5rem; }
        h2 { color: var(--secondary); margin-top: 3rem; }
        .card { background: white; border-radius: 0.5rem; padding: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 2rem; }
        .first-principles { background: #eff6ff; border-left: 4px solid var(--secondary); padding: 1rem; font-style: italic; margin-bottom: 1rem; }
        .example-box { background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 0.5rem; padding: 1.5rem; margin-top: 1rem; }
        .calculator-container { width: 100%; height: 400px; margin-top: 1.5rem; border: 1px solid #cbd5e1; border-radius: 0.5rem; overflow: hidden; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Chapter P: Basic Concepts of Algebra</h1>
        
        <div class="card">
            <h2>P.1 The Real Numbers and Their Properties</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> The real number system \(\mathbb{R}\) is the foundation of continuous mathematics. It includes numbers that can be written as fractions (rational) and those that cannot (irrational, like \(\pi\) and \(\sqrt{2}\)).
            </div>
            <p><strong>Absolute Value:</strong> The distance of a number from zero on the number line. \(|x| = x\) if \(x \ge 0\), and \(|x| = -x\) if \(x < 0\).</p>
            <div class="example-box">
                <strong>Deep Example:</strong> Evaluate \(|x - 5|\) when \(x = 2\).<br>
                1. Plug in: \(|2 - 5|\)<br>
                2. Inside the absolute value: \(|-3|\)<br>
                3. The distance from 0 is 3. So, 3.
            </div>
        </div>

        <div class="card">
            <h2>P.3 & P.4 Polynomials & Factoring</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> Factoring is the inverse of multiplication. By breaking a polynomial down into its irreducible "prime" factors, we reveal its roots (x-intercepts).
            </div>
            <p><strong>Difference of Squares:</strong> \(A^2 - B^2 = (A-B)(A+B)\)</p>
            <p><strong>Perfect Square Trinomial:</strong> \(A^2 \pm 2AB + B^2 = (A \pm B)^2\)</p>
            
            <h3>Interactive Visualization</h3>
            <p>Interact with the Desmos graph below to see how the factors of a polynomial dictate its roots. Change the sliders for \(a\), \(b\), and \(c\)!</p>
            <div id="calculator" class="calculator-container"></div>
        </div>

        <div class="card">
            <h2>P.6 Rational Exponents and Radicals</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> A rational exponent \(\frac{m}{n}\) is just a compact way of writing "take the \(n\)-th root, then raise to the \(m\)-th power." \(x^{m/n} = \sqrt[n]{x^m}\).
            </div>
            <div class="example-box">
                <strong>Gotcha Example:</strong> Simplify \( (-8)^{2/3} \).<br>
                Many students incorrectly try to square first, leading to massive numbers. Instead, take the root first!<br>
                1. Cube root of -8 is -2.<br>
                2. Square -2: \((-2)^2 = 4\).<br>
                Result: 4.
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

# Generate exactly 50 MCQ questions across 5 categories
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

    # Category 2: Building Skills (Factoring difference of squares)
    a = random.randint(2, 9)
    q2 = f"Factor completely: \\({a**2}x^2 - 81\\)"
    correct2 = f"\\(({a}x - 9)({a}x + 9)\\)"
    w1 = f"\\(({a}x - 9)^2\\)" # Student thinks it's a perfect square
    w2 = f"\\(({a**2}x - 9)({a**2}x + 9)\\)" # Forgot to square root a^2
    w3 = f"\\(({a}x - 81)({a}x + 81)\\)" # Forgot to square root 81
    opts2, ans2 = generate_distractors(correct2, w1, w2, w3)
    questions.append({"q": q2, "category": categories[1], "options": opts2, "answer": ans2, "explanation": "Difference of squares: \\(A^2 - B^2 = (A-B)(A+B)\\). Here A = \\({a}x\\) and B = 9."})

    # Category 3: Applying the Concepts (Exponent rules)
    b = random.randint(2, 5)
    c = random.randint(2, 4)
    q3 = "Simplify the expression using exponent rules: \\( (\\frac{x^" + str(b) + "}{y^{-" + str(c) + "}})^{-2} \\)"
    correct3 = f"\\( \\frac{{1}}{{x^{b*2}y^{c*2}}} \\)"
    w1_3 = f"\\( \\frac{{y^{c*2}}}{{x^{b*2}}} \\)" # Sign error on y
    w2_3 = f"\\( x^{b*-2} y^{c*-2} \\)" # Formatted without fraction, but wait let's make it look like a wrong fraction
    w2_3 = f"\\( \\frac{{x^{b*2}}}{{y^{c*2}}} \\)" # Flipped numerator/denominator completely wrong
    w3_3 = f"\\( \\frac{{1}}{{x^{b+2}y^{c+2}}} \\)" # Student added instead of multiplied exponents
    opts3, ans3 = generate_distractors(correct3, w1_3, w2_3, w3_3)
    questions.append({"q": q3, "category": categories[2], "options": opts3, "answer": ans3, "explanation": "First apply the negative exponent to flip the fraction, or multiply exponents: \\(x^{-2b} / y^{2c}\\). To make powers positive, move x to denominator: \\(1 / (x^{2b} y^{2c})\\)."})

    # Category 4: Beyond the Basics (Rationalizing denominator with conjugates)
    d = random.randint(2, 5)
    q4 = f"Rationalize the denominator: \\( \\frac{{{d}}}{{ \\sqrt{{x}} - {d} }} \\)"
    correct4 = f"\\( \\frac{{{d}\\sqrt{{x}} + {d**2}}}{{x - {d**2}}} \\)"
    w1_4 = f"\\( \\frac{{{d}\\sqrt{{x}} - {d**2}}}{{x - {d**2}}} \\)" # Wrong sign in numerator
    w2_4 = f"\\( \\frac{{{d}\\sqrt{{x}} + {d**2}}}{{x + {d**2}}} \\)" # Wrong sign in denominator
    w3_4 = f"\\( \\frac{{{d}\\sqrt{{x}} + {d}}}{{x - {d**2}}} \\)" # Forgot to distribute the d to the d
    opts4, ans4 = generate_distractors(correct4, w1_4, w2_4, w3_4)
    questions.append({"q": q4, "category": categories[3], "options": opts4, "answer": ans4, "explanation": "Multiply numerator and denominator by the conjugate \\(\\sqrt{{x}} + {d}\\). Denominator becomes \\(x - {d**2}\\). Numerator becomes \\({d}(\\sqrt{{x}} + {d}) = {d}\\sqrt{{x}} + {d**2}\\)."})

    # Category 5: Critical Thinking
    q5 = f"Why is the domain of \\( \\frac{{1}}{{\\sqrt{{x - {i+1}}}}} \\) restricted to \\( x > {i+1} \\) instead of \\( x \\ge {i+1} \\)?"
    correct5 = f"Because \\(x = {i+1}\\) causes division by zero, even though the square root of 0 is valid."
    w1_5 = f"Because the square root of {i+1} is irrational."
    w2_5 = f"Because you cannot take the square root of a negative number." # True but doesn't explain why not EQUAL to i+1
    w3_5 = f"Because fractions cannot have a positive denominator."
    opts5, ans5 = generate_distractors(correct5, w1_5, w2_5, w3_5)
    questions.append({"q": q5, "category": categories[4], "options": opts5, "answer": ans5, "explanation": "The radicand must be \\(\\ge 0\\) (so \\(x - {i+1} \\ge 0\\)), but since it is in the denominator, it cannot be exactly 0. Thus \\(x - {i+1} > 0\\)."})


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
# Integrating math.js to evaluate equivalence algebraically!

freeform_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chapter P: Freeform Mastery</title>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    <!-- MATH.JS SYMBOLIC GRADING ENGINE -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjs/11.8.0/math.js"></script>
    <style>
        body { font-family: 'Inter', sans-serif; background: #f8fafc; color: #1e293b; padding: 2rem; max-width: 900px; margin: 0 auto; }
        .score-board { background: #0f172a; color: white; padding: 1rem 1.5rem; border-radius: 0.5rem; display: flex; justify-content: space-between; position: sticky; top: 1rem; z-index: 100; margin-bottom: 2rem; }
        .card { background: white; border-radius: 0.5rem; padding: 1.5rem; margin-top: 1rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); border-left: 6px solid transparent; }
        .card.correct { border-left-color: #22c55e; }
        .card.wrong { border-left-color: #ef4444; }
        input[type="text"] { width: 60%; padding: 0.75rem; font-size: 1rem; border: 2px solid #cbd5e1; border-radius: 0.5rem; }
        button { background: #8b5cf6; color: white; border: none; padding: 0.75rem 1.5rem; font-size: 1rem; font-weight: bold; border-radius: 0.5rem; cursor: pointer; }
        .feedback { margin-top: 1rem; font-weight: bold; display: none; }
    </style>
</head>
<body>
    <h1>Chapter P: Freeform Quiz with Symbolic Grading</h1>
    <p><em>Type your answers using standard math notation (e.g., x^2 + 2x). Math.js will evaluate your answer algebraically against the correct answer! Even if you type x(x+2), it knows it's equal to x^2+2x.</em></p>
    
    <div class="score-board">
        <h3>Score: <span id="score">0</span> / 5</h3>
    </div>
    
    <div id="quiz-container">
        <!-- Q1 -->
        <div class="card" id="card0">
            <p><strong>1. Expanding:</strong> Expand and simplify the expression: (x - 4)(x + 5)</p>
            <input type="text" id="input0" placeholder="e.g. x^2 + x - 20">
            <button onclick="checkFreeform(0, 'x^2 + x - 20')">Check</button>
            <div class="feedback" id="feedback0"></div>
        </div>

        <!-- Q2 -->
        <div class="card" id="card1">
            <p><strong>2. Factoring:</strong> Factor out the greatest common factor: 6x^3 - 15x^2</p>
            <input type="text" id="input1" placeholder="e.g. 3x^2(2x - 5)">
            <button onclick="checkFreeform(1, '3*x^2*(2x - 5)')">Check</button>
            <div class="feedback" id="feedback1"></div>
        </div>
        
        <!-- Q3 -->
        <div class="card" id="card2">
            <p><strong>3. Special Products:</strong> Expand (2x - 3)^2</p>
            <input type="text" id="input2" placeholder="e.g. 4x^2 - 12x + 9">
            <button onclick="checkFreeform(2, '4x^2 - 12x + 9')">Check</button>
            <div class="feedback" id="feedback2"></div>
        </div>
        
        <!-- Q4 -->
        <div class="card" id="card3">
            <p><strong>4. Adding Rational Expressions:</strong> Add and simplify: 1/x + 2/(x+1)</p>
            <input type="text" id="input3" placeholder="e.g. (3x+1)/(x(x+1))">
            <button onclick="checkFreeform(3, '(3x+1)/(x*(x+1))')">Check</button>
            <div class="feedback" id="feedback3"></div>
        </div>
        
        <!-- Q5 -->
        <div class="card" id="card4">
            <p><strong>5. Critical Thinking:</strong> Simplify (x^3 - 8) / (x - 2)</p>
            <input type="text" id="input4" placeholder="e.g. x^2 + 2x + 4">
            <button onclick="checkFreeform(4, 'x^2 + 2x + 4')">Check</button>
            <div class="feedback" id="feedback4"></div>
        </div>
    </div>

    <script>
        let score = 0;
        
        function checkFreeform(index, correctAnswerStr) {
            const userStr = document.getElementById('input' + index).value;
            const card = document.getElementById('card' + index);
            const feedback = document.getElementById('feedback' + index);
            
            if(!userStr) return;

            try {
                // We use math.js to evaluate if UserExpr - CorrectExpr == 0 for random test points
                const nodeUser = math.parse(userStr).compile();
                const nodeCorrect = math.parse(correctAnswerStr).compile();
                
                let isEquivalent = true;
                
                // Test 5 random points to empirically prove algebraic equivalence
                for(let i=0; i<5; i++) {
                    const testX = Math.random() * 10 + 1; // avoid 0 to prevent div by zero
                    const scope = { x: testX };
                    
                    const valUser = nodeUser.evaluate(scope);
                    const valCorrect = nodeCorrect.evaluate(scope);
                    
                    // Allow small floating point differences
                    if(Math.abs(valUser - valCorrect) > 0.0001) {
                        isEquivalent = false;
                        break;
                    }
                }
                
                if(isEquivalent) {
                    card.classList.add('correct');
                    feedback.innerHTML = "✅ Correct! Math.js verified the algebraic equivalence.";
                    feedback.style.color = "#166534";
                    score++;
                    document.getElementById('score').innerText = score;
                } else {
                    card.classList.add('wrong');
                    feedback.innerHTML = "❌ Incorrect. Try again!";
                    feedback.style.color = "#991b1b";
                }
                feedback.style.display = "block";
            } catch (err) {
                feedback.innerHTML = "⚠️ Math Syntax Error. Make sure you use standard notation like x^2, *(multiply).";
                feedback.style.color = "#ca8a04";
                feedback.style.display = "block";
            }
        }
    </script>
</body>
</html>
"""

os.makedirs("/Users/ntnmathur/Desktop/precalc/chapters_1_2", exist_ok=True)

with open("/Users/ntnmathur/Desktop/precalc/chapters_1_2/chapter_p_notes.html", "w") as f:
    f.write(notes_html)
with open("/Users/ntnmathur/Desktop/precalc/chapters_1_2/chapter_p_quiz.html", "w") as f:
    f.write(quiz_html)
with open("/Users/ntnmathur/Desktop/precalc/chapters_1_2/chapter_p_freeform.html", "w") as f:
    f.write(freeform_html)

print("Chapter P files generated successfully!")
