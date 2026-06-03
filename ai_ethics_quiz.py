# ============================================================
# EXPERIMENT 10: AI Ethics, Safety and Biases — Interactive
# Subject: AI in Mechanical Engineering (ONT406)
# Sharda University
# ============================================================

class QuizError(ValueError):
    """Raised when quiz data is invalid or corrupted."""
    pass

class InputError(ValueError):
    """Raised when user provides completely invalid input."""
    pass

# -------------------------------------------------------
# Quiz Database
# -------------------------------------------------------
QUIZ_QUESTIONS = [
    {
        "question": "What type of failure did the Boeing 737 MAX MCAS system primarily suffer from?",
        "options": [
            "A. Software bug in the flight control computer",
            "B. Single point of failure due to one faulty AoA sensor",
            "C. Pilot error during takeoff",
            "D. Engine mechanical failure"
        ],
        "answer": "B",
        "explanation": (
            "MCAS relied on a SINGLE Angle-of-Attack sensor with no redundancy. "
            "When that sensor failed, MCAS repeatedly pushed the nose down "
            "with no way for the system to detect the sensor was wrong."
        )
    },
    {
        "question": "What is 'Sensor Bias' in AI-driven mechanical systems?",
        "options": [
            "A. Sensors that are physically tilted or misaligned",
            "B. Sensors trained in limited conditions that fail in real-world variability",
            "C. Sensors that measure incorrect physical quantities",
            "D. Sensors with outdated firmware"
        ],
        "answer": "B",
        "explanation": (
            "Sensor bias occurs when sensors are calibrated only in ideal conditions "
            "(clear weather, new machines) and fail when real conditions vary "
            "(rain, fog, worn equipment)."
        )
    },
    {
        "question": "What does a p-value < 0.05 mean in hypothesis testing?",
        "options": [
            "A. The result is definitely wrong",
            "B. Accept the null hypothesis — process is stable",
            "C. Reject the null hypothesis — process is not under control",
            "D. The sample size is too small"
        ],
        "answer": "C",
        "explanation": (
            "p < 0.05 means less than 5% probability the observed difference is "
            "random. We reject H0 and conclude the process mean differs "
            "significantly from the design value."
        )
    },
    {
        "question": "Which ethical principle requires AI decisions to be understandable by operators?",
        "options": [
            "A. Sustainability",
            "B. Accountability",
            "C. Transparency",
            "D. Efficiency"
        ],
        "answer": "C",
        "explanation": (
            "Transparency (Explainable AI) requires that every AI decision must "
            "be understandable by operators. If you cannot explain why the AI "
            "made a decision, it is unsafe to deploy."
        )
    },
    {
        "question": "What is the primary purpose of the Von Mises stress criterion?",
        "options": [
            "A. Calculate beam deflection under load",
            "B. Predict when a ductile material will yield under combined stresses",
            "C. Determine the maximum allowable temperature",
            "D. Measure the elongation of a rod"
        ],
        "answer": "B",
        "explanation": (
            "Von Mises stress combines all stress components into a single "
            "equivalent stress. When it exceeds yield strength, the material "
            "begins permanent (plastic) deformation."
        )
    },
    {
        "question": "In K-Means clustering for fault detection, what does StandardScaler do?",
        "options": [
            "A. Removes outliers from the dataset",
            "B. Normalises features so each has equal influence on clustering",
            "C. Converts sensor data from analog to digital",
            "D. Sorts data points by vibration level"
        ],
        "answer": "B",
        "explanation": (
            "StandardScaler transforms each feature to mean=0 and std=1. "
            "Without scaling, features with larger ranges (Temperature 0-120) "
            "dominate over smaller ones (Vibration 0-5), biasing clustering."
        )
    },
    {
        "question": "In a Genetic Algorithm, what is the 'fitness function'?",
        "options": [
            "A. A function that measures how physically fit the engineer is",
            "B. A function that scores how good each design solution is",
            "C. A function that removes poor-quality data",
            "D. A function that calculates the strength of materials"
        ],
        "answer": "B",
        "explanation": (
            "The fitness function scores each candidate solution. "
            "Higher fitness = better design. In beam optimisation, "
            "fitness = 1/(weight + penalty), rewarding lighter safe beams."
        )
    },
    {
        "question": "What does R² = 0.95 mean for a regression model?",
        "options": [
            "A. The model made 95 correct predictions out of 100",
            "B. The model explains 95% of the variation in the target variable",
            "C. The model has a 5% error rate",
            "D. The training accuracy is 95%"
        ],
        "answer": "B",
        "explanation": (
            "R² measures how much variation in the output (tool wear) is "
            "explained by the model's inputs. R²=0.95 means the model "
            "captures 95% of the pattern in the data."
        )
    },
    {
        "question": "Who bears ultimate accountability when an AI mechanical system causes harm?",
        "options": [
            "A. Only the software engineer who wrote the code",
            "B. Only the mechanical engineer who integrated it",
            "C. The AI system itself",
            "D. The organisation that deployed the system"
        ],
        "answer": "D",
        "explanation": (
            "While responsibility is shared among all engineers and regulators, "
            "the ORGANISATION that deployed the system bears ultimate accountability. "
            "'The AI decided' is never an acceptable answer."
        )
    },
    {
        "question": "What is 'Automation bias' in Human-Machine Interface (HMI) issues?",
        "options": [
            "A. Machines automatically detecting human errors",
            "B. Operators trusting AI too much and losing critical thinking",
            "C. AI systems that prefer certain operators over others",
            "D. Automated systems biased toward efficiency over safety"
        ],
        "answer": "B",
        "explanation": (
            "Automation bias occurs when operators over-trust AI decisions and "
            "stop thinking critically — following AI recommendations even when "
            "they contradict direct observations. A key cause of accidents in "
            "aviation, healthcare, and manufacturing."
        )
    }
]

