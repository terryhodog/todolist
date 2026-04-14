# CampusSync

> 🌐 [中文](./README.md) | [English](./README_EN.md) | [한국어](./README_KR.md)

> 대학생을 위한 로컬 올인원 학업 생산성 데스크톱 애플리케이션. 시간표 관리, 메모, 몰입형 집중 타이머를 하나로 통합합니다.

## Graphical Abstract

![Graphical Abstract](./docs/Timetable.png)
![Graphical Abstract](./docs/Memos.png)
![Graphical Abstract](./docs/Focus.png)


---

## 1. Purpose of the Software

### 1.1 Software Development Process

본 프로젝트는 **Agile Scrum** 개발 방법론을 채택하여 Sprint 단위로 점진적 빌드를 제공합니다.

### 1.2 Reason for Selection

| 요인 | 설명 |
|------|------|
| 요구사항 불확실성 | 프로젝트 초기 사용자 요구사항이 완전히 정의되지 않아 반복적 개선이 필요 |
| 빠른 피드백 | 각 Sprint 종료 시 실행 가능한 증분 버전을 통해 검증 및 조정 가능 |
| 팀 규모 적합성 | 소규모 팀(2–4명)에 적합한 경량 Agile 프로세스로 문서 부담 감소 |
| 기술 스택 검증 | 초기 Sprint에서 customtkinter UI 실현 가능성을 신속하게 검증 |

### 1.3 Target Market & Usage

| 대상 그룹 | 사용 시나리오 |
|-----------|---------------|
| 재학 대학생 | 학기 시간표 관리, 과제 마감일 추적, 포모도로 방식 집중 학습 |
| 시험 준비자 | 집중 타이머를 활용한 고효율 자율 학습 |
| 개인정보 보호 중시 사용자 | 모든 데이터가 로컬에 저장 — 계정 등록이나 네트워크 연결 불필요 |

---

## 2. Software Development Plan

### 2.1 Development Process Model

프로젝트는 Scrum 프레임워크에 따라 3개의 Sprint로 구성됩니다:

```
Sprint 1 (MVP): 핵심 아키텍처 구축, 시간표 및 메모 CRUD
Sprint 2: 집중 타이머, 사용자 정의 시간대, UI 개선
Sprint 3: i18n 시스템(중/번체/영/한), 패키징 및 문서화
```

### 2.2 역할 및 책임 

| 구성원 | 담당 영역 | 주요 작업 |
| :--- | :--- | :--- |
| **구성원 A** | **핵심 아키텍처** | JSON 데이터 저장 및 관리, 메인 내비게이션 프레임워크, 시간표 그리드 렌더링 알고리즘 개발. |
| **구성원 B** | **비즈니스 로직** | 메모 모듈 개발, 마감일(DDL) 긴급도 계산 알고리즘 및 i18n 다국어 시스템 매핑 구현. |
| **구성원 C** | **컴포넌트 및 배포** | 집중 타이머 모듈, 설정 창 구현, 전체적인 UI 디자인 최적화 및 크로스 플랫폼 패키징/배포. |

### 2.3 프로젝트 일정 (3주 스프린트)

| 단계 | 기간 | 주요 목표 |
| :--- | :--- | :--- |
| **Sprint 1** | 1주차 | **기초 프레임워크**: 데이터 모델 정의, 다국어 아키텍처 구성, 내비게이션 및 로컬 JSON 입출력 로직 완성. |
| **Sprint 2** | 2주차 | **기능 개발**: 시간표 동적 렌더링, 메모 정렬 로직, 뽀모도로 집중 타이머 핵심 기능 구현. |
| **Sprint 3** | 3주차 | **최적화 및 인도**: UI 디자인 고도화, 다국어 텍스트 적합성 테스트, 버그 수정 및 최종 EXE 빌드. |
### 2.4 Core Algorithm

**긴급도 정렬 및 시각적 경고 알고리즘**

메모 목록은 이중 키 복합 정렬 전략을 사용합니다:

```
정렬 키 = (우선순위 가중치, DDL 날짜)
우선순위 매핑: 🔴 높음 → 0, 🟡 보통 → 1, 🟢 낮음 → 2
```

렌더링 단계에서 각 레코드에 대해 다음과 같이 평가합니다:

```python
delta_days = (ddl_date - current_date).days
is_urgent = (delta_days <= 3) and (delta_days >= 0) and (priority == "높음")
```

`is_urgent == True`일 경우, 해당 작업 항목의 배경색이 `#8B0000`(진한 빨강)으로 전환되어 시각적 경고를 제공합니다.

**시간표 그리드 렌더링 알고리즘**

과목 카드는 `grid(row=start_period, column=day_of_week, rowspan=span)`을 통해 배치되며, 여기서 `span = end_period - start_period + 1`으로 7×12 그리드 내에서 정확한 위치를 보장합니다.

### 2.5 Current Status

- [x] 시간표 (7×12 시각적 그리드, 추가/삭제 지원)
- [x] 메모 (우선순위 정렬, DDL 긴급도 강조, 추가/삭제)
- [x] 집중 타이머 (사용자 정의 시간, 시작/일시정지/초기화)
- [x] 사용자 정의 시간대 (팝업 설정, 영구 저장)
- [x] 다국어 지원 (简体中文 / 繁體中文 / English / 한국어)
- [x] PyInstaller 데스크톱 패키징 (Windows .exe)

