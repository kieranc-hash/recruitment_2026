import streamlit as st
import math

# ===== DATA====================================================================================================================================================
# MAJORS
Accounting=['Catherine Dooley', 'Celeste  Gutierrez', 'Madison Taylor']
Acting=["Abby Joe", 'Katelyn Quintanilla', 'Katherine Blumenschein']
Advertising=['Abrielle Gallini', 'Annabelle Judson', 'Elyse Miller', 'Emmy Pak', 'Jazlyn Mata', 'Kate Hoog', 'Kendall Klimek', 'Macie McKie']
Anthropology=['Zoe Veliz']
ArtHistory=['Sofie Combs']
ArtsandEntertainmentTechnologies=['Andrea Yu']
BehavioralandSocialDataScience = ['Paola Castillo']
Biochemistry=['Mrinali Ganta']
Biology=['Lee Lloyd', 'Audrey Cooper', 'Audrey Jones', 'Buckley Turner', 'Emmerich Benavides', 'Farrah Childs', 'Genesis Martinez', 'Izzy Davies', 'Megan Garza', 'Neela Juarez', 'Rishona Mopur', 'Sammi Gill', 'Sanya Hoskere']
BiomedicalEngineering=['Elizabeth Porter']
Business=["Cailyn Kelsen", 'Hannah Belenkiy', 'Haylee Martin', 'Marie Jolie Day', 'Natalie Yoder', 'Olivia Alvarez', 'Sharon Yoon']
CanfieldBusinessHonors=['Hannah Belenkiy', 'Natalie Yoder', 'Olivia Alvarez']
ChemicalEngineering=['Katie Corbin']
CivicsHonors=['Ella Dillinger', 'Katie Walsh']
CommunicationandLeadership=['Annie Hoag', 'Brooke Waldman', "Delaney O'Brien", 'Emma Schneidau', 'Giada Scaramuzza', 'Jazlyn Mata']
ComputationalEngineering=['Morgan Gaitz', 'Siri Pemberton']
ComputerScience=['Kimia Forouzesh']
Dance=['Amorie Erichsen', 'Ava Hodges', 'Marie Jolie Day', 'Olivia Asay']
EarlyChildhoodEducation=['Anika Novak', 'Ella Pitts', 'Emily Bull']
Economics=["Mackenzie Short", 'Addie Brooks', 'Dylan Kaufman', 'Kaelyn Liu', 'Sofie Arroyo']
ElementaryEducation=['Elena Solano']
English=['Kaitlin Black', 'Sasha Pittsford']
EnvironmentalEngineering=['Daisy Challoner', 'Katie Windell']
EnvironmentalScience=['Elizabeth Perales']
Finance=['Hannah Belenkiy', 'Laraleigh Hackerman', 'Madison Taylor', 'Natalie Yoder']
Geography=['Skye Doughton']
Geology=['Christa Hamlin']
Geoscience=['Jacqueline Olivier']
GlobalStudies=['Addison Starr']
Government=["Cate Colman", 'Anabel Precht', 'Annie Boeh', 'Arani Walton', 'Charlie Stone', 'Hannah Reilly', 'Lily Robbins', 'May Downey', 'Mia Cisneros', 'Sofia Bartkoski', 'Zoe Westbrook', 'Zoey Bustamante']
GraphicDesign=['Natalie Juarez']
HealthandSociety=['Bella Champion', 'Ema Avila', 'Emma Levy', 'Hazel Wells', 'Sofie Martinez']
HealthPromotion=["Claire Savage"]
InternationalRelations=['Addison Starr', 'Sarah Kester', 'Sofia Bartkoski']
Journalism=['Annie Boeh', 'Brooke Rosenberg', 'Katie Walsh', 'Parker Keston', 'Zoe Westbrook']
Kinesiology=["Kamryn Jean", "Brynn Groves", 'Alyssa Garcia', 'Ava Hodges', 'Sarah Miller', 'Taylor McIlvain']
LiberalArtsHonors=['Charlie Stone']
Marketing=['Ava Dahlander']
Mathematics=['Jennifer Rosado', 'Kimia Forouzesh']
MechanicalEngineering=['Ollie Mae Harrison', 'Zeina Saghiyyah']
Neuroscience=['Braeleigh Garcia', 'Caitlin Van Sant', 'Hadley Amann', 'Hannah Dollinger', 'Hasita Karthikeyan', 'Lauren Henderson']
Nursing=["Gaby Green", 'Caelyn Prochazka', 'Ema Avila', 'Hadley Amann', 'Jasmine Valdez', 'Lexie Hale', 'Maria Sepulveda', 'Ryleigh Montgomery']
Nutrition=['Andrea Yu', 'Maria Sanchez', 'Sophie Coe']
PhysicalCultureandSports=['Annie Bryce']
PlanIIHonors=['Ella Dillinger']
PoliticalCommunications=['Victoria Olivarez']
Psychology=["Sarah Preston", 'Alexa Lira', 'Caroline Schulze', 'Ella Leininger', 'Josie Daik', 'Kassidy Bragg', 'Kate Neiman', 'Margot Rosenband', 'Sofia Argoti', 'Sophia Sayers', 'Taylor Jennings']
PublicAffairs=["Sadie Spagnoli", "Emma Woods", 'Drew Shelton', 'Madeline Gottemoller']
PublicHealth=['Sophia Labazzo']
PublicRelations=["Sophie Robins", 'Georgia Key', 'Kate Belman']
RTF=['Annabelle Judson', 'Brooke Rosenberg', 'Ella Garber', 'Kate Flanery']
Sociology=['Angie Andersen', 'Hannah Reilly']
SpeechLanguageandHearingSciences=['Emma Levy', 'Giana Toothman', 'Molly Bogar', 'Tatum Samuels']
SustainabilityStudies=['Kamryn Lowery']
Theatre=['Marie Jolie Day']

# MINORS
AdvertisingMinor=['Olivia Asay']
AmericanSignLanguageMinor=['Molly Bogar']
ArabicMinor=["Emma Woods"]
ArtsManagementandAdministrationMinor=['Sofie Combs']
BusinessAdministrationMinor=['Sophia Sayers']
BusinessMinor=["Brynn Groves", "Abby Joe", 'Abrielle Gallini', 'Annie Hoag', 'Dylan Kaufman', 'Elyse Miller', 'Emma Schneidau', 'Farrah Childs', 'Georgia Key', 'Hannah Dollinger', 'Kaelyn Liu', 'Kaitlin Black', 'Kate Belman', 'Kate Hoog', 'Katelyn Quintanilla', 'Katherine Blumenschein', 'Katie Corbin', 'Kendall Klimek', 'Natalie Juarez', 'Natalie Yoder', 'Sofie Arroyo']
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
FrenchMinor=["Abby Joe", 'Anabel Precht']
GermanMinor=['Jennifer Rosado']
GlobalSustainabilityLeadershipMinor=["Delaney O'Brien"]
HealthCommunicationsMinor=['Caitlin Van Sant', 'Kate Neiman', 'Sofie Martinez']
HealthcareReformandInnovationMinor=["Gaby Green", 'Hasita Karthikeyan', 'Megan Garza', 'Neela Juarez', 'Sophia Labazzo']
HistoryMinor=['Mia Cisneros']
JeffersonScholarsProgramMinor=['Katie Windell', 'Siri Pemberton']
JournalismMinor=['Sasha Pittsford']
KinesiologyMinor=['Angie Andersen', 'Buckley Turner', 'Caroline Schulze', 'Genesis Martinez']
LawJusticeandSocietyMinor=['Drew Shelton', 'Jazlyn Mata', 'Lily Robbins', 'Madeline Gottemoller']
LawPolicyandEqualityMinor=['Alexa Lira']
MarketingMinor=['Haylee Martin']
MediaandEntertainmentIndustriesMinor=["Abby Joe", 'Katelyn Quintanilla']
MedicalFitnessRehabMinor=['Sarah Miller']
MedicalSpanishMinor=['Giana Toothman', 'Lauren Henderson']
PatientsPractitionersandtheCulturesofCareMinor=['Jasmine Valdez']
PhilosophyMinor=['Anabel Precht']
PreHealthProfessionsMinor=["Kamryn Jean", "Claire Savage", 'Andrea Yu', 'Audrey Cooper', 'Bella Champion', 'Braeleigh Garcia', 'Buckley Turner', 'Farrah Childs', 'Hazel Wells', 'Izzy Davies', 'Lauren Henderson', 'Rishona Mopur', 'Sophie Coe']
PreMedMinor=["Kamryn Jean", 'Lee Lloyd', 'Buckley Turner', 'Hannah Dollinger']
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
McCombsSchoolofBusiness=["Cailyn Kelsen", 'Ava Dahlander', 'Catherine Dooley', 'Celeste Gutierrez', 'Hannah Belenkiy', 'Haylee Martin', 'Kate Belman', 'Katie Corbin', 'Kendall Klimek', 'Laraleigh Hackerman', 'Madison Taylor', 'Marie Jolie Day', 'Natalie Yoder', 'Olivia Alvarez', 'Sharon Yoon']
CockrellSchoolofEngineering=['Daisy Challoner', 'Elizabeth Porter', 'Katie Corbin', 'Katie Windell', 'Morgan Gaitz', 'Ollie Mae Harrison', 'Siri Pemberton', 'Zeina Saghiyyah']
CollegeofNaturalSciences=['Andrea Yu', 'Audrey Cooper', 'Audrey Jones', 'Braeleigh Garcia', 'Buckley Turner', 'Caitlin Van Sant', 'Elizabeth Perales', 'Emmerich Benavides', 'Farrah Childs', 'Genesis Martinez', 'Hadley Amann', 'Hannah Dollinger', 'Hasita Karthikeyan', 'Izzy Davies', 'Jennifer Rosado', 'Kimia Forouzesh', 'Lauren Henderson', 'Lee Lloyd', 'Maria Sanchez', 'Megan Garza', 'Mrinali Ganta', 'Neela Juarez', 'Rishona Mopur', 'Sammi Gill', 'Sanya Hoskere', 'Sophia Labazzo', 'Sophie Coe']
MoodyCollegeofCommunication=["Sophie Robins", 'Abrielle Gallini', 'Annabelle Judson', 'Annie Boeh', 'Annie Hoag', 'Brooke Rosenberg', 'Brooke Waldman', "Delaney O’Brien", 'Elizabeth Scull', 'Ella Garber', 'Elyse Miller', 'Emma Levy', 'Emma Schneidau', 'Emmy Pak', 'Georgia Key', 'Giada Scaramuzza', 'Giana Toothman', 'Jazlyn Mata', 'Kate Belman', 'Kate Flanery', 'Kate Hoog', 'Katie Walsh', 'Kendall Klimek', 'Kirra Vrzal', 'Macie McKie', 'Molly Bogar', 'Parker Keston', 'Tatum Samuels', 'Victoria Olivarez', 'Zoe Westbrook']
CollegeofLiberalArts=["Sarah Preston", "Mackenzie Short", "Cate Colman", 'Addie Brooks', 'Addison Starr', 'Alexa Lira', 'Angie Andersen', 'Annie Boeh', 'Arani Walton', 'Bella Champion', 'Caroline Schulze', 'Charlie Stone', 'Dylan Kaufman', 'Ella Leininger', 'Ema Avila', 'Emma Levy', 'Hannah Reilly', 'Hazel Wells', 'Josie Daik', 'Kaelyn Liu', 'Kaitlin Black', 'Kamryn Lowery', 'Kassidy Bragg', 'Lily Robbins', 'Margot Rosenband', 'May Downey', 'Mia Cisneros', 'Paola Castillo', 'Sarah Kester', 'Sasha Pittsford', 'Skye Doughton', 'Sofia Argoti', 'Sofia Bartkoski', 'Sofie Arroyo', 'Sofie Martinez', 'Sophia Sayers', 'Taylor Jennings', 'Zoe Veliz', 'Zoey Bustamante', 'Zoe Westbrook', 'Anabel Precht']
CollegeofEducation=["Kamryn Jean", "Claire Savage", "Brynn Groves", 'Alyssa Garcia', 'Anika Novak', 'Annie Bryce', 'Ella Pitts', 'Sarah Miller', 'Taylor McIlvain', 'Elena Solano', 'Emily Bull']
CollegeofFineArts=["Abby Joe", 'Amorie Erichsen', 'Ava Hodges', 'Kate Neiman', 'Katelyn Quintanilla', 'Katherine Blumenschein', 'Macie McKie', 'Marie Jolie Day', 'Natalie Juarez', 'Olivia Asay', 'Sofie Combs']
SchoolofNursing=["Gaby Green", 'Caelyn Prochazka', 'Ema Avila', 'Jasmine Valdez', 'Lexie Hale', 'Maria Sepulveda', 'Ryleigh Montgomery']
JacksonSchoolofGeosciences=['Christa Hamlin', 'Jacqueline Olivier']
LBJSchoolofPublicAffairs=["Sadie Spagnoli", "Emma Woods", 'Drew Shelton', 'Madeline Gottemoller']
SchoolofCivicLeadership=['Ella Dillinger', 'Katie Walsh']

# HOMETOWNS
Austin=["Mackenzie Short", "Taylor McIlvain", "Sarah Kester", "Mrinali Ganta", "Brooke Waldman", "Ava Hodges", "Annabelle Judson", "Sofie Combs", "Addison Starr", "Ema Avila", "Jacqueline Olivier", "Giada Scaramuzza", "Molly Bogar", "Kaitlin Black", "Amorie Erichsen", "Lily Robbins", "Charlie Stone", "Annie Bryce", "Paola Castillo"]
Dallas=["Claire Savage", "Gaby Green", "Lee Lloyd", "Hazel Wells", "Ava Dahlander", "Lexie Hale", "Sofia Bartkoski", "Delaney O'Brien", "Zoe Veliz", "Alexa Lira", "Kaelyn Liu"]
Houston=["Sophie Robins", "Sarah Preston", "Emma Woods", "Laraleigh Hackerman", "Neela Juarez", "Josie Daik", "Annie Hoag", "Sarah Miller", "Christa Hamlin", "Zeina Saghiyyah", "Ollie Mae Harrison", "Emma Schneidau", "Anabel Precht"]
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
McKinney_TX=["Brynn Groves", "Giana Toothman"]
LeagueCity_TX=["Sophie Robins", "Caelyn Prochazka"]
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
Illinois=["Cailyn Kelsen", "Alyssa Garcia", "Natalie Yoder", "Kendall Klimek", "Hannah Belenkiy"]
Michigan=["Hadley Amann"]
Colorado=["Hannah Reilly"]
Maryland=["Sofia Argoti", "Kate Belman"]
Washington=["Caitlin Van Sant"]
NewYork=["Sadie Spagnoli", "Dylan Kaufman", "Jennifer Rosado"]
NewJersey=["Margot Rosenband", "Sophia Labazzo", "Katie Walsh"]
Virginia=["Catherine Dooley"]
Mexico=["Maria Sanchez"]
ElPaso_TX=["Andrea Yu"]
McAllen_TX=["Genesis Martinez", "Sofie Martinez"]
WashingtonDC=["Abby Joe"]

# UT ORGANIZATIONS
IntramuralSports=["Sophie Robins", "Brynn Groves", "Emma Woods", "Georgia Key", "Emmy Pak", "Drew Shelton", "Audrey Cooper", "Sarah Kester", "Lauren Henderson", "Parker Keston", "Dylan Kaufman", "Sofia Bartkoski", "Zoe Westbrook", "Sarah Miller", "Natalie Juarez", "Caroline Schulze", "Hasita Karthikeyan", "Megan Garza", "Maria Sanchez", "Bella Champion", "Daisy Challoner", "Ella Garber", "Sharon Yoon", "Annie Bryce", "Kendall Klimek", "Siri Pemberton", "Angie Andersen"]
BusinessFinanceMarketingEconomics=["Sadie Spagnoli", "Celeste Gutierrez", "Laraleigh Hackerman", "Addie Brooks", "Macie McKie", "Olivia Asay", "Natalie Yoder", "Hasita Karthikeyan", "Margot Rosenband", "Catherine Dooley", "Emma Schneidau", "Sharon Yoon", "Madison Taylor", "Haylee Martin", "Sofie Arroyo", "Kaelyn Liu", "Hannah Belenkiy", "Marie Jolie Day"]
PreHealth=["Kamryn Jean", "Claire Savage", "Cailyn Kelsen", "Brynn Groves", "Audrey Cooper", "Lauren Henderson", "Farrah Childs", "Neela Juarez", "Josie Daik", "Caitlin Van Sant", "Sofie Martinez", "Tatum Samuels", "Caroline Schulze", "Hasita Karthikeyan", "Hannah Dollinger", "Megan Garza", "Lexie Hale", "Maria Sanchez", "Emmerich Benavides", "Genesis Martinez", "Elizabeth Porter", "Sammi Gill", "Caelyn Prochazka", "Taylor Jennings", "Jasmine Valdez", "Maria Sepulveda", "Hadley Amann", "Braeleigh Garcia", "Izzy Davies", "Sophia Labazzo", "Rishona Mopur", "Andrea Yu"]
PreLaw=["Sarah Preston", "Emma Woods", "Kamryn Lowery", "Drew Shelton", "Ella Leininger", "May Downey", "Sofia Bartkoski", "Addison Starr", "Mia Cisneros", "Arani Walton", "Lily Robbins", "Margot Rosenband", "Alexa Lira", "Victoria Olivarez", "Charlie Stone", "Katie Walsh", "Anabel Precht", "Zoey Bustamante"]
ReligiousOrg=["Brynn Groves", "Cate Colman", "Emma Woods", "Abby Joe", "Kamryn Lowery", "Audrey Cooper", "Sarah Kester", "Annie Boeh", "Mrinali Ganta", "Farrah Childs", "Dylan Kaufman", "Ryleigh Montgomery", "Annabelle Judson", "Ella Dillinger", "Morgan Gaitz", "Ema Avila", "Christa Hamlin", "Caroline Schulze", "Hasita Karthikeyan", "Buckley Turner", "Ella Pitts",  "Kaitlin Black", "Emma Levy", "Amorie Erichsen", "Giada Scaramuzza", "Kaelyn Liu", "Annie Bryce", "Brooke Rosenberg", "Paola Castillo", "Elizabeth Scull", "Sanya Hoskere"]
STEM=["Cailyn Kelsen", "Gaby Green", "Mrinali Ganta", "Farrah Childs", "Neela Juarez", "Katie Windell", "Andrea Yu", "Sophie Coe", "Morgan Gaitz", "Zeina Saghiyyah", "Lexie Hale", "Emmerich Benavides", "Sofia Argoti", "Audrey Jones", "Kimia Forouzesh", "Elizabeth Porter", "Katie Corbin", "Ollie Mae Harrison", "Hadley Amann"]
ArtOrg=["Parker Keston", "Brooke Waldman", "Annabelle Judson", "Zoe Westbrook", "Natalie Juarez", "Margot Rosenband", "Kate Flanery", "Ella Garber", "Delaney O'Brien", "Anabel Precht", "Brooke Rosenberg", "Katie Walsh", "Kirra Vrzal"]
PerformingArtsOrg=["Sophie Robins", "Claire Savage", "Abby Joe", "Ava Hodges", "Annie Hoag", "Olivia Asay", "Kaitlin Black", "Giana Toothman", "Marie Jolie Day", "Brooke Rosenberg", "Katelyn Quintanilla"]
CulturalOrg=["Gaby Green", "Celeste Gutierrez", "Natalie Juarez", "Ema Avila", "Olivia Alvarez", "Kimia Forouzesh", "Andrea Yu", "Sharon Yoon", "Kaelyn Liu", "Alexa Lira"]
GovernmentOrg=["Kamryn Lowery", "Ella Leininger", "Madeline Gottemoller", "Sofia Bartkoski",  "Sofie Combs", "Lily Robbins", "Zoey Bustamante", "Katie Walsh"]
EnvironmentalScienceOrg=["Kamryn Lowery", "Neela Juarez", "Katie Windell", "Daisy Challoner", "Elizabeth Perales"]
SocialInterestActivism=["Emma Woods", "Sofie Combs", "Sofia Argoti", "Hannah Reilly", "Olivia Alvarez", "Emily Bull", "Zoe Veliz", "Anabel Precht", "Brooke Rosenberg"]
Volunteer=["Emmy Pak", "Emily Bull", "Hazel Wells", "Ella Dillinger", "Kate Neiman"]
Publications=["Sasha Pittsford", "Kate Belman"]
AdvertisingOrg=["Elyse Miller", "Jacqueline Olivier", "Kate Hoog", "Kendall Klimek"]
SpiritOrg=["Natalie Juarez", "Elizabeth Perales"]
Student_Television=[ "Parker Keston", "Brooke Waldman", "Annabelle Judson", "Zoe Westbrook", "Natalie Juarez", "Delaney O'Brien", "Kate Flanery", "Ella Garber", "Anabel Precht", "Brooke Rosenberg" ] 
TexasWake=[ "Hadley Amann", "Sarah Miller"] 

