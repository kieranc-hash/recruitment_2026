import streamlit as st
import math

# ===== DATA====================================================================================================================================================
# MAJORS
Accounting=['Catherine Dooley', 'Celeste  Gutierrez', 'Madison Taylor']
Acting=['Katelyn Quintanilla', 'Katherine Blumenschein']
Advertising=['Abrielle Gallini', 'Annabelle Judson', 'Elyse Miller', 'Emmy Pak', 'Jazlyn Mata', 'Kate Hoog', 'Kendall Klimek', 'Macie McKie']
Anthropology=['Zoe Veliz']
ArtHistory=['Sofie Combs']
ArtsandEntertainmentTechnologies=['Andrea Yu']
BehavioralandSocialDataScience = ['Paola Castillo']
Biochemistry=['Mrinali Ganta']
Biology=['Lee Lloyd', 'Audrey Cooper', 'Audrey Jones', 'Buckley Turner', 'Emmerich Benavides', 'Farrah Childs', 'Genesis Martinez', 'Izzy Davies', 'Megan Garza', 'Neela Juarez', 'Rishona Mopur', 'Sammi Gill', 'Sanya Hoskere']
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
ForensicScienceMinor=['Lee Lloyd', 'Ella Leininger']
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
PreMedMinor=['Lee Lloyd', 'Buckley Turner', 'Hannah Dollinger']
RealEstateMinor=['Addie Brooks']
RiskManagementMinor=['Jennifer Rosado']
SalesandBusinessDevelopmentMinor=['Macie McKie', 'Sofia Argoti']
SocialandBehavioralSciencesMinor=['Charlie Stone', 'Kassidy Bragg']
SociologyMinor=['Skye Doughton']
SpanishMinor=['Addison Starr', 'Giana Toothman', 'Sofia Bartkoski']
SportsBroadcastingandProductionMinor=['Amorie Erichsen']
SportsMediaMinor=['Emmy Pak', 'Kate Hoog', 'Parker Keston']
UTeachMinor=['Elizabeth Perales', 'Sasha Pittsford']
WealthManagementMinor=['Hannah Belenkiy', 'Laraleigh Hackerman']

# COLLEGES
McCombsSchoolofBusiness=['Ava Dahlander', 'Catherine Dooley', 'Celeste Gutierrez', 'Hannah Belenkiy', 'Haylee Martin', 'Kate Belman', 'Katie Corbin', 'Kendall Klimek', 'Laraleigh Hackerman', 'Madison Taylor', 'Marie Jolie Day', 'Natalie Yoder', 'Olivia Alvarez', 'Sharon Yoon']
CockrellSchoolofEngineering=['Daisy Challoner', 'Elizabeth Porter', 'Katie Corbin', 'Katie Windell', 'Morgan Gaitz', 'Ollie Mae Harrison', 'Siri Pemberton', 'Zeina Saghiyyah']
CollegeofNaturalSciences=['Andrea Yu', 'Audrey Cooper', 'Audrey Jones', 'Braeleigh Garcia', 'Buckley Turner', 'Caitlin Van Sant', 'Elizabeth Perales', 'Emmerich Benavides', 'Farrah Childs', 'Genesis Martinez', 'Hadley Amann', 'Hannah Dollinger', 'Hasita Karthikeyan', 'Izzy Davies', 'Jennifer Rosado', 'Kimia Forouzesh', 'Lauren Henderson', 'Lee Lloyd', 'Maria Sanchez', 'Megan Garza', 'Mrinali Ganta', 'Neela Juarez', 'Rishona Mopur', 'Sammi Gill', 'Sanya Hoskere', 'Sophia Labazzo', 'Sophie Coe']
MoodyCollegeofCommunication=['Abrielle Gallini', 'Annabelle Judson', 'Annie Boeh', 'Annie Hoag', 'Brooke Rosenberg', 'Brooke Waldman', "Delaney O’Brien", 'Elizabeth Scull', 'Ella Garber', 'Elyse Miller', 'Emma Levy', 'Emma Schneidau', 'Emmy Pak', 'Georgia Key', 'Giada Scaramuzza', 'Giana Toothman', 'Jazlyn Mata', 'Kate Belman', 'Kate Flanery', 'Kate Hoog', 'Katie Walsh', 'Kendall Klimek', 'Kirra Vrzal', 'Macie McKie', 'Molly Bogar', 'Parker Keston', 'Tatum Samuels', 'Victoria Olivarez', 'Zoe Westbrook']
CollegeofLiberalArts=['Addie Brooks', 'Addison Starr', 'Alexa Lira', 'Angie Andersen', 'Annie Boeh', 'Arani Walton', 'Bella Champion', 'Caroline Schulze', 'Charlie Stone', 'Dylan Kaufman', 'Ella Leininger', 'Ema Avila', 'Emma Levy', 'Hannah Reilly', 'Hazel Wells', 'Josie Daik', 'Kaelyn Liu', 'Kaitlin Black', 'Kamryn Lowery', 'Kassidy Bragg', 'Lily Robbins', 'Margot Rosenband', 'May Downey', 'Mia Cisneros', 'Paola Castillo', 'Sarah Kester', 'Sasha Pittsford', 'Skye Doughton', 'Sofia Argoti', 'Sofia Bartkoski', 'Sofie Arroyo', 'Sofie Martinez', 'Sophia Sayers', 'Taylor Jennings', 'Zoe Veliz', 'Zoey Bustamante', 'Zoe Westbrook', 'Anabel Precht']
CollegeofEducation=['Alyssa Garcia', 'Anika Novak', 'Annie Bryce', 'Ella Pitts', 'Sarah Miller', 'Taylor McIlvain', 'Elena Solano', 'Emily Bull']
CollegeofFineArts=['Amorie Erichsen', 'Ava Hodges', 'Kate Neiman', 'Katelyn Quintanilla', 'Katherine Blumenschein', 'Macie McKie', 'Marie Jolie Day', 'Natalie Juarez', 'Olivia Asay', 'Sofie Combs']
SchoolofNursing=['Caelyn Prochazka', 'Ema Avila', 'Jasmine Valdez', 'Lexie Hale', 'Maria Sepulveda', 'Ryleigh Montgomery']
JacksonSchoolofGeosciences=['Christa Hamlin', 'Jacqueline Olivier']
LBJSchoolofPublicAffairs=['Drew Shelton', 'Madeline Gottemoller']
SchoolofCivicLeadership=['Ella Dillinger', 'Katie Walsh']

