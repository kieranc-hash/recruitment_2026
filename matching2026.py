import streamlit as st
import math

# ===== DATA====================================================================================================================================================
# MAJORS
Accounting=['Catherine Dooley', 'Celeste  Gutierrez', 'Madison Taylor']
Acting=['Katelyn Quintanilla', 'Katherine Blumenschein']
Advertising=['Abrielle Gallini', 'Annabelle Judson', 'Elyse Miller', 'Emerson Pak', 'Jazlyn Mata', 'Kate Hoog', 'Kendall Klimek', 'Macie McKie']
Anthropology=['Zoe Veliz']
ArtHistory=['Sofie Combs']
ArtsandEntertainmentTechnologies=['Andrea Yu']
Biochemistry=['Mrinali Ganta']
Biology=['Aaleyah Lloyd', 'Audrey Cooper', 'Audrey Jones', 'Buckley Turner', 'Emmerich Benavides', 'Farrah Childs', 'Genesis Martinez', 'Izzy Davies', 'Megan Garza', 'Neela Juarez', 'Rishona Mopur', 'Sammi Gill', 'Sanya Hoskere']
BiomedicalEngineering=['Elizabeth Porter']
Business=['Hannah Belenkiy', 'Haylee Martin', 'Marie Jolie Day', 'Natalie Yoder', 'Olivia Alvarez', 'Sharon Yoon']
CanfieldBusinessHonors=['Hannah Belenkiy', 'Natalie Yoder', 'Olivia Alvarez']
ChemicalEngineering=['Katie Corbin']
CivicsHonors=['Ella Dillinger', 'Katie Walsh']
CommunicationandLeadership=['Annie Hoag', 'Brooke Waldman', "Delaney O'Brien", 'Emma Schneidau', 'Giada Scaramuzza', 'Jazlyn Mata']
ComputationalEngineering=['Morgan Gaitz', 'Siri Pemberton']
ComputerScience=['Kimia Forouzesh']
Dance=['Amorie Erichsen', 'Ava Hodges', 'Marie Jolie Day', 'Olivia Asay']
EarlyChildhoodEducation=['Anika Novak', 'Ella Pitts', 'Emily Bull']
Economics=['Addie Brooks', 'Dylan Kaufman', 'Kaelyn Liu', 'Sofie Arroyo']
ElementaryEducation=['Elena Solano']
English=['Kaitlin Black', 'Sasha Pittsford']
EnvironmentalEngineering=['Daisy Challoner', 'Katie Windell']
EnvironmentalScience=['Elizabeth Perales']
Finance=['Hannah Belenkiy', 'Laraleigh Hackerman', 'Madison Taylor', 'Natalie Yoder']
Geography=['Skye Doughton']
Geology=['Christa Hamlin']
Geoscience=['Jacqueline Olivier']
GlobalStudies=['Addison Starr']
Government=['Anabel Precht', 'Annie Boeh', 'Arani Walton', 'Charlie Stone', 'Hannah Reilly', 'Lily Robbins', 'May Downey', 'Mia Cisneros', 'Sofia Bartkoski', 'Zoe Westbrook', 'Zoey Bustamante']
GraphicDesign=['Natalie Juarez']
HealthandSociety=['Bella Champion', 'Ema Avila', 'Emma Levy', 'Hazel Wells', 'Sofie Martinez']
InternationalRelations=['Addison Starr', 'Sarah Kester', 'Sofia Bartkoski']
Journalism=['Annie Boeh', 'Brooke Rosenberg', 'Katie Walsh', 'Parker Keston', 'Zoe Westbrook']
Kinesiology=['Alyssa Garcia', 'Ava Hodges', 'Sarah Miller', 'Taylor McIlvain']
LiberalArtsHonors=['Charlie Stone']
Marketing=['Ava Dahlander']
Mathematics=['Jennifer Rosado', 'Kimia Forouzesh']
MechanicalEngineering=['Ollie Mae Harrison', 'Zeina Saghiyyah']
Neuroscience=['Braeleigh Garcia', 'Caitlin Van Sant', 'Hadley Amann', 'Hannah Dollinger', 'Hasita Karthikeyan', 'Lauren Henderson']
Nursing=['Caelyn Prochazka', 'Ema Avila', 'Hadley Amann', 'Jasmine Valdez', 'Lexie Hale', 'Maria Sepulveda', 'Ryleigh Montgomery']
Nutrition=['Andrea Yu', 'Maria Sanchez', 'Sophie Coe']
PhysicalCultureandSports=['Annie Bryce']
PlanIIHonors=['Ella Dillinger']
PoliticalCommunications=['Victoria Olivarez']
Psychology=['Alexa Lira', 'Caroline Schulze', 'Ella Leininger', 'Josie Daik', 'Kassidy Bragg', 'Kate Neiman', 'Margot Rosenband', 'Sofia Argoti', 'Sophia Sayers', 'Taylor Jennings']
PublicAffairs=['Drew Shelton', 'Madeline Gottemoller']
PublicHealth=['Sophia Labazzo']
PublicRelations=['Georgia Key', 'Kate Belman']
RTF=['Annabelle Judson', 'Brooke Rosenberg', 'Ella Garber', 'Kate Flanery']
Sociology=['Angie Andersen', 'Hannah Reilly']
SpeechLanguageandHearingSciences=['Emma Levy', 'Giana Toothman', 'Molly Bogar', 'Tatum Samuels']
SustainabilityStudies=['Kamryn Lowery']
Theatre=['Marie Jolie Day']

