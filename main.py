import customtkinter as ctk
import json
import os
import sys
from datetime import datetime
import uuid
import random

# --- 配置与初始化 ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def get_data_path():
    if getattr(sys, 'frozen', False):
        return os.path.join(os.path.dirname(sys.executable), "campus_data.json")
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "campus_data.json")

DATA_FILE = get_data_path()
COURSE_COLORS = ["#7180AC", "#2B4570", "#A8D0DB", "#E49273", "#A37A74", "#66A182", "#EDAE49", "#D1495B"]

DEFAULT_TIME_SLOTS = [
    "08:00\n08:45", "08:55\n09:40", "10:00\n10:45", "10:55\n11:40",
    "13:30\n14:15", "14:25\n15:10", "15:30\n16:15", "16:25\n17:10",
    "18:30\n19:15", "19:25\n20:10", "20:20\n21:05", "21:15\n22:00"
]

# ========== 多语言 i18n 系统 ==========
LANGUAGES = {
    "简体中文": {
        "app_title": "CampusSync / 学业中枢",
        "nav_timetable": "核心课表 (Timetable)",
        "nav_memo": "备忘录 (Memos)",
        "nav_timer": "专注计时 (Focus)",
        "course_name": "课程名",
        "classroom": "教室/老师",
        "add_course": "+ 添加课程",
        "custom_time": "⚙️ 自定义时间段",
        "days": ["", "周一", "周二", "周三", "周四", "周五", "周六", "周日"],
        "memo_placeholder": "记录您的待办事项...",
        "ddl_placeholder": "DDL: YYYY-MM-DD",
        "priority_high": "🔴 高优",
        "priority_mid": "🟡 中优",
        "priority_low": "🟢 低优",
        "add_confirm": "确认添加",
        "done_delete": "完成/删除",
        "focus_label": "专注时长 (分钟):",
        "set_btn": "设定",
        "start_btn": "▶ 开始",
        "pause_btn": "⏸ 暂停",
        "reset_btn": "⏹ 重置",
        "settings_title": "自定义上课时间段",
        "settings_hint": "请设置1~12节课的时间范围\n(建议格式: 08:00 - 08:45)",
        "period_label": "第{}节:",
        "reset_default": "重置默认",
        "save_settings": "保存设置",
        "lang_label": "语言 / Lang",
    },
    "繁體中文": {
        "app_title": "CampusSync / 學業中樞",
        "nav_timetable": "核心課表 (Timetable)",
        "nav_memo": "備忘錄 (Memos)",
        "nav_timer": "專注計時 (Focus)",
        "course_name": "課程名",
        "classroom": "教室/老師",
        "add_course": "+ 新增課程",
        "custom_time": "⚙️ 自訂時間段",
        "days": ["", "週一", "週二", "週三", "週四", "週五", "週六", "週日"],
        "memo_placeholder": "記錄您的待辦事項...",
        "ddl_placeholder": "DDL: YYYY-MM-DD",
        "priority_high": "🔴 高優",
        "priority_mid": "🟡 中優",
        "priority_low": "🟢 低優",
        "add_confirm": "確認新增",
        "done_delete": "完成/刪除",
        "focus_label": "專注時長 (分鐘):",
        "set_btn": "設定",
        "start_btn": "▶ 開始",
        "pause_btn": "⏸ 暫停",
        "reset_btn": "⏹ 重置",
        "settings_title": "自訂上課時間段",
        "settings_hint": "請設置1~12節課的時間範圍\n(建議格式: 08:00 - 08:45)",
        "period_label": "第{}節:",
        "reset_default": "重置預設",
        "save_settings": "儲存設定",
        "lang_label": "語言 / Lang",
    },
    "English": {
        "app_title": "CampusSync / Study Hub",
        "nav_timetable": "Timetable",
        "nav_memo": "Memos",
        "nav_timer": "Focus Timer",
        "course_name": "Course",
        "classroom": "Room/Teacher",
        "add_course": "+ Add Course",
        "custom_time": "⚙️ Time Slots",
        "days": ["", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "memo_placeholder": "Add a to-do item...",
        "ddl_placeholder": "DDL: YYYY-MM-DD",
        "priority_high": "🔴 High",
        "priority_mid": "🟡 Medium",
        "priority_low": "🟢 Low",
        "add_confirm": "Add",
        "done_delete": "Done",
        "focus_label": "Focus Duration (min):",
        "set_btn": "Set",
        "start_btn": "▶ Start",
        "pause_btn": "⏸ Pause",
        "reset_btn": "⏹ Reset",
        "settings_title": "Customize Time Slots",
        "settings_hint": "Set time range for periods 1~12\n(Format: 08:00 - 08:45)",
        "period_label": "Period {}:",
        "reset_default": "Reset",
        "save_settings": "Save",
        "lang_label": "Language",
    },
    "한국어": {
        "app_title": "CampusSync / 학업 허브",
        "nav_timetable": "시간표 (Timetable)",
        "nav_memo": "메모 (Memos)",
        "nav_timer": "집중 타이머 (Focus)",
        "course_name": "과목명",
        "classroom": "교실/교수",
        "add_course": "+ 과목 추가",
        "custom_time": "⚙️ 시간 설정",
        "days": ["", "월", "화", "수", "목", "금", "토", "일"],
        "memo_placeholder": "할 일을 입력하세요...",
        "ddl_placeholder": "마감일: YYYY-MM-DD",
        "priority_high": "🔴 높음",
        "priority_mid": "🟡 보통",
        "priority_low": "🟢 낮음",
        "add_confirm": "추가",
        "done_delete": "완료",
        "focus_label": "집중 시간 (분):",
        "set_btn": "설정",
        "start_btn": "▶ 시작",
        "pause_btn": "⏸ 일시정지",
        "reset_btn": "⏹ 초기화",
        "settings_title": "수업 시간 설정",
        "settings_hint": "1~12교시 시간 범위를 설정하세요\n(형식: 08:00 - 08:45)",
        "period_label": "{}교시:",
        "reset_default": "초기화",
        "save_settings": "저장",
        "lang_label": "언어 / Lang",
    },
}

# 当前语言（全局状态）
current_lang = "简体中文"

def t(key):
    """获取当前语言的翻译文本"""
    return LANGUAGES.get(current_lang, LANGUAGES["简体中文"]).get(key, key)


def init_data_file():
    if not os.path.exists(DATA_FILE):
        default_data = {
            "memos": [],
            "courses": [],
            "time_slots": DEFAULT_TIME_SLOTS
        }
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(default_data, f, indent=4, ensure_ascii=False)
    else:
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            updated = False
            if "courses" not in data:
                data["courses"] = []
                updated = True
            if "time_slots" not in data or len(data["time_slots"]) < 12:
                data["time_slots"] = DEFAULT_TIME_SLOTS
                updated = True
            if updated:
                with open(DATA_FILE, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=4, ensure_ascii=False)
        except Exception:
            pass

def load_data():
    init_data_file()
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"memos": [], "courses": [], "time_slots": DEFAULT_TIME_SLOTS}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


