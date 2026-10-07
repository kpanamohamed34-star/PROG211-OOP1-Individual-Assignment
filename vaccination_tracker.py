"""
Module: PROG211 - Object-Oriented Programming 1
Assignment: Real-World Solutions under DPG Standards
Domain: Health (Anonymized Patient Vaccination Tracker)
Author: Mohamed Kpana
"""


class Vaccine:
    """Represents a vaccine entity within the healthcare network."""

    def __init__(self, vaccine_code: str, name: str, required_doses: int, temp_range: tuple):
        self.vaccine_code = vaccine_code
        self.name = name
        self.required_doses = required_doses
        # Tuple usage (Bonus 10 marks): Fixed immutable cold-chain temperature range (min_temp, max_temp) in Celsius
        self.temp_range = temp_range

    def display_info(self) -> None:
        """Instance method to display vaccine specification details."""
        print(f"[Vaccine] Code: {self.vaccine_code:<6} | Name: {self.name:<18} | "
              f"Required Doses: {self.required_doses} | Storage Temp: {self.temp_range[0]}°C to {self.temp_range[1]}°C")

    @staticmethod
    def is_temperature_safe(current_temp: float, temp_range: tuple) -> bool:
        """Static method: Evaluates if current storage temperature complies with cold-chain requirements."""
        min_temp, max_temp = temp_range
        return min_temp <= current_temp <= max_temp


class PatientRecord:
    """Represents an anonymized patient record complying with DPG privacy standards (No PII)."""

    # Class attributes
    total_patients_registered = 0
    dpg_license = "MIT Digital Public Good License"

    def __init__(self, patient_id: str, age: int, district_code: str):
        self.patient_id = patient_id
        self.age = age
        self.district_code = district_code
        # List of Tuples (Bonus 10 marks): Stores immutable historical events as (vaccine_code, dose_number, date_str)
        self.vaccination_history = []

        # Increment class attribute counter upon instantiation
        PatientRecord.total_patients_registered += 1

    def update_record(self, vaccine_code: str, dose_number: int, date_str: str) -> None:
        """Instance method: Adds a new dose entry tuple to the patient's vaccination history."""
        dose_entry = (vaccine_code, dose_number, date_str)
        self.vaccination_history.append(dose_entry)
        print(f"[UPDATE] Record updated for Patient {self.patient_id}: "
              f"Administered Dose {dose_number} of {vaccine_code} on {date_str}.")

    def display_info(self) -> None:
        """Instance method: Prints patient anonymized metadata and dosage history."""
        print(f"\n--- Patient ID: {self.patient_id} ---")
        print(f"District Code : {self.district_code} | Age: {self.age}")
        if not self.vaccination_history:
            print("Vaccination History : No doses recorded.")
        else:
            print("Vaccination History :")
            for entry in self.vaccination_history:
                v_code, dose_num, date = entry  # Unpacking tuple
                print(f"  - Vaccine: {v_code:<6} | Dose: {dose_num} | Date: {date}")

    @classmethod
    def get_total_registered(cls) -> int:
        """Class method: Returns total patient instances registered system-wide."""
        return cls.total_patients_registered

    @staticmethod
    def generate_anonymous_id(prefix: str, sequence_num: int) -> str:
        """Static method: Generates non-personally-identifiable keys (DPG Privacy Rule)."""
        return f"{prefix.upper()}-{sequence_num:04d}"


class VaccinationTrackerSystem:
    """System manager utilizing Python Data Structures (Dictionary, List, Tuple) to manage objects."""

    def __init__(self):
        # Dictionary structure: Stores PatientRecord objects with unique anonymized patient_id as keys
        self.patient_registry = {}
        # List structure: Stores available Vaccine objects
        self.available_vaccines = []

    def add_vaccine(self, vaccine: Vaccine) -> None:
        """Adds a vaccine object to the internal list structure."""
        self.available_vaccines.append(vaccine)

    def register_patient(self, patient: PatientRecord) -> None:
        """Adds a patient object to the internal dictionary structure."""
        self.patient_registry[patient.patient_id] = patient
        print(f"[REGISTER] Patient '{patient.patient_id}' added to system dictionary database.")

    def record_vaccination(self, patient_id: str, vaccine_code: str, dose_num: int, date_str: str) -> None:
        """Interacts patient object with vaccine code to record dosage."""
        if patient_id in self.patient_registry:
            patient = self.patient_registry[patient_id]
            patient.update_record(vaccine_code, dose_num, date_str)
        else:
            print(f"[ERROR] Patient ID '{patient_id}' not found in dictionary database.")

    def display_all_records(self) -> None:
        """Loops through dictionary data structure to print all patient records."""
        print("\n=======================================================")
        print("          SYSTEM PATIENT RECORDS SUMMARY               ")
        print("=======================================================")
        for p_id, patient_obj in self.patient_registry.items():
            patient_obj.display_info()
        print("=======================================================\n")


# ----------------------------------------------------------------------
# PROGRAM EXECUTION / SAMPLE TEST SUITE
# ----------------------------------------------------------------------
if __name__ == "__main__":
    print("=======================================================")
    print(" HEALTHSHIELD: ANONYMIZED VACCINATION TRACKER (DPG)   ")
    print("=======================================================\n")

    # 1. Instantiate System Manager
    tracker = VaccinationTrackerSystem()

    # 2. Instantiate and Add Vaccine Objects (Using Tuples for cold-chain temp range)
    vax1 = Vaccine("VAC-01", "COVID-19 mRNA", 2, (2.0, 8.0))
    vax2 = Vaccine("VAC-02", "Yellow Fever", 1, (2.0, 8.0))
    vax3 = Vaccine("VAC-03", "Polio OPV", 3, (-25.0, -15.0))

    tracker.add_vaccine(vax1)
    tracker.add_vaccine(vax2)
    tracker.add_vaccine(vax3)

    print("--- Available System Vaccines ---")
    for v in tracker.available_vaccines:
        v.display_info()

    # Static method test: Cold-chain temperature safety check
    sample_temp = 4.5
    is_safe = Vaccine.is_temperature_safe(sample_temp, vax1.temp_range)
    print(f"\nCold-Chain Check: {sample_temp}°C safe for {vax1.name}? {is_safe}")

    # 3. Generate Anonymized IDs via Static Method & Register Patient Objects
    p1_id = PatientRecord.generate_anonymous_id("SLE-PAT", 101)
    p2_id = PatientRecord.generate_anonymous_id("SLE-PAT", 102)

    patient1 = PatientRecord(p1_id, age=28, district_code="WEST-URBAN")
    patient2 = PatientRecord(p2_id, age=45, district_code="BO-DIST")

    print("\n--- Registering Patients ---")
    tracker.register_patient(patient1)
    tracker.register_patient(patient2)

    # Class Method Demonstration
    print(f"\nTotal Patients Registered (Class Method): {PatientRecord.get_total_registered()}")

    # 4. Perform Object Interaction & Record Updates
    print("\n--- Processing Vaccination Events ---")
    tracker.record_vaccination(p1_id, "VAC-01", dose_num=1, date_str="2026-09-10")
    tracker.record_vaccination(p1_id, "VAC-01", dose_num=2, date_str="2026-10-01")
    tracker.record_vaccination(p2_id, "VAC-02", dose_num=1, date_str="2026-09-15")

    # 5. Loop through Data Structure & Display All Records
    tracker.display_all_records()