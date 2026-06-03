# Experiment 10: AI Ethics, Safety, and Biases in Mechanical Systems

**Subject:** AI in Mechanical Engineering (ONT406)  
**Sharda University, Greater Noida**

---

## Aim
To critically evaluate safety, ethical implications, and data biases in AI-driven mechanical systems such as autonomous vehicles and automated manufacturing systems.

---

## Case Study: Boeing 737 MAX — MCAS Failure

### Background
The MCAS (Maneuvering Characteristics Augmentation System) was designed to improve aircraft stability. It relied on a **single Angle-of-Attack (AoA) sensor** to automatically push the nose down if it detected a stall.

### What Went Wrong

| Factor | Observation |
|---|---|
| Sensor Bias | Relied on a single faulty AoA sensor — no redundancy |
| Algorithm Issue | System gave repeated nose-down commands without validation |
| HMI Issue | Pilots were not adequately trained or informed about MCAS |

### Root Cause
- No redundancy in sensor design
- Poor fail-safe logic
- Insufficient pilot training on override procedures

### Lessons for Engineers
- Always use **redundant sensors** in safety-critical systems
- Implement **fail-safe and override** mechanisms
- Ensure **transparent, explainable** system behavior
- **Human override** must always be possible

---

## Types of AI Failures in Mechanical Systems

### 1. Sensor Bias
- Sensors trained only in limited conditions (e.g., daylight, clean air)
- Fail in real-world variability (rain, fog, dust, vibration)

### 2. Algorithmic Bias
- Biased training datasets → incorrect predictions
- Overfitting → model works in lab but fails in field

### 3. Human-Machine Interface (HMI) Issues
- Poor communication between AI system and human operator
- Over-reliance on automation leads to loss of manual skill

---

## Safety Checklist for AI Deployment in Factories

### Design Level
- [ ] Use redundant sensors
- [ ] Validate data from multiple sources
- [ ] Include fail-safe shutdown mechanisms

### Algorithm Level
- [ ] Test on diverse and representative datasets
- [ ] Avoid overfitting
- [ ] Implement real-time anomaly detection

### Operational Level
- [ ] Human override must always exist
- [ ] Provide regular operator training
- [ ] Maintain system logs for auditing

### Ethical Level
- [ ] Ensure system transparency
- [ ] Define accountability clearly
- [ ] Assess environmental impact of AI deployment

---

## Accountability Framework

| Stakeholder | Responsibility |
|---|---|
| Software Engineer | Algorithm correctness and testing |
| Mechanical Engineer | System safety and physical integration |
| Company | Deployment, training, and compliance |
| Regulator | Certification and safety standards |

**Conclusion:** Responsibility is shared, but ultimate accountability lies with the organization deploying the system.

---

## Workforce Adaptation Strategies

When AI replaces manual tasks in factories:
- Upskill workers in AI-assisted operations
- Introduce human-AI collaboration roles
- Train workers in data interpretation and machine supervision
- Create hybrid roles: Machine Operator + Data Analyst

---

## Ethical Manifesto for AI-Mechanical Engineers

1. Design for **safety** over efficiency
2. Ensure **transparency** and explainability
3. Minimize **bias** in data and models
4. Protect **human employment** through adaptation
5. Take **full responsibility** for engineering decisions

---

## Practice Questions

**Q1:** An autonomous car fails to detect pedestrians at night. Identify the failure type and propose solutions.

**Q2:** A factory introduces AI-based quality inspection replacing manual workers. Discuss ethical concerns and workforce adaptation strategies.