# HOMETOWNS
Austin=["Taylor McIlvain", "Sarah Kester", "Mrinali Ganta", "Brooke Waldman", "Ava Hodges", "Annabelle Judson", "Sofie Combs", "Addison Starr", "Ema Avila", "Jacqueline Olivier", "Giada Scaramuzza", "Molly Bogar", "Kaitlin Black", "Amorie Erichsen", "Lily Robbins", "Charlie Stone", "Annie Bryce", "Paola Castillo"]
Dallas=["Lee Lloyd", "Hazel Wells", "Ava Dahlander", "Lexie Hale", "Sofia Bartkoski", "Delaney O'Brien", "Zoe Veliz", "Alexa Lira", "Kaelyn Liu"]
Houston=["Laraleigh Hackerman", "Neela Juarez", "Josie Daik", "Annie Hoag", "Sarah Miller", "Christa Hamlin", "Zeina Saghiyyah", "Ollie Mae Harrison", "Emma Schneidau", "Anabel Precht"]
SanAntonio=["Elyse Miller", "Elizabeth Porter", "Skye Doughton", "Kassidy Bragg", "Kate Neiman", "Kirra Vrzal"]
SugarLand_TX=["Farrah Childs", "Emma Levy", "Marie Jolie Day"]
Mansfield_TX=["Georgia Key"]
Richmond_TX=["Celeste Gutierrez", "Audrey Jones"]
Leander_TX=["Siri Pemberton", "Kamryn Lowery", "Emmerich Benavides"]
Buda_TX=["Drew Shelton"]
NewBraunfels_TX=["Ella Leininger", "Braeleigh Garcia"]
Hutto_TX=["May Downey"]
Colleyville_TX=["Anika Novak"]
Pearland_TX=["Audrey Cooper"]
Galveston_TX=["Annie Boeh"]
Keller_TX=["Lauren Henderson"]
Friendswood_TX=["Neela Juarez", "Sammi Gill"]
Cypress_TX=["Ryleigh Montgomery", "Morgan Gaitz"]
Allen_TX=["Addie Brooks", "Tatum Samuels", "Hannah Dollinger", "Daisy Challoner"]
Boerne_TX=["Ella Dillinger", "Sofie Arroyo"]
FlowerMound_TX=["Macie McKie"]
Atascocita_TX=["Zoe Westbrook"]
EaglePass_TX=["Jazlyn Mata", "Ella Pitts"]
Palestine_TX=["Sophie Coe"]
Florence_TX=["Natalie Juarez"]
CedarPark_TX=["Abrielle Gallini", "Sanya Hoskere"]
Brownsville_TX=["Mia Cisneros"]
Frisco_TX=["Caroline Schulze", "Hasita Karthikeyan"]
Humble_TX=["Megan Garza"]
Pottsboro_TX=["Buckley Turner"]
Lubbock_TX=["Bella Champion", "Katelyn Quintanilla"]
SanJuan_TX=["Sofie Martinez"]
TheWoodlands_TX=["Arani Walton", "Olivia Alvarez", "Katie Corbin"]
Paris_TX=["Kate Hoog"]
Jasper_TX=["Sophia Sayers"]
Cleburne_TX=["Angie Andersen"]
Arlington_TX=["Kimia Forouzesh"]
McKinney_TX=["Giana Toothman"]
LeagueCity_TX=["Caelyn Prochazka"]
CollegeStation_TX=["Taylor Jennings"]
Mission_TX=["Victoria Olivarez"]
Laredo_TX=["Jasmine Valdez", "Maria Sepulveda"]
Grapevine_TX=["Elena Solano"]
CarrizoSprings_TX=["Elizabeth Perales"]
Lakeway_TX=["Ella Garber"]
RoundRock_TX=["Zoey Bustamante", "Sharon Yoon"]
Lufkin_TX=["Rishona Mopur"]
SanMarcos_TX=["Elizabeth Scull"]
Richardson_TX=["Sofia Bartkoski"]
Rockwall_TX=["Katie Windell"]
FortWorth_TX=["Olivia Asay", "Kate Flanery"]
Southlake_TX=["Katherine Blumenschein"]
Denton_TX=["Izzy Davies"]
Brock_TX=["Sasha Pittsford"]
California=["Emmy Pak", "Parker Keston", "Emily Bull", "Brooke Rosenberg"]
Illinois=["Alyssa Garcia", "Natalie Yoder", "Kendall Klimek", "Hannah Belenkiy"]
Michigan=["Hadley Amann"]
Colorado=["Hannah Reilly"]
Maryland=["Sofia Argoti", "Kate Belman"]
Washington=["Caitlin Van Sant"]
NewYork=["Dylan Kaufman", "Jennifer Rosado"]
NewJersey=["Margot Rosenband", "Sophia Labazzo", "Katie Walsh"]
Virginia=["Catherine Dooley"]
Mexico=["Maria Sanchez"]
ElPaso_TX=["Andrea Yu"]
McAllen_TX=["Genesis Martinez", "Sofie Martinez"]

