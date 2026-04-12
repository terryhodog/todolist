# CampusSync

> 🌐 [中文](./README.md) | [English](./README_EN.md) | [한국어](./README_KR.md)

> A local, all-in-one academic productivity desktop application for university students, integrating timetable management, memos, and an immersive focus timer.

## Graphical Abstract

![Graphical Abstract](./docs/abstract.png)

---

## 1. Purpose of the Software

### 1.1 Software Development Process

This project follows the **Agile Scrum** development methodology, delivering incremental builds through iterative Sprints.

### 1.2 Reason for Selection

| Factor | Explanation |
|--------|-------------|
| Requirement Uncertainty | User requirements were not fully defined at the start; iterative refinement was necessary |
| Rapid Feedback | Each Sprint produces a runnable increment for validation and adjustment |
| Team Size Fit | A small team (2–4 members) benefits from lightweight Agile processes with reduced documentation overhead |
| Tech Stack Validation | Early Sprints allowed rapid verification of customtkinter's UI feasibility |

### 1.3 Target Market & Usage

| Target Group | Usage Scenario |
|--------------|----------------|
| University Students | Manage semester timetables, track assignment deadlines, conduct Pomodoro-style focus sessions |
| Exam Preparation Candidates | Utilize the focus timer for disciplined, high-efficiency study sessions |
| Privacy-Conscious Users | All data stored locally — no account registration or network connectivity required |

---

## 2. Software Development Plan

### 2.1 Development Process Model

The project is organized under the Scrum framework across 3 Sprints:

```
Sprint 1 (MVP): Core architecture, timetable and memo CRUD
Sprint 2: Focus timer, custom time slots, UI refinement
Sprint 3: i18n system (ZH/ZH-TW/EN/KR), packaging & documentation
```

### 2.2 Roles & Responsibilities

| Member | Role | Primary Responsibilities | Contribution |
|--------|------|--------------------------|--------------|
| Member A | Product Owner / Full-stack | Requirements definition, core architecture, timetable module | 30% |
| Member B | Frontend Developer | UI/UX design, customtkinter components, dark theme implementation | 25% |
| Member C | Backend Developer | JSON persistence layer, i18n multilingual system | 25% |
| Member D | QA / Documentation | Test case authoring, PyInstaller packaging, README documentation | 20% |

### 2.3 Project Schedule

| Sprint | Duration | Deliverables | Effort (Person-Days) |
|--------|----------|--------------|----------------------|
| Sprint 1 | Week 1–2 | Main layout framework, timetable CRUD, memo CRUD | 14 |
| Sprint 2 | Week 3–4 | Pomodoro timer (custom duration), time slot settings popup, DDL urgency highlighting | 12 |
| Sprint 3 | Week 5–6 | Four-language i18n live switching, PyInstaller packaging, documentation & demo video | 10 |
| **Total** | **6 Weeks** | **Complete deliverable product** | **36** |

### 2.4 Core Algorithm

**Urgency Sorting & Visual Alert Algorithm**

The memo list employs a dual-key composite sorting strategy:

```
Sort Key = (Priority Weight, DDL Date)
Priority Mapping: 🔴 High → 0, 🟡 Medium → 1, 🟢 Low → 2
```

During the rendering phase, each record is evaluated as follows:

```python
delta_days = (ddl_date - current_date).days
is_urgent = (delta_days <= 3) and (delta_days >= 0) and (priority == "High")
```

When `is_urgent == True`, the task entry background switches to `#8B0000` (dark red) for visual alert.

**Timetable Grid Rendering Algorithm**

Course cards are positioned via `grid(row=start_period, column=day_of_week, rowspan=span)`, where `span = end_period - start_period + 1`, ensuring precise placement within the 7×12 grid.

### 2.5 Current Status

- [x] Timetable (7×12 visual grid with add/delete)
- [x] Memos (priority sorting, DDL urgency highlighting, add/delete)
- [x] Focus Timer (custom duration, start/pause/reset)
- [x] Custom Time Slots (popup settings, persistent storage)
- [x] Multilingual Support (简体中文 / 繁體中文 / English / 한국어)
- [x] PyInstaller Desktop Packaging (Windows .exe)

