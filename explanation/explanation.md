# Experiment 10 — Code Explanation
# AI Ethics, Safety and Biases in Mechanical Systems

---

## What is this experiment about?

Unlike the previous 9 experiments which had Python code,
Experiment 10 is a **case study and analysis**.

It asks a deeper question:

> "We CAN build AI systems for machines — but SHOULD we?
> And if we do, what responsibilities do engineers have?"

This experiment teaches you to think like a **responsible engineer**,
not just a programmer.

---

## Why Ethics Matters in Engineering

Every engineering decision affects real people.
A poorly designed bridge collapses. A faulty car kills.
A biased AI system makes wrong decisions that harm people.

**Engineering ethics is not optional — it is fundamental.**

The Boeing 737 MAX crash killed 346 people.
Not because of a programming mistake.
But because of **poor ethical decision-making** at every level.

---

## Case Study Deep Dive: Boeing 737 MAX

---

### Background

In 2011, Boeing needed to compete with Airbus A320neo.
They updated the 737 with larger, more fuel-efficient engines.
But the larger engines changed how the plane handled —
it tended to pitch nose-up at high power, risking a stall.

Boeing's solution: **MCAS (Maneuvering Characteristics Augmentation System)**
A software system that automatically pushed the nose DOWN
when it detected a high angle-of-attack.

---

### What Went Wrong — Technical Analysis

**Problem 1: Single Point of Failure (Sensor Bias)**
```
MCAS relied on ONE Angle-of-Attack (AoA) sensor.
If that sensor gave wrong data → MCAS activated incorrectly.
This is called a "single point of failure" — catastrophic.

Engineering lesson:
Safety-critical systems MUST have redundancy.
Two sensors → compare values → if different → alert pilot.
Three sensors → majority vote → override the faulty one.
```

**Problem 2: No Input Validation (Algorithm Bias)**
```
MCAS did not validate sensor data.
It trusted whatever the sensor said — even impossible values.
When sensor failed, MCAS kept pushing nose down repeatedly.

Engineering lesson:
Always validate inputs. Check if sensor value is
physically possible. Add range checks and sanity checks.
```

**Problem 3: Human-Machine Interface Failure**
```
Pilots were NOT told MCAS existed.
They were NOT trained on how to override it.
In the cockpit, they had no idea what was happening.

Engineering lesson:
Every automated system needs a clear human override.
Operators MUST be trained. System behavior must be transparent.
```

**Problem 4: Commercial Pressure Over Safety**
```
Boeing rushed the 737 MAX to market to compete with Airbus.
Safety concerns were downplayed to avoid delays and costs.
Regulators trusted Boeing's self-certification.

Engineering lesson:
No commercial pressure justifies compromising safety.
Independent safety verification is essential.
```

---

## Types of AI Bias — Explained

---

### 1. Sensor Bias

**Definition:**
When sensors are trained or calibrated in limited conditions
but deployed in different real-world conditions.

**Example in mechanical engineering:**
A vibration sensor trained in a clean factory environment
fails to detect faults when there is dust, humidity, or temperature extremes.

**Example in autonomous vehicles:**
Camera-based lane detection trained on sunny daylight roads
fails in rain, fog, snow, or night conditions.

**How to prevent:**
- Test sensors in ALL expected operating conditions
- Use diverse training environments
- Include edge cases deliberately

---

### 2. Algorithmic Bias

**Definition:**
When the AI model makes systematically wrong predictions
because of biased or unrepresentative training data.

**Example:**
A predictive maintenance model trained only on new machines
will incorrectly classify old machines as "faulty"
because it has never seen normal wear patterns of aged equipment.

**How to prevent:**
- Use diverse, representative training data
- Test model on different machine types, ages, environments
- Regularly retrain with new data

---

### 3. Human-Machine Interface (HMI) Bias

**Definition:**
The interface between human operator and AI system
creates confusion, over-reliance, or misunderstanding.

**Types:**
- **Automation bias:** Operators trust AI too much, stop thinking critically
- **Alert fatigue:** Too many warnings → operators ignore them
- **Skill degradation:** Operators lose manual skills due to over-automation

**How to prevent:**
- Design interfaces that explain AI decisions (explainable AI)
- Train operators to understand AI limitations
- Require operators to maintain manual skills

---

## Safety Checklist Analysis

---

### Design Level Safety

```
✅ Redundant sensors
   Why: Single sensor failure cannot cause catastrophe
   Example: Two AoA sensors on aircraft, both must agree

✅ Multi-source data validation
   Why: One bad sensor can be overridden by others
   Example: Cross-check temperature with vibration data

✅ Fail-safe shutdown
   Why: When uncertain, stop safely rather than continue wrongly
   Example: If all sensors fail, machine stops, alert is raised
```

### Algorithm Level Safety

```
✅ Diverse training datasets
   Why: Model must work in ALL conditions, not just ideal ones
   Example: Train fault detection on new AND old machines

✅ Avoid overfitting
   Why: Model that memorizes training data fails on new data
   Example: Test on machines the model has never seen

✅ Real-time anomaly detection
   Why: Catch unusual behavior before it becomes catastrophic
   Example: Alert when sensor reading is outside historical range
```