class SettingsWindow(ctk.CTkToplevel):
    def __init__(self, master, current_slots, callback):
        super().__init__(master)
        self.title(t("settings_title"))
        self.geometry("380x650")
        self.attributes("-topmost", True)
        self.callback = callback

        ctk.CTkLabel(self, text=t("settings_hint"), font=ctk.CTkFont(weight="bold")).pack(pady=15)

        self.scroll = ctk.CTkScrollableFrame(self, corner_radius=10)
        self.scroll.pack(fill="both", expand=True, padx=20, pady=5)

        self.entries = []
        for i in range(12):
            f = ctk.CTkFrame(self.scroll, fg_color="transparent")
            f.pack(fill="x", pady=5)
            ctk.CTkLabel(f, text=t("period_label").format(i + 1), width=60).pack(side="left")
            disp_val = current_slots[i].replace("\n", " - ") if i < len(current_slots) else ""
            e = ctk.CTkEntry(f, width=180)
            e.insert(0, disp_val)
            e.pack(side="right")
            self.entries.append(e)

        btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        btn_frame.pack(pady=15)
        ctk.CTkButton(btn_frame, text=t("reset_default"), width=100, fg_color="transparent", border_width=1, command=self.reset_def).pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text=t("save_settings"), width=100, command=self.save_slots).pack(side="left", padx=10)

    def reset_def(self):
        for i, e in enumerate(self.entries):
            e.delete(0, 'end')
            e.insert(0, DEFAULT_TIME_SLOTS[i].replace("\n", " - "))

    def save_slots(self):
        new_slots = []
        for e in self.entries:
            val = e.get().strip()
            if "-" in val:
                parts = val.split("-", 1)
                new_slots.append(f"{parts[0].strip()}\n{parts[1].strip()}")
            else:
                new_slots.append(val)
        self.callback(new_slots)
        self.destroy()


class CampusSyncApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(t("app_title"))
        self.geometry("1100x750")

        # Grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # --- 左侧导航栏 ---
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0, width=200)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.logo_label = ctk.CTkLabel(self.navigation_frame, text="CampusSync",
                                       font=ctk.CTkFont(size=22, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 30))

        self.timetable_btn = self._create_nav_btn(t("nav_timetable"), self.show_timetable_frame, 1)
        self.memo_btn = self._create_nav_btn(t("nav_memo"), self.show_memo_frame, 2)
        self.timer_btn = self._create_nav_btn(t("nav_timer"), self.show_timer_frame, 3)

        # 语言切换放在导航栏底部
        lang_frame = ctk.CTkFrame(self.navigation_frame, fg_color="transparent")
        lang_frame.grid(row=6, column=0, padx=10, pady=(0, 15), sticky="sew")
        ctk.CTkLabel(lang_frame, text=t("lang_label"), font=ctk.CTkFont(size=11)).pack(pady=(0, 5))
        self.lang_combo = ctk.CTkComboBox(lang_frame, values=list(LANGUAGES.keys()), width=150, command=self.change_language)
        self.lang_combo.set(current_lang)
        self.lang_combo.pack()

        # --- 右侧内容区 ---
        self.timetable_frame = TimetableFrame(self)
        self.memo_frame = MemoFrame(self)
        self.timer_frame = TimerFrame(self)

        self.show_timetable_frame()

    def _create_nav_btn(self, text, command, row):
        btn = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=45, border_spacing=10,
                            text=text, fg_color="transparent", text_color=("gray10", "gray90"),
                            hover_color=("gray70", "gray30"), anchor="w", font=ctk.CTkFont(size=14),
                            command=command)
        btn.grid(row=row, column=0, sticky="ew")
        return btn

    def change_language(self, lang_name):
        global current_lang
        current_lang = lang_name

        # 更新窗口标题
        self.title(t("app_title"))

        # 更新导航按钮文字
        self.timetable_btn.configure(text=t("nav_timetable"))
        self.memo_btn.configure(text=t("nav_memo"))
        self.timer_btn.configure(text=t("nav_timer"))

        # 重建右侧各 Frame 的 UI 文本
        self.timetable_frame.rebuild_ui()
        self.memo_frame.rebuild_ui()
        self.timer_frame.rebuild_ui()

    def select_frame_by_name(self, name):
        self.timetable_btn.configure(fg_color=("gray75", "gray25") if name == "timetable" else "transparent")
        self.memo_btn.configure(fg_color=("gray75", "gray25") if name == "memo" else "transparent")
        self.timer_btn.configure(fg_color=("gray75", "gray25") if name == "timer" else "transparent")

        for frame in [self.timetable_frame, self.memo_frame, self.timer_frame]:
            frame.grid_forget()

        target = getattr(self, f"{name}_frame")
        target.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    def show_timetable_frame(self):
        self.select_frame_by_name("timetable")
        self.timetable_frame.render_grid()

    def show_memo_frame(self):
        self.select_frame_by_name("memo")
        self.memo_frame.refresh_list()

    def show_timer_frame(self):
        self.select_frame_by_name("timer")


class TimetableFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=15, fg_color="transparent")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.add_course_frame = ctk.CTkFrame(self, corner_radius=10)
        self.add_course_frame.grid(row=0, column=0, sticky="ew", pady=(0, 15), padx=5)

        self.c_name = ctk.CTkEntry(self.add_course_frame, placeholder_text=t("course_name"), width=140)
        self.c_name.grid(row=0, column=0, padx=8, pady=10)

        self.c_room = ctk.CTkEntry(self.add_course_frame, placeholder_text=t("classroom"), width=110)
        self.c_room.grid(row=0, column=1, padx=8, pady=10)

        self.c_day = ctk.CTkComboBox(self.add_course_frame, values=t("days")[1:], width=80)
        self.c_day.grid(row=0, column=2, padx=8, pady=10)
        self.c_day.set(t("days")[1])

        self.c_start = ctk.CTkComboBox(self.add_course_frame, values=[str(i) for i in range(1, 13)], width=60)
        self.c_start.grid(row=0, column=3, padx=8, pady=10)
        self.c_start.set("1")

        self.c_end = ctk.CTkComboBox(self.add_course_frame, values=[str(i) for i in range(1, 13)], width=60)
        self.c_end.grid(row=0, column=4, padx=8, pady=10)
        self.c_end.set("2")

        self.add_btn = ctk.CTkButton(self.add_course_frame, text=t("add_course"), command=self.add_course, width=100, font=ctk.CTkFont(weight="bold"))
        self.add_btn.grid(row=0, column=5, padx=(20, 10), pady=10)

        self.settings_btn = ctk.CTkButton(self.add_course_frame, text=t("custom_time"), width=110, fg_color="#2b2b2b", hover_color="#3b3b3b", command=self.open_settings)
        self.settings_btn.grid(row=0, column=6, padx=(10, 8), pady=10)

        self.scroll_canvas = ctk.CTkScrollableFrame(self, corner_radius=15)
        self.scroll_canvas.grid(row=1, column=0, sticky="nsew")
        for i in range(8):
            self.scroll_canvas.grid_columnconfigure(i, weight=1, minsize=110)

    def rebuild_ui(self):
        """语言切换时重建所有文本"""
        self.c_name.configure(placeholder_text=t("course_name"))
        self.c_room.configure(placeholder_text=t("classroom"))
        self.c_day.configure(values=t("days")[1:])
        self.c_day.set(t("days")[1])
        self.add_btn.configure(text=t("add_course"))
        self.settings_btn.configure(text=t("custom_time"))
        self.render_grid()

    def open_settings(self):
        data = load_data()
        current_slots = data.get("time_slots", DEFAULT_TIME_SLOTS)
        SettingsWindow(self, current_slots, self.update_time_slots)

    def update_time_slots(self, new_slots):
        data = load_data()
        data["time_slots"] = new_slots
        save_data(data)
        self.render_grid()

    def add_course(self):
        name = self.c_name.get().strip()
        room = self.c_room.get().strip()
        start = int(self.c_start.get())
        end = int(self.c_end.get())

        if not name or start > end:
            return

        # 将当前语言的星期文案映射为数字 1-7
        day_text = self.c_day.get()
        day_values = t("days")
        day_index = day_values.index(day_text) if day_text in day_values else 1

        new_course = {
            "id": str(uuid.uuid4()),
            "name": name,
            "location": room,
            "day_of_week": day_index,
            "start_period": start,
            "end_period": end,
            "color": random.choice(COURSE_COLORS)
        }

        data = load_data()
        data["courses"].append(new_course)
        save_data(data)
        self.c_name.delete(0, 'end')
        self.render_grid()

    def render_grid(self):
        for widget in self.scroll_canvas.winfo_children():
            widget.destroy()
        days = t("days")
        for j, text in enumerate(days):
            ctk.CTkLabel(self.scroll_canvas, text=text, font=ctk.CTkFont(weight="bold", size=14)).grid(row=0, column=j, pady=(15, 10))

        data = load_data()
        time_slots = data.get("time_slots", DEFAULT_TIME_SLOTS)

        # 左侧时间列渲染
        for i in range(1, 13):
            disp = time_slots[i - 1] if i - 1 < len(time_slots) else f"{i}"
            slot_frame = ctk.CTkFrame(self.scroll_canvas, fg_color="transparent")
            slot_frame.grid(row=i, column=0, pady=15, padx=5)
            ctk.CTkLabel(slot_frame, text=f"{i}", font=ctk.CTkFont(size=14, weight="bold")).pack()
            ctk.CTkLabel(slot_frame, text=disp, font=ctk.CTkFont(size=10), text_color="gray60").pack()

        for course in data.get("courses", []):
            try:
                row_start = course["start_period"]
                row_span = course["end_period"] - course["start_period"] + 1
                col = course["day_of_week"]
                card = ctk.CTkFrame(self.scroll_canvas, fg_color=course["color"], corner_radius=10)
                card.grid(row=row_start, column=col, rowspan=row_span, sticky="nsew", padx=3, pady=3)
                ctk.CTkLabel(card, text=course["name"], font=ctk.CTkFont(size=12, weight="bold"), text_color="white", wraplength=90).pack(pady=(8, 0))
                ctk.CTkLabel(card, text=course["location"], font=ctk.CTkFont(size=10), text_color="#F0F0F0", wraplength=90).pack(pady=2)
                del_btn = ctk.CTkButton(card, text="×", width=18, height=18, fg_color="transparent", hover_color="#990000",
                                        command=lambda c_id=course["id"]: self.delete_course(c_id))
                del_btn.place(relx=1.0, rely=0, anchor="ne")
            except Exception:
                pass

    def delete_course(self, c_id):
        data = load_data()
        data["courses"] = [c for c in data["courses"] if c["id"] != c_id]
        save_data(data)
        self.render_grid()


class MemoFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=15, fg_color="transparent")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.input_frame = ctk.CTkFrame(self, corner_radius=10)
        self.input_frame.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        self.input_frame.grid_columnconfigure(0, weight=3)
        self.input_frame.grid_columnconfigure((1, 2, 3), weight=1)

        self.task_entry = ctk.CTkEntry(self.input_frame, placeholder_text=t("memo_placeholder"))
        self.task_entry.grid(row=0, column=0, padx=15, pady=20, sticky="ew")

        self.ddl_entry = ctk.CTkEntry(self.input_frame, placeholder_text=t("ddl_placeholder"), width=130)
        self.ddl_entry.grid(row=0, column=1, padx=10, pady=20, sticky="ew")

        self.priority_combo = ctk.CTkComboBox(self.input_frame, values=[t("priority_high"), t("priority_mid"), t("priority_low")], width=100)
        self.priority_combo.grid(row=0, column=2, padx=10, pady=20)
        self.priority_combo.set(t("priority_mid"))

        self.add_btn = ctk.CTkButton(self.input_frame, text=t("add_confirm"), command=self.add_task, width=110, font=ctk.CTkFont(weight="bold"))
        self.add_btn.grid(row=0, column=3, padx=15, pady=20)

        self.list_frame = ctk.CTkScrollableFrame(self, corner_radius=15)
        self.list_frame.grid(row=1, column=0, sticky="nsew")
        self.list_frame.grid_columnconfigure(0, weight=1)

    def rebuild_ui(self):
        """语言切换时重建所有文本"""
        self.task_entry.configure(placeholder_text=t("memo_placeholder"))
        self.ddl_entry.configure(placeholder_text=t("ddl_placeholder"))
        self.priority_combo.configure(values=[t("priority_high"), t("priority_mid"), t("priority_low")])
        self.priority_combo.set(t("priority_mid"))
        self.add_btn.configure(text=t("add_confirm"))
        self.refresh_list()

    def add_task(self):
        name = self.task_entry.get().strip()
        ddl = self.ddl_entry.get().strip()
        if not name or not ddl:
            return
        try:
            datetime.strptime(ddl, "%Y-%m-%d")
        except ValueError:
            return
        task = {"id": str(uuid.uuid4()), "name": name, "priority": self.priority_combo.get(), "ddl": ddl, "completed": False}
        data = load_data()
        data["memos"].append(task)
        save_data(data)
        self.task_entry.delete(0, 'end')
        self.refresh_list()

    def refresh_list(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()
        data = load_data()
        memos = data.get("memos", [])

        # 按优先级排序（使用 emoji 前缀判断）
        def priority_key(m):
            p = m.get("priority", "")
            if "🔴" in p:
                return 0
            elif "🟡" in p:
                return 1
            elif "🟢" in p:
                return 2
            return 99
        memos.sort(key=lambda x: (priority_key(x), x.get("ddl", "")))

        for i, memo in enumerate(memos):
            bg = ("gray25", "gray30")
            try:
                days_left = (datetime.strptime(memo["ddl"], "%Y-%m-%d") - datetime.now()).days
                if days_left <= 3 and days_left >= 0 and "🔴" in memo.get("priority", ""):
                    bg = "#8B0000"
            except Exception:
                pass

            f = ctk.CTkFrame(self.list_frame, fg_color=bg, corner_radius=10)
            f.grid(row=i, column=0, sticky="ew", pady=8, padx=10)
            f.grid_columnconfigure(0, weight=1)

            lbl = ctk.CTkLabel(f, text=f" {memo.get('name')}     |    DDL: {memo.get('ddl')}    |    {memo.get('priority')}",
                               font=ctk.CTkFont(size=14, weight="bold"), text_color="white", anchor="w")
            lbl.grid(row=0, column=0, padx=20, pady=15, sticky="w")

            ctk.CTkButton(f, text=t("done_delete"), width=90, fg_color="#4CAF50", hover_color="#388E3C",
                          command=lambda m_id=memo["id"]: self.delete_task(m_id)).grid(row=0, column=1, padx=20)

    def delete_task(self, m_id):
        data = load_data()
        data["memos"] = [m for m in data["memos"] if m["id"] != m_id]
        save_data(data)
        self.refresh_list()


class TimerFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=15, fg_color="transparent")

        self.time_left = 25 * 60
        self.running = False
        self.timer_id = None

        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_columnconfigure(0, weight=1)

        # 自定义设定框
        self.setup_frame = ctk.CTkFrame(self, corner_radius=20)
        self.setup_frame.grid(row=0, column=0, pady=40, ipadx=10, ipady=5)

        self.focus_lbl = ctk.CTkLabel(self.setup_frame, text=t("focus_label"), font=ctk.CTkFont(size=16, weight="bold"))
        self.focus_lbl.pack(side="left", padx=15, pady=10)
        self.min_entry = ctk.CTkEntry(self.setup_frame, width=70, font=ctk.CTkFont(size=16), justify="center")
        self.min_entry.insert(0, "25")
        self.min_entry.pack(side="left", padx=5, pady=10)

        self.apply_btn = ctk.CTkButton(self.setup_frame, text=t("set_btn"), width=70,
                                       font=ctk.CTkFont(weight="bold"), command=self.apply_time)
        self.apply_btn.pack(side="left", padx=15, pady=10)

        self.time_label = ctk.CTkLabel(self, text="25:00", font=ctk.CTkFont(size=160, weight="bold"))
        self.time_label.grid(row=1, column=0, pady=20)

        ctrl = ctk.CTkFrame(self, fg_color="transparent")
        ctrl.grid(row=2, column=0, pady=40)

        self.start_btn = ctk.CTkButton(ctrl, text=t("start_btn"), command=self.start_timer, width=140, height=55, corner_radius=27, font=ctk.CTkFont(size=18, weight="bold"))
        self.start_btn.grid(row=0, column=0, padx=20)

        self.pause_btn = ctk.CTkButton(ctrl, text=t("pause_btn"), command=self.pause_timer, width=140, height=55, corner_radius=27, font=ctk.CTkFont(size=18, weight="bold"))
        self.pause_btn.grid(row=0, column=1, padx=20)

        self.reset_btn_widget = ctk.CTkButton(ctrl, text=t("reset_btn"), command=self.reset_timer, width=140, height=55, corner_radius=27, fg_color="#D32F2F", font=ctk.CTkFont(size=18, weight="bold"))
        self.reset_btn_widget.grid(row=0, column=2, padx=20)

    def rebuild_ui(self):
        """语言切换时重建所有文本"""
        self.focus_lbl.configure(text=t("focus_label"))
        self.apply_btn.configure(text=t("set_btn"))
        self.start_btn.configure(text=t("start_btn"))
        self.pause_btn.configure(text=t("pause_btn"))
        self.reset_btn_widget.configure(text=t("reset_btn"))

    def apply_time(self):
        if self.running:
            return
        val = self.min_entry.get().strip()
        if val.isdigit() and int(val) > 0:
            self.time_left = int(val) * 60
            self.update_label()

    def update_label(self):
        mins, secs = divmod(self.time_left, 60)
        self.time_label.configure(text=f"{mins:02d}:{secs:02d}")

    def count_down(self):
        if self.running and self.time_left > 0:
            self.time_left -= 1
            self.update_label()
            self.timer_id = self.after(1000, self.count_down)
        elif self.time_left <= 0 and self.running:
            self.running = False
            self.reset_timer()

    def start_timer(self):
        if not self.running:
            self.running = True
            self.count_down()

    def pause_timer(self):
        self.running = False
        if self.timer_id:
            self.after_cancel(self.timer_id)
            self.timer_id = None

    def reset_timer(self):
        self.pause_timer()
        val = self.min_entry.get().strip()
        minutes = int(val) if val.isdigit() and int(val) > 0 else 25
        self.time_left = minutes * 60
        self.update_label()


if __name__ == "__main__":
    app = CampusSyncApp()
    app.mainloop()