# MUSIC ARTISTS
TaylorSwift=["Brynn Groves", "Siri Pemberton", "Taylor McIlvain", "Anika Novak", "Lauren Henderson", "Dylan Kaufman", "Madeline Gottemoller", "Josie Daik", "Parker Keston", "Farrah Childs", "Addison Starr", "Macie McKie", "Sofie Martinez", "Caroline Schulze", "Lexie Hale", "Margot Rosenband", "Buckley Turner", "Emma Levy", "Kassidy Bragg", "Catherine Dooley", "Victoria Olivarez", "Braeleigh Garcia", "Katie Walsh", "Sammi Gill", "Kate Belman", "Paola Castillo"]
NoahKahan=["Cate Colman", "Georgia Key", "Anika Novak", "Lauren Henderson", "Dylan Kaufman", "Annie Boeh", "Ella Dillinger", "Annie Hoag", "Ava Dahlander", "Olivia Asay", "Hasita Karthikeyan", "Kate Hoog", "Hannah Reilly", "Emma Levy", "Skye Doughton", "Margot Rosenband", "Caelyn Prochazka", "Kimia Forouzesh", "Taylor Jennings"]
SabrinaCarpenter=["Claire Savage", "Brynn Groves", "Siri Pemberton", "Taylor McIlvain", "Drew Shelton", "May Downey", "Katherine Blumenschein", "Madeline Gottemoller", "Josie Daik", "Katie Windell", "Andrea Yu", "Addie Brooks", "Annie Boeh", "Ella Pitts", "Kaitlin Black", "Buckley Turner", "Kassidy Bragg", "Braeleigh Garcia", "Charlie Stone", "Elizabeth Scull", "Katie Walsh"]
MorganWallen=["Sarah Preston", "Gaby Green", "Georgia Key", "Parker Keston", "Annabelle Judson", "Caitlin Van Sant", "Hannah Dollinger", "Emily Bull", "Hannah Belenkiy", "Celeste Gutierrez"]
ZachBryan=["Gaby Green", "Emmy Pak", "Parker Keston", "Dylan Kaufman", "Natalie Yoder", "Ava Dahlander", "Margot Rosenband", "Bella Champion"]
OliviaDean=["Claire Savage", "Cailyn Kelsen", "Hazel Wells", "Annie Boeh", "Ryleigh Montgomery", "Ava Dahlander", "Audrey Jones", "Maria Sanchez", "Hannah Reilly", "Buckley Turner", "Sharon Yoon", "Madison Taylor", "Sophia Labazzo", "Ryleigh Montgomery"]
LanaDelRey=["Sophie Robins", "Kamryn Lowery", "Ella Leininger", "Josie Daik", "Brooke Waldman", "Macie McKie", "Victoria Olivarez", "Hadley Amann", "Olivia Alvarez", "Katie Corbin", "Rishona Mopur"]
HarryStyles=["Audrey Cooper", "Ryleigh Montgomery", "Natalie Juarez", "Olivia Asay", "Giada Scaramuzza", "Kate Hoog", "Jennifer Rosado", "Ollie Mae Harrison", "Ella Garber", "Zoe Veliz"]
SZA=["May Downey", "Hazel Wells", "Alyssa Garcia", "Sofia Argoti", "Addison Starr", "Ema Avila", "Alexa Lira", "Elizabeth Perales", "Izzy Davies", "Annie Bryce", "Taylor Jennings", "Haylee Martin"]
Drake=["Sadie Spagnoli", "Mackenzie Short", "Neela Juarez", "Alyssa Garcia", "Ema Avila", "Amorie Erichsen", "Kaelyn Liu", "Maria Sepulveda", "Annie Bryce", "Paola Castillo", "Zoey Bustamante"]
BadBunny=["Andrea Yu", "Natalie Juarez", "Ema Avila", "Maria Sanchez", "Zoey Bustamante", "Jasmine Valdez", "Maria Sepulveda", "Paola Castillo"]
ArianaGrande=["Taylor McIlvain", "Drew Shelton", "Ava Hodges", "Amorie Erichsen", "Kimia Forouzesh", "Rishona Mopur", "Kate Neiman", "Jasmine Valdez"]
FleetwoodMac=["Mrinali Ganta", "Sofia Bartkoski", "Annie Hoag", "Addison Starr", "Hannah Reilly", "Elizabeth Porter", "Daisy Challoner", "Ryleigh Montgomery", "Ella Garber"]
Hozier=["Cate Colman", "Ella Leininger", "Katie Windell", "Morgan Gaitz", "Olivia Asay", "Marie Jolie Day", "Giada Scaramuzza"]
EllaLangley=["Cailyn Kelsen", "Emma Woods", "Georgia Key", "Celeste Gutierrez", "Elyse Miller", "Parker Keston", "Hasita Karthikeyan", "Abrielle Gallini", "Emmerich Benavides", "Annabelle Judson"]
GracieAbrams=["Siri Pemberton", "Annie Boeh", "Lexie Hale", "Sammi Gill", "Emma Levy", "Katie Walsh"]
TateMcRae=["May Downey", "Macie McKie", "Giada Scaramuzza", "Bella Champion", "Jazlyn Mata", "Arani Walton", "Kimia Forouzesh", "Sanya Hoskere", "Catherine Dooley"]
TheWeeknd=["Emmy Pak", "Sofia Argoti", "Sammi Gill", "Sanya Hoskere", "Kate Neiman"]
TylerChilders=["Gaby Green", "Kamryn Lowery", "Abrielle Gallini", "Emmerich Benavides", "Elizabeth Porter", "Haylee Martin"]
ZachTop=["Celeste Gutierrez", "Sasha Pittsford", "Bella Champion"]
LukeCombs=["Gaby Green", "Caitlin Van Sant", "Hannah Dollinger", "Haylee Martin"]
ChrisStapleton=["Cailyn Kelsen", "Gaby Green", "Ella Leininger", "Ryleigh Montgomery", "Emily Bull", "Audrey Cooper"]
JohnSummit=["Laraleigh Hackerman", "Natalie Juarez", "Hasita Karthikeyan", "Giana Toothman", "Elizabeth Porter", "Rishona Mopur"]
RoleModel=["Kamryn Jean", "Katherine Blumenschein", "Farrah Childs", "Zoë Westbrook", "Molly Bogar", "Natalie Yoder", "Kate Hoog", "Caelyn Prochazka", "Sofia Sayers"]
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
HudsonWestbrook=["Emma Woods", "Sasha Pittsford", "Ella Pitts"]
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
SiennaSpiro=["Kamryn Jean", "Emma Schneidau", "Elizabeth Scull"]
The1975=["Zoe Veliz"]
TyMyers=["Kirra Vrzal"]
KPop=["Sofie Combs"]
HouseMusic=["Sophie Robins", "Rishona Mopur"]

# SUMMER CAMPS
ACULeadershipCamps=['Kamryn Lowery']
AreaHealthEducationCenterAHECCamp=['Maria Sepulveda']
CampAgawak=['Brooke Rosenberg']
CampAllen=['Annie Boeh', 'Ema Avila', 'Taylor McIlvain']
CampBelovedandBeyond=['Kamryn Lowery']
CampChoYeh=['Audrey Cooper']
CampDeerRun=['Kate Hoog']
CampLaurelwood=['Margot Rosenband']
CampLonestar=['Drew Shelton']
CampLonghorn=['Addison Starr', 'Annabelle Judson', 'Annie Hoag', 'Madeline Gottemoller', 'Molly Bogar', 'Rishona Mopur', 'Sofie Combs']
CampLonghornIndianSprings=['Sofie Combs', 'Zeina Saghiyyah']
CampLonghornInksLake=['Annabelle Judson']
CampMystic=['Josie Daik']
CampOlympia=['Sarah Miller']
CampOzark=['Ella Garber']
CampPineSprings=['Kamryn Lowery']
CampRamah=['Brooke Rosenberg']
CampTexas=['Natalie Juarez', 'Zoe Westbrook']
CampThurman=['Olivia Asay']
CampWaldemar=['Annabelle Judson']
CatalinaIslandCamps=['Parker Keston']
ChurchCamp=['Rishona Mopur']
Fifthgradecamp=['Caitlin Van Sant']
GeoFORCETexasSummerAcademies=['Jacqueline Olivier']
IgniteTexas=['Annabelle Judson']
Kickapoo=['Sarah Kester']
LaityLodgeYouthCamp=['Annie Bryce']
MissionTrips=['Caroline Schulze']
NASASummerProgram=['Olivia Alvarez']
NationalCheerleadingAssociationCamp=['Morgan Gaitz']
NationalHispanicInstituteCollegeWorldSeriesSummerProgram=['Olivia Alvarez']
NationalHispanicInstituteTexasLorenzoDeZavalaProgram=['Olivia Alvarez']
PineCove=["Emma Woods", 'Ella Dillinger', 'Katie Corbin', 'Sarah Miller']
PineywoodsChurchCamp=['Sophia Sayers']
SandyHillCamp=['Kate Belman']
SkyRanch=["Brynn Groves", "Cate Colman", 'Ava Dahlander', 'Hannah Dollinger']
StMarysSummerCamps=['Maria Sepulveda']
SuperSummeratDallasBaptistUniversity=['Sophia Sayers']
TbarMCamp=['Kate Neiman']
TCUWilsonTennisCamp=['Angie Andersen']
TapiaSTEMCampsatRiceUniversity=['Olivia Alvarez']
TexasGirlsStateProgram=['Olivia Alvarez']
TheatreCamp=['Katelyn Quintanilla', 'Katherine Blumenschein']
TimberlakeCamp=['Dylan Kaufman']
UTComputerScienceAcademyforAll=['Olivia Alvarez']
UTVolleyballCamp=['Ema Avila']
VacationBibleSchool=['Emily Bull']
YMCASummerCamp=['Drew Shelton']
YoungLifeCamp=['Annie Bryce', 'Giada Scaramuzza']
YoungLifeCrookedCreek=['Giada Scaramuzza']
YoungLifeLoneHollowRanch=['Giada Scaramuzza']
YoungLifeWilderness=['Giada Scaramuzza']

# BOOKS
NineteenEightyFour=['Aaleyah Lloyd', 'Ella Dillinger', 'Elyse Miller']
ALittleLife=['Ella Garber', 'Ollie Mae Harrison', 'Sofia Bartkoski', 'Zoe Westbrook']
ASeriesofUnfortunateEvents=['Sophia Sayers']
AThousandSplendidSuns=['Olivia Alvarez', 'Taylor Jennings']
ACOTAR=['Drew Shelton', 'Kate Neiman', 'Katie Windell']
AbbyJimenez=['Kassidy Bragg']
AmericanDirt=['Natalie Yoder']
AnimalFarm=['Ella Dillinger']
Anythingfantasy=['Giana Toothman']
Anythingthrillingmystery=['Madison Taylor']
AtomicHabits=['Buckley Turner']
BeachRead=['Daisy Challoner', 'Morgan Gaitz']
BeforetheCoffeeGetsCold=['Zeina Saghiyyah']
BetterThantheMovies=['Arani Walton', 'Kamryn Lowery']
Binding13=['Daisy Challoner', 'Kaitlin Black', 'Sofia Argoti']
BoysofTommenSeries=['Sofia Argoti']
CallItWhatYouWant=['Arani Walton']
CallMeByYourName=['Zoe Westbrook']
ChristianLivingBooks=['Ava Dahlander']
Circe=['Kate Flanery']
ConversationswithFriends=['Sofia Argoti']
DaisyJonesandTheSix=['Dylan Kaufman', 'Hazel Wells']
DiaryOfAWimpyKid=["Mackenzie Short"]
EmilyHenry=['Kassidy Bragg', 'Ollie Mae Harrison', 'Parker Keston']
Emma=['Mia Cisneros']
EverythingIKnowAboutLove=['Marie Jolie Day']
Fahrenheit451=['Katherine Blumenschein']
Float=['Zoe Veliz']
FourthWing=['Abrielle Gallini', 'Anika Novak', 'Kate Neiman', 'Ryleigh Montgomery', 'Sophie Coe']
FreidaMcFadden=['Emma Schneidau', 'Zoey Bustamante']
GiovannisRoom=['Lily Robbins']
GodoftheWoods=['Lauren Henderson']
GreatBigBeautifulLife=['Anabel Precht', 'Haylee Martin']
HappyPlace=['Hannah Reilly']
HarryPotter=["Cate Colman", 'Addison Starr', 'Drew Shelton', 'Giada Scaramuzza', 'Marie Jolie Day', 'Neela Juarez', 'Siri Pemberton', 'Victoria Olivarez']
HeatedRivalry=['Annie Hoag', 'Caelyn Prochazka', 'Molly Bogar']
IfOnlyIHadToldHim=['Bella Champion']
ImGladMyMomDied=['Brooke Rosenberg', 'Olivia Alvarez']
It=['Aaleyah Lloyd']
JaneAusten=['Abrielle Gallini', 'Neela Juarez']
Keeping13=['Jennifer Rosado', 'Kaitlin Black']
LessonsinChemistry=['Zeina Saghiyyah']
LittleWomen=['Lily Robbins']
LookingforAlaska=['Katie Walsh']
LoveandGelato=['Kaelyn Liu']
MeetMeattheLake=['Maria Sanchez']
MenWhoHateWomen=['Zeina Saghiyyah']
Misery=['Elyse Miller']
NormalPeople=['Andrea Yu', 'Hannah Reilly', 'Maria Sanchez']
NotesonanExecution=['Lauren Henderson']
OffCampusSeries=['Daisy Challoner', 'Ryleigh Montgomery']
OneDayinDecember=['Katie Walsh']
OneLastStop=['Annie Hoag']
PeopleWeMeetonVacation=['Anika Novak']
PercyJackson=['Jennifer Rosado', 'Victoria Olivarez']
Powerless=['Sophia Sayers']
PrideandPrejudice=['Addison Starr', 'Anabel Precht', 'Mia Cisneros', 'Zoe Veliz']
ReadyPlayerOne=['Brooke Rosenberg']
RedQueenSeries=['Taylor McIlvain']
RedRising=['Katie Windell']
RedWhiteandRoyalBlue=['Morgan Gaitz']
RomCombooks=["Sarah Preston", 'Sofia Bartkoski']
Romancebooks=['Sofie Combs']
ShatterMe=['Braeleigh Garcia']
SixofCrows=['Annie Hoag', 'Braeleigh Garcia']
SlowDaysFastCompany=['Ella Garber']
StephenKing=['Hannah Dollinger']
SylviaPlath=['Lily Robbins']
TheAlchemist=['Mia Cisneros']
TheConditionsofWill=['Molly Bogar']
TheCrimsonMoth=['Macie McKie']
TheCruelPrince=['Macie McKie']
TheDeal=['Arani Walton', 'Kamryn Lowery', 'Marie Jolie Day']
TheDinnerList=['Hasita Karthikeyan']
TheFaultinOurStars=['Dylan Kaufman']
TheFinalGirlSupportGroup=['Madison Taylor']
TheGiver=['Sharon Yoon', 'Siri Pemberton']
TheGlassCastle=['Molly Bogar']
TheGoldfinch=['Kate Flanery']
TheGreatAlone=['Audrey Jones', 'Kaitlin Black']
TheGreatGatsby=['Hasita Karthikeyan', 'Morgan Gaitz', 'Neela Juarez']
TheHungerGames=['Brooke Rosenberg', 'Ella Dillinger', 'Hannah Reilly', 'Hasita Karthikeyan', 'Hazel Wells', 'Kaelyn Liu', 'Katherine Blumenschein', 'Ollie Mae Harrison', 'Sasha Pittsford', 'Sharon Yoon', 'Zoe Westbrook']
TheInvisibleLifeofAddieLarue=['Abrielle Gallini']
TheKnightandtheMoth=['Haylee Martin']
TheLastOlympian=['Katherine Blumenschein']
TheLetThemTheory=['Maria Sanchez']
TheMillontheFloss=['Sasha Pittsford']
TheNightingale=['Kaitlin Black']
TheOutsiders=['Buckley Turner']
ThePerksofBeingaWallflower=['Aaleyah Lloyd', 'Caelyn Prochazka', 'Zoe Veliz']
ThePosoinnwoodBible=['Madison Taylor']
TheSecretHistory=['Anabel Precht', 'Sofia Bartkoski']
TheSecretLifeofBees=['Olivia Alvarez']
TheSelection=['Kaelyn Liu']
TheSevenHusbandsofEvelynHugo=['Addison Starr', 'Dylan Kaufman', 'Kate Belman', 'Katie Walsh', 'Parker Keston', 'Siri Pemberton', 'Sophie Coe']
TheShinning=['Elyse Miller']
TheSilentPatient=['Kate Neiman', 'Taylor Jennings']
TheStand=['Ella Garber']
TheSummerITurnedPretty=['Bella Champion', 'Kamryn Lowery', 'Margot Rosenband', 'Sammi Gill']
TheSummerofBrokenRules=['Sharon Yoon']
TheTattooist=['Sarah Miller']
TheUnmakingofJuneFarrow=['Macie McKie']
TheVanishingHalf=['Natalie Yoder']
TheWallofWinnipegandMe=['Jennifer Rosado']
ThingsWeNeverGotOver=['Haylee Martin']
ThroneofGlass=['Drew Shelton', 'Kate Flanery', 'Katie Windell', 'Sophie Coe']
TinyBeautifulThings=['Caelyn Prochazka']
ToAlltheBoysIveLovedBefore=['Sasha Pittsford']
ToKillaMockingbird=['Audrey Jones', 'Natalie Yoder']
TuesdayswithMorrie=['Lauren Henderson']
TwilightSaga=['Braeleigh Garcia']
UglyLove=['Sarah Miller']
Verity=['Sarah Miller']
WeHaveAlwaysLivedintheCastle=['Lily Robbins']
WheretheCrawdadsSing=['Audrey Jones']
WideSargassoSea=['Hazel Wells']
WindyCitySeries=['Buckley Turner', 'Ryleigh Montgomery']
Wonder=['Margot Rosenband', 'Sophia Sayers']
WutheringHeights=['Anika Novak', 'Bella Champion', 'Margot Rosenband']
YouAreaBadass=['Sofia Argoti']