# UT ORGANIZATIONS
IntramuralSports=["Georgia Key", "Emmy Pak", "Drew Shelton", "Audrey Cooper", "Sarah Kester", "Lauren Henderson", "Parker Keston", "Dylan Kaufman", "Sofia Bartkoski", "Zoe Westbrook", "Sarah Miller", "Natalie Juarez", "Caroline Schulze", "Hasita Karthikeyan", "Megan Garza", "Maria Sanchez", "Bella Champion", "Daisy Challoner", "Ella Garber", "Sharon Yoon", "Annie Bryce", "Kendall Klimek", "Siri Pemberton", "Angie Andersen"]
BusinessFinanceMarketingEconomics=["Celeste Gutierrez", "Laraleigh Hackerman", "Addie Brooks", "Macie McKie", "Olivia Asay", "Natalie Yoder", "Hasita Karthikeyan", "Margot Rosenband", "Catherine Dooley", "Emma Schneidau", "Sharon Yoon", "Madison Taylor", "Haylee Martin", "Sofie Arroyo", "Kaelyn Liu", "Hannah Belenkiy", "Marie Jolie Day"]
PreHealth=["Audrey Cooper", "Lauren Henderson", "Farrah Childs", "Neela Juarez", "Josie Daik", "Caitlin Van Sant", "Sofie Martinez", "Tatum Samuels", "Caroline Schulze", "Hasita Karthikeyan", "Hannah Dollinger", "Megan Garza", "Lexie Hale", "Maria Sanchez", "Emmerich Benavides", "Genesis Martinez", "Elizabeth Porter", "Sammi Gill", "Caelyn Prochazka", "Taylor Jennings", "Jasmine Valdez", "Maria Sepulveda", "Hadley Amann", "Braeleigh Garcia", "Izzy Davies", "Sophia Labazzo", "Rishona Mopur", "Andrea Yu"]
PreLaw=["Kamryn Lowery", "Drew Shelton", "Ella Leininger", "May Downey", "Sofia Bartkoski", "Addison Starr", "Mia Cisneros", "Arani Walton", "Lily Robbins", "Margot Rosenband", "Alexa Lira", "Victoria Olivarez", "Charlie Stone", "Katie Walsh", "Anabel Precht", "Zoey Bustamante"]
Religious=["Kamryn Lowery", "Audrey Cooper", "Sarah Kester", "Annie Boeh", "Mrinali Ganta", "Farrah Childs", "Dylan Kaufman", "Ryleigh Montgomery", "Annabelle Judson", "Ella Dillinger", "Morgan Gaitz", "Ema Avila", "Christa Hamlin", "Caroline Schulze", "Hasita Karthikeyan", "Buckley Turner", "Ella Pitts",  "Kaitlin Black", "Emma Levy", "Amorie Erichsen", "Giada Scaramuzza", "Kaelyn Liu", "Annie Bryce", "Brooke Rosenberg", "Paola Castillo", "Elizabeth Scull", "Sanya Hoskere"]
STEM=["Mrinali Ganta", "Farrah Childs", "Neela Juarez", "Katie Windell", "Andrea Yu", "Sophie Coe", "Morgan Gaitz", "Zeina Saghiyyah", "Lexie Hale", "Emmerich Benavides", "Sofia Argoti", "Audrey Jones", "Kimia Forouzesh", "Elizabeth Porter", "Katie Corbin", "Ollie Mae Harrison", "Hadley Amann"]
Art=["Parker Keston", "Brooke Waldman", "Annabelle Judson", "Zoe Westbrook", "Natalie Juarez", "Margot Rosenband", "Kate Flanery", "Ella Garber", "Delaney O'Brien", "Anabel Precht", "Brooke Rosenberg", "Katie Walsh", "Kirra Vrzal"]
PerformingArtsOrg=["Ava Hodges", "Annie Hoag", "Olivia Asay", "Kaitlin Black", "Giana Toothman", "Marie Jolie Day", "Brooke Rosenberg", "Katelyn Quintanilla"]
CulturalOrg=["Celeste Gutierrez", "Natalie Juarez", "Ema Avila", "Olivia Alvarez", "Kimia Forouzesh", "Andrea Yu", "Sharon Yoon", "Kaelyn Liu", "Alexa Lira"]
GovernmentOrg=["Kamryn Lowery", "Ella Leininger", "Madeline Gottemoller", "Sofia Bartkoski",  "Sofie Combs", "Lily Robbins", "Zoey Bustamante", "Katie Walsh"]
EnvironmentalScienceOrg=["Kamryn Lowery", "Neela Juarez", "Katie Windell", "Daisy Challoner", "Elizabeth Perales"]
SocialInterestActivism=["Sofie Combs", "Sofia Argoti", "Hannah Reilly", "Olivia Alvarez", "Emily Bull", "Zoe Veliz", "Anabel Precht", "Brooke Rosenberg"]
Volunteer=["Emmy Pak", "Emily Bull", "Hazel Wells", "Ella Dillinger", "Kate Neiman"]
Publications=["Sasha Pittsford", "Kate Belman"]
AdvertisingOrg=["Elyse Miller", "Jacqueline Olivier", "Kate Hoog", "Kendall Klimek"]
SpiritOrg=["Natalie Juarez", "Elizabeth Perales"]
Student_Television=[ "Parker Keston", "Brooke Waldman", "Annabelle Judson", "Zoe Westbrook", "Natalie Juarez", "Delaney O'Brien", "Kate Flanery", "Ella Garber", "Anabel Precht", "Brooke Rosenberg" ] 
TexasWake=[ "Hadley Amann", "Sarah Miller"] 