# MINORS
AdvertisingMinor=['Olivia Asay']
AmericanSignLanguageMinor=['Molly Bogar']
ArtsManagementandAdministrationMinor=['Sofie Combs']
BusinessAdministrationMinor=['Sophia Sayers']
BusinessMinor=['Abrielle Gallini', 'Annie Hoag', 'Dylan Kaufman', 'Elyse Miller', 'Emma Schneidau', 'Farrah Childs', 'Georgia Key', 'Hannah Dollinger', 'Kaelyn Liu', 'Kaitlin Black', 'Kate Belman', 'Kate Hoog', 'Katelyn Quintanilla', 'Katherine Blumenschein', 'Katie Corbin', 'Kendall Klimek', 'Natalie Juarez', 'Natalie Yoder', 'Sofie Arroyo']
BusinessandPublicPolicyMinor=['Katie Walsh']
ChineseMinor=['Kaelyn Liu']
CommunicationStudiesMinor=['Arani Walton', 'Jennifer Rosado', 'Margot Rosenband']
CreativeWritingMinor=['Kaitlin Black']
DataScienceMinor=['Emmerich Benavides']
DesignStrategiesMinor=['Ollie Mae Harrison']
EconomicsMinor=['Jennifer Rosado']
EducationalPsychologyMinor=['Anika Novak', 'Elena Solano', 'Ella Leininger', 'Ella Pitts', 'Sofie Martinez']
EnergyFinanceMinor=['Laraleigh Hackerman']
EnglishMinor=['Ella Garber']
ForensicScienceMinor=['Aaleyah Lloyd', 'Ella Leininger']
FrenchMinor=['Anabel Precht']
GermanMinor=['Jennifer Rosado']
GlobalSustainabilityLeadershipMinor=["Delaney O'Brien"]
HealthCommunicationsMinor=['Caitlin Van Sant', 'Kate Neiman', 'Sofie Martinez']
HealthcareReformandInnovationMinor=['Hasita Karthikeyan', 'Megan Garza', 'Neela Juarez', 'Sophia Labazzo']
HistoryMinor=['Mia Cisneros']
JeffersonScholarsProgramMinor=['Katie Windell', 'Siri Pemberton']
JournalismMinor=['Sasha Pittsford']
KinesiologyMinor=['Angie Andersen', 'Buckley Turner', 'Caroline Schulze', 'Genesis Martinez']
LawJusticeandSocietyMinor=['Drew Shelton', 'Jazlyn Mata', 'Lily Robbins', 'Madeline Gottemoller']
LawPolicyandEqualityMinor=['Alexa Lira']
MarketingMinor=['Haylee Martin']
MediaandEntertainmentIndustriesMinor=['Katelyn Quintanilla']
MedicalFitnessRehabMinor=['Sarah Miller']
MedicalSpanishMinor=['Giana Toothman', 'Lauren Henderson']
PatientsPractitionersandtheCulturesofCareMinor=['Jasmine Valdez']
PhilosophyMinor=['Anabel Precht']
PreHealthProfessionsMinor=['Andrea Yu', 'Audrey Cooper', 'Bella Champion', 'Braeleigh Garcia', 'Buckley Turner', 'Farrah Childs', 'Hazel Wells', 'Izzy Davies', 'Lauren Henderson', 'Rishona Mopur', 'Sophie Coe']
PreMedMinor=['Aaleyah Lloyd', 'Buckley Turner', 'Hannah Dollinger']
RealEstateMinor=['Addie Brooks']
RiskManagementMinor=['Jennifer Rosado']
SalesandBusinessDevelopmentMinor=['Macie McKie', 'Sofia Argoti']
SocialandBehavioralSciencesMinor=['Charlie Stone', 'Kassidy Bragg']
SociologyMinor=['Skye Doughton']
SpanishMinor=['Addison Starr', 'Giana Toothman', 'Sofia Bartkoski']
SportsBroadcastingandProductionMinor=['Amorie Erichsen']
SportsMediaMinor=['Emerson Pak', 'Kate Hoog', 'Parker Keston']
UTeachMinor=['Elizabeth Perales', 'Sasha Pittsford']
WealthManagementMinor=['Hannah Belenkiy', 'Laraleigh Hackerman']