# HIGH SCHOOL SPORTS
Badminton=["Kendall Klimek"]
Ballet=["Claire Savage", "Ava Dahlander", "Olivia Asay", "Lexie Hale", "Amorie Erichsen", "Giana Toothman", "Zoey Bustamante"]
Basketball=["Cailyn Kelsen", "Mackenzie Short", "Cate Colman", "Lee Lloyd", "Hazel Wells", "Dylan Kaufman", "Zoe Westbrook", "Caitlin Van Sant", "Sarah Miller", "Ema Avila", "Natalie Yoder", "Caroline Schulze", "Buckley Turner", "Bella Champion", "Anabel Precht", "Sanya Hoskere", "Kendall Klimek"]
Cheerleading=["Gaby Green", "May Downey", "Farrah Childs", "Sasha Pittsford", "Sofie Martinez", "Annabelle Judson", "Morgan Gaitz", "Alyssa Garcia", "Natalie Juarez", "Mia Cisneros", "Giada Scaramuzza", "Ella Pitts", "Kate Hoog", "Genesis Martinez", "Sophia Sayers", "Kaitlin Black", "Giana Toothman", "Victoria Olivarez", "Izzy Davies", "Delaney O’Brien", "Annie Bryce", "Rishona Mopur", "Kate Neiman", "Elizabeth Scull", "Angie Andersen"]
Crew=["Jennifer Rosado"]
CrossCountry=["Cate Colman", "Lee Lloyd", "Neela Juarez", "Brooke Waldman", "Andrea Yu", "Sofia Bartkoski", "Elizabeth Porter", "Katie Corbin", "Ella Garber", "Kendall Klimek"]
DanceTeam=["Kamryn Jean", "Sophie Robins", "Claire Savage", "Georgia Key", "Mrinali Ganta", "Ava Hodges", "Annabelle Judson", "Ava Dahlander", "Olivia Asay", "Abrielle Gallini", "Tatum Samuels", "Lexie Hale", "Amorie Erichsen", "Giana Toothman", "Jasmine Valdez", "Zoey Bustamante", "Sharon Yoon"]
DrillTeam=["Sophie Robins", "Claire Savage", "Georgia Key", "Mrinali Ganta", "Annabelle Judson", "Ava Dahlander", "Abrielle Gallini", "Tatum Samuels", "Lexie Hale", "Amorie Erichsen", "Giana Toothman", "Jasmine Valdez", "Zoey Bustamante", "Sharon Yoon", "Caelyn Prochazka"]
Equestrian=["Sarah Miller"]
FieldHockey=["Cailyn Kelsen", "Sofia Argoti", "Margot Rosenband", "Katie Walsh", "Kate Belman"]
Golf=["Celeste Gutierrez", "Annie Boeh", "Elyse Miller", "Madeline Gottemoller", "Christa Hamlin", "Audrey Jones", "Molly Bogar", "Bella Champion", "Victoria Olivarez", "Haylee Martin"]
Lacrosse=["Sadie Spagnoli", "Cailyn Kelsen", "Zoe Westbrook", "Molly Bogar", "Giana Toothman", "Sophia Labazzo", "Katie Walsh", "Kate Belman"]
MarchingBand=["Kate Flanery"]
MartialArts=["Brooke Rosenberg"]
Mascoting=["Angie Andersen"]
Powerlifting=["Buckley Turner", "Elizabeth Perales", "Annie Bryce"]
Rowing=["Taylor McIlvain", "Jennifer Rosado"]
Skiing=["Hadley Amann", "Caitlin Van Sant"]
Soccer=["Sophie Robins", "Brynn Groves", "Drew Shelton", "Audrey Cooper", "Dylan Kaufman", "Brooke Waldman", "Addie Brooks", "Ella Dillinger", "Hannah Dollinger", "Megan Garza", "Natalie Juarez", "Daisy Challoner", "Taylor Jennings", "Maria Sepulveda", "Jennifer Rosado", "Ella Garber", "Annie Bryce"]
Softball=["Lauren Henderson", "Dylan Kaufman", "Hadley Amann", "Natalie Yoder", "Emily Bull", "Hannah Belenkiy", "Kirra Vrzal", "Paola Castillo", "Elizabeth Scull"]
SportsMedicine=["Annie Bryce"]
SwimmingDiving=["Emma Woods", "Siri Pemberton", "Sarah Kester", "Farrah Childs", "Katie Windell", "Sofia Argoti", "Margot Rosenband", "Hannah Belenkiy", "Catherine Dooley"]
Tennis=["Laraleigh Hackerman", "Anika Novak", "Parker Keston", "Farrah Childs", "Neela Juarez", "Ella Dillinger", "Macie McKie", "Sofie Combs", "Maria Sanchez", "Audrey Jones", "Sophia Sayers", "Angie Andersen", "Kimia Forouzesh", "Sammi Gill", "Catherine Dooley", "Delaney O’Brien", "Kendall Klimek", "Skye Doughton", "Kirra Vrzal"]
Track=["Lee Lloyd", "Lauren Henderson", "Brooke Waldman", "Andrea Yu", "Sofia Bartkoski", "Jazlyn Mata", "Natalie Juarez", "Abrielle Gallini", "Mia Cisneros", "Sofia Argoti", "Jennifer Rosado", "Katie Corbin", "Braeleigh Garcia", "Emma Schneidau", "Annie Bryce", "Paola Castillo", "Kendall Klimek"]
Volleyball=["Sarah Preston", "Mackenzie Short", "Gaby Green", "Cate Colman", "Kamryn Lowery", "Emmy Pak", "Laraleigh Hackerman", "Hazel Wells", "Elyse Miller", "Dylan Kaufman", "Sarah Miller", "Ema Avila", "Christa Hamlin", "Addison Starr", "Emmerich Benavides", "Lily Robbins", "Emma Levy", "Bella Champion", "Victoria Olivarez", "Alexa Lira", "Madison Taylor", "Kate Neiman", "Kirra Vrzal"]
WaterPolo=["Emma Woods", "Audrey Cooper", "Sarah Kester", "Katie Windell", "Hannah Belenkiy"]
Weightlifting=["Alyssa Garcia"]

# HIGH SCHOOL INVOLVEMENT
GirlScouts=["Kamryn Lowery", "Ryleigh Montgomery", "Ema Avila", "Christa Hamlin", "Molly Bogar", "Jennifer Rosado", "Giana Toothman", "Hadley Amann"]
GovernmentDebate=["Siri Pemberton", "Drew Shelton", "Madeline Gottemoller", "Sofia Bartkoski", "Mia Cisneros", "Olivia Alvarez", "Victoria Olivarez", "Maria Sepulveda", "Charlie Stone", "Emma Schneidau", "Sophia Labazzo", "Kate Neiman", "Alexa Lira", "Katie Walsh"]
HonorSocieties=["Kamryn Jean", "Sarah Preston", "Gaby Green", "Celeste Gutierrez", "Siri Pemberton", "Drew Shelton", "Audrey Cooper", "Annie Boeh", "Lauren Henderson", "Farrah Childs", "Neela Juarez", "Madeline Gottemoller", "Sofia Bartkoski", "Ryleigh Montgomery", "Megan Garza", "Zeina Saghiyyah", "Hasita Karthikeyan", "Emmerich Benavides", "Daisy Challoner", "Elizabeth Porter", "Angie Andersen", "Giana Toothman", "Sammi Gill", "Maria Sepulveda", "Sanya Hoskere", "Kate Belman", "Kate Neiman", "Kirra Vrzal", "Katelyn Quintanilla"]
HOSA=[ "Taylor McIlvain", "Ella Leininger", "Neela Juarez", "Ryleigh Montgomery", "Megan Garza", "Hannah Dollinger", "Lexie Hale", "Ema Avila", "Emmerich Benavides", "Giana Toothman", "Sammi Gill", "Jasmine Valdez", "Maria Sanchez", "Maria Sepulveda", "Kate Flanery", "Sanya Hoskere", "Sofie Arroyo", "Braeleigh Garcia", "Ryleigh Montgomery"]
IBProgram=["Siri Pemberton", "Sarah Kester", "Hazel Wells", "Katie Windell", "Madeline Gottemoller", "Sofia Argoti", "Ava Dahlander"]
KeyClub=["Dylan Kaufman", "Macie McKie", "Lexie Hale", "Maria Sanchez", "Daisy Challoner", "Amorie Erichsen", "Kate Hoog", "Giada Scaramuzza", "Jacqueline Olivier", "Izzy Davies", "Anabel Precht", "Andrea Yu", "Ryleigh Montgomery", "Emma Schneidau"]
NationalCharityLeague=["Hazel Wells", "Mrinali Ganta", "Josie Daik", "Brooke Waldman", "Sofie Combs", "Ava Hodges", "Ryleigh Montgomery", "Annabelle Judson", "Ella Dillinger", "Morgan Gaitz", "Tatum Samuels", "Zeina Saghiyyah", "Hannah Dollinger", "Addison Starr", "Ava Dahlander", "Giada Scaramuzza", "Molly Bogar", "Kaitlin Black", "Giana Toothman", "Ollie Mae Harrison", "Ella Garber", "Izzy Davies", "Brooke Rosenberg"]
NationalHonorSociety=["Sophie Robins", "Claire Savage", "Sadie Spagnoli", "Cailyn Kelsen", "Sarah Preston", "Mackenzie Short", "Gaby Green", "Brynn Groves", "Cate Colman", "Emma Woods", "Georgia Key", "Celeste Gutierrez", "Siri Pemberton", "Taylor McIlvain", "Kamryn Lowery", "Drew Shelton", "Ella Leininger", "May Downey", "Laraleigh Hackerman", "Anika Novak", "Audrey Cooper", "Sarah Kester", "Hazel Wells", "Annie Boeh", "Lauren Henderson", "Katherine Blumenschein", "Mrinali Ganta", "Farrah Childs", "Neela Juarez", "Dylan Kaufman", "Madeline Gottemoller", "Josie Daik", "Sasha Pittsford", "Hadley Amann", "Andrea Yu", "Sofie Martinez", "Sofia Bartkoski", "Ryleigh Montgomery", "Annabelle Judson", "Ella Dillinger", "Morgan Gaitz", "Sofie Combs", "Sofia Argoti", "Zoe Westbrook", "Caitlin Van Sant", "Jazlyn Mata", "Sarah Miller", "Sophie Coe", "Ava Dahlander", "Natalie Juarez", "Olivia Asay", "Emmerich Benavides", "Daisy Challoner", "Buckley Turner", "Giada Scaramuzza", "Bella Champion", "Hannah Reilly", "Ella Pitts", "Kaitlin Black", "Kassidy Bragg", "Angie Andersen", "Kimia Forouzesh", "Giana Toothman", "Sammi Gill", "Caelyn Prochazka", "Taylor Jennings", "Victoria Olivarez", "Maria Sepulveda", "Ollie Mae Harrison", "Elizabeth Perales", "Kate Flanery", "Katie Corbin", "Sofie Arroyo", "Braeleigh Garcia", "Izzy Davies", "Emma Schneidau", "Hannah Belenkiy", "Zoe Veliz", "Brooke Rosenberg", "Madison Taylor", "Katie Walsh", "Sanya Hoskere", "Haylee Martin", "Rishona Mopur", "Kate Belman", "Kate Neiman", "Kirra Vrzal", "Paola Castillo", "Elizabeth Scull"]
PerformingArts=["Abby Joe", "Lee Lloyd", "Drew Shelton", "Katherine Blumenschein", "Annie Hoag", "Addie Brooks", "Madeline Gottemoller", "Ava Dahlander", "Olivia Asay", "Ema Avila", "Annie Hoag", "Hannah Reilly", "Kaitlin Black", "Elizabeth Perales", "Katelyn Quintanilla", "Marie Jolie Day", "Giana Toothman", "Ella Dillinger", "Kate Flanery", "Zoey Bustamante"]
Religious=["Cailyn Kelsen", "Emma Woods", "Kamryn Lowery", "Ella Leininger", "Elyse Miller", "Annabelle Judson", "Ava Dahlander", "Ema Avila", "Christa Hamlin", "Caroline Schulze", "Hannah Dollinger", "Bella Champion", "Hannah Reilly", "Kaitlin Black", "Sophia Sayers", "Ella Garber", "Paola Castillo", "Annie Bryce"]
ServiceVolunteer=["Kamryn Lowery", "Hazel Wells", "Sarah Kester", "Ryleigh Montgomery", "Caroline Schulze", "Emma Levy", "Emily Bull", "Elena Solano", "Anabel Precht", "Kendall Klimek", "Charlie Stone", "Izzy Davies", "Brooke Rosenberg", "Paola Castillo", "Victoria Olivarez"]
STEMAcademic=["Lauren Henderson", "Mrinali Ganta", "Farrah Childs", "Neela Juarez", "Andrea Yu", "Sofia Argoti", "Zeina Saghiyyah", "Hasita Karthikeyan", "Megan Garza", "Daisy Challoner", "Arani Walton", "Olivia Alvarez", "Elizabeth Porter", "Kimia Forouzesh", "Kate Flanery", "Katie Corbin", "Sanya Hoskere", "Hannah Belenkiy", "Annie Boeh", "Audrey Cooper"]
StudentCouncil=["Sophie Robins", "Gaby Green", "Cate Colman", "Celeste Gutierrez", "Laraleigh Hackerman", "Anika Novak", "Hazel Wells", "Katherine Blumenschein", "Dylan Kaufman", "Madeline Gottemoller", "Ella Dillinger", "Macie McKie", "Caitlin Van Sant", "Sarah Miller", "Sophie Coe", "Natalie Juarez", "Olivia Asay", "Abrielle Gallini", "Christa Hamlin", "Caroline Schulze", "Hasita Karthikeyan", "Hannah Dollinger", "Buckley Turner", "Tatum Samuels", "Emmerich Benavides", "Victoria Olivarez", "Maria Sepulveda", "Elena Solano", "Elizabeth Perales", "Kaelyn Liu", "Delaney O’Brien", "Annabelle Judson", "Charlie Stone", "Madison Taylor", "Katie Walsh", "Kate Belman", "Kirra Vrzal", "Paola Castillo", "Elizabeth Scull"]
StudentPublications=["Kamryn Jean", "Emmy Pak", "Elyse Miller", "Parker Keston", "Sasha Pittsford", "Josie Daik", "Abrielle Gallini", "Ella Dillinger", "Hannah Reilly", "Margot Rosenband", "Lily Robbins", "Giana Toothman", "Kate Flanery", "Zoe Veliz", "Brooke Rosenberg", "Katie Walsh", "Kate Belman", "Kate Neiman", "Elizabeth Perales", "Sasha Pittsford"]
TutoringPeerMentoring=["Claire Savage", "Cailyn Kelsen", "Brynn Groves", "Cate Colman", "Lauren Henderson", "Mrinali Ganta", "Sofia Bartkoski", "Caitlin Van Sant", "Sophie Coe", "Emmerich Benavides", "Lily Robbins", "Olivia Alvarez", "Sophia Sayers", "Giana Toothman", "Elizabeth Porter", "Katie Corbin", "Ella Garber", "Izzy Davies", "Zoe Veliz", "Annie Bryce", "Madison Taylor", "Katie Walsh", "Andrea Yu"]