# MUSIC ARTISTS
TaylorSwift=["Siri Pemberton", "Taylor McIlvain", "Anika Novak", "Lauren Henderson", "Dylan Kaufman", "Madeline Gottemoller", "Josie Daik", "Parker Keston", "Farrah Childs", "Addison Starr", "Macie McKie", "Sofie Martinez", "Caroline Schulze", "Lexie Hale", "Margot Rosenband", "Buckley Turner", "Emma Levy", "Kassidy Bragg", "Catherine Dooley", "Victoria Olivarez", "Braeleigh Garcia", "Katie Walsh", "Sammi Gill", "Kate Belman", "Paola Castillo"]
NoahKahan=["Georgia Key", "Anika Novak", "Lauren Henderson", "Dylan Kaufman", "Annie Boeh", "Ella Dillinger", "Annie Hoag", "Ava Dahlander", "Olivia Asay", "Hasita Karthikeyan", "Kate Hoog", "Hannah Reilly", "Emma Levy", "Skye Doughton", "Margot Rosenband", "Caelyn Prochazka", "Kimia Forouzesh", "Taylor Jennings"]
SabrinaCarpenter=["Siri Pemberton", "Taylor McIlvain", "Drew Shelton", "May Downey", "Katherine Blumenschein", "Madeline Gottemoller", "Josie Daik", "Katie Windell", "Andrea Yu", "Addie Brooks", "Annie Boeh", "Ella Pitts", "Kaitlin Black", "Buckley Turner", "Kassidy Bragg", "Braeleigh Garcia", "Charlie Stone", "Elizabeth Scull", "Katie Walsh"]
MorganWallen=["Georgia Key", "Parker Keston", "Annabelle Judson", "Caitlin Van Sant", "Hannah Dollinger", "Emily Bull", "Hannah Belenkiy", "Celeste Gutierrez"]
ZachBryan=["Emmy Pak", "Parker Keston", "Dylan Kaufman", "Natalie Yoder", "Ava Dahlander", "Margot Rosenband", "Bella Champion"]
OliviaDean=["Hazel Wells", "Annie Boeh", "Ryleigh Montgomery", "Ava Dahlander", "Audrey Jones", "Maria Sanchez", "Hannah Reilly", "Buckley Turner", "Sharon Yoon", "Madison Taylor", "Sophia Labazzo", "Ryleigh Montgomery"]
LanaDelRey=["Kamryn Lowery", "Ella Leininger", "Josie Daik", "Brooke Waldman", "Macie McKie", "Victoria Olivarez", "Hadley Amann", "Olivia Alvarez", "Katie Corbin", "Rishona Mopur"]
HarryStyles=["Audrey Cooper", "Ryleigh Montgomery", "Natalie Juarez", "Olivia Asay", "Giada Scaramuzza", "Kate Hoog", "Jennifer Rosado", "Ollie Mae Harrison", "Ella Garber", "Zoe Veliz"]
SZA=["May Downey", "Hazel Wells", "Alyssa Garcia", "Sofia Argoti", "Addison Starr", "Ema Avila", "Alexa Lira", "Elizabeth Perales", "Izzy Davies", "Annie Bryce", "Taylor Jennings", "Haylee Martin"]
Drake=["Neela Juarez", "Alyssa Garcia", "Ema Avila", "Amorie Erichsen", "Kaelyn Liu", "Maria Sepulveda", "Annie Bryce", "Paola Castillo", "Zoey Bustamante"]
BadBunny=["Andrea Yu", "Natalie Juarez", "Ema Avila", "Maria Sanchez", "Zoey Bustamante", "Jasmine Valdez", "Maria Sepulveda", "Paola Castillo"]
ArianaGrande=["Taylor McIlvain", "Drew Shelton", "Ava Hodges", "Amorie Erichsen", "Kimia Forouzesh", "Rishona Mopur", "Kate Neiman", "Jasmine Valdez"]
FleetwoodMac=["Mrinali Ganta", "Sofia Bartkoski", "Annie Hoag", "Addison Starr", "Hannah Reilly", "Elizabeth Porter", "Daisy Challoner", "Ryleigh Montgomery", "Ella Garber"]
Hozier=["Ella Leininger", "Katie Windell", "Morgan Gaitz", "Olivia Asay", "Marie Jolie Day", "Giada Scaramuzza"]
EllaLangley=["Georgia Key", "Celeste Gutierrez", "Elyse Miller", "Parker Keston", "Hasita Karthikeyan", "Abrielle Gallini", "Emmerich Benavides", "Annabelle Judson"]
GracieAbrams=["Siri Pemberton", "Annie Boeh", "Lexie Hale", "Sammi Gill", "Emma Levy", "Katie Walsh"]
TateMcRae=["May Downey", "Macie McKie", "Giada Scaramuzza", "Bella Champion", "Jazlyn Mata", "Arani Walton", "Kimia Forouzesh", "Sanya Hoskere", "Catherine Dooley"]
TheWeeknd=["Emmy Pak", "Sofia Argoti", "Sammi Gill", "Sanya Hoskere", "Kate Neiman"]
TylerChilders=["Kamryn Lowery", "Abrielle Gallini", "Emmerich Benavides", "Elizabeth Porter", "Haylee Martin"]
ZachTop=["Celeste Gutierrez", "Sasha Pittsford", "Bella Champion"]
LukeCombs=["Caitlin Van Sant", "Hannah Dollinger", "Haylee Martin"]
ChrisStapleton=["Ella Leininger", "Ryleigh Montgomery", "Emily Bull", "Audrey Cooper"]
JohnSummit=["Laraleigh Hackerman", "Natalie Juarez", "Hasita Karthikeyan", "Giana Toothman", "Elizabeth Porter", "Rishona Mopur"]
RoleModel=["Katherine Blumenschein", "Farrah Childs", "Zoë Westbrook", "Molly Bogar", "Natalie Yoder", "Kate Hoog", "Caelyn Prochazka", "Sofia Sayers"]
DonToliver=["Drew Shelton", "Neela Juarez", "Ava Hodges", "Jazlyn Mata", "Genesis Martinez", "Emmerich Benavides"]
Lorde=["Sophie Coe", "Olivia Alvarez", "Kaelyn Liu", "Katelyn Quintanilla"]
RedHotChiliPeppers=["Laraleigh Hackerman", "Marie Jolie Day"]
TheNeighborhood=["Elyse Miller", "Hadley Amann", "Arani Walton", "Kate Flanery", "Kate Neiman", "Zoe Veliz"]
TheBeatles=["Lee Lloyd", "Ella Garber", "Andrea Yu"]
OliviaRodrigo=["Kaitlin Black", "Emma Schneidau", "Sophia Labazzo", "Kassidy Bragg"]
TylerTheCreator=["Sarah Kester", "Elizabeth Perales", "Izzy Davies"]
Adele=["Kate Belman"]
BrunoMars=["Emmy Pak", "Jasmine Valdez"]
Beyonce=["Brooke Rosenberg"]
Rihanna=["Jasmine Valdez", "Brooke Rosenberg"]
TameImpala=["Sofia Argoti", "Genesis Martinez", "Sophia Sayers", "Katie Corbin", "Kendall Klimek"]
Wallows=["Christa Hamlin", "Hadley Amann", "Zoe Veliz", "Kate Flanery"]
Djo=["Sophie Coe", "Christa Hamlin", "Ella Garber", "Kate Flanery"]
Clairo=["Andrea Yu"]
FrankOcean=["Ema Avila", "Zoey Bustamante"]
ASAPRocky=["Brooke Waldman", "Ema Avila"]
MacMiller=["Alexa Lira", "Annie Bryce"]
KendrickLamar=["Sharon Yoon"]
DojaCat=["Katie Corbin", "Kendall Klimek"]
CardiB=["Alyssa Garcia"]
PlayboiCarti=["Anabel Precht"]
CharliXCX=["Mia Cisneros", "Genesis Martinez", "Anabel Precht"]
KaliUchis=["Sofia Argoti"]
Khalid=["Kaelyn Liu"]
JustinBieber=["Celeste Gutierrez", "Laraleigh Hackerman", "Ava Hodges", "Molly Bogar", "Madison Taylor", "Jasmine Valdez"]
MeganTheeStallion=["Sofie Combs"]
MeganMoroney=["Sofie Martinez", "Natalie Yoder", "Bella Champion", "Emma Schneidau", "Kirra Vrzal"]
JonPardi=["Mrinali Ganta", "Megan Garza"]
LukeBryan=["Audrey Cooper", "Sarah Kester", "Victoria Olivarez"]
FlatlandCavalry=["Audrey Cooper", "Audrey Jones", "Sofie Arroyo"]
TreatyOakRevival=["Emily Bull", "Hannah Belenkiy"]
CodyJohnson=["Caroline Schulze"]
RandyTravis=["Sasha Pittsford"]
HudsonWestbrook=["Sasha Pittsford", "Ella Pitts"]
TheEagles=["Kamryn Lowery", "Megan Garza"]
TheLumineers=["Ella Leininger", "Mrinali Ganta", "Skye Doughton", "Elena Solano"]
MtJoy=["Skye Doughton"]
LizzyMcAlpine=["Hazel Wells", "Annie Hoag", "Lexie Hale", "Charlie Stone"]
ConanGray=["Ella Dillinger", "Charlie Stone"]
Laufey=["Sofia Bartkoski", "Zeina Saghiyyah"]
CentralCee=["Sofia Bartkoski"]
GlassAnimals=["Zeina Saghiyyah"]
Paramore=["Katie Windell"]
Halsey=["Hadley Amann"]
TheBackseatLovers=["Zoe Westbrook", "Jennifer Rosado"]
TheCure=["Zoe Westbrook"]
Elvis=["Brooke Waldman"]
Oasis=["Mia Cisneros"]
MacDeMarco=["Mia Cisneros"]
RollingStones=["Mia Cisneros"]
FooFighters=["Delaney O’Brien"]
LedZeppelin=["Delaney O’Brien"]
CharleyCrockett=["Delaney O’Brien"]
TwentyOnePilots=["Kendall Klimek"]
ImagineDragons=["Angie Andersen"]
Pink=["Angie Andersen"]
LadyGaga=["Hadley Amann"]
Sublime=["Sarah Miller", "Paola Castillo"]
EttaJames=["Sarah Miller"]
NiallHoran=["Ella Pitts"]
Kanye=["Izzy Davies"]
DavidBowie=["Anabel Precht"]
GloRilla=["Elizabeth Scull"]
SiennaSpiro=["Emma Schneidau", "Elizabeth Scull"]
The1975=["Zoe Veliz"]
TyMyers=["Kirra Vrzal"]
KPop=["Sofie Combs"]
HouseMusic=["Rishona Mopur"]


