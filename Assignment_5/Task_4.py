class JobApplicationScoring:
    def __init__(self):
        self.applicants = []

    def add_applicant(self, name, experience, education, skills):
        self.applicants.append({
            'name': name,
            'experience': experience,
            'education': education,
            'skills': skills
        })

    def calculate_score(self, applicant):
        """
        Scoring logic:
        Experience (years) * 2
        Education level * 10
        Skills count * 5
        """
        score = (applicant['experience'] * 2) + \
                (applicant['education'] * 10) + \
                (applicant['skills'] * 5)
        return score

    def evaluate_applicants(self):
        results = []
        for applicant in self.applicants:
            score = self.calculate_score(applicant)
            results.append({'name': applicant['name'], 'score': score})
        return results
# Example Usage
if __name__ == "__main__":
    system = JobApplicationScoring()
    system.add_applicant("Alice", experience=5, education=3, skills=4)
    system.add_applicant("Bob", experience=2, education=2, skills=3)
    system.add_applicant("Charlie", experience=8, education=4, skills=5)

    evaluated = system.evaluate_applicants()

    print("Job Application Scores:")
    for result in evaluated:
        print(f"{result['name']}: {result['score']} points")
