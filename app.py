# app.py
import streamlit as st
import runpy
from pathlib import Path

st.set_page_config(page_title="Sony FX6 Checklist", page_icon="✅", layout="centered")
st.title("🎬 Sony FX6 Checklist")

# Load checklist from Sony_FS6.py (same folder)
module = Path(__file__).with_name("Sony_FS6.py")
if not module.exists():
    st.error("Sony_FS6.py not found next to app.py.")
    st.stop()

ns = runpy.run_path(str(module))  # run the file and get its variables
raw = ns.get("CHECKLIST") or ns.get("STEPS") or ns.get("ITEMS")

# Fallback: treat non-empty lines as steps if no list variable exists
if raw is None:
    raw = [ln.strip() for ln in module.read_text(encoding="utf-8").splitlines()
           if ln.strip() and not ln.strip().startswith(("#","'''",'"""'))]

def norm(x):
    if isinstance(x, str): return {"step": x, "done": False, "notes": ""}
    if isinstance(x, dict): return {"step": x.get("step",""), "done": bool(x.get("done", False)), "notes": x.get("notes","")}
    try:
        return {"step": str(x[0]), "done": bool(x[1]) if len(x)>1 else False, "notes": str(x[2]) if len(x)>2 else ""}
    except Exception:
        return {"step": str(x), "done": False, "notes": ""}

if "items" not in st.session_state:
    st.session_state.items = [norm(i) for i in raw]

left, right = st.columns(2)
with left:
    if st.button("Reset all"):
        for it in st.session_state.items: it["done"] = False
with right:
    if st.button("Mark all done"):
        for it in st.session_state.items: it["done"] = True

st.divider()
for i, item in enumerate(st.session_state.items):
    c1, c2 = st.columns([0.1, 0.9])
    with c1:
        st.session_state.items[i]["done"] = st.checkbox("", value=item["done"], key=f"d_{i}")
    with c2:
        st.write(f"**{item['step']}**")
        st.session_state.items[i]["notes"] = st.text_input("Notes", value=item["notes"], key=f"n_{i}", label_visibility="collapsed")

st.divider()
new = st.text_input("Add a new step")
if st.button("Add") and new.strip():
    st.session_state.items.append({"step": new.strip(), "done": False, "notes": ""})
    st.rerun()