# ==== MAPPING INTEREST NAME TO RECRUITER NAME LISTS ===========================================================================================================
majors = {
        "Accounting": Accounting,
        "Acting": Acting,
        "Advertising": Advertising,
        "Anthropology": Anthropology,
        "Art History": ArtHistory,
        "Arts and Entertainment Technologies": ArtsandEntertainmentTechnologies,
        "Behavioral + Social Data Science": BehavioralandSocialDataScience,
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
    "School of Nursing": SchoolofNursing,
    "Jackson School of Geosciences": JacksonSchoolofGeosciences,
    "LBJ School of Public Affairs": LBJSchoolofPublicAffairs,
    "School of Civic Leadership": SchoolofCivicLeadership,
}


hometowns = {
    "Austin": Austin,
    "Dallas": Dallas,
    "Houston": Houston,
    "San Antonio": SanAntonio,
    "Allen, TX": Allen_TX,
    "Arlington, TX": Arlington_TX,
    "Atascocita, TX": Atascocita_TX,
    "Boerne, TX": Boerne_TX,
    "Brock, TX": Brock_TX,
    "Brownsville, TX": Brownsville_TX,
    "Buda, TX": Buda_TX,
    "Carrizo Springs, TX": CarrizoSprings_TX,
    "Cedar Park, TX": CedarPark_TX,
    "Cleburne, TX": Cleburne_TX,
    "College Station, TX": CollegeStation_TX,
    "Colleyville, TX": Colleyville_TX,
    "Cypress, TX": Cypress_TX,
    "Denton, TX": Denton_TX,
    "Eagle Pass, TX": EaglePass_TX,
    "El Paso, TX": ElPaso_TX,
    "Florence, TX": Florence_TX,
    "Flower Mound, TX": FlowerMound_TX,
    "Fort Worth, TX": FortWorth_TX,
    "Frisco, TX": Frisco_TX,
    "Friendswood, TX": Friendswood_TX,
    "Galveston, TX": Galveston_TX,
    "Grapevine, TX": Grapevine_TX,
    "Humble, TX": Humble_TX,
    "Hutto, TX": Hutto_TX,
    "Jasper, TX": Jasper_TX,
    "Keller, TX": Keller_TX,
    "Lakeway, TX": Lakeway_TX,
    "League City, TX": LeagueCity_TX,
    "Leander, TX": Leander_TX,
    "Laredo, TX": Laredo_TX,
    "Lubbock, TX": Lubbock_TX,
    "Lufkin, TX": Lufkin_TX,
    "Mansfield, TX": Mansfield_TX,
    "McAllen, TX": McAllen_TX,
    "McKinney, TX": McKinney_TX,
    "Mission, TX": Mission_TX,
    "New Braunfels, TX": NewBraunfels_TX,
    "Paris, TX": Paris_TX,
    "Palestine, TX": Palestine_TX,
    "Pearland, TX": Pearland_TX,
    "Pottsboro, TX": Pottsboro_TX,
    "Richmond, TX": Richmond_TX,
    "Rockwall, TX": Rockwall_TX,
    "Round Rock, TX": RoundRock_TX,
    "San Juan, TX": SanJuan_TX,
    "San Marcos, TX": SanMarcos_TX,
    "Southlake, TX": Southlake_TX,
    "Sugar Land, TX": SugarLand_TX,
    "The Woodlands, TX": TheWoodlands_TX,
    "California": California,
    "Colorado": Colorado,
    "Illinois": Illinois,
    "Maryland": Maryland,
    "Michigan": Michigan,
    "Mexico": Mexico,
    "New Jersey": NewJersey,
    "New York": NewYork,
    "Virginia": Virginia,
    "Washington": Washington
}

