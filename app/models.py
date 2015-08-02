from django.db import models


# Create your models here.

class Category(models.Model):
    #id = models.AutoField(unique=True, primary_key=True)
    category_name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):              
        return self.category_name

    def __str__(self):
        return self.category_name

class Provider(models.Model):
    # blank=True necessary to allow for incomplete data entry edits
    # makes it so the field is NOT required
    id = models.AutoField(unique=True, primary_key=True)
    provider_name = models.CharField(max_length=128)
    location_name = models.CharField(max_length=128, null=True, blank=True)
    image = models.CharField(max_length=128, null=True, blank=True)
    website = models.CharField(max_length=128, null=True, blank=True)
    address1 = models.CharField(max_length=128, blank=True)
    address2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=128, blank=True)
    state = models.CharField(max_length=128, blank=True)
    zipcode = models.CharField(max_length=128, blank=True)
    contact = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=128, blank=True)
    hours = models.CharField(max_length=1000, blank=True)

    # begin categories
    SoupKitchen = models.CharField(max_length=128, blank=True)
    FoodPantries = models.CharField(max_length=128, blank=True)
    Food = models.CharField(max_length=128, blank=True)
    FoodCooperatives = models.CharField(max_length=128, blank=True)
    NutritionEducation = models.CharField(max_length=128, blank=True)
    Nutrition = models.CharField(max_length=128, blank=True)
    ThriftShop = models.CharField(max_length=128, blank=True)
    clothing = models.CharField(max_length=128, blank=True)
    WinterClothing = models.CharField(max_length=128, blank=True)
    CriminalRecordExpungementAssisstance = models.CharField(max_length=128, blank=True)
    legalServices = models.CharField(max_length=128, blank=True)
    Language = models.CharField(max_length=128, blank=True)
    FluVaccinesAndImmunizations = models.CharField(max_length=128, blank=True)
    GeneralHealthEducation = models.CharField(max_length=128, blank=True)
    MedicalEquipmentAndSupplies = models.CharField(max_length=128, blank=True)
    medicalCare = models.CharField(max_length=128, blank=True)
    Dental_Care = models.CharField(max_length=128, blank=True)
    Education = models.CharField(max_length=128, blank=True)
    SchoolSupplies = models.CharField(max_length=128, blank=True)
    HouseholdGoods = models.CharField(max_length=128, blank=True)
    GraduationRequirementsProgram = models.CharField(max_length=128, blank=True)
    TutoringServices = models.CharField(max_length=128, blank=True)
    ReligiousServices = models.CharField(max_length=128, blank=True)
    InformationAndReferral = models.CharField(max_length=128, blank=True)
    transportation = models.CharField(max_length=128, blank=True)
    FinancialCounseling = models.CharField(max_length=128, blank=True)
    Drug_and_Alcohol_Treatment_Program = models.CharField(max_length=128, blank=True)
    MethadoneMaintenance = models.CharField(max_length=128, blank=True)
    SubsanceAbuseReferrals = models.CharField(max_length=128, blank=True)
    SubstanceAbuseAssistance = models.CharField(max_length=128, blank=True)
    AlcoholDependencySupportGroups = models.CharField(max_length=128, blank=True)
    SexuallyTransmittedDiseaseScreening = models.CharField(max_length=128, blank=True)
    HIVtesting = models.CharField(max_length=128, blank=True)
    CaseManagement = models.CharField(max_length=128, blank=True)
    DonorServices = models.CharField(max_length=128, blank=True)
    DonationPickups = models.CharField(max_length=128, blank=True)
    VehicleDonationProgram = models.CharField(max_length=128, blank=True)
    OfficeSuppliesDonationPrograms = models.CharField(max_length=128, blank=True)
    ClothingDonationPrograms = models.CharField(max_length=128, blank=True)
    FoodDonationPrograms = models.CharField(max_length=128, blank=True)
    HomeGoodsDonations = models.CharField(max_length=128, blank=True)
    HolidayDonations = models.CharField(max_length=128, blank=True)
    ToysDonationProgram = models.CharField(max_length=128, blank=True)
    PersonalGroomingDonationPrograms = models.CharField(max_length=128, blank=True)
    TelephoneFacilities = models.CharField(max_length=128, blank=True)
    OutreachPrograms = models.CharField(max_length=128, blank=True)
    AdvocacyGroups = models.CharField(max_length=128, blank=True)
    CommunityShelters = models.CharField(max_length=128, blank=True)
    TransitionalHousing = models.CharField(max_length=128, blank=True)
    EmergencyShelter = models.CharField(max_length=128, blank=True)
    PermanentHousing = models.CharField(max_length=128, blank=True)
    WaterServicePaymentAssistance = models.CharField(max_length=128, blank=True)
    ElectricServicePaymentAssistance = models.CharField(max_length=128, blank=True)
    GasServicePayAssistance = models.CharField(max_length=128, blank=True)
    HeatingFuelPaymentAssistance = models.CharField(max_length=128, blank=True)
    EyeCareExpenseAssistance = models.CharField(max_length=128, blank=True)
    MedicalCareExpenseAssistance = models.CharField(max_length=128, blank=True)
    PerscriptionExpenseAssistance = models.CharField(max_length=128, blank=True)
    RentPaymentAssistance = models.CharField(max_length=128, blank=True)
    DentalExpenseAssistance = models.CharField(max_length=128, blank=True)
    TransportationExpenseAssistance = models.CharField(max_length=128, blank=True)
    ComputerClasses = models.CharField(max_length=128, blank=True)
    DropinCenter = models.CharField(max_length=128, blank=True)
    BenefitsScreening = models.CharField(max_length=128, blank=True)
    GovernmentServices = models.CharField(max_length=128, blank=True)
    TaxPreparationAssistance = models.CharField(max_length=128, blank=True)
    FinancialManagementWorkshops = models.CharField(max_length=128, blank=True)
    FormsCertificateAssistance = models.CharField(max_length=128, blank=True)
    BirthCertficateFeeHelp = models.CharField(max_length=128, blank=True)
    IDCardFeeHelp = models.CharField(max_length=128, blank=True)
    HealthDisabilitySupportGroup = models.CharField(max_length=128, blank=True)
    JobAssistance = models.CharField(max_length=128, blank=True)
    PersonalGroomingSupplies = models.CharField(max_length=128, blank=True)
    Showers = models.CharField(max_length=128, blank=True)
    Laundry = models.CharField(max_length=128, blank=True)
    LifeSkillsEducation = models.CharField(max_length=128, blank=True)
    MentoringPrograms = models.CharField(max_length=128, blank=True)
    YouthDevelopment = models.CharField(max_length=128, blank=True)
    ReproductiveHealthServices = models.CharField(max_length=128, blank=True)
    BabySupplies = models.CharField(max_length=128, blank=True)
    ParentingEducation = models.CharField(max_length=128, blank=True)
    SummerCamps = models.CharField(max_length=128, blank=True)
    DayCamps = models.CharField(max_length=128, blank=True)
    RecreationAndPsychicalFitness = models.CharField(max_length=128, blank=True)
    SeniorCenters = models.CharField(max_length=128, blank=True)
    GroceryDelivery = models.CharField(max_length=128, blank=True)
    PublicTrashCans = models.CharField(max_length=128, blank=True)
    DisasterPreparedness = models.CharField(max_length=128, blank=True)
    CommunityGardening = models.CharField(max_length=128, blank=True)
    VolunteerOpportunities = models.CharField(max_length=128, blank=True)
    ChristmasMeals = models.CharField(max_length=128, blank=True)
    ChristmasBaskets = models.CharField(max_length=128, blank=True)
    ThanksgivingMeals = models.CharField(max_length=128, blank=True)
    ThanksgivingBaskets = models.CharField(max_length=128, blank=True)
    HolidayPrograms = models.CharField(max_length=128, blank=True)
    HolidayGifts_Toys = models.CharField(max_length=128, blank=True)
    EasterMeals = models.CharField(max_length=128, blank=True)
    Public_Computer_Access = models.CharField(max_length=128, blank=True)
    other = models.CharField(max_length=128, blank=True)
    preferred = models.CharField(max_length=128, blank=True)
    # end categories

    AgencyDescription = models.CharField(max_length=1000, blank=True)
    Eligibity = models.CharField(max_length=1000, blank=True)
    FeeStructureSource = models.CharField(max_length=1000, blank=True)
    ApplicationProcess = models.CharField(max_length=1000, blank=True)
    DocumentsRequired = models.CharField(max_length=1000, blank=True)
    Details = models.CharField(max_length=1000, blank=True)
    Details_Continued = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        return self.provider_name

    def __str__(self):
        return self.provider_name

# from django.db import models


# # Create your models here.

# class Category(models.Model):
#     category_name = models.CharField(max_length=30)

#     def __unicode__(self):              
#         return self.category_name

# class Provider(models.Model):
#     # blank=True necessary to allow for incomplete data entry edits
#     # makes it so the field is NOT required
#     id = models.IntegerField(max_length=None, unique=True, primary_key=True)
#     provider_name = models.CharField(max_length=128)
#     location_name = models.CharField(max_length=128, null=True, blank=True)
#     image = models.CharField(max_length=128, null=True, blank=True)
#     website = models.CharField(max_length=128, null=True, blank=True)
#     address1 = models.CharField(max_length=128, blank=True)
#     address2 = models.CharField(max_length=128, blank=True)
#     city = models.CharField(max_length=128, blank=True)
#     state = models.CharField(max_length=128, blank=True)
#     zipcode = models.CharField(max_length=128, blank=True)
#     categories = models.ManyToManyField(Category, blank=True)

#     def __unicode__(self):
#         return self.provider_name

#     def __str__(self):
#         return self.provider_name
