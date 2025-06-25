# VIEW SORTED TASKS

priority_levels = ["LOW", "MEDIUM", "HIGH"]

def sort_key(task):
    p_index = priority_levels.index(task["Priority"]) # priority index
    y, m, d = task["Deadline"][0].split("-")    # deadline
    m_padded = m.zfill(2)   # one-two digits  "2025-6-5" → "2025-06-25"
    d_padded = d.zfill(2)   # one-two digits
    ymd_str = f"{y}-{m_padded}-{d_padded}"
    return p_index, ymd_str

tasks.sort(key=sort_key)

for i in range(len(tasks)):
    print(f"{i + 1}. {tasks[i]}")