# PHILANTHROPY
WorkingWithAnimals=["Georgia Key", "Siri Pemberton", "Kamryn Lowery", "Drew Shelton", "Ella Leininger", "Lauren Henderson", "Neela Juarez", "Brooke Waldman", "Katie Windell", "Ava Hodges", "Addie Brooks", "Morgan Gaitz", "Macie McKie", "Jazlyn Mata", "Sarah Miller", "Natalie Juarez", "Ema Avila", "Christa Hamlin", "Zeina Saghiyyah", "Giada Scaramuzza", "Molly Bogar", "Kaitlin Black", "Emmerich Benavides", "Emma Levy", "Skye Doughton", "Giana Toothman", "Maria Sepulveda", "Elizabeth Perales", "Ella Garber", "Sofie Arroyo", "Izzy Davies", "Charlie Stone", "Madison Taylor", "Paola Castillo", "Hannah Belenkiy"]
WorkingWithChildren=["Kamryn Jean", "Sophie Robins", "Claire Savage", "Cailyn Kelsen", "Sarah Preston", "Brynn Groves", "Cate Colman", "Celeste Gutierrez", "Siri Pemberton", "Lee Lloyd", "Kamryn Lowery", "Drew Shelton", "Ella Leininger", "May Downey", "Anika Novak", "Audrey Cooper", "Sarah Kester", "Hazel Wells", "Annie Boeh", "Lauren Henderson", "Katherine Blumenschein", "Parker Keston", "Farrah Childs", "Neela Juarez", "Dylan Kaufman", "Josie Daik", "Brooke Waldman", "Hadley Amann", "Katie Windell", "Andrea Yu", "Sofie Martinez", "Sofia Bartkoski", "Ryleigh Montgomery", "Ava Dahlander", "Olivia Asay", "Ema Avila", "Abrielle Gallini", "Mia Cisneros", "Christa Hamlin", "Tatum Samuels", "Caroline Schulze", "Hasita Karthikeyan", "Lexie Hale", "Margot Rosenband", "Audrey Jones", "Buckley Turner", "Giada Scaramuzza", "Molly Bogar", "Bella Champion", "Hannah Reilly", "Ella Pitts", "Kaitlin Black", "Daisy Challoner", "Arani Walton", "Amorie Erichsen", "Lily Robbins", "Olivia Alvarez", "Kate Hoog", "Sophia Sayers", "Jennifer Rosado", "Emma Levy", "Elizabeth Porter", "Skye Doughton", "Kassidy Bragg", "Angie Andersen", "Kimia Forouzesh", "Giana Toothman", "Caelyn Prochazka", "Emily Bull", "Hadley Amann", "Elena Solano", "Ollie Mae Harrison", "Elizabeth Perales", "Kate Flanery", "Kaelyn Liu", "Marie Jolie Day", "Ryleigh Montgomery", "Braeleigh Garcia", "Izzy Davies", "Delaney O’Brien", "Hannah Belenkiy", "Zoe Veliz", "Zoey Bustamante", "Emma Schneidau", "Sophia Labazzo", "Annie Bryce", "Anabel Precht", "Sharon Yoon", "Madison Taylor", "Katie Walsh", "Haylee Martin", "Rishona Mopur", "Andrea Yu", "Kendall Klimek", "Kate Belman", "Kirra Vrzal", "Paola Castillo", "Elizabeth Scull"]
WorkingWithElderlyDisabled=["Sophie Robins", "Sadie Spagnoli", "Brynn Groves", "Cate Colman", "Lee Lloyd", "Kamryn Lowery", "Drew Shelton", "Audrey Cooper", "Katherine Blumenschein", "Farrah Childs", "Andrea Yu", "Ryleigh Montgomery", "Annie Hoag", "Macie McKie", "Zoë Westbrook", "Sarah Miller", "Ava Dahlander", "Ema Avila", "Christa Hamlin", "Tatum Samuels", "Natalie Yoder", "Hasita Karthikeyan", "Hannah Dollinger", "Lexie Hale", "Audrey Jones", "Buckley Turner", "Molly Bogar", "Hannah Reilly", "Ella Pitts", "Kaitlin Black", "Amorie Erichsen", "Olivia Alvarez", "Emma Levy", "Elizabeth Porter", "Skye Doughton", "Kassidy Bragg", "Giana Toothman", "Caelyn Prochazka", "Emily Bull", "Ollie Mae Harrison", "Ryleigh Montgomery", "Braeleigh Garcia", "Izzy Davies", "Brooke Rosenberg", "Sanya Hoskere", "Haylee Martin", "Andrea Yu", "Kirra Vrzal", "Paola Castillo", "Elizabeth Scull"]
WorkingWithEnvironmentalConservation=["Kamryn Lowery", "Ella Leininger", "Anika Novak", "Lauren Henderson", "Parker Keston", "Neela Juarez", "Brooke Waldman", "Katie Windell", "Andrea Yu", "Mia Cisneros", "Christa Hamlin", "Caitlin Van Sant", "Giada Scaramuzza", "Hannah Reilly", "Daisy Challoner", "Olivia Alvarez", "Kate Hoog", "Emma Levy", "Skye Doughton", "Elizabeth Perales", "Kaelyn Liu", "Ella Garber", "Hannah Belenkiy", "Zoe Veliz", "Anabel Precht", "Madison Taylor", "Rishona Mopur", "Kirra Vrzal", "Paola Castillo", "Maria Sepulveda"]
WorkingWithHealthcare=["Cailyn Kelsen", "Brynn Groves", "Taylor McIlvain", "Kamryn Lowery", "Lauren Henderson", "Neela Juarez", "Farrah Childs", "Ryleigh Montgomery", "Caitlin Van Sant", "Sarah Miller", "Sophie Coe", "Hasita Karthikeyan", "Hannah Dollinger", "Lexie Hale", "Audrey Jones", "Buckley Turner", "Maria Sanchez", "Emmerich Benavides", "Taylor Jennings", "Jasmine Valdez", "Hadley Amann", "Sanya Hoskere", "Rishona Mopur", "Braeleigh Garcia", "Izzy Davies", "Sophia Labazzo", "Kirra Vrzal"]
WorkingWithUnhousedImpoverished=["Sophie Robins", "Sadie Spagnoli", "Cailyn Kelsen", "Sarah Preston", "Gaby Green", "Emma Woods", "Kamryn Lowery", "Mrinali Ganta", "Neela Juarez", "Josie Daik", "Sofie Combs", "Addison Starr", "Annabelle Judson", "Morgan Gaitz", "Tatum Samuels", "Jacqueline Olivier", "Buckley Turner", "Molly Bogar", "Kaitlin Black", "Sophie Sayers", "Sophia Sayers", "Emma Levy", "Elizabeth Porter", "Skye Doughton", "Kimia Forouzesh", "Giana Toothman", "Catherine Dooley", "Elizabeth Perales", "Katie Corbin", "Alexa Lira", "Kaelyn Liu", "Ella Garber", "Sofie Arroyo", "Ryleigh Montgomery", "Izzy Davies", "Anabel Precht", "Sharon Yoon", "Emma Schneidau", "Sophia Labazzo", "Kate Neiman", "Katelyn Quintanilla", "Paola Castillo"]
WorkingWithSocialActivism=["Siri Pemberton", "Lauren Henderson", "Sofia Bartkoski", "Sofie Combs", "Natalie Juarez", "Caroline Schulze", "Margot Rosenband", "Lily Robbins", "Olivia Alvarez", "Sammi Gill", "Zoe Veliz", "Annie Bryce", "Anabel Precht", "Katie Walsh", "Emma Levy"]

