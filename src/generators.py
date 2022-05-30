import random
import string
from faker import Faker

fake = Faker(use_weighting=False)

def random_string(len=15):
    lst =  [random.choice(string.hexdigits) for n in range(len)]
    return "".join(lst)

def number():
    return random.randrange(1, 1000)

def number_employees():
    return random.randrange(1, 10000)

def long_text():
    return fake.paragraph(nb_sentences=1)

def sex():
    return random.choice(['Male', 'Female'])

def department():
    # https://www.quora.com/What-are-the-main-departments-in-a-company
    return random.choice([
        "Marketing & Proposals Department",
        "sales Department",
        "Project Department",
        "Designing Department",
        "Production Department",
        "Maintenance Department",
        "Store Department",
        "Procurement Department",
        "Quality Department",
        "Inspection department",
        "Packaging Department",
        "Finance Department",
        "Dispatch Department",
        "Account Department",
        "Research & Development Department",
        "Information Technology Department",
        "Human Resource Department",
        "Security Department",
        "Administration department"
    ])

def industry():
    # https://gist.github.com/mbejda/19012b99a12e9d014389
    return random.choice(["Accounting",
"Airlines / Aviation",
"Alternative Dispute Resolution",
"Alternative Medicine",
"Animation",
"Apparel / Fashion",
"Architecture / Planning",
"Arts / Crafts",
"Automotive",
"Aviation / Aerospace",
"Banking / Mortgage",
"Biotechnology / Greentech",
"Broadcast Media",
"Building Materials",
"Business Supplies / Equipment",
"Capital Markets / Hedge Fund / Private Equity",
"Chemicals",
"Civic / Social Organization",
"Civil Engineering",
"Commercial Real Estate",
"Computer Games",
"Computer Hardware",
"Computer Networking",
"Computer Software / Engineering",
"Computer / Network Security",
"Construction",
"Consumer Electronics",
"Consumer Goods",
"Consumer Services",
"Cosmetics",
"Dairy",
"Defense / Space",
"Design",
"E - Learning",
"Education Management",
"Electrical / Electronic Manufacturing",
"Entertainment / Movie Production",
"Environmental Services",
"Events Services",
"Executive Office",
"Facilities Services",
"Farming",
"Financial Services",
"Fine Art",
"Fishery",
"Food Production",
"Food / Beverages",
"Fundraising",
"Furniture",
"Gambling / Casinos",
"Glass / Ceramics / Concrete",
"Government Administration",
"Government Relations",
"Graphic Design / Web Design",
"Health / Fitness",
"Higher Education / Acadamia",
"Hospital / Health Care",
"Hospitality",
"Human Resources / HR",
"Import / Export",
"Individual / Family Services",
"Industrial Automation",
"Information Services",
"Information Technology / IT",
"Insurance",
"International Affairs",
"International Trade / Development",
"Internet",
"Investment Banking / Venture",
"Investment Management / Hedge Fund / Private Equity",
"Judiciary",
"Law Enforcement",
"Law Practice / Law Firms",
"Legal Services",
"Legislative Office",
"Leisure / Travel",
"Library",
"Logistics / Procurement",
"Luxury Goods / Jewelry",
"Machinery",
"Management Consulting",
"Maritime",
"Market Research",
"Marketing / Advertising / Sales",
"Mechanical or Industrial Engineering",
"Media Production",
"Medical Equipment",
"Medical Practice",
"Mental Health Care",
"Military Industry",
"Mining / Metals",
"Motion Pictures / Film",
"Museums / Institutions",
"Music",
"Nanotechnology",
"Newspapers / Journalism",
"Non - Profit / Volunteering",
"Oil / Energy / Solar / Greentech",
"Online Publishing",
"Other Industry",
"Outsourcing / Offshoring",
"Package / Freight Delivery",
"Packaging / Containers",
"Paper / Forest Products",
"Performing Arts",
"Pharmaceuticals",
"Philanthropy",
"Photography",
"Plastics",
"Political Organization",
"Primary / Secondary Education",
"Printing",
"Professional Training",
"Program Development",
"Public Relations / PR",
"Public Safety",
"Publishing Industry",
"Railroad Manufacture",
"Ranching",
"Real Estate / Mortgage",
"Recreational Facilities / Services",
"Religious Institutions",
"Renewables / Environment",
"Research Industry",
"Restaurants",
"Retail Industry",
"Security / Investigations",
"Semiconductors",
"Shipbuilding",
"Sporting Goods",
"Sports",
"Staffing / Recruiting",
"Supermarkets",
"Telecommunications",
"Textiles",
"Think Tanks",
"Tobacco",
"Translation / Localization",
"Transportation",
"Utilities",
"Venture Capital / VC",
"Veterinary",
"Warehousing",
"Wholesale",
"Wine / Spirits",
"Wireless",
"Writing / Editing"])

TYPES_TO_GENERATORS = {
    'id': random_string,
    'first_name': fake.first_name,
    'last_name': fake.last_name,
    'company': fake.company,
    'industry': industry,
    'business_department': department,
    'company_desc': fake.catch_phrase,
    'company_number_employees': number_employees,
    'city': fake.city,
    'country': fake.country,
    'sex': sex,
    'url': fake.url,
    'email': fake.email,
    'business_email': fake.company_email,
    'website': fake.url,
    'job': fake.job,
    'number': number,
    'date': fake.date,
    'year': fake.year,
    'datetime': fake.date_time,
    'date_this_decade': fake.date_this_decade,
    'date_of_birth': fake.date_of_birth,
    'long_text': long_text,
    'address': fake.address,
    'phone': fake.phone_number
}
