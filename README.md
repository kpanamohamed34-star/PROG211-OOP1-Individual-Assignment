# HealthShield: Anonymized Vaccination Tracker

## Overview
**HealthShield** is an open-source, modular Python software developed for the **PROG211: Object-Oriented Programming 1** course at **Limkokwing University of Creative Technology**.

This system solves real-world health record management challenges by tracking patient vaccination history while strictly adhering to **Digital Public Goods (DPG)** standards.

---

## Domain Selection: Health
The system provides public health workers and clinics with a lightweight tool to log administered doses and maintain cold-chain safety checks across multiple regional districts.

---

## Digital Public Goods (DPG) Principles Alignment
1. **Open Source:** Published under the open MIT License to encourage community contributions and deployment in public health centers.
2. **Privacy-Respecting (Zero PII):** No personally identifiable information (e.g., full names, contact info, home address) is captured or stored. Patients are uniquely identified using anonymized hashes/IDs (`SLE-PAT-XXXX`).
3. **Inclusive & Accessible Design:** Built with standard Python libraries requiring minimal hardware overhead, allowing execution on low-cost computing hardware in remote clinics.
4. **Modular & Reusable:** Encapsulated OOP design allows seamless integration with larger national public health software systems.

---

## Object-Oriented Design & Architecture

### Classes
- **`Vaccine`**: Stores metadata for vaccine types, required doses, and safe temperature limits.
- **`PatientRecord`**: Encapsulates patient details, district location, and dose history.
- **`VaccinationTrackerSystem`**: Manager class maintaining overall database state.

### Methods Implementation
- **Instance Methods**: `display_info()`, `update_record()`, `add_vaccine()`, `record_vaccination()`.
- **Class Method (`@classmethod`)**: `PatientRecord.get_total_registered()` — tracks total patient instances created system-wide.
- **Static Methods (`@staticmethod`)**:
  - `Vaccine.is_temperature_safe()` — checks cold-chain storage compliance.
  - `PatientRecord.generate_anonymous_id()` — creates formatted non-PII identification tags.

### Data Structures Applied
- **Dictionary**: Maps unique anonymized patient IDs to `PatientRecord` instances (`{patient_id: PatientRecord}`).
- **List**: Stores collections of `Vaccine` objects.
- **Tuples (Bonus Feature)**:
  1. Safe storage temperature ranges `(min_temp, max_temp)`.
  2. Vaccination history entries `(vaccine_code, dose_number, date_str)` ensuring immutable event logging.

---

## How to Run the Program

### Prerequisites
- Python 3.8+ installed on your machine.

### Execution
1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/PROG211_OOP1_Assignment.attr](https://github.com/YOUR_GITHUB_USERNAME/PROG211_OOP1_Assignment.attr)
   ```
2. Navigate to the project directory:
   ```bash
   cd PROG211_OOP1_Assignment
   ```
3. Run the script:
   ```bash
   python vaccination_tracker.py
   ```

---

## Sample Program Output
```text
=======================================================
 HEALTHSHIELD: ANONYMIZED VACCINATION TRACKER (DPG)   
=======================================================

--- Available System Vaccines ---
[Vaccine] Code: VAC-01 | Name: COVID-19 mRNA       | Required Doses: 2 | Storage Temp: 2.0°C to 8.0°C
[Vaccine] Code: VAC-02 | Name: Yellow Fever        | Required Doses: 1 | Storage Temp: 2.0°C to 8.0°C
[Vaccine] Code: VAC-03 | Name: Polio OPV           | Required Doses: 3 | Storage Temp: -25.0°C to -15.0°C

Cold-Chain Check: 4.5°C safe for COVID-19 mRNA? True

--- Registering Patients ---
[REGISTER] Patient 'SLE-PAT-0101' added to system dictionary database.
[REGISTER] Patient 'SLE-PAT-0102' added to system dictionary database.

Total Patients Registered (Class Method): 2

--- Processing Vaccination Events ---
[UPDATE] Record updated for Patient SLE-PAT-0101: Administered Dose 1 of VAC-01 on 2026-09-10.
[UPDATE] Record updated for Patient SLE-PAT-0101: Administered Dose 2 of VAC-01 on 2026-10-01.
[UPDATE] Record updated for Patient SLE-PAT-0102: Administered Dose 1 of VAC-02 on 2026-09-15.

=======================================================
          SYSTEM PATIENT RECORDS SUMMARY               
=======================================================

--- Patient ID: SLE-PAT-0101 ---
District Code : WEST-URBAN | Age: 28
Vaccination History :
  - Vaccine: VAC-01 | Dose: 1 | Date: 2026-09-10
  - Vaccine: VAC-01 | Dose: 2 | Date: 2026-10-01

--- Patient ID: SLE-PAT-0102 ---
District Code : BO-DIST | Age: 45
Vaccination History :
  - Vaccine: VAC-02 | Dose: 1 | Date: 2026-09-15
=======================================================
```