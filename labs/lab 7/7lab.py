#1задание
objects = [
    ("Containment Cell A", 4),
    ("Archive Vault", 1),
    ("Bio Lab Sector", 3),
    ("Observation Wing", 2)
]
new_objects = sorted(objects, key=lambda x: x[1])
print(new_objects)


#2задание
staff_shifts = [
    {"name": "Dr. Shaw", "shift_cost": 120, "shifts": 15},
    {"name": "Agent Torres", "shift_cost": 90, "shifts": 22},
    {"name": "Researcher Hall", "shift_cost": 150, "shifts": 10}
]
total_costs = list(map(lambda x: x["shift_cost"] * x["shifts"], staff_shifts))
max_cost = max(total_costs)
print("Общая стоимость работы каждого сотрудника:", total_costs)
print("Максимальная стоимость:", max_cost)


#3задание
personnel = [
    {"name": "Dr. Klein", "clearance": 2},
    {"name": "Agent Brooks", "clearance": 4},
    {"name": "Technician Reed", "clearance": 1}
]
result = list(map(lambda p: {
    "name": p["name"],
    "clearance": p["clearance"],
    "category": "Restricted" if p["clearance"] == 1 else
                "Confidential" if p["clearance"] <= 3 else
                "Top Secret"
}, personnel))
print(result)


#4задание
zones = [
    {"zone": "Sector-12", "active_from": 8, "active_to": 18},
    {"zone": "Deep Storage", "active_from": 0, "active_to": 24},
    {"zone": "Research Wing", "active_from": 9, "active_to": 17}
]
new_zone = list(filter(lambda x: x["active_from"] >= 8 and x["active_to"] <= 18, zones))
print(new_zone)


#5задание
reports = [
    {"author": "Dr. Moss", "text": "Analysis completed. Reference: http://external-archive.net"},
    {"author": "Agent Lee", "text": "Incident resolved without escalation."},
    {"author": "Dr. Patel", "text": "Supplementary data available at https://secure-research.org"},
    {"author": "Supervisor Kane", "text": "No anomalies detected during inspection."},
    {"author": "Researcher Bloom", "text": "Extended observations uploaded to http://research-notes.lab"},
    {"author": "Agent Novak", "text": "Perimeter secured. No external interference observed."},
    {"author": "Dr. Hargreeve", "text": "Full containment log stored at https://internal-db.scp"},
    {"author": "Technician Moore", "text": "Routine maintenance completed successfully."},
    {"author": "Dr. Alvarez", "text": "Cross-reference materials: http://crosslink.foundation"},
    {"author": "Security Officer Tan", "text": "Shift completed without incidents."},
    {"author": "Analyst Wright", "text": "Statistical model published at https://analysis-hub.org"},
    {"author": "Dr. Kowalski", "text": "Behavioral deviations documented internally."},
    {"author": "Agent Fischer", "text": "Additional footage archived: http://video-storage.sec"},
    {"author": "Senior Researcher Hall", "text": "All test results verified and approved."},
    {"author": "Operations Lead Grant", "text": "Emergency protocol draft shared via https://ops-share.scp"}
]
reports_with_links = []
for report in reports:
    if "http://" in report["text"] or "https://" in report["text"]:
        reports_with_links.append(report)
res = []
for report in reports_with_links:
    text = report["text"]
    if "http://" in text:
        text = text.replace("http://", "[ДАННЫЕ УДАЛЕНЫ]")
    if "https://" in text:
        text = text.replace("https://", "[ДАННЫЕ УДАЛЕНЫ]")
    res.append({"author": report["author"], "text": text})
print(res)


#6задание
scp_objects = [
    {"scp": "SCP-096", "class": "Euclid"},
    {"scp": "SCP-173", "class": "Euclid"},
    {"scp": "SCP-055", "class": "Keter"},
    {"scp": "SCP-999", "class": "Safe"},
    {"scp": "SCP-3001", "class": "Keter"}
]
new_scp_objects = list(filter(lambda x: x["class"] != 'Safe', scp_objects))
print(new_scp_objects)


#7задание
incidents = [
    {"id": 101, "staff": 4},
    {"id": 102, "staff": 12},
    {"id": 103, "staff": 7},
    {"id": 104, "staff": 20}
]
new_incidents = sorted(incidents, key=lambda x: x["staff"], reverse=True)
print(new_incidents[:3])


#8задание
protocols = [
    ("Lockdown", 5),
    ("Evacuation", 4),
    ("Data Wipe", 3),
    ("Routine Scan", 1)
]
new_protocol = list(map(lambda x: f"Protocol {x[0]} - Criticality {x[1]}", protocols))
print(new_protocol)


#9задание
shifts = [6, 12, 8, 24, 10, 4]
new_shifts = list(filter(lambda x:8 <= x <= 12, shifts))
print(new_shifts)


#10задание
evaluations = [
    {"name": "Agent Cole", "score": 78},
    {"name": "Dr.Weiss", "score": 92},
    {"name": "Technician Moore", "score": 61},
    {"name": "Researcher Lin", "score": 88}
]
max_ev = max(evaluations, key=lambda x: x['score'])
print(f'{max_ev['name']}: {max_ev['score']}')