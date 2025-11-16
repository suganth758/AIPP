from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Optional

class EducationLevel(Enum):
    HIGH_SCHOOL = "High School"
    ASSOCIATES = "Associate"
    BACHELORS = "Bachelor's"
    MASTERS = "Master's"
    PHD = "Ph.D."

@dataclass
class Applicant:
    name: str
    education: EducationLevel
    years_experience: float
    skills: List[str]
    personality_score: float     # 1-5
    communication_score: float   # 1-5
    references_score: float      # 1-5
    gender: Optional[str] = None # stored if needed; not used in scoring

class ApplicantScorer:
    """Weighted applicant scoring system (total = 100). Gender-neutral by design."""
    WEIGHTS = {
        "education": 20,
        "experience": 30,
        "skills": 25,
        "personality": 10,
        "communication": 10,
        "references": 5
    }

    def __init__(self, required_skills: List[str]):
        self.required_skills = [s.lower() for s in required_skills]

    def score_education(self, level: EducationLevel) -> float:
        mapping = {
            EducationLevel.HIGH_SCHOOL: 0.2,
            EducationLevel.ASSOCIATES: 0.4,
            EducationLevel.BACHELORS: 0.7,
            EducationLevel.MASTERS: 0.9,
            EducationLevel.PHD: 1.0
        }
        return mapping.get(level, 0.0) * self.WEIGHTS["education"]

    def score_experience(self, years: float) -> float:
        # Full credit at 10+ years, linear scale
        frac = min(max(years / 10.0, 0.0), 1.0)
        return frac * self.WEIGHTS["experience"]

    def score_skills(self, skills: List[str]) -> float:
        if not self.required_skills:
            return self.WEIGHTS["skills"]
        matched = sum(1 for s in skills if s.lower() in self.required_skills)
        frac = matched / len(self.required_skills)
        return min(1.0, frac) * self.WEIGHTS["skills"]

    def score_soft(self, value: float, weight_key: str) -> float:
        # value expected 1..5
        v = min(max(value, 1.0), 5.0)
        return ((v - 1.0) / 4.0) * self.WEIGHTS[weight_key]

    def evaluate(self, applicant: Applicant) -> Dict[str, float]:
        scores = {}
        scores["education"] = round(self.score_education(applicant.education), 2)
        scores["experience"] = round(self.score_experience(applicant.years_experience), 2)
        scores["skills"] = round(self.score_skills(applicant.skills), 2)
        scores["personality"] = round(self.score_soft(applicant.personality_score, "personality"), 2)
        scores["communication"] = round(self.score_soft(applicant.communication_score, "communication"), 2)
        scores["references"] = round(self.score_soft(applicant.references_score, "references"), 2)
        scores["total"] = round(sum(scores[k] for k in scores if k != "total"), 2)
        return scores

    @staticmethod
    def recommendation(total: float) -> str:
        if total >= 85:
            return "Strong Hire"
        if total >= 70:
            return "Hire"
        if total >= 60:
            return "Consider"
        return "Do Not Hire"

def format_report(applicant: Applicant, scores: Dict[str, float]) -> None:
    print(f"\nApplicant: {applicant.name}")
    if applicant.gender:
        print(f"(Gender stored but not used in scoring: {applicant.gender})")
    print("-" * 40)
    for k in ("education","experience","skills","personality","communication","references"):
        print(f"{k.title():12}: {scores[k]:5.2f} / {ApplicantScorer.WEIGHTS[k]:.0f}")
    print("-" * 40)
    print(f"Total Score : {scores['total']:5.2f} / 100")
    print("Recommendation:", ApplicantScorer.recommendation(scores["total"]))

if __name__ == "__main__":
    required = ["Python", "SQL", "Data Analysis", "Communication"]
    scorer = ApplicantScorer(required)

    # Example applicants
    a1 = Applicant(
        name="Alex Morgan",
        education=EducationLevel.MASTERS,
        years_experience=4.0,
        skills=["Python","SQL","Data Analysis"],
        personality_score=4.5,
        communication_score=4.0,S
        references_score=4.0,
        gender="Non-binary"
    )

    a2 = Applicant(
        name="Taylor Reed",
        education=EducationLevel.BACHELORS,
        years_experience=1.5,
        skills=["Python","Communication"],
        personality_score=3.5,
        communication_score=4.0,
        references_score=3.0
    )

    for applicant in (a1, a2):
        result = scorer.evaluate(applicant)
        format_report(applicant, result)