# PHYSICAL / OUTDOOR ACTIVITIES
BasketballAct=["Emma Woods", "Lee Lloyd", "Taylor McIlvain", "Zoe Westbrook", "Caitlin Van Sant", "Sarah Miller", "Ema Avila", "Natalie Yoder", "Caroline Schulze", "Buckley Turner", "Sammi Gill", "Sanya Hoskere", "Andrea Yu", "Kendall Klimek", "Kate Flanery"]
Biking=["Emma Woods", "Taylor McIlvain", "Lee Lloyd", "Caitlin Van Sant", "Sarah Miller", "Natalie Juarez", "Margot Rosenband", "Audrey Jones", "Giada Scaramuzza", "Katie Corbin", "Victoria Olivarez", "Kate Neiman", "Kendall Klimek", "Kate Belman"]
Boating=["Sophie Robins", "Cailyn Kelsen", "Brynn Groves", "Emma Woods", "Taylor McIlvain", "Kamryn Lowery", "Mrinali Ganta", "Parker Keston", "Madeline Gottemoller", "Hadley Amann", "Katie Windell", "Caitlin Van Sant", "Sarah Miller", "Sofia Bartkoski", "Ryleigh Montgomery", "Christa Hamlin", "Natalie Juarez", "Ema Avila", "Caroline Schulze", "Audrey Jones", "Buckley Turner", "Molly Bogar", "Victoria Olivarez", "Ella Garber", "Madison Taylor", "Elizabeth Scull"]
Camping=["Cate Colman", "Lee Lloyd", "Kamryn Lowery", "Neela Juarez", "Katie Windell", "Hadley Amann", "Sofia Bartkoski", "Zoe Westbrook", "Caitlin Van Sant", "Sarah Miller", "Ava Dahlander", "Ema Avila", "Natalie Yoder", "Hannah Reilly", "Giada Scaramuzza", "Molly Bogar", "Buckley Turner", "Anabel Precht", "Brooke Rosenberg", "Elizabeth Perales", "Charlie Stone", "Ella Garber", "Delaney O’Brien"]
ConcertsLiveMusic=["Kamryn Jean", "Sophie Robins", "Claire Savage", "Sadie Spagnoli", "Cailyn Kelsen", "Mackenzie Short", "Brynn Groves", "Cate Colman", "Emma Woods", "Georgia Key", "Lee Lloyd", "Taylor McIlvain", "Kamryn Lowery", "Emmy Pak", "Drew Shelton", "Ella Leininger", "Anika Novak", "Audrey Cooper", "Hazel Wells", "Annie Boeh", "Lauren Henderson", "Elyse Miller", "Mrinali Ganta", "Parker Keston", "Farrah Childs", "Neela Juarez", "Dylan Kaufman", "Josie Daik", "Brooke Waldman", "Sasha Pittsford", "Hadley Amann", "Katie Windell", "Sofie Martinez", "Ava Hodges", "Ryleigh Montgomery", "Addie Brooks", "Annie Hoag", "Annabelle Judson", "Ella Dillinger", "Macie McKie", "Sofie Combs", "Sofia Argoti", "Zoe Westbrook", "Caitlin Van Sant", "Jazlyn Mata", "Sarah Miller", "Ava Dahlander", "Natalie Juarez", "Olivia Asay", "Ema Avila", "Abrielle Gallini", "Mia Cisneros", "Christa Hamlin", "Tatum Samuels", "Natalie Yoder", "Caroline Schulze", "Zeina Saghiyyah", "Hasita Karthikeyan", "Megan Garza", "Lexie Hale", "Margot Rosenband", "Jacqueline Olivier", "Giada Scaramuzza", "Molly Bogar", "Maria Sanchez", "Bella Champion", "Hannah Reilly", "Ella Pitts", "Kaitlin Black", "Emmerich Benavides", "Daisy Challoner", "Arani Walton", "Amorie Erichsen", "Lily Robbins", "Olivia Alvarez", "Kate Hoog", "Genesis Martinez", "Sophia Sayers", "Jennifer Rosado", "Emma Levy", "Elizabeth Porter", "Skye Doughton", "Kassidy Bragg", "Angie Andersen", "Giana Toothman", "Marie Jolie Day", "Ella Garber", "Sofie Arroyo", "Braeleigh Garcia", "Izzy Davies", "Delaney O’Brien", "Hannah Belenkiy", "Zoe Veliz", "Zoey Bustamante", "Emma Schneidau", "Sophia Labazzo", "Annie Bryce", "Anabel Precht", "Brooke Rosenberg", "Sharon Yoon", "Madison Taylor", "Katie Walsh", "Sanya Hoskere", "Haylee Martin", "Rishona Mopur", "Andrea Yu", "Kendall Klimek", "Kate Belman", "Kate Neiman", "Katelyn Quintanilla", "Paola Castillo", "Elizabeth Scull"]
Dancing=["Kamryn Jean", "Sophie Robins", "Claire Savage", "Abby Joe", "Georgia Key", "Taylor McIlvain", "Kamryn Lowery", "Emmy Pak", "Elyse Miller", "Mrinali Ganta", "Ava Hodges", "Sofia Bartkoski", "Annabelle Judson", "Ella Dillinger", "Abrielle Gallini", "Mia Cisneros", "Tatum Samuels", "Amorie Erichsen", "Lily Robbins", "Olivia Asay", "Arani Walton", "Giana Toothman", "Jasmine Valdez", "Kaelyn Liu", "Kate Neiman"]
ExploringAustin=["Sophie Robins", "Claire Savage", "Sadie Spagnoli", "Cailyn Kelsen", "Sarah Preston", "Mackenzie Short", "Brynn Groves", "Cate Colman", "Emma Woods", "Abby Joe", "Georgia Key", "Taylor McIlvain", "Kamryn Lowery", "Emmy Pak", "Drew Shelton", "Ella Leininger", "May Downey", "Anika Novak", "Audrey Cooper", "Sarah Kester", "Hazel Wells", "Annie Boeh", "Lauren Henderson", "Elyse Miller", "Mrinali Ganta", "Parker Keston", "Farrah Childs", "Neela Juarez", "Dylan Kaufman", "Madeline Gottemoller", "Josie Daik", "Brooke Waldman", "Hadley Amann", "Katie Windell", "Ava Hodges", "Ryleigh Montgomery", "Addie Brooks", "Annabelle Judson", "Ella Dillinger", "Macie McKie", "Alyssa Garcia", "Sofie Combs", "Sofia Argoti", "Zoe Westbrook", "Caitlin Van Sant", "Jazlyn Mata", "Sarah Miller", "Sophie Coe", "Addison Starr", "Ava Dahlander", "Natalie Juarez", "Olivia Asay", "Ema Avila", "Abrielle Gallini", "Mia Cisneros", "Christa Hamlin", "Tatum Samuels", "Natalie Yoder", "Caroline Schulze", "Zeina Saghiyyah", "Hasita Karthikeyan", "Megan Garza", "Lexie Hale", "Margot Rosenband", "Jacqueline Olivier", "Buckley Turner", "Giada Scaramuzza", "Molly Bogar", "Maria Sanchez", "Bella Champion", "Hannah Reilly", "Kaitlin Black", "Emmerich Benavides", "Daisy Challoner", "Arani Walton", "Amorie Erichsen", "Lily Robbins", "Olivia Alvarez", "Sophia Sayers", "Jennifer Rosado", "Emma Levy", "Elizabeth Porter", "Skye Doughton", "Kassidy Bragg", "Kimia Forouzesh", "Giana Toothman", "Catherine Dooley", "Caelyn Prochazka", "Emily Bull", "Elena Solano", "Elizabeth Perales", "Kate Flanery", "Kaelyn Liu", "Marie Jolie Day", "Ella Garber", "Sofie Arroyo", "Braeleigh Garcia", "Izzy Davies", "Delaney O’Brien", "Hannah Belenkiy", "Zoe Veliz", "Zoey Bustamante", "Emma Schneidau", "Sophia Labazzo", "Anabel Precht", "Brooke Rosenberg", "Sharon Yoon", "Madison Taylor", "Katie Walsh", "Sanya Hoskere", "Haylee Martin", "Rishona Mopur", "Andrea Yu", "Kendall Klimek", "Kate Belman", "Kate Neiman", "Katelyn Quintanilla", "Paola Castillo", "Elizabeth Scull"]
FieldHockeyAct=["Margot Rosenband", "Katie Walsh", "Kate Belman"]
Fishing=["Cate Colman", "Kamryn Lowery", "Katie Windell", "Sofie Combs", "Sarah Miller", "Tatum Samuels", "Jennifer Rosado", "Victoria Olivarez", "Annabelle Judson", "Paola Castillo", "Elizabeth Scull"]
GolfingAct=["Sadie Spagnoli", "Celeste Gutierrez", "Annie Boeh", "Elyse Miller", "Madeline Gottemoller", "Christa Hamlin", "Audrey Jones", "Molly Bogar", "Bella Champion", "Caroline Schulze", "Angie Andersen", "Katie Walsh", "Haylee Martin", "Victoria Olivarez", "Elizabeth Scull"]
Hiking=["Sophie Robins", "Sadie Spagnoli", "Sarah Preston", "Mackenzie Short", "Cate Colman", "Emma Woods", "Lee Lloyd", "Kamryn Lowery", "Ella Leininger", "Lauren Henderson", "Neela Juarez", "Hadley Amann", "Katie Windell", "Zoe Westbrook", "Caitlin Van Sant", "Jazlyn Mata", "Sophie Coe", "Ava Dahlander", "Natalie Juarez", "Abrielle Gallini", "Natalie Yoder", "Caroline Schulze", "Hasita Karthikeyan", "Margot Rosenband", "Audrey Jones", "Buckley Turner", "Giada Scaramuzza", "Molly Bogar", "Hannah Reilly", "Kaitlin Black", "Emmy Pak", "Emmerich Benavides", "Lily Robbins", "Skye Doughton", "Elizabeth Perales", "Ella Garber", "Delaney O’Brien", "Annabelle Judson", "Anabel Precht", "Brooke Rosenberg", "Sharon Yoon", "Haylee Martin", "Katelyn Quintanilla", "Elizabeth Scull"]
HorsebackRiding=["Emma Woods", "Lee Lloyd", "Sarah Miller", "Abrielle Gallini", "Tatum Samuels", "Zeina Saghiyyah", "Jennifer Rosado", "Hadley Amann", "Delaney O’Brien", "Kate Neiman", "Alexa Lira"]
Hunting=["Sarah Miller", "Caroline Schulze", "Audrey Jones", "Kaitlin Black", "Elizabeth Porter", "Victoria Olivarez", "Elizabeth Perales"]
IceSkating=["Taylor McIlvain", "Ava Hodges", "Sofia Bartkoski", "Hadley Amann", "Kate Belman"]
LacrosseAct=["Cailyn Kelsen", "Katherine Blumenschein", "Zoe Westbrook", "Molly Bogar", "Sophia Labazzo"]
PaddleboardingKayaking=["Cailyn Kelsen", "Emma Woods", "Taylor McIlvain", "Kamryn Lowery", "Ella Leininger", "Anika Novak", "Lauren Henderson", "Parker Keston", "Neela Juarez", "Hadley Amann", "Katie Windell", "Annabelle Judson", "Sofia Argoti", "Caitlin Van Sant", "Sarah Miller", "Ava Dahlander", "Natalie Juarez", "Ema Avila", "Abrielle Gallini", "Christa Hamlin", "Natalie Yoder", "Caroline Schulze", "Hasita Karthikeyan", "Audrey Jones", "Buckley Turner", "Giada Scaramuzza", "Hannah Reilly", "Skye Doughton", "Zoey Bustamante", "Anabel Precht", "Brooke Rosenberg", "Sharon Yoon", "Madison Taylor", "Sanya Hoskere", "Andrea Yu", "Kate Belman", "Paola Castillo", "Elizabeth Perales", "Ella Garber", "Sofie Arroyo", "Katelyn Quintanilla"]
Pickleball=["Sophie Robins", "Cailyn Kelsen", "Brynn Groves", "Celeste Gutierrez", "Lee Lloyd", "Taylor McIlvain", "Kamryn Lowery", "Emmy Pak", "Audrey Cooper", "Lauren Henderson", "Parker Keston", "Farrah Childs", "Neela Juarez", "Dylan Kaufman", "Madeline Gottemoller", "Hadley Amann", "Annabelle Judson", "Sofia Argoti", "Zoe Westbrook", "Caitlin Van Sant", "Jazlyn Mata", "Natalie Juarez", "Abrielle Gallini", "Natalie Yoder", "Caroline Schulze", "Audrey Jones", "Buckley Turner", "Molly Bogar", "Hannah Reilly", "Bella Champion", "Emmerich Benavides", "Sophia Sayers", "Emma Levy", "Skye Doughton", "Annie Bryce", "Brooke Rosenberg", "Sharon Yoon", "Madison Taylor", "Sanya Hoskere", "Rishona Mopur", "Andrea Yu", "Kendall Klimek", "Sofie Arroyo", "Caelyn Prochazka", "Paola Castillo", "Elizabeth Scull"]
Pilates=["Sophie Robins", "Claire Savage", "Cailyn Kelsen", "Mackenzie Short", "Brynn Groves", "Cate Colman", "Georgia Key", "Celeste Gutierrez", "Taylor McIlvain", "Drew Shelton", "Ella Leininger", "Lauren Henderson", "Katherine Blumenschein", "Parker Keston", "Neela Juarez", "Madeline Gottemoller", "Ava Hodges", "Sofia Bartkoski", "Ryleigh Montgomery", "Morgan Gaitz", "Alyssa Garcia", "Jazlyn Mata", "Sarah Miller", "Addison Starr", "Natalie Juarez", "Abrielle Gallini", "Mia Cisneros", "Margot Rosenband", "Audrey Jones", "Buckley Turner", "Giada Scaramuzza", "Maria Sanchez", "Bella Champion", "Hannah Reilly", "Ella Pitts", "Daisy Challoner", "Lily Robbins", "Olivia Alvarez", "Sophia Sayers", "Emma Levy", "Skye Doughton", "Kimia Forouzesh", "Catherine Dooley", "Caelyn Prochazka", "Taylor Jennings", "Elizabeth Perales", "Katie Corbin", "Kaelyn Liu", "Marie Jolie Day", "Ella Garber", "Izzy Davies", "Sharon Yoon", "Sanya Hoskere", "Rishona Mopur", "Kendall Klimek", "Kate Belman", "Elizabeth Scull"]
RockClimbing=["Cate Colman", "Sarah Miller", "Hasita Karthikeyan", "Skye Doughton"]
RunningJogging=["Sophie Robins", "Brynn Groves", "Cate Colman", "Siri Pemberton", "Taylor McIlvain", "Drew Shelton", "Lauren Henderson", "Farrah Childs", "Neela Juarez", "Sofia Bartkoski", "Annabelle Judson", "Morgan Gaitz", "Sofia Argoti", "Jazlyn Mata", "Sarah Miller", "Ava Dahlander", "Natalie Juarez", "Abrielle Gallini", "Mia Cisneros", "Natalie Yoder", "Hasita Karthikeyan", "Megan Garza", "Margot Rosenband", "Audrey Jones", "Buckley Turner", "Molly Bogar", "Maria Sanchez", "Kaitlin Black", "Daisy Challoner", "Amorie Erichsen", "Jennifer Rosado", "Katie Corbin", "Braeleigh Garcia", "Andrea Yu", "Kendall Klimek", "Taylor Jennings", "Delaney O’Brien"]
ScubaDiving=["Mackenzie Short", "Kamryn Lowery", "Sofie Combs", "Zeina Saghiyyah", "Audrey Jones", "Hannah Reilly", "Hadley Amann", "Zoey Bustamante", "Kate Neiman"]
SkiingSnowboarding=["Neela Juarez", "Hannah Dollinger"]
SoulCycle=["Laraleigh Hackerman"]
Surfing=["Emma Woods", "Kamryn Lowery", "Hadley Amann", "Sarah Miller", "Natalie Yoder", "Molly Bogar", "Skye Doughton", "Brooke Rosenberg", "Zoey Bustamante", "Kate Neiman"]
SwimmingDiving=["Cate Colman", "Emma Woods", "Siri Pemberton", "Kamryn Lowery", "Emmy Pak", "Ella Leininger", "Anika Novak", "Audrey Cooper", "Sarah Kester", "Farrah Childs", "Katie Windell", "Neela Juarez", "Sofia Bartkoski", "Zoe Westbrook", "Caitlin Van Sant", "Jazlyn Mata", "Sarah Miller", "Ema Avila", "Christa Hamlin", "Margot Rosenband", "Audrey Jones", "Molly Bogar", "Hannah Reilly", "Kaitlin Black", "Amorie Erichsen", "Jennifer Rosado", "Catherine Dooley", "Hannah Belenkiy", "Zoey Bustamante", "Ollie Mae Harrison", "Victoria Olivarez", "Hadley Amann"]
Tanning=["Sophie Robins", "Sarah Preston", "Mackenzie Short", "Gaby Green", "Brynn Groves", "Cate Colman", "Emma Woods", "Abby Joe", "Georgia Key", "Celeste Gutierrez", "Lee Lloyd", "Taylor McIlvain", "Kamryn Lowery", "Emmy Pak", "Drew Shelton", "Ella Leininger", "Anika Novak", "Hazel Wells", "Elyse Miller", "Parker Keston", "Farrah Childs", "Dylan Kaufman", "Madeline Gottemoller", "Hadley Amann", "Andrea Yu", "Sofia Bartkoski", "Ryleigh Montgomery", "Alyssa Garcia", "Sofia Argoti", "Zoe Westbrook", "Caitlin Van Sant", "Jazlyn Mata", "Sarah Miller", "Ava Dahlander", "Abrielle Gallini", "Christa Hamlin", "Tatum Samuels", "Margot Rosenband", "Audrey Jones", "Jacqueline Olivier", "Giada Scaramuzza", "Molly Bogar", "Maria Sanchez", "Bella Champion", "Ella Pitts", "Sofie Martinez", "Kaitlin Black", "Emmerich Benavides", "Daisy Challoner", "Arani Walton", "Amorie Erichsen", "Lily Robbins", "Olivia Alvarez", "Sophia Sayers", "Jennifer Rosado", "Emma Levy", "Elizabeth Porter", "Skye Doughton", "Kassidy Bragg", "Angie Andersen", "Giana Toothman", "Kimia Forouzesh", "Catherine Dooley", "Victoria Olivarez", "Emily Bull", "Ollie Mae Harrison", "Katie Corbin", "Alexa Lira", "Kaelyn Liu", "Marie Jolie Day", "Ella Garber", "Izzy Davies", "Delaney O’Brien", "Annabelle Judson", "Hannah Belenkiy", "Zoe Veliz", "Zoey Bustamante", "Emma Schneidau", "Sophia Labazzo", "Annie Bryce", "Brooke Rosenberg", "Sharon Yoon", "Madison Taylor", "Sanya Hoskere", "Haylee Martin", "Rishona Mopur", "Kendall Klimek", "Kate Belman", "Kate Neiman", "Elizabeth Scull"]
TennisAct=["Anika Novak", "Farrah Childs", "Neela Juarez", "Parker Keston", "Macie McKie", "Sofie Combs", "Hadley Amann", "Audrey Jones", "Maria Sanchez", "Sophia Sayers", "Skye Doughton", "Kimia Forouzesh", "Sammi Gill", "Catherine Dooley", "Victoria Olivarez", "Delaney O’Brien", "Kendall Klimek", "Kate Belman", "Kate Neiman"]
Thrifting=["Sophie Robins", "Mackenzie Short", "Gaby Green", "Cate Colman", "Lee Lloyd", "Taylor McIlvain", "Kamryn Lowery", "Emmy Pak", "Ella Leininger", "Anika Novak", "Lauren Henderson", "Katherine Blumenschein", "Neela Juarez", "Ava Hodges", "Addie Brooks", "Macie McKie", "Sofie Combs", "Sofia Argoti", "Zoe Westbrook", "Jazlyn Mata", "Sarah Miller", "Mia Cisneros", "Abrielle Gallini", "Lexie Hale", "Margot Rosenband", "Jacqueline Olivier", "Giada Scaramuzza", "Molly Bogar", "Maria Sanchez", "Bella Champion", "Hannah Reilly", "Lily Robbins", "Olivia Alvarez", "Sophia Sayers", "Emma Levy", "Skye Doughton", "Kassidy Bragg", "Elizabeth Perales", "Kate Flanery", "Marie Jolie Day", "Ella Garber", "Izzy Davies", "Delaney O’Brien", "Zoey Bustamante", "Anabel Precht", "Brooke Rosenberg", "Sharon Yoon", "Madison Taylor", "Katelyn Quintanilla", "Paola Castillo", "Elizabeth Scull"]
Traveling=["Sophie Robins", "Sadie Spagnoli", "Sarah Preston", "Mackenzie Short", "Brynn Groves", "Cate Colman", "Abby Joe", "Siri Pemberton", "Taylor McIlvain", "Kamryn Lowery", "Emmy Pak", "Drew Shelton", "Ella Leininger", "May Downey", "Anika Novak", "Audrey Cooper", "Sarah Kester", "Hazel Wells", "Lauren Henderson", "Mrinali Ganta", "Parker Keston", "Farrah Childs", "Neela Juarez", "Dylan Kaufman", "Madeline Gottemoller", "Josie Daik", "Hadley Amann", "Sofia Bartkoski", "Ryleigh Montgomery", "Macie McKie", "Sofia Argoti", "Caitlin Van Sant", "Sarah Miller", "Sophie Coe", "Addison Starr", "Ava Dahlander", "Natalie Juarez", "Christa Hamlin", "Natalie Yoder", "Caroline Schulze", "Hasita Karthikeyan", "Megan Garza", "Margot Rosenband", "Jacqueline Olivier", "Giada Scaramuzza", "Molly Bogar", "Maria Sanchez", "Bella Champion", "Hannah Reilly", "Sofie Martinez", "Kaitlin Black", "Daisy Challoner", "Arani Walton", "Lily Robbins", "Olivia Alvarez", "Sophia Sayers", "Emma Levy", "Elizabeth Porter", "Skye Doughton", "Kassidy Bragg", "Caelyn Prochazka", "Taylor Jennings", "Victoria Olivarez", "Elena Solano", "Marie Jolie Day", "Ella Garber", "Braeleigh Garcia", "Zoey Bustamante", "Emma Schneidau", "Sophia Labazzo", "Anabel Precht", "Brooke Rosenberg", "Madison Taylor", "Sanya Hoskere", "Rishona Mopur", "Kate Belman", "Kate Neiman", "Katelyn Quintanilla", "Elizabeth Scull"]
VolleyballAct=["Sarah Preston", "Cate Colman", "Taylor McIlvain", "Kamryn Lowery", "Emmy Pak", "Drew Shelton", "Lauren Henderson", "Elyse Miller", "Neela Juarez", "Ryleigh Montgomery", "Alyssa Garcia", "Zoe Westbrook", "Caitlin Van Sant", "Sarah Miller", "Addison Starr", "Natalie Juarez", "Ema Avila", "Christa Hamlin", "Natalie Yoder", "Bella Champion", "Emmerich Benavides", "Lily Robbins", "Emma Levy", "Megan Garza", "Victoria Olivarez", "Maria Sepulveda", "Hannah Belenkiy", "Madison Taylor", "Kate Neiman", "Kirra Vrzal"]
WalksOutdoors=["Sophie Robins", "Claire Savage", "Sadie Spagnoli", "Sarah Preston", "Mackenzie Short", "Cate Colman", "Lee Lloyd", "Taylor McIlvain", "Kamryn Lowery", "Emmy Pak", "Ella Leininger", "May Downey", "Anika Novak", "Audrey Cooper", "Hazel Wells", "Annie Boeh", "Lauren Henderson", "Mrinali Ganta", "Parker Keston", "Farrah Childs", "Neela Juarez", "Dylan Kaufman", "Brooke Waldman", "Hadley Amann", "Katie Windell", "Andrea Yu", "Ryleigh Montgomery", "Morgan Gaitz", "Zoe Westbrook", "Caitlin Van Sant", "Jazlyn Mata", "Sarah Miller", "Sophie Coe", "Ava Dahlander", "Natalie Juarez", "Olivia Asay", "Abrielle Gallini", "Christa Hamlin", "Tatum Samuels", "Natalie Yoder", "Caroline Schulze", "Hasita Karthikeyan", "Megan Garza", "Margot Rosenband", "Audrey Jones", "Buckley Turner", "Giada Scaramuzza", "Molly Bogar", "Maria Sanchez", "Hannah Reilly", "Sofie Martinez", "Kaitlin Black", "Emmerich Benavides", "Daisy Challoner", "Arani Walton", "Lily Robbins", "Olivia Alvarez", "Jennifer Rosado", "Emma Levy", "Elizabeth Porter", "Skye Doughton", "Kassidy Bragg", "Giana Toothman", "Catherine Dooley", "Taylor Jennings", "Victoria Olivarez", "Emily Bull", "Elena Solano", "Elizabeth Perales", "Kate Flanery", "Kaelyn Liu", "Marie Jolie Day", "Ella Garber", "Braeleigh Garcia", "Izzy Davies", "Delaney O’Brien", "Annabelle Judson", "Hannah Belenkiy", "Zoe Veliz", "Zoey Bustamante", "Emma Schneidau", "Charlie Stone", "Annie Bryce", "Anabel Precht", "Brooke Rosenberg", "Sharon Yoon", "Madison Taylor", "Katie Walsh", "Sanya Hoskere", "Haylee Martin", "Rishona Mopur", "Kendall Klimek", "Kate Belman", "Katelyn Quintanilla", "Paola Castillo", "Elizabeth Scull"]
WaterSkiing=["Sophie Robins", "Emma Woods", "Taylor McIlvain", "Hadley Amann"]
WorkingOut=["Kamryn Jean", "Sophie Robins", "Claire Savage", "Sarah Preston", "Mackenzie Short", "Brynn Groves", "Cate Colman", "Emma Woods", "Siri Pemberton", "Taylor McIlvain", "Kamryn Lowery", "Drew Shelton", "Ella Leininger", "Sarah Kester", "Hazel Wells", "Lauren Henderson", "Elyse Miller", "Mrinali Ganta", "Parker Keston", "Dylan Kaufman", "Hadley Amann", "Katie Windell", "Ava Hodges", "Sofia Bartkoski", "Ryleigh Montgomery", "Alyssa Garcia", "Sofia Argoti", "Zoë Westbrook", "Caitlin Van Sant", "Jazlyn Mata", "Sarah Miller", "Sophie Coe", "Addison Starr", "Natalie Juarez", "Olivia Asay", "Abrielle Gallini", "Christa Hamlin", "Tatum Samuels", "Natalie Yoder", "Caroline Schulze", "Hasita Karthikeyan", "Megan Garza", "Margot Rosenband", "Audrey Jones", "Buckley Turner", "Giada Scaramuzza", "Molly Bogar", "Maria Sanchez", "Bella Champion", "Hannah Reilly", "Kaitlin Black", "Emmy Pak", "Emmerich Benavides", "Daisy Challoner", "Arani Walton", "Amorie Erichsen", "Lily Robbins", "Sophia Sayers", "Emma Levy", "Elizabeth Porter", "Skye Doughton", "Kimia Forouzesh", "Taylor Jennings", "Emily Bull", "Elizabeth Perales", "Kate Flanery", "Katie Corbin", "Ella Garber", "Braeleigh Garcia", "Izzy Davies", "Annabelle Judson", "Hannah Belenkiy", "Zoey Bustamante", "Annie Bryce", "Sharon Yoon", "Sanya Hoskere", "Rishona Mopur", "Andrea Yu", "Kendall Klimek", "Kate Belman", "Kate Neiman", "Paola Castillo", "Elizabeth Scull"]
Yoga=["Kamryn Jean", "Sophie Robins", "Claire Savage", "Brynn Groves", "Cate Colman", "Taylor McIlvain", "Kamryn Lowery", "Drew Shelton", "Ella Leininger", "Hazel Wells", "Lauren Henderson", "Parker Keston", "Neela Juarez", "Dylan Kaufman", "Brooke Waldman", "Sasha Pittsford", "Hadley Amann", "Morgan Gaitz", "Alyssa Garcia", "Jazlyn Mata", "Sarah Miller", "Sofia Bartkoski", "Addison Starr", "Ema Avila", "Abrielle Gallini", "Mia Cisneros", "Natalie Yoder", "Caroline Schulze", "Hasita Karthikeyan", "Buckley Turner", "Maria Sanchez", "Bella Champion", "Hannah Reilly", "Kaitlin Black", "Amorie Erichsen", "Lily Robbins", "Olivia Alvarez", "Sophia Sayers", "Skye Doughton", "Annie Bryce", "Brooke Rosenberg", "Sharon Yoon", "Rishona Mopur", "Andrea Yu", "Kate Belman", "Kate Neiman", "Katelyn Quintanilla", "Paola Castillo", "Elizabeth Scull"]

