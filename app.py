import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="NurseShift Zero-Cost", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>.stButton button{width:100%;} .patient-card{border:1px solid #ddd;border-radius:8px;padding:8px;margin:4px 0;border-left:6px solid #007bff;} .urgent{color:#dc3545;font-weight:bold;}</style>""", unsafe_allow_html=True)

if "patients" not in st.session_state:
    st.session_state.patients = [
        {"id":1,"name":"Maria Garcia","age":68,"sex":"F","code_status":"Full Code","allergies":["Penicillin"],"isolation":"Contact","status":"stable","diagnosis":"CHF exacerbation","hospital_day":3,"brief_history":"SOB, bilateral edema. PMH: HTN, T2DM","treating_physician":"Dr. Patel","admission_date":"2026-07-02","active_orders":{"iv_fluid":{"type":"NS + KCl","volume":"1000mL","additives":"KCl 20mEq","rate":"75 ml/hr"},"diet":"Cardiac 2g Na","activity":"OOB assist","o2_therapy":{"device":"NC","rate":"2 L/min","spo2_target":"92-96%"},"urinary":"Foley","samples_other":"Strict I/O, daily wt"},"medications":[{"drug":"Furosemide","dose":"40mg","route":"IV","frequency":"BID","scheduled_times":["08:00","20:00"],"status":"active","added_at":None},{"drug":"Metformin","dose":"500mg","route":"PO","frequency":"BID","scheduled_times":["08:00","18:00"],"status":"active","added_at":None}],"tasks":[{"category":"med","time":"08:00","status":"done","desc":"Furosemide IV"},{"category":"assess","time":"09:30","status":"upcoming","desc":"Volume status"},{"category":"lab","time":"06:00","status":"overdue","desc":"BMP"},{"category":"dressing","time":"10:00","status":"upcoming","desc":"Foley care"}],"diagnostics":[{"type":"test","name":"CXR","ordered_time":"2026-07-03 10:00","due_time":"2026-07-03 14:00","status":"done","done_time":"13:30"},{"type":"consult","name":"Cardiology","ordered_time":"2026-07-04 08:00","due_time":"2026-07-05 09:00","status":"pending","done_time":None}],"charges":[{"category":"med","item":"Furosemide 40mg vial","qty":2,"charged_in_his":True},{"category":"supply","item":"Foley kit","qty":1,"charged_in_his":False}],"nursing_notes":[{"timestamp":"2026-07-05 08:15","text":"Improved SOB post diuresis. No edema increase.","vitals":{"bp":"128/72","hr":88,"temp":"36.8","spo2":"94","rr":18},"io":{"in":250,"out":1800,"balance":-1550}}],"midshift_updates":[{"timestamp":"2026-07-05 09:30","field":"tasks[2].status","old":"upcoming","new":"done"}],"io_balance":-1550},
        {"id":2,"name":"Robert Chen","age":55,"sex":"M","code_status":"DNR","allergies":["NKDA"],"isolation":"None","status":"deteriorating","diagnosis":"Post-op CABG day 2","hospital_day":2,"brief_history":"CABG x3. Now AFib, low output.","treating_physician":"Dr. Kim","admission_date":"2026-07-03","active_orders":{"iv_fluid":{"type":"LR","volume":"500mL","additives":"None","rate":"50 ml/hr"},"diet":"NPO","activity":"CBR","o2_therapy":{"device":"NC","rate":"3 L/min","spo2_target":"94-98%"},"urinary":"Foley","samples_other":"q1h neuro checks"},"medications":[{"drug":"Amiodarone","dose":"150mg","route":"IV","frequency":"x1 now","scheduled_times":["09:15"],"status":"active","added_at":"2026-07-05 09:15"},{"drug":"Metoprolol","dose":"25mg","route":"PO","frequency":"TID","scheduled_times":["08:00","14:00","20:00"],"status":"active","added_at":None}],"tasks":[{"category":"med","time":"09:15","status":"done","desc":"Amiodarone load"},{"category":"assess","time":"10:00","status":"upcoming","desc":"Neuro checks q1h"},{"category":"lab","time":"07:00","status":"overdue","desc":"Troponin"},{"category":"fup","time":"11:00","status":"upcoming","desc":"Echo review"}],"diagnostics":[{"type":"test","name":"Troponin","ordered_time":"2026-07-05 07:00","due_time":"2026-07-05 08:00","status":"pending","done_time":None}],"charges":[{"category":"med","item":"Amiodarone 150mg","qty":1,"charged_in_his":True}],"nursing_notes":[{"timestamp":"2026-07-05 09:45","text":"HR 112 AFib. BP 88/54. Notified MD.","vitals":{"bp":"88/54","hr":112,"temp":"37.1","spo2":"93","rr":22},"io":{"in":120,"out":45,"balance":75}}],"midshift_updates":[],"io_balance":75},
        {"id":3,"name":"Aisha Patel","age":42,"sex":"F","code_status":"Full Code","allergies":["Sulfa"],"isolation":"Droplet","status":"improving","diagnosis":"Pneumonia + AKI","hospital_day":4,"brief_history":"Fever, cough, hypoxia. Cr 2.1 baseline 0.9.","treating_physician":"Dr. Lopez","admission_date":"2026-07-01","active_orders":{"iv_fluid":{"type":"NS","volume":"1000mL","additives":"None","rate":"100 ml/hr"},"diet":"Soft","activity":"OOB","o2_therapy":{"device":"NC","rate":"4 L/min","spo2_target":"92%"},"urinary":"Self-void","samples_other":"q6h I/O, renal diet"},"medications":[{"drug":"Ceftriaxone","dose":"1g","route":"IV","frequency":"Daily","scheduled_times":["08:00"],"status":"active","added_at":None},{"drug":"Furosemide","dose":"20mg","route":"IV","frequency":"Daily","scheduled_times":["09:00"],"status":"active","added_at":None}],"tasks":[{"category":"med","time":"08:00","status":"done","desc":"Ceftriaxone"},{"category":"lab","time":"06:30","status":"done","desc":"BMP/Cr"},{"category":"assess","time":"10:30","status":"upcoming","desc":"Lung sounds"}],"diagnostics":[{"type":"test","name":"CT Chest","ordered_time":"2026-07-04 14:00","due_time":"2026-07-05 08:00","status":"done","done_time":"07:45"}],"charges":[{"category":"test","item":"CT Chest w/o contrast","qty":1,"charged_in_his":True}],"nursing_notes":[{"timestamp":"2026-07-05 07:50","text":"SpO2 95% on 4L. Improved cough. Cr stable 1.8.","vitals":{"bp":"118/68","hr":92,"temp":"36.9","spo2":"95","rr":20},"io":{"in":800,"out":650,"balance":150}}],"midshift_updates":[],"io_balance":150},
        {"id":4,"name":"James Wilson","age":78,"sex":"M","code_status":"Comfort Care","allergies":["NKDA"],"isolation":"None","status":"discharge","diagnosis":"Hip fracture s/p ORIF","hospital_day":5,"brief_history":"Fall at home. ORIF yesterday. Pain controlled.","treating_physician":"Dr. Singh","admission_date":"2026-06-30","active_orders":{"iv_fluid":{"type":"None","volume":"-","additives":"-","rate":"-"},"diet":"Regular","activity":"OOB with PT","o2_therapy":{"device":"Room air","rate":"-","spo2_target":"-"},"urinary":"Self-void","samples_other":"PT/OT eval"},"medications":[{"drug":"Oxycodone","dose":"5mg","route":"PO","frequency":"q4h PRN","scheduled_times":["08:00","12:00","16:00","20:00"],"status":"active","added_at":None}],"tasks":[{"category":"med","time":"08:00","status":"done","desc":"Oxycodone"},{"category":"assess","time":"09:00","status":"upcoming","desc":"Pain 2/10"},{"category":"fup","time":"14:00","status":"upcoming","desc":"Discharge planning"}],"diagnostics":[{"type":"procedure","name":"XR Hip","ordered_time":"2026-07-04 16:00","due_time":"2026-07-04 17:00","status":"done","done_time":"16:45"}],"charges":[{"category":"procedure","item":"ORIF hip","qty":1,"charged_in_his":True}],"nursing_notes":[{"timestamp":"2026-07-05 08:45","text":"Ready for SNF. Pain 3/10. Ambulated 20ft with PT.","vitals":{"bp":"134/78","hr":78,"temp":"36.6","spo2":"97","rr":16},"io":{"in":400,"out":350,"balance":50}}],"midshift_updates":[],"io_balance":50},
        {"id":5,"name":"Elena Rodriguez","age":61,"sex":"F","code_status":"Full Code","allergies":["Aspirin"],"isolation":"None","status":"stable","diagnosis":"T2DM + cellulitis","hospital_day":2,"brief_history":"Left leg cellulitis, uncontrolled sugars.","treating_physician":"Dr. Nguyen","admission_date":"2026-07-03","active_orders":{"iv_fluid":{"type":"D5NS","volume":"1000mL","additives":"None","rate":"80 ml/hr"},"diet":"Diabetic","activity":"OOB","o2_therapy":{"device":"Room air","rate":"-","spo2_target":"-"},"urinary":"Self-void","samples_other":"qAC FSBS"},"medications":[{"drug":"Insulin glargine","dose":"24 units","route":"SQ","frequency":"Daily","scheduled_times":["08:00"],"status":"active","added_at":None},{"drug":"Vancomycin","dose":"1g","route":"IV","frequency":"q12h","scheduled_times":["09:00","21:00"],"status":"active","added_at":None}],"tasks":[{"category":"med","time":"08:00","status":"done","desc":"Glargine"},{"category":"lab","time":"06:00","status":"done","desc":"FSBS 142"},{"category":"dressing","time":"10:00","status":"upcoming","desc":"Leg wound care"}],"diagnostics":[{"type":"test","name":"Wound culture","ordered_time":"2026-07-04 11:00","due_time":"2026-07-05 10:00","status":"pending","done_time":None}],"charges":[{"category":"med","item":"Vancomycin 1g","qty":2,"charged_in_his":False}],"nursing_notes":[{"timestamp":"2026-07-05 07:20","text":"FSBS 142. Leg erythema decreasing. Afebrile.","vitals":{"bp":"122/74","hr":84,"temp":"36.7","spo2":"98","rr":18},"io":{"in":600,"out":480,"balance":120}}],"midshift_updates":[],"io_balance":120},
        {"id":6,"name":"Thomas Brown","age":49,"sex":"M","code_status":"Full Code","allergies":["NKDA"],"isolation":"Contact","status":"stable","diagnosis":"AKI on CKD stage 3","hospital_day":1,"brief_history":"N/V, elevated Cr. Dehydration vs obstruction.","treating_physician":"Dr. Rao","admission_date":"2026-07-05","active_orders":{"iv_fluid":{"type":"NS","volume":"1000mL","additives":"None","rate":"125 ml/hr"},"diet":"Renal 2g K","activity":"OOB","o2_therapy":{"device":"Room air","rate":"-","spo2_target":"-"},"urinary":"Foley","samples_other":"Strict I/O, bladder scan q4h"},"medications":[{"drug":"Furosemide","dose":"20mg","route":"IV","frequency":"Daily","scheduled_times":["10:00"],"status":"active","added_at":None}],"tasks":[{"category":"med","time":"10:00","status":"upcoming","desc":"Furosemide"},{"category":"lab","time":"08:00","status":"done","desc":"BMP/Cr 3.2"},{"category":"assess","time":"11:00","status":"upcoming","desc":"Volume exam"}],"diagnostics":[{"type":"test","name":"Renal US","ordered_time":"2026-07-05 09:00","due_time":"2026-07-05 11:00","status":"pending","done_time":None}],"charges":[{"category":"test","item":"Renal ultrasound","qty":1,"charged_in_his":False}],"nursing_notes":[{"timestamp":"2026-07-05 08:30","text":"Cr 3.2 (baseline 2.1). Foley output low. MD notified.","vitals":{"bp":"108/62","hr":96,"temp":"36.5","spo2":"96","rr":20},"io":{"in":950,"out":120,"balance":830}}],"midshift_updates":[],"io_balance":830},
        {"id":7,"name":"Sophia Kim","age":35,"sex":"F","code_status":"Full Code","allergies":["Latex"],"isolation":"None","status":"stable","diagnosis":"Postpartum hemorrhage s/p D&C","hospital_day":1,"brief_history":"PPH after delivery. Transfused 2U PRBC.","treating_physician":"Dr. Martinez","admission_date":"2026-07-04","active_orders":{"iv_fluid":{"type":"LR + Pitocin","volume":"1000mL","additives":"Pitocin 20U","rate":"125 ml/hr"},"diet":"Regular","activity":"OOB","o2_therapy":{"device":"Room air","rate":"-","spo2_target":"-"},"urinary":"Foley","samples_other":"q15min fundal checks x1h then q30min"},"medications":[{"drug":"Oxytocin","dose":"20U","route":"IV","frequency":"in IV fluid","scheduled_times":["ongoing"],"status":"active","added_at":None},{"drug":"Ibuprofen","dose":"600mg","route":"PO","frequency":"q6h","scheduled_times":["08:00","14:00","20:00"],"status":"active","added_at":None}],"tasks":[{"category":"assess","time":"08:30","status":"done","desc":"Fundal tone firm"},{"category":"med","time":"08:00","status":"done","desc":"Ibuprofen"},{"category":"fup","time":"12:00","status":"upcoming","desc":"Hgb check"}],"diagnostics":[{"type":"test","name":"CBC","ordered_time":"2026-07-05 07:00","due_time":"2026-07-05 08:00","status":"done","done_time":"07:45"}],"charges":[{"category":"med","item":"Oxytocin 20U","qty":1,"charged_in_his":True}],"nursing_notes":[{"timestamp":"2026-07-05 08:40","text":"Fundus firm, lochia moderate. Hgb 9.8 stable. Pain 4/10.","vitals":{"bp":"118/66","hr":88,"temp":"36.8","spo2":"99","rr":16},"io":{"in":1100,"out":280,"balance":820}}],"midshift_updates":[],"io_balance":820},
        {"id":8,"name":"David Lee","age":82,"sex":"M","code_status":"DNR","allergies":["NKDA"],"isolation":"None","status":"improving","diagnosis":"Delirium + UTI","hospital_day":3,"brief_history":"Confusion, fever. UA +leuk. Now oriented x3.","treating_physician":"Dr. Chen","admission_date":"2026-07-02","active_orders":{"iv_fluid":{"type":"NS","volume":"500mL","additives":"None","rate":"75 ml/hr"},"diet":"Regular","activity":"OOB with assist","o2_therapy":{"device":"Room air","rate":"-","spo2_target":"-"},"urinary":"Condom cath","samples_other":"CAM-ICU qshift"},"medications":[{"drug":"Ceftriaxone","dose":"1g","route":"IV","frequency":"Daily","scheduled_times":["08:00"],"status":"active","added_at":None},{"drug":"Haloperidol","dose":"0.5mg","route":"PO","frequency":"q6h PRN","scheduled_times":["08:00","14:00","20:00"],"status":"active","added_at":None}],"tasks":[{"category":"med","time":"08:00","status":"done","desc":"Ceftriaxone"},{"category":"assess","time":"09:00","status":"upcoming","desc":"CAM-ICU"},{"category":"fup","time":"13:00","status":"upcoming","desc":"UA results"}],"diagnostics":[{"type":"test","name":"UA","ordered_time":"2026-07-04 20:00","due_time":"2026-07-05 08:00","status":"done","done_time":"07:30"}],"charges":[{"category":"test","item":"Urinalysis","qty":1,"charged_in_his":True}],"nursing_notes":[{"timestamp":"2026-07-05 08:50","text":"CAM-ICU negative. Oriented. Afebrile. Appetite good.","vitals":{"bp":"126/70","hr":76,"temp":"36.4","spo2":"97","rr":16},"io":{"in":450,"out":380,"balance":70}}],"midshift_updates":[],"io_balance":70}
    ]

if "selected_id" not in st.session_state: st.session_state.selected_id = None
if "shift" not in st.session_state: st.session_state.shift = "Morning"

shifts = {"Morning": ("07:00", "14:00"), "Evening": ("13:00", "20:00"), "Night": ("19:00", "08:00")}

def get_patient(pid):
    return next((p for p in st.session_state.patients if p["id"] == pid), None)

def update_patient(pid, key, value):
    for i, p in enumerate(st.session_state.patients):
        if p["id"] == pid:
            st.session_state.patients[i][key] = value
            st.session_state.patients[i]["midshift_updates"].append({
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "field": key, "old": "previous", "new": str(value)[:50]
            })
            break

# Top bar
st.title("🩺 NurseShift • Zero-Cost Kardex")
col1, col2 = st.columns([2,1])
with col1:
    new_shift = st.selectbox("Shift", list(shifts.keys()), index=list(shifts.keys()).index(st.session_state.shift), key="shift_sel")
    if new_shift != st.session_state.shift:
        st.session_state.shift = new_shift
        st.rerun()
with col2:
    st.metric("Now", datetime.now().strftime("%H:%M"))

nav = st.tabs(["📋 Overview", "⏱️ Timeline", "➕ Add Patient", "📤 End of Shift"])

# OVERVIEW
with nav[0]:
    st.subheader("Patient Cards — Tap to open detail")
    for p in st.session_state.patients:
        color = {"stable":"#28a745", "deteriorating":"#dc3545", "improving":"#17a2b8", "discharge":"#6c757d"}.get(p["status"], "#6c757d")
        with st.container():
            c1, c2 = st.columns([4,1])
            with c1:
                st.markdown(f"""<div class="patient-card" style="border-left-color:{color}">
                <b>{p['name']}</b> ({p['age']}y {p['sex']}) | Code: <b>{p['code_status']}</b><br>
                Allergies: {', '.join(p['allergies']) or 'NKDA'} | Isolation: {p['isolation']}<br>
                <span style="color:{color};font-weight:bold;">{p['status'].upper()}</span> • Hosp Day {p['hospital_day']} • {p['diagnosis'][:40]}
                </div>""", unsafe_allow_html=True)
            with c2:
                if st.button("Open", key=f"open_{p['id']}"):
                    st.session_state.selected_id = p["id"]
                    st.rerun()
    if st.session_state.selected_id:
        p = get_patient(st.session_state.selected_id)
        if p:
            st.divider()
            st.header(f"📋 {p['name']} Detail")
            dtabs = st.tabs(["✅ Tasks", "💊 Orders", "🔬 Diagnostics", "💰 Charges", "📝 Notes"])
            
            # Tasks
            with dtabs[0]:
                st.subheader("Shift Tasks (color-coded)")
                tasks_df = pd.DataFrame(p["tasks"])
                edited = st.data_editor(tasks_df, num_rows="dynamic", key=f"tasks_{p['id']}", use_container_width=True)
                if st.button("Save Tasks", key=f"save_tasks_{p['id']}"):
                    update_patient(p["id"], "tasks", edited.to_dict("records"))
                    st.success("Tasks saved + mid-shift log added")
                    st.rerun()
            
            # Orders
            with dtabs[1]:
                st.subheader("Active Orders (Front Kardex)")
                o = p["active_orders"]
                with st.form(f"orders_{p['id']}"):
                    iv_t = st.text_input("IV Type/Volume/Additives", f"{o['iv_fluid']['type']} {o['iv_fluid']['volume']} {o['iv_fluid']['additives']}")
                    iv_r = st.text_input("IV Rate (ml/hr)", o['iv_fluid']['rate'])
                    diet = st.text_input("Diet", o["diet"])
                    act = st.text_input("Activity", o["activity"])
                    o2d = st.text_input("O2 Device", o["o2_therapy"]["device"])
                    o2r = st.text_input("O2 Rate / SpO2 Target", f"{o['o2_therapy']['rate']} / {o['o2_therapy']['spo2_target']}")
                    uri = st.text_input("Urinary", o["urinary"])
                    other = st.text_input("Samples/Other", o["samples_other"])
                    if st.form_submit_button("Update Orders"):
                        new_o = {"iv_fluid":{"type":iv_t.split()[0] if iv_t else "", "volume":iv_t, "additives":iv_t, "rate":iv_r},
                                 "diet":diet, "activity":act,
                                 "o2_therapy":{"device":o2d, "rate":o2r.split("/")[0].strip() if "/" in o2r else o2r, "spo2_target":o2r.split("/")[-1].strip() if "/" in o2r else ""},
                                 "urinary":uri, "samples_other":other}
                        update_patient(p["id"], "active_orders", new_o)
                        st.success("Orders updated")
                        st.rerun()
            
            # Diagnostics
            with dtabs[2]:
                st.subheader("Diagnostics & Consults (Back Kardex)")
                dx_df = pd.DataFrame(p["diagnostics"])
                edited_dx = st.data_editor(dx_df, num_rows="dynamic", key=f"dx_{p['id']}")
                if st.button("Save Diagnostics", key=f"save_dx_{p['id']}"):
                    update_patient(p["id"], "diagnostics", edited_dx.to_dict("records"))
                    st.success("Diagnostics saved")
                    st.rerun()
            
            # Charges
            with dtabs[3]:
                st.subheader("Charges (pre-populated + add)")
                ch_df = pd.DataFrame(p["charges"])
                edited_ch = st.data_editor(ch_df, num_rows="dynamic", key=f"ch_{p['id']}")
                if st.button("Save Charges", key=f"save_ch_{p['id']}"):
                    update_patient(p["id"], "charges", edited_ch.to_dict("records"))
                    st.success("Charges saved")
                    st.rerun()
            
            # Notes + I/O
            with dtabs[4]:
                st.subheader("Nursing Notes + I/O Running Balance")
                for n in p["nursing_notes"][-4:]:
                    st.caption(f"**{n['timestamp']}** {n['text']}")
                    if n.get("vitals"): st.caption(f"Vitals: {n['vitals']}")
                    if n.get("io"): st.caption(f"I/O In/Out/Balance: {n['io']['in']}/{n['io']['out']}/{n['io']['balance']}")
                with st.form(f"note_{p['id']}"):
                    txt = st.text_area("Observation")
                    c1,c2,c3,c4,c5 = st.columns(5)
                    bp = c1.text_input("BP", "120/80")
                    hr = c2.number_input("HR", 40, 200, 80)
                    temp = c3.number_input("Temp °C", 35.0, 42.0, 36.8, 0.1)
                    spo2 = c4.number_input("SpO2 %", 70, 100, 95)
                    rr = c5.number_input("RR", 8, 40, 18)
                    io_in = st.number_input("I/O In (ml)", 0)
                    io_out = st.number_input("I/O Out (ml)", 0)
                    if st.form_submit_button("Add Note + Update I/O"):
                        last_bal = p.get("io_balance", 0)
                        new_bal = last_bal + io_in - io_out
                        new_note = {"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                                    "text": txt or "Note added",
                                    "vitals": {"bp":bp, "hr":hr, "temp":temp, "spo2":spo2, "rr":rr},
                                    "io": {"in":io_in, "out":io_out, "balance":new_bal}}
                        p["nursing_notes"].append(new_note)
                        update_patient(p["id"], "io_balance", new_bal)
                        st.success(f"Note added. New balance: {new_bal} ml")
                        st.rerun()
            
            if st.button("← Back to Overview"):
                st.session_state.selected_id = None
                st.rerun()

# TIMELINE
with nav[1]:
    st.subheader(f"Shift Timeline • {st.session_state.shift} ({shifts[st.session_state.shift][0]}-{shifts[st.session_state.shift][1]})")
    events = []
    start_h, end_h = [int(x.split(":")[0]) for x in shifts[st.session_state.shift]]
    for p in st.session_state.patients:
        for t in p["tasks"]:
            try:
                h = int(t["time"].split(":")[0])
                if start_h <= h <= end_h or (st.session_state.shift == "Night" and (h >= 19 or h <= 8)):
                    events.append({"time": t["time"], "pt": p["name"], "type": "Task", "desc": f"{t['category']}: {t['desc']}", "status": t["status"]})
            except: pass
        for n in p["nursing_notes"]:
            try:
                h = int(n["timestamp"].split()[1].split(":")[0])
                if start_h <= h <= end_h or (st.session_state.shift == "Night" and (h >= 19 or h <= 8)):
                    events.append({"time": n["timestamp"].split()[1][:5], "pt": p["name"], "type": "Note", "desc": n["text"][:45], "status": ""})
            except: pass
    events.sort(key=lambda x: x["time"])
    for e in events:
        clr = "#dc3545" if e["status"] == "overdue" else "#28a745" if e["status"] == "done" else "#007bff"
        st.markdown(f"**{e['time']}** | {e['pt']} | {e['type']}: {e['desc']} <span style='color:{clr}'>{e['status']}</span>", unsafe_allow_html=True)

# ADD PATIENT + KARDEX MOCK FLOW
with nav[2]:
    st.subheader("Kardex Intake Flow (Mock — user-editable)")
    st.caption("Upload photos (display only) → Simulate AI extract → Review/edit fields → Save to live shift")
    f1 = st.file_uploader("Front page photo (Orders + care plan)", type=["png","jpg","jpeg"], key="front")
    f2 = st.file_uploader("Back page photo (History + diagnostics)", type=["png","jpg","jpeg"], key="back")
    if f1: st.image(f1, width=280, caption="Front uploaded (mock OCR)")
    if f2: st.image(f2, width=280, caption="Back uploaded (mock OCR)")
    
    if st.button("🤖 Simulate AI Extraction (Mock)"):
        mock = {"name":"Demo Patient (Kardex)","age":67,"sex":"F","code_status":"Full Code","allergies":["NKDA"],"isolation":"None","status":"stable",
                "diagnosis":"COPD exacerbation","hospital_day":2,"brief_history":"Dyspnea, wheezing. PMH: COPD, CAD","treating_physician":"Dr. Rivera",
                "admission_date":"2026-07-04","active_orders":{"iv_fluid":{"type":"NS","volume":"1000mL","additives":"None","rate":"60 ml/hr"},"diet":"Soft","activity":"OOB","o2_therapy":{"device":"NC","rate":"2 L/min","spo2_target":"90-94%"},"urinary":"Self-void","samples_other":"Daily ABG"},"medications":[{"drug":"Prednisone","dose":"40mg","route":"PO","frequency":"Daily","scheduled_times":["08:00"],"status":"active","added_at":None}],"tasks":[{"category":"med","time":"08:00","status":"upcoming","desc":"Prednisone"},{"category":"assess","time":"09:00","status":"upcoming","desc":"Resp status"}],"diagnostics":[{"type":"test","name":"ABG","ordered_time":"2026-07-05 08:00","due_time":"2026-07-05 09:00","status":"pending","done_time":None}],"charges":[],"nursing_notes":[],"midshift_updates":[],"io_balance":0}
        st.session_state["mock_extract"] = mock
        st.success("AI mock extraction complete. Review & edit below, then save.")
    
    if "mock_extract" in st.session_state:
        m = st.session_state["mock_extract"]
        st.subheader("Review + Edit Extracted Data")
        with st.form("review_form"):
            nm = st.text_input("Name", m["name"])
            ag = st.number_input("Age", 0, 120, m["age"])
            sx = st.selectbox("Sex", ["M","F","Other"], index=["M","F","Other"].index(m["sex"]))
            cd = st.selectbox("Code Status", ["Full Code","DNR","DNAR","Comfort Care"], index=0)
            al = st.text_input("Allergies (comma)", ",".join(m["allergies"]))
            iso = st.text_input("Isolation", m["isolation"])
            stt = st.selectbox("Status", ["stable","deteriorating","improving","discharge"], index=["stable","deteriorating","improving","discharge"].index(m["status"]))
            dx = st.text_input("Diagnosis", m["diagnosis"])
            hd = st.number_input("Hospital Day", 1, 30, m["hospital_day"])
            hx = st.text_area("Brief History", m["brief_history"])
            md = st.text_input("Treating MD", m["treating_physician"])
            ad = st.text_input("Admission Date", m["admission_date"])
            iv = st.text_input("IV (type/volume/add/rate)", f"{m['active_orders']['iv_fluid']['type']} {m['active_orders']['iv_fluid']['rate']}")
            o2 = st.text_input("O2 (device/rate/target)", f"{m['active_orders']['o2_therapy']['device']} {m['active_orders']['o2_therapy']['rate']}")
            if st.form_submit_button("✅ Save Reviewed Patient to Active Shift"):
                new_id = max([x["id"] for x in st.session_state.patients] or [0]) + 1
                new_p = {"id":new_id,"name":nm,"age":ag,"sex":sx,"code_status":cd,"allergies":al.split(",") if al else ["NKDA"],"isolation":iso,"status":stt,
                         "diagnosis":dx,"hospital_day":hd,"brief_history":hx,"treating_physician":md,"admission_date":ad,
                         "active_orders":{"iv_fluid":{"type":iv.split()[0] if iv else "NS","volume":"1000mL","additives":"","rate":iv.split()[-1] if iv else "60 ml/hr"},"diet":"Soft","activity":"OOB","o2_therapy":{"device":o2.split()[0] if o2 else "NC","rate":o2.split()[1] if len(o2.split())>1 else "2 L/min","spo2_target":"90-94%"},"urinary":"Self-void","samples_other":""},
                         "medications":m["medications"],"tasks":m["tasks"],"diagnostics":m["diagnostics"],"charges":m["charges"],"nursing_notes":[],"midshift_updates":[],"io_balance":0}
                st.session_state.patients.append(new_p)
                del st.session_state["mock_extract"]
                st.success(f"Patient {nm} added from Kardex mock. View in Overview.")
                st.rerun()

# END OF SHIFT
with nav[3]:
    st.subheader("End-of-Shift Handoff SBAR Compiler")
    names = [p["name"] for p in st.session_state.patients]
    sel = st.multiselect("Patients for handoff", names, default=names[:3])
    if st.button("Compile SBAR Reports"):
        for nm in sel:
            p = next(x for x in st.session_state.patients if x["name"]==nm)
            latest = p["nursing_notes"][-1] if p["nursing_notes"] else {"text":"No notes","vitals":{},"io":{}}
            sbar = f"""**S**ituation: {p['name']}, {p['age']}y {p['sex']}, Code {p['code_status']}. Status: {p['status']}. I/O balance: {p.get('io_balance',0)} ml. Latest vitals: {latest.get('vitals',{})}
**B**ackground: {p['brief_history']}. Admitted {p['admission_date']} (Day {p['hospital_day']}). Dx: {p['diagnosis']}. MD: {p['treating_physician']}
**A**ssessment: {latest.get('text','')} Pending diagnostics: {[d['name'] for d in p['diagnostics'] if d['status']=='pending']}
**R**ecommendation: Continue current orders. Monitor I/O and status. Follow up pending items. Mid-shift updates logged."""
            st.markdown(sbar)
            st.download_button(f"Download {nm} SBAR", data=sbar, file_name=f"{nm.replace(' ','_')}_SBAR.txt")