### Operational Safety

```
✅ Human override ALWAYS exists
   Why: AI makes mistakes. Human must be able to intervene.
   Example: Boeing MCAS could have been disabled by pilots
            if they had known about it and been trained

✅ Operator training
   Why: Untrained operators cannot respond to unexpected situations
   Example: Ethiopian Airlines crash — crew not trained on MCAS override

✅ System logs for auditing
   Why: After failures, you need to know exactly what happened
   Example: Black box flight recorder — essential for investigation
```

---

## Accountability Framework — Who is Responsible?

This is one of the most important questions in AI engineering.

```
Software Engineer
→ Responsible for: Correct algorithm, proper validation,
  input range checking, error handling
→ NOT an excuse: "I just wrote the code as specified"

Mechanical Engineer
→ Responsible for: Physical safety, integration of AI with
  hardware, understanding failure modes
→ NOT an excuse: "The software team handled that"

Company/Management
→ Responsible for: Deployment decisions, training programs,
  resource allocation for safety testing, regulatory compliance
→ NOT an excuse: "We were under commercial pressure"

Regulator
→ Responsible for: Independent certification, safety standards,
  not relying solely on manufacturer's self-assessment
→ NOT an excuse: "We trusted the company's reports"

CONCLUSION:
Responsibility is SHARED, but in a safety-critical failure,
the ORGANIZATION deploying the system bears ultimate accountability.
```

---

## Workforce Adaptation — The Human Side of AI

When factories introduce AI and automation, workers are affected.
Engineers have a responsibility to think about this.

---

### What happens without adaptation:
- Workers lose jobs → social and economic harm
- Remaining workers don't understand new systems → safety risk
- Knowledge gap between old workers and new AI systems

### What responsible adaptation looks like:

**Upskilling programs:**
Train existing workers in:
- Reading and interpreting AI dashboards
- Understanding when AI is right vs wrong
- Data collection and quality checking

**New hybrid roles:**
Instead of replacing workers, create new roles:
- Machine Operator + Data Analyst
- Maintenance Technician + AI System Supervisor
- Quality Inspector + Anomaly Detection Reviewer

**Gradual transition:**
Don't replace overnight. Introduce AI alongside humans.
Let workers learn the system before full automation.

---

## Practice Questions — Answers

---

**Q1: An autonomous car fails to detect pedestrians at night.**

**Failure type:** Sensor Bias + Algorithm Bias

**Analysis:**
- Camera sensors trained predominantly on daytime images
- Model never learned to detect in low-light conditions
- This is sensor bias (limited training conditions)
- AND algorithmic bias (unrepresentative training data)

**Solutions:**
- Train with diverse lighting conditions including night
- Use multiple sensor types: camera + LiDAR + radar
- LiDAR and radar work in darkness, complementing cameras
- Test extensively in all environmental conditions

**Safety checklist:**
- [ ] Multi-sensor fusion (camera + LiDAR + radar)
- [ ] Night and low-light testing datasets
- [ ] Automatic speed reduction in poor visibility
- [ ] Human override always available

---

**Q2: AI replaces manual quality inspection in a factory.**

**Ethical concerns:**
- Job displacement for inspection workers
- AI bias if training data has unrepresentative defects
- Over-reliance if AI errors go undetected
- Accountability gap if AI approves defective products

**Workforce impact:**
- Direct: Inspection jobs reduced
- Indirect: Workers may feel devalued
- Long term: Loss of human quality judgment expertise

**Adaptation strategies:**
- Retrain inspectors as AI supervisors
- Use AI to assist, not completely replace
- Maintain human review for critical decisions
- Document institutional knowledge before automation

**Bias in inspection data:**
- If training data only contains common defects, rare defects go undetected
- If training data is from one factory, model may not work in another
- Regular retraining with new defect examples is essential

---

## Ethical Manifesto for AI-Mechanical Engineers

As an engineer building AI-driven mechanical systems:

**1. Design for safety over efficiency**
Never compromise safety for speed or cost savings.
A delayed product is recoverable. A fatal accident is not.

**2. Ensure transparency**
Every AI decision should be explainable.
If you cannot explain why the AI made a decision, it's not safe to deploy.

**3. Minimize bias**
Deliberately test your system in conditions it was NOT trained on.
Assume bias exists until proven otherwise.

**4. Protect human employment**
Use AI to augment human capability, not just replace humans.
Invest in retraining programs.

**5. Take full responsibility**
"The AI decided" is not an acceptable answer.
You built the system. You are responsible for its behavior.

---

## Summary Table

| Issue | Type | Impact | Solution |
|---|---|---|---|
| Single AoA sensor (Boeing) | Sensor bias | 346 deaths | Redundant sensors |
| Night pedestrian detection | Algorithm bias | Accidents | Diverse training data |
| Operators not trained | HMI issue | Human error | Mandatory training |
| Job displacement | Ethical concern | Social harm | Upskilling programs |
| Unexplainable AI decisions | Transparency issue | Accountability gap | Explainable AI |