# OTHER ACTIVITIES / INTERESTS
Animals=["Kamryn Jean", "Sophie Robins", "Cate Colman", "Siri Pemberton", "Kamryn Lowery", "Emmy Pak", "Ella Leininger", "Anika Novak", "Audrey Cooper", "Lauren Henderson", "Katherine Blumenschein", "Mrinali Ganta", "Katie Windell", "Ava Hodges", "Sofia Bartkoski", "Ema Avila", "Morgan Gaitz", "Macie McKie", "Alyssa Garcia", "Sofie Combs", "Sofia Argoti", "Zoe Westbrook", "Jazlyn Mata", "Sarah Miller", "Audrey Jones", "Giada Scaramuzza", "Maria Sanchez", "Christa Hamlin", "Caroline Schulze", "Kassidy Bragg", "Caelyn Prochazka", "Victoria Olivarez", "Hadley Amann", "Elena Solano", "Elizabeth Perales", "Alexa Lira", "Sofie Arroyo", "Ryleigh Montgomery", "Delaney O’Brien", "Hannah Belenkiy", "Zoe Veliz", "Zoey Bustamante", "Emma Schneidau", "Annie Bryce", "Brooke Rosenberg", "Sharon Yoon", "Rishona Mopur", "Kate Neiman", "Elizabeth Scull"]
ArtsandCrafts=["Sophie Robins", "Cailyn Kelsen", "Gaby Green", "Cate Colman", "Abby Joe", "Emmy Pak", "Drew Shelton", "Ella Leininger", "May Downey", "Anika Novak", "Lauren Henderson", "Neela Juarez", "Katie Windell", "Katherine Blumenschein", "Macie McKie", "Alyssa Garcia", "Sofie Combs", "Zoë Westbrook", "Jazlyn Mata", "Sarah Miller", "Ava Dahlander", "Tatum Samuels", "Lexie Hale", "Audrey Jones", "Jacqueline Olivier", "Molly Bogar", "Amorie Erichsen", "Sophia Sayers", "Jennifer Rosado", "Angie Andersen", "Caelyn Prochazka", "Hadley Amann", "Elizabeth Perales", "Kate Flanery", "Marie Jolie Day", "Ella Garber", "Delaney O’Brien", "Zoe Veliz", "Zoey Bustamante", "Annie Bryce", "Brooke Rosenberg", "Sharon Yoon", "Andrea Yu", "Katelyn Quintanilla", "Paola Castillo", "Elizabeth Scull"]
Baking=["Claire Savage", "Sarah Preston", "Mackenzie Short", "Gaby Green", "Brynn Groves", "Cate Colman", "Emma Woods", "Celeste Gutierrez", "Siri Pemberton", "Lee Lloyd", "Taylor McIlvain", "Ella Leininger", "Anika Novak", "Lauren Henderson", "Katherine Blumenschein", "Mrinali Ganta", "Parker Keston", "Farrah Childs", "Neela Juarez", "Josie daik", "Hadley Amann", "Katie Windell", "Alyssa Garcia", "Sofie Combs", "Sophie Coe", "Addison Starr", "Ava Dahlander", "Natalie Juarez", "Olivia Asay", "Ema Avila", "Abrielle Gallini", "Mia Cisneros", "Christa Hamlin", "Tatum Samuels", "Zeina Saghiyyah", "Hasita Karthikeyan", "Lexie Hale", "Margot Rosenband", "Audrey Jones", "Jacqueline Olivier", "Buckley Turner", "Molly Bogar", "Maria Sanchez", "Bella Champion", "Kaitlin Black", "Emmy Pak", "Emmerich Benavides", "Arani Walton", "Amorie Erichsen", "Emma Levy", "Elizabeth Porter", "Angie Andersen", "Catherine Dooley", "Caelyn Prochazka", "Victoria Olivarez", "Jasmine Valdez", "Emily Bull", "Elena Solano", "Alexa Lira", "Kaelyn Liu", "Marie Jolie Day", "Sofie Arroyo", "Braeleigh Garcia", "Izzy Davies", "Zoe Veliz", "Zoey Bustamante", "Emma Schneidau", "Anabel Precht", "Brooke Rosenberg", "Sharon Yoon", "Rishona Mopur", "Kate Belman", "Katelyn Quintanilla", "Kirra Vrzal", "Paola Castillo"]
Blogging=["Madison Taylor"]
Boardgames=["Sophie Robins", "Claire Savage", "Mackenzie Short", "Siri Pemberton", "Drew Shelton", "Ella Leininger", "Lauren Henderson", "Mrinali Ganta", "Parker Keston", "Neela Juarez", "Hadley Amann", "Annabelle Judson", "Macie McKie", "Sofie Combs", "Abrielle Gallini", "Caroline Schulze", "Zeina Saghiyyah", "Hasita Karthikeyan", "Lexie Hale", "Audrey Jones", "Buckley Turner", "Kimia Forouzesh", "Caelyn Prochazka", "Giana Toothman", "Brooke Rosenberg", "Sharon Yoon", "Haylee Martin", "Rishona Mopur", "Zoey Bustamante", "Emma Schneidau", "Paola Castillo"]
CoffeeTea=["Sadie Spagnoli", "Sarah Preston", "Mackenzie Short", "Brynn Groves", "Cate Colman", "Abby Joe", "Kamryn Lowery", "Emmy Pak", "Ella Leininger", "May Downey", "Laraleigh Hackerman", "Anika Novak", "Hazel Wells", "Annie Boeh", "Lauren Henderson", "Elyse Miller", "Mrinali Ganta", "Farrah Childs", "Neela Juarez", "Katie Windell", "Sofia Bartkoski", "Addie Brooks", "Annie Hoag", "Annabelle Judson", "Ella Dillinger", "Macie McKie", "Sofia Argoti", "Zoë Westbrook", "Sarah Miller", "Sophie Coe", "Ava Dahlander", "Natalie Juarez", "Ema Avila", "Mia Cisneros", "Sofia Sayers", "Emma Levy", "Skye Doughton", "Kassidy Bragg", "Kimia Forouzesh", "Giana Toothman", "Taylor Jennings", "Victoria Olivarez", "Maria Sepulveda", "Emily Bull", "Hadley Amann", "Ollie Mae Harrison", "Kate Flanery", "Alexa Lira", "Marie Jolie Day", "Sofie Arroyo", "Ryleigh Montgomery", "Izzy Davies", "Annabelle Judson", "Hannah Belenkiy", "Zoe Veliz", "Zoey Bustamante", "Emma Schneidau", "Anabel Precht", "Sharon Yoon", "Sanya Hoskere", "Haylee Martin", "Rishona Mopur", "Andrea Yu", "Kate Belman", "Kate Neiman", "Katelyn Quintanilla", "Kirra Vrzal", "Paola Castillo", "Elizabeth Scull"]
Cooking = ["Claire Savage", "Sadie Spagnoli", "Mackenzie Short", "Brynn Groves", "Lee Lloyd", "Taylor McIlvain", "Anika Novak", "Katherine Blumenschein", "Mrinali Ganta", "Parker Keston", "Neela Juarez", "Sofia Bartkoski", "Addie Brooks", "Sofie Combs", "Zoë Westbrook", "Jazlyn Mata", "Sarah Miller", "Ava Dahlander", "Natalie Juarez", "Abrielle Gallini", "Mia Cisneros", "Tatum Samuels", "Caroline Schulze", "Megan Garza", "Lexie Hale", "Margot Rosenband", "Jacqueline Olivier", "Molly Bogar", "Maria Sanchez", "Bella Champion", "Hannah Reilly", "Kaitlin Black", "Emmy Pak", "Emmerich Benavides", "Arani Walton", "Amorie Erichsen", "Olivia Alvarez", "Sophia Labazzo", "Jennifer Rosado", "Emma Levy", "Angie Andersen", "Caelyn Prochazka", "Victoria Olivarez", "Maria Sepulveda", "Emily Bull", "Hadley Amann", "Elizabeth Perales", "Marie Jolie Day", "Ella Garber", "Sofie Arroyo", "Braeleigh Garcia", "Izzy Davies", "Delaney O’Brien", "Annie Bryce", "Brooke Rosenberg", "Sharon Yoon", "Rishona Mopur", "Andrea Yu", "Kate Belman", "Kate Neiman", "Katelyn Quintanilla", "Kirra Vrzal", "Paola Castillo", "Elizabeth Scull"]
CrochetKnitting=["Lauren Henderson", "Neela Juarez", "Katie Windell", "Ava Dahlander", "Ella Pitts", "Jacqueline Olivier", "Angie Andersen", "Alexa Lira", "Delaney O’Brien", "Zoe Veliz", "Sharon Yoon"]
Drawing=["Sophie Robins", "Drew Shelton", "Macie McKie", "Sofie Combs", "Natalie Juarez", "Tatum Samuels", "Jacqueline Olivier", "Amorie Erichsen", "Sophia Sayers", "Jennifer Rosado", "Angie Andersen", "Hadley Amann", "Kate Belman", "Katelyn Quintanilla", "Ella Garber", "Delaney O’Brien", "Zoe Veliz", "Sharon Yoon"]
ExploringNewRestaurants=["Sophie Robins", "Claire Savage", "Sadie Spagnoli", "Mackenzie Short", "Brynn Groves", "Georgia Key", "Taylor McIlvain", "Kamryn Lowery", "Ella Leininger", "May Downey", "Anika Novak", "Audrey Cooper", "Sarah Kester", "Hazel Wells", "Katherine Blumenschein", "Mrinali Ganta", "Parker Keston", "Farrah Childs", "Neela Juarez", "Dylan Kaufman", "Madeline Gottemoller", "Katie Windell", "Ava Hodges", "Ryleigh Montgomery", "Macie McKie", "Alyssa Garcia", "Sofie Combs", "Sofia Argoti", "Zoë Westbrook", "Jazlyn Mata", "Sarah Miller", "Abrielle Gallini", "Caroline Schulze", "Buckley Turner", "Molly Bogar", "Maria Sanchez", "Bella Champion", "Hannah Reilly", "Kaitlin Black", "Emmy Pak", "Emmerich Benavides", "Arani Walton", "Amorie Erichsen", "Lily Robbins", "Genesis Martinez", "Sophia Sayers", "Skye Doughton", "Kimia Forouzesh", "Giana Toothman", "Caelyn Prochazka", "Maria Sepulveda", "Emily Bull", "Hadley Amann", "Elizabeth Perales", "Kate Flanery", "Kaelyn Liu", "Marie Jolie Day", "Sofie Arroyo", "Braeleigh Garcia", "Annabelle Judson", "Hannah Belenkiy", "Zoe Veliz", "Zoey Bustamante", "Emma Schneidau", "Annie Bryce", "Anabel Precht", "Brooke Rosenberg", "Sharon Yoon", "Sanya Hoskere", "Haylee Martin", "Rishona Mopur", "Andrea Yu", "Kate Belman", "Kate Neiman", "Katelyn Quintanilla", "Kirra Vrzal", "Paola Castillo", "Elizabeth Scull"]
Formula1=["Sarah Preston", "Parker Keston", "Sofia Bartkoski", "Natalie Juarez", "Ava Dahlander", "Tatum Samuels", "Hasita Karthikeyan", "Hannah Dollinger", "Giada Scaramuzza", "Maria Sanchez", "Emmerich Benavides", "Sanya Hoskere", "Zoey Bustamante", "Marie Jolie Day", "Sofie Arroyo"]
Government=["Sophie Robins", "Sadie Spagnoli", "Cate Colman", "Emma Woods", "Siri Pemberton", "Kamryn Lowery", "Emmy Pak", "Drew Shelton", "Madeline Gottemoller", "Mrinali Ganta", "Sofia Bartkoski", "Ella Dillinger", "Zoë Westbrook", "Zeina Saghiyyah", "Hasita Karthikeyan", "Caroline Schulze", "Anabel Precht", "Charlie Stone", "Katie Walsh", "Lily Robbins", "Arani Walton", "Sharon Yoon", "Rishona Mopur", "Andrea Yu", "Sanya Hoskere"]
GraphicDesignInterest=["Emmy Pak", "Sasha Pittsford", "Andrea Yu", "Annabelle Judson", "Natalie Juarez", "Ella Dillinger", "Tatum Samuels", "Olivia Alvarez", "Marie Jolie Day", "Zoey Bustamante", "Abrielle Gallini", "Brooke Rosenberg", "Sharon Yoon", "Kate Belman", "Katelyn Quintanilla"]
Health=["Kamryn Jean", "Brynn Groves", "Cate Colman", "Kamryn Lowery", "Drew Shelton", "Audrey Cooper", "Hazel Wells", "Mrinali Ganta", "Parker Keston", "Farrah Childs", "Neela Juarez", "Andrea Yu", "Ryleigh Montgomery", "Sofia Argoti", "Zoë Westbrook", "Caitlin Van Sant", "Sarah Miller", "Sophie Coe", "Natalie Juarez", "Ema Avila", "Mia Cisneros", "Caroline Schulze", "Megan Garza", "Lexie Hale", "Audrey Jones", "Buckley Turner", "Maria Sanchez", "Emmerich Benavides", "Lily Robbins", "Emma Levy", "Elizabeth Porter", "Taylor Jennings", "Jasmine Valdez", "Maria Sepulveda", "Emily Bull", "Hadley Amann", "Sofie Arroyo", "Braeleigh Garcia", "Izzy Davies", "Annie Bryce", "Sharon Yoon", "Rishona Mopur", "Kate Neiman", "Sophia Labazzo", "Katelyn Quintanilla"]
Journaling=["Parker Keston"]
ListeningToMusic=["Kamryn Jean", "Sophie Robins", "Claire Savage", "Sadie Spagnoli", "Cailyn Kelsen", "Sarah Preston", "Mackenzie Short", "Brynn Groves", "Cate Colman", "Emma Woods", "Abby Joe", "Celeste Gutierrez", "Lee Lloyd", "Taylor McIlvain", "Kamryn Lowery", "Ella Leininger", "Anika Novak", "Audrey Cooper", "Hazel Wells", "Annie Boeh", "Lauren Henderson", "Elyse Miller", "Katherine Blumenschein", "Mrinali Ganta", "Parker Keston", "Farrah Childs", "Neela Juarez", "Dylan Kaufman", "Madeline Gottemoller", "Sasha Pittsford", "Hadley Amann", "Katie Windell", "Ava Hodges", "Sofia Bartkoski", "Addie Brooks", "Annie Hoag", "Annabelle Judson", "Macie McKie", "Alyssa Garcia", "Sofie Combs", "Sofia Argoti", "Zoë Westbrook", "Caitlin Van Sant", "Jazlyn Mata", "Sarah Miller", "Sophie Coe", "Addison Starr", "Ava Dahlander", "Natalie Juarez", "Olivia Asay", "Abrielle Gallini", "Mia Cisneros", "Christa Hamlin", "Tatum Samuels", "Caroline Schulze", "Zeina Saghiyyah", "Hasita Karthikeyan", "Megan Garza", "Margot Rosenband", "Jacqueline Olivier", "Buckley Turner", "Giada Scaramuzza", "Molly Bogar", "Maria Sanchez", "Bella Champion", "Hannah Reilly", "Kaitlin Black", "Emmy Pak", "Emmerich Benavides", "Daisy Challoner", "Arani Walton", "Kate Hoog", "Genesis Martinez", "Sophia Sayers", "Jennifer Rosado", "Emma Levy", "Elizabeth Porter", "Skye Doughton", "Kassidy Bragg", "Angie Andersen", "Kimia Forouzesh", "Giana Toothman", "Sammi Gill", "Caelyn Prochazka", "Victoria Olivarez", "Maria Sepulveda", "Emily Bull", "Ollie Mae Harrison", "Elizabeth Perales", "Kate Flanery", "Marie Jolie Day", "Ella Garber", "Sofie Arroyo", "Ryleigh Montgomery", "Braeleigh Garcia", "Izzy Davies", "Delaney O’Brien", "Annabelle Judson", "Hannah Belenkiy", "Zoe Veliz", "Zoey Bustamante", "Emma Schneidau", "Charlie Stone", "Annie Bryce", "Anabel Precht", "Brooke Rosenberg", "Sharon Yoon", "Katie Walsh", "Sanya Hoskere", "Haylee Martin", "Rishona Mopur", "Andrea Yu", "Kendall Klimek", "Kate Belman", "Kate Neiman", "Katelyn Quintanilla", "Kirra Vrzal", "Paola Castillo", "Elizabeth Scull"]
Musicals=["Sophie Robins", "Claire Savage", "Cate Colman", "Abby Joe", "Georgia Key", "Lee Lloyd", "Taylor McIlvain", "Hazel Wells", "Annie Boeh", "Lauren Henderson", "Elyse Miller", "Katherine Blumenschein", "Dylan Kaufman", "Andrea Yu", "Annie Hoag", "Zoë Westbrook", "Ava Dahlander", "Natalie Juarez", "Olivia Asay", "Tatum Samuels", "Zeina Saghiyyah", "Margot Rosenband", "Audrey Jones", "Hannah Reilly", "Kaitlin Black", "Emmy Pak", "Arani Walton", "Kate Hoog", "Charlie Stone", "Caelyn Prochazka", "Elizabeth Perales", "Kate Flanery", "Marie Jolie Day", "Izzy Davies", "Zoe Veliz", "Annie Bryce", "Brooke Rosenberg", "Sharon Yoon", "Katelyn Quintanilla", "Kate Neiman", "Paola Castillo"]
Needlepoint=["Hazel Wells"]
Painting=["Sophie Robins", "Sarah Preston", "Cate Colman", "Drew Shelton", "Lauren Henderson", "Mrinali Ganta", "Brooke Waldman", "Hadley Amann", "Macie McKie", "Sofie Combs", "Jazlyn Mata", "Ava Dahlander", "Natalie Juarez", "Ema Avila", "Tatum Samuels", "Giada Scaramuzza", "Lexie Hale", "Audrey Jones", "Jacqueline Olivier", "Molly Bogar", "Sophia Sayers", "Emma Levy", "Elena Solano", "Elizabeth Perales", "Kate Belman", "Katelyn Quintanilla", "Sharon Yoon"]
Philosophy=["Cate Colman", "Emma Woods", "Siri Pemberton", "Lee Lloyd", "Kamryn Lowery", "Ella Leininger", "Mrinali Ganta", "Zoë Westbrook", "Lily Robbins", "Ella Dillinger", "Tatum Samuels", "Sharon Yoon", "Annie Bryce", "Katelyn Quintanilla"]
Photography=["Kamryn Lowery", "Emmy Pak", "Sasha Pittsford", "Jazlyn Mata", "Sarah Miller", "Ava Dahlander", "Natalie Juarez", "Ema Avila", "Abrielle Gallini", "Tatum Samuels", "Megan Garza", "Audrey Jones", "Maria Sanchez", "Skye Doughton", "Sophia Sayers", "Giana Toothman", "Brooke Rosenberg", "Sharon Yoon", "Katelyn Quintanilla", "Kate Flanery", "Elizabeth Perales", "Marie Jolie Day"]
PlayingPercussionInstrument=["Cate Colman", "Sofia Bartkoski", "Natalie Juarez", "Olivia Alvarez", "Jacqueline Olivier", "Hannah Reilly", "Kaitlin Black", "Elizabeth Perales", "Brooke Rosenberg", "Kimia Forouzesh", "Caelyn Prochazka", "Kendall Klimek", "Marie Jolie Day"]
PlayingStringInstrument=["Cate Colman", "Annie Hoag", "Ava Dahlander", "Hasita Karthikeyan", "Hannah Reilly", "Katie Corbin", "Delaney O’Brien", "Paola Castillo"]
PlayingWindInstrument=["Drew Shelton", "Kate Flanery"]
Podcasts=["Claire Savage", "Cate Colman", "Lee Lloyd", "Kamryn Lowery", "Sarah Kester", "Hazel Wells", "Elyse Miller", "Dylan Kaufman", "Katie Windell", "Ryleigh Montgomery", "Annabelle Judson", "Morgan Gaitz", "Ava Dahlander", "Natalie Juarez", "Olivia Asay", "Ema Avila", "Mia Cisneros", "Caroline Schulze", "Megan Garza", "Audrey Jones", "Giada Scaramuzza", "Maria Sanchez", "Hannah Reilly", "Emmy Pak", "Daisy Challoner", "Giana Toothman", "Sammi Gill", "Catherine Dooley", "Caelyn Prochazka", "Taylor Jennings", "Kendall Klimek", "Annie Bryce", "Brooke Rosenberg", "Sharon Yoon", "Andrea Yu", "Katelyn Quintanilla", "Elizabeth Perales", "Marie Jolie Day", "Sofie Arroyo", "Izzy Davies"]
PotteryCeramics=["Gaby Green", "May Downey", "Neela Juarez", "Addie Brooks", "Jazlyn Mata", "Sarah Miller", "Olivia Asay", "Arani Walton", "Lily Robbins", "Jacqueline Olivier", "Sharon Yoon", "Marie Jolie Day", "Sofie Arroyo", "Kate Belman", "Katelyn Quintanilla"]
Reading=["Sadie Spagnoli", "Sarah Preston", "Cate Colman", "Georgia Key", "Siri Pemberton", "Taylor McIlvain", "Kamryn Lowery", "Drew Shelton", "Hazel Wells", "Lauren Henderson", "Katherine Blumenschein", "Mrinali Ganta", "Dylan Kaufman", "Madeline Gottemoller", "Sasha Pittsford", "Hadley Amann", "Katie Windell", "Andrea Yu", "Annie Hoag", "Macie McKie", "Sofia Argoti", "Zoë Westbrook", "Sarah Miller", "Sophie Coe", "Addison Starr", "Ava Dahlander", "Olivia Asay", "Ema Avila", "Mia Cisneros", "Natalie Yoder", "Caroline Schulze", "Zeina Saghiyyah", "Hasita Karthikeyan", "Megan Garza", "Audrey Jones", "Buckley Turner", "Maria Sanchez", "Bella Champion", "Hannah Reilly", "Ella Pitts", "Emmy Pak", "Daisy Challoner", "Arani Walton", "Lily Robbins", "Sophia Sayers", "Jennifer Rosado", "Emma Levy", "Taylor Jennings", "Ollie Mae Harrison", "Kassidy Bragg", "Giana Toothman", "Sammi Gill", "Caelyn Prochazka", "Anabel Precht", "Brooke Rosenberg", "Sharon Yoon", "Haylee Martin", "Elizabeth Perales", "Kate Flanery", "Marie Jolie Day", "Ella Garber", "Ryleigh Montgomery", "Braeleigh Garcia", "Delaney O’Brien", "Zoe Veliz", "Emma Schneidau", "Charlie Stone", "Kate Neiman", "Katelyn Quintanilla", "Paola Castillo", "Elizabeth Scull"]
RoadTrips=["Sophie Robins", "Sadie Spagnoli", "Sarah Preston", "Brynn Groves", "Cate Colman", "Georgia Key", "Taylor McIlvain", "Kamryn Lowery", "Emmy Pak", "Ella Leininger", "May Downey", "Anika Novak", "Audrey Cooper", "Sarah Kester", "Hazel Wells", "Annie Boeh", "Lauren Henderson", "Mrinali Ganta", "Parker Keston", "Neela Juarez", "Sofia Bartkoski", "Sofia Argoti", "Zoë Westbrook", "Sarah Miller", "Ava Dahlander", "Natalie Juarez", "Tatum Samuels", "Caroline Schulze", "Zeina Saghiyyah", "Hasita Karthikeyan", "Megan Garza", "Margot Rosenband", "Buckley Turner", "Giada Scaramuzza", "Molly Bogar", "Maria Sanchez", "Hannah Reilly", "Kaitlin Black", "Arani Walton", "Lily Robbins", "Skye Doughton", "Sanya Hoskere", "Haylee Martin", "Giana Toothman", "Caelyn Prochazka", "Kate Flanery", "Marie Jolie Day", "Ella Garber", "Sofie Arroyo", "Braeleigh Garcia"]
ScienceMarineScienceEcology=["Cailyn Kelsen", "Kamryn Lowery", "Mrinali Ganta", "Andrea Yu", "Ryleigh Montgomery", "Hadley Amann", "Christa Hamlin", "Zeina Saghiyyah", "Giada Scaramuzza", "Maria Sanchez", "Daisy Challoner", "Skye Doughton", "Lily Robbins", "Elizabeth Perales", "Izzy Davies"]
Scrapbooking=["Sophie Robins", "Cate Colman", "Emmy Pak", "Anika Novak", "Lauren Henderson", "Morgan Gaitz", "Sasha Pittsford", "Jazlyn Mata", "Sarah Miller", "Ava Dahlander", "Olivia Asay", "Zoë Westbrook", "Emma Levy", "Angie Andersen", "Caelyn Prochazka", "Arani Walton", "Andrea Yu", "Madison Taylor", "Braeleigh Garcia", "Ella Garber", "Brooke Rosenberg", "Sharon Yoon"]
Sewing=["Lee Lloyd"]
Shopping=["Kamryn Jean", "Sophie Robins", "Claire Savage", "Sadie Spagnoli", "Georgia Key", "Taylor McIlvain", "Kamryn Lowery", "Drew Shelton", "Ella Leininger", "May Downey", "Anika Novak", "Audrey Cooper", "Hazel Wells", "Annie Boeh", "Lauren Henderson", "Elyse Miller", "Katherine Blumenschein", "Mrinali Ganta", "Parker Keston", "Dylan Kaufman", "Madeline Gottemoller", "Josie daik", "Brooke Waldman", "Sasha Pittsford", "Ava Hodges", "Ryleigh Montgomery", "Annabelle Judson", "Morgan Gaitz", "Macie McKie", "Sofia Argoti", "Zoë Westbrook", "Jazlyn Mata", "Sarah Miller", "Sophie Coe", "Addison Starr", "Ava Dahlander", "Natalie Juarez", "Olivia Asay", "Ema Avila", "Abrielle Gallini", "Mia Cisneros", "Christa Hamlin", "Caroline Schulze", "Zeina Saghiyyah", "Hasita Karthikeyan", "Megan Garza", "Lexie Hale", "Audrey Jones", "Jacqueline Olivier", "Buckley Turner", "Molly Bogar", "Maria Sanchez", "Bella Champion", "Hannah Reilly", "Sofie Martinez", "Kaitlin Black", "Emmy Pak", "Emmerich Benavides", "Daisy Challoner", "Arani Walton", "Lily Robbins", "Kate Hoog", "Sophia Sayers", "Jennifer Rosado", "Emma Levy", "Elizabeth Porter", "Skye Doughton", "Kassidy Bragg", "Kimia Forouzesh", "Giana Toothman", "Sammi Gill", "Catherine Dooley", "Caelyn Prochazka", "Taylor Jennings", "Victoria Olivarez", "Maria Sepulveda", "Emily Bull", "Hadley amann", "Elizabeth Perales", "Kate Flanery", "Katie Corbin", "Kaelyn Liu", "Marie Jolie Day", "Sofie Arroyo", "Braeleigh Garcia", "Delaney O’Brien", "Annabelle Judson", "Hannah Belenkiy", "Zoe Veliz", "Zoey Bustamante", "Emma Schneidau", "Anabel Precht", "Brooke Rosenberg", "Sharon Yoon", "Sanya Hoskere", "Haylee Martin", "Rishona Mopur", "Andrea Yu", "Kendall Klimek", "Kate Belman", "Katelyn Quintanilla", "Kirra Vrzal", "Paola Castillo", "Elizabeth Scull"]
Singing=["Cate Colman", "Abby Joe", "Taylor McIlvain", "Katherine Blumenschein", "Addie Brooks", "Annie Hoag", "Alyssa Garcia", "Christa Hamlin", "Tatum Samuels", "Zeina Saghiyyah", "Ava Dahlander", "Kaitlin Black", "Emmy Pak", "Arani Walton", "Kimia Forouzesh", "Caelyn Prochazka", "Brooke Rosenberg", "Katelyn Quintanilla", "Marie Jolie Day"]
Skincare=["Mackenzie Short", "Gaby Green", "Abby Joe", "Kamryn Lowery", "Emmy Pak", "Anika Novak", "Audrey Cooper", "Hazel Wells", "Sasha Pittsford", "Brooke Waldman", "Andrea Yu", "Jazlyn Mata", "Sarah Miller", "Ava Dahlander", "Natalie Juarez", "Ema Avila", "Abrielle Gallini", "Mia Cisneros", "Christa Hamlin", "Caroline Schulze", "Hasita Karthikeyan", "Megan Garza", "Lexie Hale", "Audrey Jones", "Giada Scaramuzza", "Maria Sanchez", "Bella Champion", "Ella Pitts", "Sofie Martinez", "Kaitlin Black", "Taylor Jennings", "Jasmine Valdez", "Maria Sepulveda", "Elena Solano", "Ollie Mae Harrison", "Kate Flanery", "Alexa Lira", "Sofie Arroyo", "Braeleigh Garcia", "Sophia Labazzo", "Katelyn Quintanilla", "Kirra Vrzal", "Paola Castillo", "Elizabeth Scull"]
SocialMedia=["Kamryn Jean", "Sophie Robins", "Mackenzie Short", "Abby Joe", "Georgia Key", "Celeste Gutierrez", "Kamryn Lowery", "Ella Leininger", "Laraleigh Hackerman", "Anika Novak", "Audrey Cooper", "Hazel Wells", "Annie Boeh", "Lauren Henderson", "Elyse Miller", "Katherine Blumenschein", "Parker Keston", "Dylan Kaufman", "Josie daik", "Sasha Pittsford", "Sofie Martinez", "Ava Hodges", "Ryleigh Montgomery", "Addie Brooks", "Annabelle Judson", "Morgan Gaitz", "Macie McKie", "Alyssa Garcia", "Sofia Argoti", "Zoë Westbrook", "Jazlyn Mata", "Sarah Miller", "Ava Dahlander", "Natalie Juarez", "Olivia Asay", "Ema Avila", "Mia Cisneros", "Christa Hamlin", "Caroline Schulze", "Kaitlin Black", "Emmy Pak", "Daisy Challoner", "Arani Walton", "Kate Hoog", "Sophia Sayers", "Emma Levy", "Elizabeth Porter", "Skye Doughton", "Kassidy Bragg", "Kimia Forouzesh", "Giana Toothman", "Sammi Gill", "Caelyn Prochazka", "Victoria Olivarez", "Maria Sepulveda", "Rishona Mopur", "Kendall Klimek", "Kate Belman", "Katelyn Quintanilla", "Kirra Vrzal", "Paola Castillo", "Elizabeth Scull", "Braeleigh Garcia", "Zoe Veliz", "Zoey Bustamante", "Emma Schneidau", "Annie Bryce", "Brooke Rosenberg", "Sharon Yoon", "Madison Taylor", "Sanya Hoskere", "Haylee Martin", "Andrea Yu", "Alexa Lira", "Kaelyn Liu"]
TwoSteppingLineDancing=["Annabelle Judson"]
Vlogging=["Sophie Robins", "Abby Joe", "Kamryn Lowery", "Audrey Cooper", "Hazel Wells", "Annie Boeh", "Sofie Martinez", "Ava Hodges", "Ryleigh Montgomery", "Natalie Juarez", "Olivia Asay", "Ema Avila", "Alyssa Garcia", "Sofia Argoti", "Jazlyn Mata", "Sasha Pittsford", "Caroline Schulze", "Giada Scaramuzza", "Maria Sanchez", "Emmy Pak", "Arani Walton", "Lily Robbins", "Elizabeth Porter", "Sofie Arroyo", "Rishona Mopur", "Maria Sepulveda", "Katelyn Quintanilla", "Elizabeth Scull", "Sharon Yoon", "Haylee Martin", "Annie Bryce", "Zoe Veliz", "Zoey Bustamante"]
WatchingSports=["Sophie Robins", "Sarah Preston", "Mackenzie Short", "Emma Woods", "Siri Pemberton", "Taylor McIlvain", "Drew Shelton", "Anika Novak", "Audrey Cooper", "Lauren Henderson", "Parker Keston", "Madeline Gottemoller", "Hadley Amann", "Ava Hodges", "Annabelle Judson", "Macie McKie", "Sophie Coe", "Addison Starr", "Natalie Juarez", "Abrielle Gallini", "Caroline Schulze", "Zeina Saghiyyah", "Hasita Karthikeyan", "Hannah Dollinger", "Megan Garza", "Audrey Jones", "Buckley Turner", "Giada Scaramuzza", "Maria Sanchez", "Bella Champion", "Hannah Reilly", "Emmy Pak", "Daisy Challoner", "Arani Walton", "Lily Robbins", "Sophia Sayers", "Jennifer Rosado", "Emma Levy", "Skye Doughton", "Kimia Forouzesh", "Caelyn Prochazka", "Victoria Olivarez", "Elizabeth Perales", "Kate Flanery", "Marie Jolie Day", "Annabelle Judson", "Zoey Bustamante", "Annie Bryce", "Brooke Rosenberg", "Madison Taylor", "Sanya Hoskere", "Haylee Martin", "Kendall Klimek", "Kate Belman", "Kirra Vrzal", "Paola Castillo"]
WatchingTVMovies=["Sophie Robins", "Sarah Preston", "Mackenzie Short", "Emma Woods", "Georgia Key", "Celeste Gutierrez", "Lee Lloyd", "Taylor McIlvain", "Kamryn Lowery", "Ella Leininger", "May Downey", "Laraleigh Hackerman", "Anika Novak", "Hazel Wells", "Annie Boeh", "Lauren Henderson", "Elyse Miller", "Katherine Blumenschein", "Mrinali Ganta", "Parker Keston", "Dylan Kaufman", "Madeline Gottemoller", "Josie daik", "Brooke Waldman", "Sasha Pittsford", "Hadley Amann", "Ava Hodges", "Sofia Bartkoski", "Addie Brooks", "Annie Hoag", "Annabelle Judson", "Macie McKie", "Alyssa Garcia", "Sofie Combs", "Sofia Argoti", "Zoë Westbrook", "Jazlyn Mata", "Sarah Miller", "Sophie Coe", "Addison Starr", "Natalie Juarez", "Olivia Asay", "Abrielle Gallini", "Mia Cisneros", "Christa Hamlin", "Caroline Schulze", "Zeina Saghiyyah", "Hasita Karthikeyan", "Megan Garza", "Margot Rosenband", "Audrey Jones", "Buckley Turner", "Maria Sanchez", "Bella Champion", "Hannah Reilly", "Ella Pitts", "Kaitlin Black", "Emmy Pak", "Emmerich Benavides", "Daisy Challoner", "Arani Walton", "Sophia Sayers", "Jennifer Rosado", "Emma Levy", "Skye Doughton", "Kassidy Bragg", "Angie Andersen", "Caelyn Prochazka", "Victoria Olivarez", "Jasmine Valdez", "Maria Sepulveda", "Emily Bull", "Elizabeth Perales", "Kate Flanery", "Marie Jolie Day", "Ella Garber", "Izzy Davies", "Delaney O’Brien", "Annabelle Judson", "Hannah Belenkiy", "Zoe Veliz", "Zoey Bustamante", "Emma Schneidau", "Annie Bryce", "Anabel Precht", "Brooke Rosenberg", "Sharon Yoon", "Sanya Hoskere", "Haylee Martin", "Rishona Mopur", "Andrea Yu", "Kendall Klimek", "Kate Belman", "Kate Neiman", "Katelyn Quintanilla", "Kirra Vrzal", "Paola Castillo", "Elizabeth Scull"]
Writing=["Cate Colman", "Lee Lloyd", "Kamryn Lowery", "Hazel Wells", "Annie Boeh", "Sasha Pittsford", "Zoë Westbrook", "Mia Cisneros", "Lily Robbins", "Jacqueline Olivier", "Kaitlin Black", "Arani Walton", "Ella Garber", "Elizabeth Porter", "Annie Bryce", "Brooke Rosenberg", "Sharon Yoon", "Katelyn Quintanilla", "Kate Flanery"]