### 2.6 Future Plan

| Priority | Feature | Description |
|----------|---------|-------------|
| P0 | Data Import/Export | Backup and restore via JSON files |
| P1 | Analytics Dashboard | Study time statistics based on focus timer logs |
| P1 | Calendar View | Monthly grid view marking DDLs and courses |
| P2 | Cross-Platform Support | macOS and Linux packaging |
| P2 | Theme Customization | Light mode and custom color scheme support |

---

## 3. Environments & Requirements

### 3.1 Programming Language

| Item | Version |
|------|---------|
| Python | >= 3.8 |

### 3.2 Minimum Hardware Requirements

| Resource | Requirement |
|----------|-------------|
| RAM | >= 2 GB |
| Disk Space | >= 200 MB (including packaged executable) |
| Display Resolution | >= 1280 × 720 |

### 3.3 Minimum Software Requirements

| Platform | Minimum Version |
|----------|-----------------|
| Windows | 10 (64-bit) |
| macOS | 12 Monterey (source code execution) |
| Linux | Ubuntu 20.04 (source code execution) |

### 3.4 Required Packages

| Package | Purpose | License |
|---------|---------|---------|
| `customtkinter` | Modern Tkinter UI framework | MIT |
| `darkdetect` | System dark mode detection (customtkinter dependency) | BSD-3 |
| `pyinstaller` | Desktop executable packaging (build-time only) | GPL-2.0 |

Installation:

```bash
pip install customtkinter
```

---

## 4. Declaration

The following third-party open-source software and tools were used during the development of this project. None of them were developed by our team:

| Name | Type | License | Description |
|------|------|---------|-------------|
| [customtkinter](https://github.com/TomSchimansky/CustomTkinter) | UI Framework | MIT | Provides modernized Tkinter widgets |
| [darkdetect](https://github.com/albertosottile/darkdetect) | System Utility | BSD-3 | Detects OS dark/light mode |
| [PyInstaller](https://github.com/pyinstaller/pyinstaller) | Packaging Tool | GPL-2.0 | Bundles Python programs into standalone executables |
| Python Standard Library (`json`, `uuid`, `datetime`, `os`, `sys`, `random`) | Runtime Library | PSF | Built-in Python modules |

All business logic, UI layout design, i18n translation texts, and documentation in this project were independently produced by the team members.

---

## 5. Demonstration

### 5.1 Demo Video

[![Demo Video](https://img.shields.io/badge/YouTube-Demo_Video-red?style=for-the-badge&logo=youtube)](https://youtu.be/ntVf8tTPNJ0)

### 5.2 How to Start & Run

#### Option 1: Run from Source (Development Mode)

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/CampusSync.git
cd CampusSync

# 2. Install dependencies
pip install customtkinter

# 3. Launch the application
python main.py
```

#### Option 2: Run Pre-built Binary (Windows)

1. Navigate to the [Releases](https://github.com/YOUR_USERNAME/CampusSync/releases) page and download the latest `CampusSync.zip`.
2. Extract and double-click `CampusSync.exe` to run. No Python installation required.

> **Note**: On first launch, the application automatically generates a `campus_data.json` file in the same directory. Do not delete this file to avoid data loss.

---

## Project Structure

```
CampusSync/
├── main.py                 # Main application entry point
├── campus_data.json        # Local data storage (auto-generated)
├── README.md               # Project documentation (Chinese)
├── README_EN.md            # Project documentation (English)
├── README_KR.md            # Project documentation (Korean)
├── docs/
│   └── abstract.png        # Graphical Abstract image
├── dist/                   # PyInstaller build output
│   └── CampusSync/
│       └── CampusSync.exe
└── build/                  # Build artifacts (not version-controlled)
```

---

## License

This project is licensed under the [MIT License](./LICENSE).
