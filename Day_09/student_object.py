from subject_object import Subject

class Student: 
    def __init__(self, id, name): 
        self.id = id
        self.name = name
        self.subjects = []
        
    def add_subject_with_grade(self, subject):
        self.subjects.append(subject)
        
    def remove_subject(self, subject_name):
        for subject in self.subjects: 
            if subject.get_subject() == subject_name:
                self.subjects.remove(subject)
                print(f"Course '{subject_name}' removed from student {self.name}.")
                return 
            
        print(f"Course '{subject_name}' not found for student {self.name}.")
        
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_gpa(self):
        if not self.subjects: 
            return 0.0
        total_score = sum(float(subject.get_score()) for subject in self.subjects)
        gpa =  total_score / len(self.subjects)
        return gpa
    
    def show_info(self):
        print(f"ID: {self.id} | Name: {self.name} | GPA: {self.get_gpa():.2f}")
    
    def to_dict(self): 
        return {
            "id": self.id, 
            "name": self.name, 
            "courses": [subject.to_dict() for subject in self.subjects],
            "gpa": self.get_gpa()
        }
    @staticmethod
    def from_dict(data):
        student = Student(data['id'], data['name'])
        for subject_data in data['courses']:
            subject = Subject.from_dict(subject_data)
            student.add_subject_with_grade(subject)
        return student
    
    
        
        
    
    
            
        
        
        
    

            
            
        
    