utorgs = {
    "Intramural Sports": IntramuralSports,
    "Business/Finance/Marketing/Economics": BusinessFinanceMarketingEconomics,
    "Pre Health": PreHealth,
    "Pre Law": PreLaw,
    "Religious": Religious,
    "STEM": STEM,
    "Art": Art,
    "Performing Arts Org": PerformingArtsOrg,
    "Cultural Org": CulturalOrg,
    "Government Org": GovernmentOrg,
    "Environmental Science Org": EnvironmentalScienceOrg,
    "Social Interest/Activism": SocialInterestActivism,
    "Volunteer": Volunteer,
    "Publications": Publications,
    "Advertising Org": AdvertisingOrg,
    "Spirit Organization": SpiritOrg,
    "Student Television (TSTV/KVRX)": Student_Television,
    "Texas Wake": TexasWake
}

# MUSIC ARTISTS

music = {
    "Taylor Swift": TaylorSwift,
    "Noah Kahan": NoahKahan,
    "Sabrina Carpenter": SabrinaCarpenter,
    "Morgan Wallen": MorganWallen,
    "Ella Langley": EllaLangley,
    "Zach Bryan": ZachBryan,
    "Fleetwood Mac": FleetwoodMac,
    "Hozier": Hozier,
    "Gracie Abrams": GracieAbrams,
    "Tate McRae": TateMcRae,
    "The Weeknd": TheWeeknd,
    "Tyler Childers": TylerChilders,
    "Zach Top": ZachTop,
    "Luke Combs": LukeCombs,
    "Chris Stapleton": ChrisStapleton,
    "John Summit": JohnSummit,
    "Role Model": RoleModel,
    "Don Toliver": DonToliver,
    "Lorde": Lorde,
    "Ariana Grande": ArianaGrande,
    "Red Hot Chili Peppers": RedHotChiliPeppers,
    "The Neighborhood": TheNeighborhood,
    "The Beatles": TheBeatles,
    "Olivia Rodrigo": OliviaRodrigo,
    "Tyler the Creator": TylerTheCreator,
    "Adele": Adele,
    "Bruno Mars": BrunoMars,
    "Beyoncé": Beyonce,
    "Rihanna": Rihanna,
    "Tame Impala": TameImpala,
    "Wallows": Wallows,
    "Djo": Djo,
    "Clairo": Clairo,
    "Frank Ocean": FrankOcean,
    "ASAP Rocky": ASAPRocky,
    "Mac Miller": MacMiller,
    "Kendrick Lamar": KendrickLamar,
    "Doja Cat": DojaCat,
    "Cardi B": CardiB,
    "Playboi Carti": PlayboiCarti,
    "Charli XCX": CharliXCX,
    "Kali Uchis": KaliUchis,
    "Khalid": Khalid,
    "Justin Bieber": JustinBieber,
    "Megan Thee Stallion": MeganTheeStallion,
    "Megan Moroney": MeganMoroney,
    "Jon Pardi": JonPardi,
    "Luke Bryan": LukeBryan,
    "Flatland Cavalry": FlatlandCavalry,
    "Treaty Oak Revival": TreatyOakRevival,
    "Cody Johnson": CodyJohnson,
    "Randy Travis": RandyTravis,
    "Hudson Westbrook": HudsonWestbrook,
    "The Eagles": TheEagles,
    "The Lumineers": TheLumineers,
    "Mt. Joy": MtJoy,
    "Lizzy McAlpine": LizzyMcAlpine,
    "Conan Gray": ConanGray,
    "Laufey": Laufey,
    "Central Cee": CentralCee,
    "Glass Animals": GlassAnimals,
    "Paramore": Paramore,
    "Halsey": Halsey,
    "The Backseat Lovers": TheBackseatLovers,
    "The Cure": TheCure,
    "Elvis": Elvis,
    "Oasis": Oasis,
    "Mac DeMarco": MacDeMarco,
    "Rolling Stones": RollingStones,
    "Foo Fighters": FooFighters,
    "Led Zeppelin": LedZeppelin,
    "Charley Crockett": CharleyCrockett,
    "Twenty One Pilots": TwentyOnePilots,
    "Imagine Dragons": ImagineDragons,
    "P!nk": Pink,
    "Lady Gaga": LadyGaga,
    "Sublime": Sublime,
    "Etta James": EttaJames,
    "Niall Horan": NiallHoran,
    "Kanye": Kanye,
    "David Bowie": DavidBowie,
    "GloRilla": GloRilla,
    "Sienna Spiro": SiennaSpiro,
    "The 1975": The1975,
    "Ty Myers": TyMyers,
    "K-Pop": KPop,
    "House Music": HouseMusic
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
selected_colleges = checkbox_columns("College/Track"+"\U0001FA7A", list(colleges.keys()), num_cols=4)
selected_hometowns = checkbox_columns("Hometowns"+"\U0001F3E0", list(hometowns.keys()), num_cols=4)
selected_music = checkbox_columns("Music"+"\U0001F3EB", list(music.keys()), num_cols=4)
#selected_extras = checkbox_columns("HS Extracurriculars"+"\U0001F483", list(extras.keys()), num_cols=4)
selected_orgs = checkbox_columns("UT Organizations"+"\U0000266B", list(utorgs.keys()), num_cols=4)
#selected_activities = checkbox_columns("Activities/Interests for Fun"+"\U0001F3C3", list(activities.keys()), num_cols=4)
#selected_summercamps = checkbox_columns("Summer Camp"+"\U0001F525", list(summercamps.keys()), num_cols=4)
#selected_nicheinterests = checkbox_columns("Niche Interests"+"\U0001F388", list(nicheinterests.keys()), num_cols=4)
#selected_transfers = checkbox_columns("Transfer Students"+"\U0001F501", list(transfers.keys()), num_cols=4)

selected_interests = selected_majors + selected_minors + selected_colleges + selected_hometowns + selected_orgs + selected_music #+ selected_schools + selected_extras + selected_orgs + selected_activities + selected_summercamps + selected_nicheinterests + selected_transfers

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
        elif interest in colleges:
            names = colleges[interest]
        elif interest in hometowns:
            names = hometowns[interest]
        elif interest in utorgs:
            names = utorgs[interest]
        elif interest in music:
            names = music[interest]
        #elif interest in extras:
         #   names = extras[interest]
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
    blue_names = ['Lee Lloyd', 'Abrielle Gallini', 'Addie Brooks',
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
       'Ema Avila', 'Emmy Pak', 'Emily Bull', 'Emma Levy',
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