CASE_STUDIES = {
    "1": {
        "title": "Boeing 737 MAX — MCAS Failure",
        "description": (
            "The MCAS system relied on a single AoA sensor. "
            "When the sensor failed, MCAS repeatedly commanded nose-down. "
            "Pilots were untrained to override it. 346 people died."
        ),
        "failure_type": "Sensor Bias + Algorithm Error + HMI Failure",
        "lessons": [
            "Use redundant sensors in all safety-critical systems",
            "Validate sensor inputs — check for physically impossible values",
            "Operator training on all automated systems is mandatory",
            "Human override must always be possible and clearly documented",
            "No commercial pressure justifies compromising safety"
        ]
    },
    "2": {
        "title": "Autonomous Car — Night Pedestrian Detection Failure",
        "description": (
            "A self-driving car trained on daytime data fails to detect "
            "pedestrians at night or in rain. The camera system was never "
            "tested in low-light or adverse weather conditions."
        ),
        "failure_type": "Sensor Bias + Algorithmic Bias",
        "lessons": [
            "Train AI on diverse, representative datasets",
            "Include ALL expected operating conditions in testing",
            "Use multiple sensor types: camera + LiDAR + radar",
            "LiDAR and radar operate reliably in darkness unlike cameras",
            "Never deploy without comprehensive edge-case testing"
        ]
    },
    "3": {
        "title": "AI Quality Inspection Replacing Manual Workers",
        "description": (
            "A factory replaces human quality inspectors with an AI vision "
            "system trained only on common defects. Rare defects go undetected. "
            "Workers are displaced without any retraining programme."
        ),
        "failure_type": "Algorithmic Bias + Ethical Failure",
        "lessons": [
            "Train inspection AI on ALL defect types including rare ones",
            "Maintain human oversight for unusual or critical decisions",
            "Invest in retraining programmes for displaced workers",
            "Create hybrid human-AI roles rather than pure replacement",
            "Regularly retrain AI model with new defect examples"
        ]
    }
}