# COLLEGES
McCombsSchoolofBusiness=['Ava Dahlander', 'Catherine Dooley', 'Celeste Gutierrez', 'Hannah Belenkiy', 'Haylee Martin', 'Kate Belman', 'Katie Corbin', 'Kendall Klimek', 'Laraleigh Hackerman', 'Madison Taylor', 'Marie Jolie Day', 'Natalie Yoder', 'Olivia Alvarez', 'Sharon Yoon']
CockrellSchoolofEngineering=['Daisy Challoner', 'Elizabeth Porter', 'Katie Corbin', 'Katie Windell', 'Morgan Gaitz', 'Ollie Mae Harrison', 'Siri Pemberton', 'Zeina Saghiyyah']
CollegeofNaturalSciences=['Andrea Yu', 'Audrey Cooper', 'Audrey Jones', 'Braeleigh Garcia', 'Buckley Turner', 'Caitlin Van Sant', 'Elizabeth Perales', 'Emmerich Benavides', 'Farrah Childs', 'Genesis Martinez', 'Hadley Amann', 'Hannah Dollinger', 'Hasita Karthikeyan', 'Izzy Davies', 'Jennifer Rosado', 'Kimia Forouzesh', 'Lauren Henderson', 'Lee Lloyd', 'Maria Sanchez', 'Megan Garza', 'Mrinali Ganta', 'Neela Juarez', 'Rishona Mopur', 'Sammi Gill', 'Sanya Hoskere', 'Sophia Labazzo', 'Sophie Coe']
MoodyCollegeofCommunication=['Abrielle Gallini', 'Annabelle Judson', 'Annie Boeh', 'Annie Hoag', 'Brooke Rosenberg', 'Brooke Waldman', 'Delaney O’Brien', 'Elizabeth Scull', 'Ella Garber', 'Elyse Miller', 'Emma Levy', 'Emma Schneidau', 'Emmy Pak', 'Georgia Key', 'Giada Scaramuzza', 'Giana Toothman', 'Jazlyn Mata', 'Kate Belman', 'Kate Flanery', 'Kate Hoog', 'Katie Walsh', 'Kendall Klimek', 'Kirra Vrzal', 'Macie McKie', 'Molly Bogar', 'Parker Keston', 'Tatum Samuels', 'Victoria Olivarez', 'Zoë Westbrook']
CollegeofLiberalArts=['Addie Brooks', 'Addison Starr', 'Alexa Lira', 'Angie Andersen', 'Annie Boeh', 'Arani Walton', 'Bella Champion', 'Caroline Schulze', 'Charlie Stone', 'Dylan Kaufman', 'Ella Leininger', 'Ema Avila', 'Emma Levy', 'Hannah Reilly', 'Hazel Wells', 'Josie Daik', 'Kaelyn Liu', 'Kaitlin Black', 'Kamryn Lowery', 'Kassidy', 'Lily Robbins', 'Margot Rosenband', 'May Downey', 'Mia Cisneros', 'Paola Castillo', 'Sarah Kester', 'Sasha Pittsford', 'Skye Doughton', 'Sofia Argoti', 'Sofia Bartkoski', 'Sofie Arroyo', 'Sofie Martinez', 'Sophia Sayers', 'Taylor Jennings', 'Zoe Veliz', 'Zoey Bustamante', 'Zoë Westbrook', 'Anabel Precht']
CollegeofEducation=['Alyssa Garcia', 'Anika Novak', 'Annie Bryce', 'Ella Pitts', 'Sarah Miller', 'Taylor McIlvain', 'Elena Solano', 'Emily Bull']
CollegeofFineArts=['Amorie Erichsen', 'Ava Hodges', 'Kate Neiman', 'Katelyn Quintanilla', 'Katherine Blumenschein', 'Macie McKie', 'Marie Jolie Day', 'Natalie Juarez', 'Olivia Asay', 'Sofie Combs']
SchoolofNursing=['Caelyn Prochazka', 'Ema Avila', 'Jasmine Valdez', 'Lexie Hale', 'Maria Sepulveda', 'Ryleigh Montgomery']
JacksonSchoolofGeosciences=['Christa Hamlin', 'Jacqueline Olivier']
LBJSchoolofPublicAffairs=['Drew Shelton', 'Madeline Gottemoller']
SchoolofCivicLeadership=['Ella Dillinger', 'Katie Walsh']


