class Subject: 
    def __init__(self, subject, score): 
        self.subject = subject
        self.score = score
        
    def get_subject(self):
        return self.subject
    
    def get_score(self):
        return self.score
    
    def to_dict(self):
        return {
            "subject": self.subject, 
            "score": self.score
        }
        
    def from_dict(data):
        return Subject(data['subject'], data['score'])
    
    