SAFETY_CHECKLIST = {
    "Design Level": [
        "Redundant sensors installed",
        "Multi-source data validation implemented",
        "Fail-safe shutdown mechanism exists",
        "Physical safety guards in place"
    ],
    "Algorithm Level": [
        "Trained on diverse and representative datasets",
        "Tested for overfitting using held-out test set",
        "Real-time anomaly detection implemented",
        "Model performance monitored continuously in production"
    ],
    "Operational Level": [
        "Human override mechanism clearly documented",
        "Operator training programme completed",
        "System logs maintained for auditing",
        "Emergency stop procedure posted at workstation"
    ],
    "Ethical Level": [
        "AI decisions are explainable to operators",
        "Accountability clearly defined across all stakeholders",
        "Environmental impact of AI deployment assessed",
        "Workforce adaptation plan created and communicated"
    ]
}

# -------------------------------------------------------
# Input Helpers
# -------------------------------------------------------
def get_valid_menu_choice(valid_options):
    """
    Keep prompting until user enters one of the valid options.
    Raises InputError only if options list is empty (programming error).
    """
    if not valid_options:
        raise InputError("No valid options provided — programming error.")
    while True:
        raw = input("  Your choice: ").strip().upper()
        if raw in valid_options:
            return raw
        print(f"  Error: Invalid input. Please enter one of: {', '.join(valid_options)}")

def get_yes_no(prompt):
    """Get a yes/no answer from user."""
    while True:
        raw = input(prompt).strip().lower()
        if raw in ['y', 'yes']:
            return True
        if raw in ['n', 'no']:
            return False
        print("  Error: Please enter 'y' or 'n'.")

def press_enter():
    input("\n  Press Enter to continue...")

def separator(char="=", width=58):
    print(char * width)

# -------------------------------------------------------
# Quiz
# -------------------------------------------------------
def validate_questions(questions):
    """Check quiz data integrity before running."""
    for i, q in enumerate(questions):
        required_keys = {"question", "options", "answer", "explanation"}
        missing = required_keys - set(q.keys())
        if missing:
            raise QuizError(
                f"Question {i+1} is missing fields: {missing}"
            )
        if q["answer"] not in ["A", "B", "C", "D"]:
            raise QuizError(
                f"Question {i+1} has invalid answer: {q['answer']}"
            )
        if len(q["options"]) != 4:
            raise QuizError(
                f"Question {i+1} must have exactly 4 options."
            )

def run_quiz():
    """Run the 10-question ethics and concepts quiz."""
    try:
        validate_questions(QUIZ_QUESTIONS)
    except QuizError as e:
        print(f"  Quiz Error: {e}")
        return

    separator()
    print("  AI ETHICS AND CONCEPTS QUIZ")
    print(f"  {len(QUIZ_QUESTIONS)} Questions — Test Your Understanding")
    separator()

    score        = 0
    wrong_list   = []

    for i, q in enumerate(QUIZ_QUESTIONS):
        print(f"\n  Question {i+1} of {len(QUIZ_QUESTIONS)}:")
        print(f"  {q['question']}\n")
        for opt in q["options"]:
            print(f"    {opt}")

        try:
            answer = get_valid_menu_choice(["A", "B", "C", "D"])
        except InputError as e:
            print(f"  System Error: {e}")
            continue

        if answer == q["answer"]:
            print("  ✓ Correct!")
            score += 1
        else:
            print(f"  ✗ Wrong. Correct answer: {q['answer']}")
            wrong_list.append((i + 1, q["answer"], answer))

        print(f"\n  Explanation: {q['explanation']}")
        press_enter()

    # Results
    separator()
    print("  QUIZ RESULTS")
    separator()
    total      = len(QUIZ_QUESTIONS)
    percentage = (score / total) * 100 if total > 0 else 0.0
    print(f"  Score      : {score} / {total}")
    print(f"  Percentage : {percentage:.0f}%")

    if percentage >= 90:
        grade = "Excellent ✓✓ — Outstanding understanding!"
    elif percentage >= 75:
        grade = "Good ✓ — Strong grasp of concepts."
    elif percentage >= 60:
        grade = "Satisfactory — Review the weak areas."
    else:
        grade = "Needs Improvement — Revisit the lab manual."
    print(f"  Grade      : {grade}")

    if wrong_list:
        print(f"\n  Questions to review:")
        for num, correct, given in wrong_list:
            print(f"    Q{num}: You answered {given}, correct was {correct}")
    separator()