# ==== MAPPING INTEREST NAME TO RECRUITER NAME LISTS ===========================================================================================================
majors = {
        "Accounting": Accounting,
        "Acting": Acting,
        "Advertising": Advertising,
        "Anthropology": Anthropology,
        "Art History": ArtHistory,
        "Arts and Entertainment Technologies": ArtsandEntertainmentTechnologies,
        "Biochemistry": Biochemistry,
        "Biology": Biology,
        "Biomedical Engineering": BiomedicalEngineering,
        "Business": Business,
        "Canfield Business Honors": CanfieldBusinessHonors,
        "Chemical Engineering": ChemicalEngineering,
        "Civics Honors": CivicsHonors,
        "Communication and Leadership": CommunicationandLeadership,
        "Computational Engineering": ComputationalEngineering,
        "Computer Science": ComputerScience,
        "Dance": Dance,
        "Early Childhood Education": EarlyChildhoodEducation,
        "Economics": Economics,
        "Elementary Education": ElementaryEducation,
        "English": English,
        "Environmental Engineering": EnvironmentalEngineering,
        "Environmental Science": EnvironmentalScience,
        "Finance": Finance,
        "Geography": Geography,
        "Geology": Geology,
        "Geoscience": Geoscience,
        "Global Studies": GlobalStudies,
        "Government": Government,
        "Graphic Design": GraphicDesign,
        "Health and Society": HealthandSociety,
        "International Relations": InternationalRelations,
        "Journalism": Journalism,
        "Kinesiology": Kinesiology,
        "Liberal Arts Honors": LiberalArtsHonors,
        "Marketing": Marketing,
        "Mathematics": Mathematics,
        "Mechanical Engineering": MechanicalEngineering,
        "Neuroscience": Neuroscience,
        "Nursing": Nursing,
        "Nutrition": Nutrition,
        "Physical Culture and Sports": PhysicalCultureandSports,
        "Plan II Honors": PlanIIHonors,
        "Political Communications": PoliticalCommunications,
        "Psychology": Psychology,
        "Public Affairs": PublicAffairs,
        "Public Health": PublicHealth,
        "Public Relations": PublicRelations,
        "RTF": RTF,
        "Sociology": Sociology,
        "Speech Language and Hearing Sciences": SpeechLanguageandHearingSciences,
        "Sustainability Studies": SustainabilityStudies,
        "Theatre": Theatre
}