# TRANSFER
transfer = ["Josie daik", "Sasha Pittsford", "Addie Brooks", "Sofia Argoti", "Addison Starr", "Ema Avila", "Mia Cisneros", "Caroline Schulze", "Maria Sanchez", "Lily Robbins", "Kassidy Bragg", "Alexa Lira", "Emma Schneidau", "Paola Castillo"]
UTA = ["Sasha Pittsford", "Caroline Schulze"]
TexasTech = ["Addie Brooks"]
UTEP = ["Sofia Argoti"]
TuftsUniversity = ["Addison Starr"]
UTSA = ["Ema Avila", "Maria Sanchez", "Kassidy Bragg", "Alexa Lira", "Emma Schneidau", "Paola Castillo"]
UTRGV = ["Mia Cisneros"]
TrinityUniversity = ["Lily Robbins"]


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
        "Health Promotion & Behavioral Science": HealthPromotion, 
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
        "Arabic Minor": ArabicMinor,
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
    "Pre Health": PreHealth,
    "Pre Law": PreLaw,
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
    "Washington": Washington,
    "Washington DC": WashingtonDC
}

utorgs = {
    "Advertising Org": AdvertisingOrg,
    "Art": ArtOrg,
    "Business/Finance/Marketing/Economics": BusinessFinanceMarketingEconomics,
    "Cultural Org": CulturalOrg,
    "Environmental Science Org": EnvironmentalScienceOrg,
    "Government Org": GovernmentOrg,
    "Intramural Sports": IntramuralSports,
    "Performing Arts Org": PerformingArtsOrg,
    "Publications": Publications,
    "Religious": ReligiousOrg,
    "Social Interest/Activism": SocialInterestActivism,
    "Spirit Organization": SpiritOrg,
    "STEM": STEM,
    "Student Television (TSTV/KVRX)": Student_Television,
    "Texas Wake": TexasWake,
    "Volunteer": Volunteer
}

# MUSIC ARTISTS

music = {
    "Taylor Swift": TaylorSwift,
    "Adele": Adele,
    "Ariana Grande": ArianaGrande,
    "ASAP Rocky": ASAPRocky,
    "Beyoncé": Beyonce,
    "Bruno Mars": BrunoMars,
    "Cardi B": CardiB,
    "Central Cee": CentralCee,
    "Charley Crockett": CharleyCrockett,
    "Charli XCX": CharliXCX,
    "Chris Stapleton": ChrisStapleton,
    "Clairo": Clairo,
    "Cody Johnson": CodyJohnson,
    "Conan Gray": ConanGray,
    "David Bowie": DavidBowie,
    "Djo": Djo,
    "Doja Cat": DojaCat,
    "Don Toliver": DonToliver,
    "Ella Langley": EllaLangley,
    "Elvis": Elvis,
    "Etta James": EttaJames,
    "Flatland Cavalry": FlatlandCavalry,
    "Fleetwood Mac": FleetwoodMac,
    "Foo Fighters": FooFighters,
    "Frank Ocean": FrankOcean,
    "Glass Animals": GlassAnimals,
    "GloRilla": GloRilla,
    "Gracie Abrams": GracieAbrams,
    "Halsey": Halsey,
    "House Music": HouseMusic,
    "Hozier": Hozier,
    "Hudson Westbrook": HudsonWestbrook,
    "Imagine Dragons": ImagineDragons,
    "John Summit": JohnSummit,
    "Jon Pardi": JonPardi,
    "Justin Bieber": JustinBieber,
    "K-Pop": KPop,
    "Kali Uchis": KaliUchis,
    "Kanye": Kanye,
    "Kendrick Lamar": KendrickLamar,
    "Khalid": Khalid,
    "Lady Gaga": LadyGaga,
    "Laufey": Laufey,
    "Led Zeppelin": LedZeppelin,
    "Lizzy McAlpine": LizzyMcAlpine,
    "Lorde": Lorde,
    "Luke Bryan": LukeBryan,
    "Luke Combs": LukeCombs,
    "Mac DeMarco": MacDeMarco,
    "Mac Miller": MacMiller,
    "Megan Moroney": MeganMoroney,
    "Megan Thee Stallion": MeganTheeStallion,
    "Morgan Wallen": MorganWallen,
    "Mt. Joy": MtJoy,
    "Niall Horan": NiallHoran,
    "Noah Kahan": NoahKahan,
    "Oasis": Oasis,
    "Olivia Rodrigo": OliviaRodrigo,
    "P!nk": Pink,
    "Paramore": Paramore,
    "Playboi Carti": PlayboiCarti,
    "Randy Travis": RandyTravis,
    "Red Hot Chili Peppers": RedHotChiliPeppers,
    "Rihanna": Rihanna,
    "Role Model": RoleModel,
    "Rolling Stones": RollingStones,
    "Sabrina Carpenter": SabrinaCarpenter,
    "Sienna Spiro": SiennaSpiro,
    "Sublime": Sublime,
    "Tame Impala": TameImpala,
    "Tate McRae": TateMcRae,
    "The 1975": The1975,
    "The Backseat Lovers": TheBackseatLovers,
    "The Beatles": TheBeatles,
    "The Cure": TheCure,
    "The Eagles": TheEagles,
    "The Lumineers": TheLumineers,
    "The Neighborhood": TheNeighborhood,
    "The Weeknd": TheWeeknd,
    "Treaty Oak Revival": TreatyOakRevival,
    "Twenty One Pilots": TwentyOnePilots,
    "Ty Myers": TyMyers,
    "Tyler Childers": TylerChilders,
    "Tyler the Creator": TylerTheCreator,
    "Wallows": Wallows,
    "Zach Bryan": ZachBryan,
    "Zach Top": ZachTop,
}