# -------------------------------------------------------
# Case Studies Browser
# -------------------------------------------------------
def browse_case_studies():
    """Browse available case studies one at a time."""
    while True:
        print("\n  --- Available Case Studies ---")
        for key, cs in CASE_STUDIES.items():
            print(f"  {key}. {cs['title']}")
        print("  0. Back to main menu")

        valid = list(CASE_STUDIES.keys()) + ["0"]
        try:
            choice = get_valid_menu_choice(valid)
        except InputError as e:
            print(f"  System Error: {e}")
            break

        if choice == "0":
            break

        cs = CASE_STUDIES.get(choice)
        if cs is None:
            print("  Error: Case study not found.")
            continue

        separator()
        print(f"  CASE STUDY: {cs['title']}")
        separator()
        print(f"\n  Description:\n  {cs['description']}")
        print(f"\n  Failure Type: {cs['failure_type']}")
        print(f"\n  Engineering Lessons:")
        for idx, lesson in enumerate(cs["lessons"], 1):
            print(f"    {idx}. {lesson}")
        separator()
        press_enter()

# -------------------------------------------------------
# Safety Checklist
# -------------------------------------------------------
def run_safety_checklist():
    """Interactive safety checklist with scoring."""
    separator()
    print("  AI DEPLOYMENT SAFETY CHECKLIST")
    separator()

    total     = 0
    completed = 0

    for category, items in SAFETY_CHECKLIST.items():
        print(f"\n  [{category}]")
        for item in items:
            total += 1
            try:
                done = get_yes_no(f"    ✓ {item}? (y/n): ")
            except EOFError:
                print("  Input stream ended — marking as incomplete.")
                done = False
            if done:
                completed += 1

    percentage = (completed / total * 100) if total > 0 else 0.0
    separator()
    print(f"  Checklist: {completed}/{total} items complete ({percentage:.0f}%)")

    if percentage == 100:
        status = "READY FOR DEPLOYMENT ✓"
    elif percentage >= 75:
        status = "NEARLY READY — address remaining items"
    elif percentage >= 50:
        status = "PARTIAL — significant gaps remain"
    else:
        status = "NOT READY — critical safety gaps exist ✗"

    print(f"  Status    : {status}")
    separator()

# -------------------------------------------------------
# Accountability Framework
# -------------------------------------------------------
def show_accountability():
    """Display the stakeholder accountability table."""
    separator()
    print("  ACCOUNTABILITY FRAMEWORK")
    separator()
    rows = [
        ("Software Engineer",    "Algorithm correctness, input validation, testing"),
        ("Mechanical Engineer",  "Physical safety, hardware integration, failure modes"),
        ("Company/Management",   "Deployment decisions, training, compliance"),
        ("Regulator",            "Independent certification, safety standards, auditing"),
    ]
    print(f"\n  {'Stakeholder':<26}{'Responsibility'}")
    print(f"  {'-'*55}")
    for stakeholder, responsibility in rows:
        print(f"  {stakeholder:<26}{responsibility}")

    print(f"\n  Key Principle:")
    print(f"  Responsibility is SHARED, but the ORGANISATION that")
    print(f"  deploys the system bears ultimate accountability.")
    print(f"  'The AI decided' is NEVER an acceptable answer.")
    separator()

# -------------------------------------------------------
# Main Program
# -------------------------------------------------------
def main():
    separator()
    print("  EXPERIMENT 10: AI Ethics, Safety and Biases")
    print("  AI in Mechanical Engineering — ONT406")
    print("  Sharda University")
    separator()

    while True:
        print("\n--- MENU ---")
        print("1. Take Ethics and Concepts Quiz (10 Questions)")
        print("2. Browse Case Studies")
        print("3. Run Safety Deployment Checklist")
        print("4. View Accountability Framework")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            run_quiz()
        elif choice == "2":
            browse_case_studies()
        elif choice == "3":
            run_safety_checklist()
        elif choice == "4":
            show_accountability()
        elif choice == "5":
            print("\nExiting. Goodbye!")
            break
        else:
            print("  Error: Invalid choice. Please enter 1 through 5.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Program interrupted by user. Goodbye!")