minors = {
        "Advertising Minor": AdvertisingMinor,
        "American Sign Language Minor": AmericanSignLanguageMinor,
        "Arts Management and Administration Minor": ArtsManagementandAdministrationMinor,
        "Business Administration Minor": BusinessAdministrationMinor,
        "Business Minor": BusinessMinor,
        "Business and Public Policy Minor": BusinessandPublicPolicyMinor,
        "Chinese Minor": ChineseMinor,
        "Communication Studies Minor": CommunicationStudiesMinor,
        "Creative Writing Minor": CreativeWritingMinor,
        "Data Science Minor": DataScienceMinor,
        "Design Strategies Minor": DesignStrategiesMinor,
        "Economics Minor": EconomicsMinor,
        "Educational Psychology Minor": EducationalPsychologyMinor,
        "Energy Finance Minor": EnergyFinanceMinor,
        "English Minor": EnglishMinor,
        "Forensic Science Minor": ForensicScienceMinor,
        "French Minor": FrenchMinor,
        "German Minor": GermanMinor,
        "Global Sustainability Leadership Minor": GlobalSustainabilityLeadershipMinor,
        "Health Communications Minor": HealthCommunicationsMinor,
        "Healthcare Reform and Innovation Minor": HealthcareReformandInnovationMinor,
        "History Minor": HistoryMinor,
        "Jefferson Scholars Program Minor": JeffersonScholarsProgramMinor,
        "Journalism Minor": JournalismMinor,
        "Kinesiology Minor": KinesiologyMinor,
        "Law Justice and Society Minor": LawJusticeandSocietyMinor,
        "Law Policy and Equality Minor": LawPolicyandEqualityMinor,
        "Marketing Minor": MarketingMinor,
        "Media and Entertainment Industries Minor": MediaandEntertainmentIndustriesMinor,
        "Medical Fitness Rehab Minor": MedicalFitnessRehabMinor,
        "Medical Spanish Minor": MedicalSpanishMinor,
        "Patients Practitioners and the Cultures of Care Minor": PatientsPractitionersandtheCulturesofCareMinor,
        "Philosophy Minor": PhilosophyMinor,
        "Pre Health Professions Minor": PreHealthProfessionsMinor,
        "Pre Med Minor": PreMedMinor,
        "Real Estate Minor": RealEstateMinor,
        "Risk Management Minor": RiskManagementMinor,
        "Sales and Business Development Minor": SalesandBusinessDevelopmentMinor,
        "Social and Behavioral Sciences Minor": SocialandBehavioralSciencesMinor,
        "Sociology Minor": SociologyMinor,
        "Spanish Minor": SpanishMinor,
        "Sports Broadcasting and Production Minor": SportsBroadcastingandProductionMinor,
        "Sports Media Minor": SportsMediaMinor,
        "UTeach Minor": UTeachMinor,
        "Wealth Management Minor": WealthManagementMinor
}

colleges = {
    "McCombs Business": McCombsSchoolofBusiness,
    "Cockrell Engineering": CockrellSchoolofEngineering,
    "College of Natural Sciences": CollegeofNaturalSciences,
    "Moody Communication": MoodyCollegeofCommunication,
    "College of Liberal Arts": CollegeofLiberalArts,
    "Education": CollegeofEducation,
    "College of Fine Arts": CollegeofFineArts,
    "Nursing": SchoolofNursing,
    "Jackson School of Geosciences": JacksonSchoolofGeosciences,
    "LBJ School of Public Affairs": LBJSchoolofPublicAffairs,
    "School of Civic Leadership": SchoolofCivicLeadership,
}


# ===== STREAMLIT USER INTERFACE ===============================================================================================================================
st.title("Interest Finder")