### 2.6 Future Plan

| 우선순위 | 기능 | 설명 |
|----------|------|------|
| P0 | 데이터 가져오기/내보내기 | JSON 파일을 통한 백업 및 복원 |
| P1 | 분석 대시보드 | 집중 타이머 로그 기반 과목별 학습 시간 통계 |
| P1 | 캘린더 뷰 | DDL 및 수업을 표시하는 월간 그리드 뷰 |
| P2 | 크로스 플랫폼 지원 | macOS 및 Linux 패키징 |
| P2 | 테마 커스터마이징 | 라이트 모드 및 사용자 정의 색상 구성 지원 |

---

## 3. Environments & Requirements

### 3.1 Programming Language

| 항목 | 버전 |
|------|------|
| Python | >= 3.8 |

### 3.2 Minimum Hardware Requirements

| 자원 | 요구사항 |
|------|----------|
| RAM | >= 2 GB |
| 디스크 공간 | >= 200 MB (패키징된 실행 파일 포함) |
| 디스플레이 해상도 | >= 1280 × 720 |

### 3.3 Minimum Software Requirements

| 플랫폼 | 최소 버전 |
|--------|----------|
| Windows | 10 (64-bit) |
| macOS | 12 Monterey (소스 코드 실행) |
| Linux | Ubuntu 20.04 (소스 코드 실행) |

### 3.4 Required Packages

| 패키지 | 용도 | 라이선스 |
|--------|------|----------|
| `customtkinter` | 모던 Tkinter UI 프레임워크 | MIT |
| `darkdetect` | 시스템 다크 모드 감지 (customtkinter 의존성) | BSD-3 |
| `pyinstaller` | 데스크톱 실행 파일 패키징 (빌드 시에만 필요) | GPL-2.0 |

설치:

```bash
pip install customtkinter
```

---

## 4. Declaration

본 프로젝트 개발 과정에서 다음과 같은 서드파티 오픈소스 소프트웨어 및 도구가 사용되었습니다. 이들은 본 팀이 개발한 것이 아닙니다:

| 이름 | 유형 | 라이선스 | 설명 |
|------|------|----------|------|
| [customtkinter](https://github.com/TomSchimansky/CustomTkinter) | UI 프레임워크 | MIT | 현대적인 Tkinter 위젯 제공 |
| [darkdetect](https://github.com/albertosottile/darkdetect) | 시스템 유틸리티 | BSD-3 | OS 다크/라이트 모드 감지 |
| [PyInstaller](https://github.com/pyinstaller/pyinstaller) | 패키징 도구 | GPL-2.0 | Python 프로그램을 독립 실행 파일로 번들링 |
| Python 표준 라이브러리 (`json`, `uuid`, `datetime`, `os`, `sys`, `random`) | 런타임 라이브러리 | PSF | Python 내장 모듈 |

본 프로젝트의 모든 비즈니스 로직, UI 레이아웃 설계, i18n 번역 텍스트 및 문서는 팀원들이 독립적으로 작성하였습니다.

---

## 5. Demonstration

### 5.1 Demo Video

[![Demo Video](https://img.shields.io/badge/YouTube-Demo_Video-red?style=for-the-badge&logo=youtube)](https://youtu.be/ntVf8tTPNJ0)

### 5.2 How to Start & Run

#### 방법 1: 소스 코드로 실행 (개발 모드)

```bash
# 1. 저장소 클론
git clone https://github.com/YOUR_USERNAME/CampusSync.git
cd CampusSync

# 2. 의존성 설치
pip install customtkinter

# 3. 애플리케이션 실행
python main.py
```

#### 방법 2: 사전 빌드된 바이너리 실행 (Windows)

1. [Releases](https://github.com/YOUR_USERNAME/CampusSync/releases) 페이지에서 최신 `CampusSync.zip`을 다운로드합니다.
2. 압축 해제 후 `CampusSync.exe`를 더블 클릭하여 실행합니다. Python 설치가 필요 없습니다.

> **참고**: 첫 실행 시 애플리케이션이 같은 디렉터리에 `campus_data.json` 파일을 자동으로 생성합니다. 데이터 손실을 방지하려면 이 파일을 삭제하지 마십시오.

---

## Project Structure

```
CampusSync/
├── main.py                 # 메인 애플리케이션 진입점
├── campus_data.json        # 로컬 데이터 저장소 (자동 생성)
├── README.md               # 프로젝트 문서 (중국어)
├── README_EN.md            # 프로젝트 문서 (English)
├── README_KR.md            # 프로젝트 문서 (한국어)
├── docs/
│   └── abstract.png        # Graphical Abstract 이미지
├── dist/                   # PyInstaller 빌드 출력
│   └── CampusSync/
│       └── CampusSync.exe
└── build/                  # 빌드 아티팩트 (버전 관리에 포함하지 않음)
```

---

## License

This project is licensed under the [MIT License](./LICENSE).