summercamps = {
        "ACU Leadership Camps": ACULeadershipCamps,
        "Area Health Education Center (AHEC) Camp": AreaHealthEducationCenterAHECCamp,
        "Camp Agawak": CampAgawak,
        "Camp Allen": CampAllen,
        "Camp Beloved and Beyond": CampBelovedandBeyond,
        "Camp ChoYeh": CampChoYeh,
        "Camp Deer Run": CampDeerRun,
        "Camp Laurelwood": CampLaurelwood,
        "Camp Lonestar": CampLonestar,
        "Camp Longhorn": CampLonghorn,
        "Camp Longhorn Indian Springs": CampLonghornIndianSprings,
        "Camp Longhorn Inks Lake": CampLonghornInksLake,
        "Camp Mystic": CampMystic,
        "Camp Olympia": CampOlympia,
        "Camp Ozark": CampOzark,
        "Camp Pine Springs": CampPineSprings,
        "Camp Ramah": CampRamah,
        "Camp Texas": CampTexas,
        "Camp Thurman": CampThurman,
        "Camp Waldemar": CampWaldemar,
        "Catalina Island Camps": CatalinaIslandCamps,
        "Church Camp": ChurchCamp,
        "Fifth grade camp": Fifthgradecamp,
        "GeoFORCE Texas Summer Academies": GeoFORCETexasSummerAcademies,
        "Ignite Texas": IgniteTexas,
        "Kickapoo": Kickapoo,
        "Laity Lodge Youth Camp": LaityLodgeYouthCamp,
        "Mission Trips": MissionTrips,
        "NASA Summer Program": NASASummerProgram,
        "National Cheerleading Association Camp": NationalCheerleadingAssociationCamp,
        "National Hispanic Institute College World Series Summer Program": NationalHispanicInstituteCollegeWorldSeriesSummerProgram,
        "National Hispanic Institute Texas Lorenzo De Zavala Program": NationalHispanicInstituteTexasLorenzoDeZavalaProgram,
        "Pine Cove": PineCove,
        "Pineywoods Church Camp": PineywoodsChurchCamp,
        "Sandy Hill Camp": SandyHillCamp,
        "Sky Ranch": SkyRanch,
        "St Marys Summer Camps": StMarysSummerCamps,
        "Super Summer at Dallas Baptist University": SuperSummeratDallasBaptistUniversity,
        "T bar M Camp": TbarMCamp,
        "TCU Wilson Tennis Camp": TCUWilsonTennisCamp,
        "Tapia STEM Camps at Rice University": TapiaSTEMCampsatRiceUniversity,
        "Texas Girls State Program": TexasGirlsStateProgram,
        "Theatre Camp": TheatreCamp,
        "Timberlake Camp": TimberlakeCamp,
        "UT Computer Science Academy for All": UTComputerScienceAcademyforAll,
        "UT Volleyball Camp": UTVolleyballCamp,
        "Vacation Bible School": VacationBibleSchool,
        "YMCA Summer Camp": YMCASummerCamp,
        "YoungLife Camp": YoungLifeCamp,
        "YoungLife Crooked Creek": YoungLifeCrookedCreek,
        "YoungLife Lone Hollow Ranch": YoungLifeLoneHollowRanch,
        "YoungLife Wilderness": YoungLifeWilderness
}

books = {
        "1984": NineteenEightyFour,
        "A Little Life": ALittleLife,
        "A Series of Unfortunate Events": ASeriesofUnfortunateEvents,
        "A Thousand Splendid Suns": AThousandSplendidSuns,
        "ACOTAR": ACOTAR,
        "Abby Jimenez": AbbyJimenez,
        "American Dirt": AmericanDirt,
        "Animal Farm": AnimalFarm,
        "Anything fantasy": Anythingfantasy,
        "Anything thrilling/mystery": Anythingthrillingmystery,
        "Atomic Habits": AtomicHabits,
        "Beach Read": BeachRead,
        "Before the Coffee Gets Cold": BeforetheCoffeeGetsCold,
        "Better Than the Movies": BetterThantheMovies,
        "Binding 13": Binding13,
        "Boys of Tommen Series": BoysofTommenSeries,
        "Call It What You Want": CallItWhatYouWant,
        "Call Me By Your Name": CallMeByYourName,
        "Christian Living Books": ChristianLivingBooks,
        "Circe": Circe,
        "Conversations with Friends": ConversationswithFriends,
        "Daisy Jones and The Six": DaisyJonesandTheSix,
        "Diary of A Wimpy Kid": DiaryOfAWimpyKid,
        "Emily Henry": EmilyHenry,
        "Emma": Emma,
        "Everything I Know About Love": EverythingIKnowAboutLove,
        "Fahrenheit 451": Fahrenheit451,
        "Float": Float,
        "Fourth Wing": FourthWing,
        "Freida McFadden": FreidaMcFadden,
        "Giovannis Room": GiovannisRoom,
        "God of the Woods": GodoftheWoods,
        "Great Big Beautiful Life": GreatBigBeautifulLife,
        "Happy Place": HappyPlace,
        "Harry Potter": HarryPotter,
        "Heated Rivalry": HeatedRivalry,
        "If Only I Had Told Him": IfOnlyIHadToldHim,
        "Im Glad My Mom Died": ImGladMyMomDied,
        "It": It,
        "Jane Austen": JaneAusten,
        "Keeping 13": Keeping13,
        "Lessons in Chemistry": LessonsinChemistry,
        "Little Women": LittleWomen,
        "Looking for Alaska": LookingforAlaska,
        "Love and Gelato": LoveandGelato,
        "Meet Me at the Lake": MeetMeattheLake,
        "Men Who Hate Women": MenWhoHateWomen,
        "Misery": Misery,
        "Normal People": NormalPeople,
        "Notes on an Execution": NotesonanExecution,
        "Off Campus Series": OffCampusSeries,
        "One Day in December": OneDayinDecember,
        "One Last Stop": OneLastStop,
        "People We Meet on Vacation": PeopleWeMeetonVacation,
        "Percy Jackson": PercyJackson,
        "Powerless": Powerless,
        "Pride and Prejudice": PrideandPrejudice,
        "Ready Player One": ReadyPlayerOne,
        "Red Queen Series": RedQueenSeries,
        "Red Rising": RedRising,
        "Red White and Royal Blue": RedWhiteandRoyalBlue,
        "Rom Com books": RomCombooks,
        "Romance books": Romancebooks,
        "Shatter Me": ShatterMe,
        "Six of Crows": SixofCrows,
        "Slow Days Fast Company": SlowDaysFastCompany,
        "Stephen King": StephenKing,
        "Sylvia Plath": SylviaPlath,
        "The Alchemist": TheAlchemist,
        "The Conditions of Will": TheConditionsofWill,
        "The Crimson Moth": TheCrimsonMoth,
        "The Cruel Prince": TheCruelPrince,
        "The Deal": TheDeal,
        "The Dinner List": TheDinnerList,
        "The Fault in Our Stars": TheFaultinOurStars,
        "The Final Girl Support Group": TheFinalGirlSupportGroup,
        "The Giver": TheGiver,
        "The Glass Castle": TheGlassCastle,
        "The Goldfinch": TheGoldfinch,
        "The Great Alone": TheGreatAlone,
        "The Great Gatsby": TheGreatGatsby,
        "The Hunger Games": TheHungerGames,
        "The Invisible Life of Addie Larue": TheInvisibleLifeofAddieLarue,
        "The Knight and the Moth": TheKnightandtheMoth,
        "The Last Olympian": TheLastOlympian,
        "The Let Them Theory": TheLetThemTheory,
        "The Mill on the Floss": TheMillontheFloss,
        "The Nightingale": TheNightingale,
        "The Outsiders": TheOutsiders,
        "The Perks of Being a Wallflower": ThePerksofBeingaWallflower,
        "The Posoinnwood Bible": ThePosoinnwoodBible,
        "The Secret History": TheSecretHistory,
        "The Secret Life of Bees": TheSecretLifeofBees,
        "The Selection": TheSelection,
        "The Seven Husbands of Evelyn Hugo": TheSevenHusbandsofEvelynHugo,
        "The Shinning": TheShinning,
        "The Silent Patient": TheSilentPatient,
        "The Stand": TheStand,
        "The Summer I Turned Pretty": TheSummerITurnedPretty,
        "The Summer of Broken Rules": TheSummerofBrokenRules,
        "The Tattooist": TheTattooist,
        "The Unmaking of June Farrow": TheUnmakingofJuneFarrow,
        "The Vanishing Half": TheVanishingHalf,
        "The Wall of Winnipeg and Me": TheWallofWinnipegandMe,
        "Things We Never Got Over": ThingsWeNeverGotOver,
        "Throne of Glass": ThroneofGlass,
        "Tiny Beautiful Things": TinyBeautifulThings,
        "To All the Boys Ive Loved Before": ToAlltheBoysIveLovedBefore,
        "To Kill a Mockingbird": ToKillaMockingbird,
        "Tuesdays with Morrie": TuesdayswithMorrie,
        "Twilight Saga": TwilightSaga,
        "Ugly Love": UglyLove,
        "Verity": Verity,
        "We Have Always Lived in the Castle": WeHaveAlwaysLivedintheCastle,
        "Where the Crawdads Sing": WheretheCrawdadsSing,
        "Wide Sargasso Sea": WideSargassoSea,
        "Windy City Series": WindyCitySeries,
        "Wonder": Wonder,
        "Wuthering Heights": WutheringHeights,
        "You Are a Badass": YouAreaBadass
}

sports = {
    "Badminton": Badminton,
    "Ballet": Ballet,
    "Basketball": Basketball,
    "Cheerleading": Cheerleading,
    "Cross Country": CrossCountry,
    "Dance Team": DanceTeam,
    "Drill Team": DrillTeam,
    "Equestrian / Horse Riding": Equestrian,
    "Field Hockey": FieldHockey,
    "Golf": Golf,
    "Lacrosse": Lacrosse,
    "Marching Band": MarchingBand,
    "Martial Arts": MartialArts,
    "Mascoting": Mascoting,
    "Powerlifting": Powerlifting,
    "Rowing": Rowing,
    "Skiing": Skiing,
    "Soccer": Soccer,
    "Softball": Softball,
    "Sports Medicine": SportsMedicine,
    "Swimming / Diving": SwimmingDiving,
    "Tennis": Tennis,
    "Track": Track,
    "Volleyball": Volleyball,
    "Water Polo": WaterPolo,
    "Weightlifting": Weightlifting
}

clubs = {
    "Girl Scouts": GirlScouts,
    "Government / Debate / Model UN": GovernmentDebate,
    "Honor Societies": HonorSocieties,
    "HOSA": HOSA,
    "IB Program": IBProgram,
    "Key Club": KeyClub,
    "National Charity League": NationalCharityLeague,
    "National Honor Society": NationalHonorSociety,
    "Performing Arts": PerformingArts,
    "Religious": Religious,
    "Service / Volunteer": ServiceVolunteer,
    "STEM / Academic": STEMAcademic,
    "Student Council": StudentCouncil,
    "Student Publications": StudentPublications,
    "Tutoring / Peer Mentoring": TutoringPeerMentoring
}

philanthropy = {
    "Working with Animals": WorkingWithAnimals,
    "Working with Children": WorkingWithChildren,
    "Working with Elderly / Disabled People": WorkingWithElderlyDisabled,
    "Working with Environmental Conservation": WorkingWithEnvironmentalConservation,
    "Working with Healthcare Related Fields": WorkingWithHealthcare,
    "Working with Unhoused / Impoverished People": WorkingWithUnhousedImpoverished,
    "Working with Social Activism": WorkingWithSocialActivism,
}

physical_activities = {
    "Basketball": BasketballAct,
    "Biking": Biking,
    "Boating": Boating,
    "Camping": Camping,
    "Dancing": Dancing,
    "Field Hockey": FieldHockeyAct,
    "Fishing": Fishing,
    "Golfing": GolfingAct,
    "Hiking": Hiking,
    "Horseback Riding": HorsebackRiding,
    "Hunting": Hunting,
    "Ice Skating": IceSkating,
    "Lacrosse": LacrosseAct,
    "Paddleboarding / Kayaking": PaddleboardingKayaking,
    "Pickleball": Pickleball,
    "Pilates": Pilates,
    "Rock Climbing": RockClimbing,
    "Running / Jogging": RunningJogging,
    "Scuba Diving": ScubaDiving,
    "Skiing / Snowboarding": SkiingSnowboarding,
    "SoulCycle": SoulCycle,
    "Surfing": Surfing,
    "Swimming / Diving": SwimmingDiving,
    "Tennis": TennisAct,
    "Volleyball": VolleyballAct,
    "Walks Outdoors": WalksOutdoors,
    "Water Skiing": WaterSkiing,
    "Working Out": WorkingOut,
    "Yoga": Yoga,
}

other_activities = {
    "Animals": Animals,
    "Arts and Crafts": ArtsandCrafts,
    "Baking": Baking,
    "Boardgames": Boardgames,
    "Blogging": Blogging
    "Concerts / Live Music / Music Festivals": ConcertsLiveMusic,
    "Coffee/Tea": CoffeeTea,
    "Cooking": Cooking,
    "Crochet/Knitting": CrochetKnitting,
    "Drawing": Drawing,
    "Exploring Austin": ExploringAustin,
    "Exploring New Restaurants": ExploringNewRestaurants,
    "Formula 1": Formula1,
    "Government": Government,
    "Graphic Design": GraphicDesignInterest,
    "Health": Health,
    "Journaling": Journaling,
    "Listening to Music": ListeningToMusic,
    "Musicals": Musicals,
    "Needlepoint": Needlepoint,
    "Painting": Painting,
    "Philosophy": Philosophy,
    "Photography": Photography,
    "Playing a Percussion Instrument (drums, piano, etc.)": PlayingPercussionInstrument,
    "Playing a String Instrument (violin, cello, etc.)": PlayingStringInstrument,
    "Playing a Wind Instrument (flute, clarinet, etc.)": PlayingWindInstrument,
    "Podcasts": Podcasts,
    "Pottery/Ceramics": PotteryCeramics,
    "Reading": Reading,
    "Road Trips": RoadTrips,
    "Scrapbooking": Scrapbooking,
    "Science/Marine Science/Ecology": ScienceMarineScienceEcology,
    "Sewing": Sewing,
    "Shopping": Shopping,
    "Singing": Singing,
    "Skincare": Skincare,
    "Social Media (Tiktok, Instagram, etc.)": SocialMedia,
    "Tanning": Tanning,
    "Thrifting": Thrifting,
    "Traveling": Traveling,
    "Two-stepping/line dancing": TwoSteppingLineDancing,
    "Vlogging": Vlogging,
    "Watching Sports": WatchingSports,
    "Watching TV/Movies": WatchingTVMovies,
    "Writing": Writing
}

transfers = {
    "Transfer Student": transfer,
    "UTA": UTA,
    "Texas Tech": TexasTech,
    "UTEP": UTEP,
    "Tufts University": TuftsUniversity,
    "UTSA": UTSA,
    "UTRGV": UTRGV,
    "Trinity University": TrinityUniversity
}



# ===== STREAMLIT USER INTERFACE ===============================================================================================================================
st.title("Interest Finder")

def checkbox_columns(section_name, interests, num_cols=4):
    selected = []
    # Create dropdown/expander for the entire section
    with st.expander(section_name, expanded=False):
        cols = st.columns(num_cols)

        for i, interest in enumerate(interests):
            col = cols[i % num_cols]

            if col.checkbox(interest, key=f"{section_name}_{interest}"):
                selected.append(interest)

    return selected

        
selected_majors = checkbox_columns("Majors"+'\U0001F4DA', list(majors.keys()), num_cols=4)
selected_minors = checkbox_columns("Minors"+"\U0001F4DD", list(minors.keys()), num_cols=4)
selected_colleges = checkbox_columns("College/Track"+"\U0001FA7A", list(colleges.keys()), num_cols=4)
selected_transfers = checkbox_columns("Transfer"+"\U0001F501", list(transfers.keys()), num_cols=4)
selected_hometowns = checkbox_columns("Hometowns"+"\U0001F3E0", list(hometowns.keys()), num_cols=4)
selected_sports = checkbox_columns("High School Sports"+"\U0001F3C6", list(sports.keys()), num_cols=4)
selected_clubs = checkbox_columns("HS Clubs"+"\U0001F3E2", list(clubs.keys()), num_cols=4)
selected_orgs = checkbox_columns("UT Organizations"+"\U0001F396", list(utorgs.keys()), num_cols=4)
selected_physical_activities = checkbox_columns("Physical Activities for Fun"+"\U0001F3C3", list(physical_activities.keys()), num_cols=4)
selected_other_activities = checkbox_columns("Activities/Interests for Fun"+"\U0001F3A8", list(other_activities.keys()), num_cols=4)
selected_philanthropy = checkbox_columns("Philanthropy"+"\U0001FAF6", list(philanthropy.keys()), num_cols=4)
selected_summercamps = checkbox_columns("Summer Camp"+"\U0001F525", list(summercamps.keys()), num_cols=4)
selected_music = checkbox_columns("Music"+"\U0001F3B5", list(music.keys()), num_cols=4)
selected_books = checkbox_columns("Books/Authors"+"\U0001F4D6", list(books.keys()), num_cols=4)

selected_interests = selected_majors + selected_minors + selected_colleges + selected_hometowns + selected_sports + selected_orgs + selected_clubs + selected_summercamps + selected_philanthropy + selected_physical_activities + selected_other_activities + selected_music + selected_books + selected_transfers #+ selected_schools + selected_extras + selected_orgs + selected_activities + selected_summercamps + selected_nicheinterests + selected_transfers

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
        elif interest in sports:
            names = sports[interest]
        elif interest in utorgs:
            names = utorgs[interest]
        elif interest in clubs:
            names = clubs[interest]
        elif interest in music:
            names = music[interest]
        elif interest in summercamps:
            names = summercamps[interest]
        elif interest in philanthropy:
            names = philanthropy[interest]
        elif interest in physical_activities:
            names = physical_activities[interest]
        elif interest in other_activities:
            names = other_activities[interest]
        elif interest in books:
            names = books[interest]
        elif interest in transfers:
            names = transfers[interest]
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
        some_match_sorted = sorted(some_match, key=lambda x: len(x[1]), reverse=True)
        for name, matches in some_match_sorted:
            colored_names = coloring(name)
            st.markdown(f"{colored_names}: {', '.join(matches)}", unsafe_allow_html=True)

    st.subheader("⚪ One Match")
    if one_match:
        for name, matches in one_match:
            colored_names = coloring(name)
            st.markdown(f"{colored_names}: {', '.join(matches)}", unsafe_allow_html=True)
