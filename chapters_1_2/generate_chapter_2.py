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
        h2 { color: var(--secondary); margin-top: 3rem; }
        .card { background: white; border-radius: 0.5rem; padding: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 2rem; }
        .first-principles { background: #faf5ff; border-left: 4px solid var(--secondary); padding: 1rem; font-style: italic; margin-bottom: 1rem; }
        .example-box { background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 0.5rem; padding: 1.5rem; margin-top: 1rem; }
        .calculator-container { width: 100%; height: 400px; margin-top: 1.5rem; border: 1px solid #cbd5e1; border-radius: 0.5rem; overflow: hidden; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Chapter 2: Graphs and Functions</h1>
        
        <div class="card">
            <h2>2.3 Lines</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> The slope of a line represents its rate of change. It's the ratio of the vertical change to the horizontal change. Parallel lines have equal slopes. Perpendicular lines have negative reciprocal slopes.
            </div>
            <p>Point-slope form: \( y - y_1 = m(x - x_1) \)</p>
        </div>

        <div class="card">
            <h2>2.7 Transformations of Functions</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> Modifying the input \(x\) translates/stretches the graph horizontally. Modifying the output \(f(x)\) translates/stretches the graph vertically.
            </div>
            <h3>Interactive Visualization</h3>
            <p>Observe how \(a, h,\) and \(k\) transform the parent function \(f(x) = |x|\) in \(y = a|x - h| + k\).</p>
            <div id="calculator" class="calculator-container"></div>
        </div>

        <div class="card">
            <h2>2.9 Inverse Functions</h2>
            <div class="first-principles">
                <strong>First Principles:</strong> An inverse function completely undoes the original function. Graphically, it is a reflection across the line \(y = x\).
            </div>
            <div class="example-box">
                <strong>Gotcha Example:</strong> Does \(f(x) = x^2\) have an inverse?<br>
                Many say yes, \(y = \pm \sqrt{x}\). But \(\pm\) makes it NOT a function! A function must be One-to-One (pass the Horizontal Line Test) to have an inverse. Thus, \(x^2\) only has an inverse if we restrict its domain to \(x \ge 0\).
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
    <h1>Chapter 2: Freeform Quiz with Symbolic Grading</h1>
    <p><em>Type your answers algebraically. Math.js will evaluate equivalence!</em></p>
    
    <div class="score-board">
        <h3>Score: <span id="score">0</span> / 5</h3>
    </div>
    
    <div id="quiz-container">
        <!-- Q1 -->
        <div class="card" id="card0">
            <p><strong>1. Functions:</strong> Evaluate f(x) = x^2 - 3x at x = 2.</p>
            <input type="text" id="input0" placeholder="e.g. -2">
            <button onclick="checkFreeform(0, '-2')">Check</button>
            <div class="feedback" id="feedback0"></div>
        </div>

        <!-- Q2 -->
        <div class="card" id="card1">
            <p><strong>2. Composite Functions:</strong> If f(x) = x+1 and g(x) = x^2, find f(g(x)).</p>
            <input type="text" id="input1" placeholder="e.g. x^2 + 1">
            <button onclick="checkFreeform(1, 'x^2 + 1')">Check</button>
            <div class="feedback" id="feedback1"></div>
        </div>
        
        <!-- Q3 -->
        <div class="card" id="card2">
            <p><strong>3. Inverse Functions:</strong> Find the inverse of y = 3x - 1.</p>
            <input type="text" id="input2" placeholder="e.g. (x+1)/3">
            <button onclick="checkFreeform(2, '(x+1)/3')">Check</button>
            <div class="feedback" id="feedback2"></div>
        </div>
        
        <!-- Q4 -->
        <div class="card" id="card3">
            <p><strong>4. Lines:</strong> What is the slope of the line 4x - 2y = 8?</p>
            <input type="text" id="input3" placeholder="e.g. 2">
            <button onclick="checkFreeform(3, '2')">Check</button>
            <div class="feedback" id="feedback3"></div>
        </div>
        
        <!-- Q5 -->
        <div class="card" id="card4">
            <p><strong>5. Critical Thinking:</strong> Simplify the difference quotient (f(x+h) - f(x))/h for f(x) = x^2.</p>
            <input type="text" id="input4" placeholder="e.g. 2x + h">
            <button onclick="checkFreeform(4, '2x + h')">Check</button>
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
"""

os.makedirs("/Users/ntnmathur/Desktop/precalc/chapters_1_2", exist_ok=True)
with open("/Users/ntnmathur/Desktop/precalc/chapters_1_2/chapter_2_notes.html", "w") as f: f.write(notes_html)
with open("/Users/ntnmathur/Desktop/precalc/chapters_1_2/chapter_2_quiz.html", "w") as f: f.write(quiz_html)
with open("/Users/ntnmathur/Desktop/precalc/chapters_1_2/chapter_2_freeform.html", "w") as f: f.write(freeform_html)
print("Chapter 2 files generated successfully!")
