from exceptions.company_exception import CompanyException
from rest_framework import status
from models.company_model import Company


class CompanyManager:

    company = None

    def __init__(self, **kwargs):
        try:
            if 'slug' in kwargs:
                self.slug = kwargs['slug']
                self.company = Company.objects.get(slug=self.slug)
            elif 'company_id' in kwargs:
                self.company_id = kwargs['company_id']
                self.company = Company.objects.get(id=self.comapny_id)
            elif 'company' in kwargs:
                self.company = kwargs['company']
            else:
                self.logger.log("CompanyManager initialized")
                self.new = True
        except Company.DoesNotExist as e:
            self.logger.log(
                "CompanyManager initialization failed for company")
            raise CompanyException("company not found", status.HTTP_404_NOT_FOUND)

    def get_company(self):
        return self.company

    def create_company(self, company_data: dict):
        try:
            company = Company(
                name=company_data['name'],
                description=company_data['description'],
                title=company_data['title'],
                keywords=company_data['keywords'],
                slug=company_data['slug'],
                first_name=company_data['first_name'],
                last_name=company_data['last_name'],
                phone=company_data['phone'],
                email=company_data['email'],
                designation=company_data['designation'],
                date_joined=company_data['date_joined'],
            )
            company.save()
            return company
        except Exception as e:
            self.logger.log("Failed to create company")
            return False