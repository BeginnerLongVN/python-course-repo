class Contact: 
    def __init__(self, name, phone, email):
        self.name = name 
        self.phone = phone 
        self.email = email 
    
    def get_name(self): 
        return self.name 
    
    def get_phone(self): 
        return self.phone 
    
    def get_email(self): 
        return self.email
    
    def change_name(self, new_name): 
        self.name = new_name
        
    def change_phone(self, new_phone):
        self.phone = new_phone      
    
    def change_email(self, new_email):
        self.email = new_email
        
    def update_contact(self, new_name=None, new_phone=None, new_email=None):
        if new_name:
            self.change_name(new_name)
        if new_phone:
            self.change_phone(new_phone)
        if new_email:
            self.change_email(new_email)
        
class Personal_contact(Contact):
    def __init__(self, name, phone, email, birthday):
        super().__init__(name, phone, email)
        self.birthday = birthday
    
    def get_birthday(self):
        return self.birthday
    
    def change_birthday(self, new_birthday):
        self.birthday = new_birthday
        
    def show_contact_info(self):
        print(f"➡️ Name: {self.name} | Phone: {self.phone} | Email: {self.email} | Birthday: {self.birthday}")
        
    def update_contact(self, new_name=None, new_phone=None, new_email=None, new_birthday=None):
        super().update_contact(new_name, new_phone, new_email)
        if new_birthday:
            self.change_birthday(new_birthday)
        print(f"Contact '{self.name}' updated successfully!")
        self.show_contact_info()

    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'birthday': self.birthday
        }
    @staticmethod
    def from_dict(data):
        return Personal_contact(
            name=data['name'],
            phone=data['phone'],
            email=data['email'],
            birthday=data['birthday']
        )

class Business_contact(Contact):
    def __init__(self, name, phone, email, company, job_title=None):
        super().__init__(name, phone, email)
        self.company = company
        self.job_title = job_title
    
    def get_company(self):
        return self.company
    
    def change_company(self, new_company):
        self.company = new_company
        
    def get_job_title(self):
        return self.job_title
    
    def change_job_title(self, new_job_title):
        self.job_title = new_job_title
        
    def show_contact_info(self):
        print(f"➡️ Name: {self.name} | Phone: {self.phone} | Email: {self.email} | Company: {self.company} | Job Title: {self.job_title if self.job_title else 'N/A'}")
        
    def update_contact(self, new_name=None, new_phone=None, new_email=None, new_company=None, new_job_title=None):
        super().update_contact(new_name, new_phone, new_email)
        if new_company:
            self.change_company(new_company)
        if new_job_title:
            self.change_job_title(new_job_title)
        print(f"Contact '{self.name}' updated successfully!")
        self.show_contact_info()
        
    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone, 
            "email": self.email, 
            "company": self.company,
            "job_title": self.job_title
        }    
        
    @staticmethod
    def from_dict(data):
        return Business_contact(
            name=data['name'],
            phone=data['phone'],
            email=data['email'],
            company=data['company'],
            job_title=data.get('job_title')
        )
    
        