def checkbox_columns(title, items, num_cols=2):
    st.markdown(f'### {title}')
    with st.expander('Select Here', expanded=False):
        cols = st.columns(num_cols)
        chunk_size = math.ceil(len(items) / num_cols)
        selected = []
        for i, interest in enumerate(items):
            col = cols[i // chunk_size]
            if col.checkbox(interest):
                selected.append(interest)
        return selected

# uncomment these as you add them back in
        
selected_majors = checkbox_columns("Majors"+'\U0001F4DA', list(majors.keys()), num_cols=4)
selected_minors = checkbox_columns("Minors"+"\U0001F4DD", list(minors.keys()), num_cols=4)
#selected_college = checkbox_columns("College/Track"+"\U0001FA7A", list(college.keys()), num_cols=4)
#selected_hometowns = checkbox_columns("Hometowns"+"\U0001F3E0", list(hometowns.keys()), num_cols=4)
#selected_schools = checkbox_columns("High Schools"+"\U0001F3EB", list(schools.keys()), num_cols=4)
#selected_extras = checkbox_columns("HS Extracurriculars"+"\U0001F483", list(extras.keys()), num_cols=4)
#selected_orgs = checkbox_columns("UT Organizations"+"\U0000266B", list(utorgs.keys()), num_cols=4)
#selected_activities = checkbox_columns("Activities/Interests for Fun"+"\U0001F3C3", list(activities.keys()), num_cols=4)
#selected_summercamps = checkbox_columns("Summer Camp"+"\U0001F525", list(summercamps.keys()), num_cols=4)
#selected_nicheinterests = checkbox_columns("Niche Interests"+"\U0001F388", list(nicheinterests.keys()), num_cols=4)
#selected_transfers = checkbox_columns("Transfer Students"+"\U0001F501", list(transfers.keys()), num_cols=4)

selected_interests = selected_majors + selected_minors #+ selected_college + selected_hometowns + selected_schools + selected_extras + selected_orgs + selected_activities + selected_summercamps + selected_nicheinterests + selected_transfers

# ===== Matching Logic =====
if selected_interests:
    people_matches = {}

    # Loop over all selected interests with category info
    for interest in selected_interests:
        # Determine which category dict it belongs to
        if interest in majors:
            names = majors[interest]
        elif interest in minors:
            names = minors[interest]
        #elif interest in college:
         #   names = college[interest]
        #elif interest in hometowns:
         #   names = hometowns[interest]
        #elif interest in schools:
         #   names = schools[interest]
        #elif interest in extras:
         #   names = extras[interest]
        #elif interest in utorgs:
         #   names = utorgs[interest]
        #elif interest in activities:
         #   names = activities[interest]
        #elif interest in summercamps:
         #   names = summercamps[interest]
        #elif interest in nicheinterests:
         #   names = nicheinterests[interest]
        #elif interest in transfers:
         #   names = transfers[interest]
        else:
            continue

        # Store each match as a tuple (category, interest) to prevent confusion
        for name in names:
            if name not in people_matches:
                people_matches[name] = set()
            people_matches[name].add(interest)  # add the exact checkbox label

    all_selected = set(selected_interests)
    all_match = []
    some_match = []
    one_match = []

    for person, matched_set in people_matches.items():
        # intersection of what the person has with what was actually selected
        matched_selected = matched_set & all_selected
        if matched_selected == all_selected:
            all_match.append((person, matched_selected))
        elif len(matched_selected) > 1:
            some_match.append((person, matched_selected))
        elif len(matched_selected) == 1:
            one_match.append((person, matched_selected))

    # Color blues and whites #NOTE: I randomly sorted the names into blues, whites, and violets -- update these with the correct lists!
    blue_names = ['Aaleyah Lloyd', 'Abrielle Gallini', 'Addie Brooks',
       'Addison Starr', 'Alexa Lira', 'Alyssa Garcia', 'Amorie Erichsen',
       'Anabel Precht', 'Andrea Yu', 'Angie Andersen', 'Anika Novak',
       'Annabelle Judson', 'Annie Boeh', 'Annie Bryce', 'Annie Hoag',
       'Arani Walton', 'Audrey Cooper', 'Audrey Jones', 'Ava Dahlander',
       'Ava Hodges', 'Bella Champion', 'Braeleigh Garcia',
       'Brooke Rosenberg', 'Brooke Waldman', 'Buckley Turner',
       'Caelyn Prochazka', 'Caitlin Van Sant', 'Caroline Schulze',
       'Catherine Dooley', 'Celeste  Gutierrez', 'Charlie Stone',
       'Christa Hamlin', 'Daisy Challoner', "Delaney O'Brien",
       'Drew Shelton', 'Dylan Kaufman', 'Elena Solano',
       'Elizabeth Perales', 'Elizabeth Porter', 'Ella Dillinger',
       'Ella Garber', 'Ella Leininger', 'Ella Pitts', 'Elyse Miller',
       'Ema Avila', 'Emerson Pak', 'Emily Bull', 'Emma Levy',
       'Emma Schneidau', 'Emmerich Benavides', 'Farrah Childs',
       'Genesis Martinez', 'Georgia Key', 'Giada Scaramuzza',
       'Giana Toothman', 'Hadley Amann', 'Hannah Belenkiy',
       'Hannah Dollinger', 'Hannah Reilly', 'Hasita Karthikeyan']
    violet_names = ['Haylee Martin', 'Hazel Wells', 'Izzy Davies',
       'Jacqueline Olivier', 'Jasmine Valdez', 'Jazlyn Mata',
       'Jennifer Rosado', 'Josie Daik', 'Kaelyn Liu', 'Kaitlin Black',
       'Kamryn Lowery', 'Kassidy Bragg', 'Kate Belman', 'Kate Flanery',
       'Kate Hoog', 'Kate Neiman', 'Katelyn Quintanilla',
       'Katherine Blumenschein', 'Katie Corbin', 'Katie Walsh',
       'Katie Windell', 'Kendall Klimek', 'Kimia Forouzesh',
       'Laraleigh Hackerman', 'Lauren Henderson', 'Lexie Hale',
       'Lily Robbins', 'Macie McKie', 'Madeline Gottemoller',
       'Madison Taylor', 'Margot Rosenband', 'Maria Sanchez',
       'Maria Sepulveda', 'Marie Jolie Day', 'May Downey', 'Megan Garza',
       'Mia Cisneros', 'Molly Bogar', 'Morgan Gaitz', 'Mrinali Ganta',
       'Natalie Juarez', 'Natalie Yoder', 'Neela Juarez',
       'Olivia Alvarez', 'Olivia Asay', 'Ollie Mae Harrison',
       'Parker Keston', 'Rishona Mopur', 'Ryleigh Montgomery',
       'Sammi Gill', 'Sanya Hoskere', 'Sarah Kester', 'Sarah Miller',
       'Sasha Pittsford', 'Sharon Yoon', 'Siri Pemberton',
       'Skye Doughton', 'Sofia Argoti', 'Sofia Bartkoski', 'Sofie Arroyo']
    gray_names = ['Sofie Combs', 'Sofie Martinez', 'Sophia Labazzo', 'Sophia Sayers',
       'Sophie Coe', 'Tatum Samuels', 'Taylor Jennings',
       'Taylor McIlvain', 'Victoria Olivarez', 'Zeina Saghiyyah',
       'Zoe Veliz', 'Zoe Westbrook', 'Zoey Bustamante']
    
    def coloring(names):
        if name in blue_names:
            return f"<span style='color:blue'>{name}</span></b>"
        elif name in violet_names:
            return f"<span style='color:darkviolet'>{name}</span></b>"
        elif name in gray_names:
            return f"<span style='color:darkgray'>{name}</span></b>"
        else:
            return f"<b>{name}</b>"

    #Display
    st.subheader("✅ All Matches")
    if all_match:
        for name, matches in all_match:
            colored_names = coloring(name)
            st.markdown(f"{colored_names}: {', '.join(matches)}", unsafe_allow_html=True)

    st.subheader("🔹 Some Matches")
    if some_match:
        for name, matches in some_match:
            colored_names = coloring(name)
            st.markdown(f"{colored_names}: {', '.join(matches)}", unsafe_allow_html=True)

    st.subheader("⚪ One Match")
    if one_match:
        for name, matches in one_match:
            colored_names = coloring(name)
            st.markdown(f"{colored_names}: {', '.join(matches)}", unsafe_allow_html=True)
