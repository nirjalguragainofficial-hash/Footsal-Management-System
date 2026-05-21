import urllib.request
import json
import sys

puml_text = """@startuml
left to right direction
skinparam packageStyle rectangle

actor "General User" as U
actor "Administrator" as A

rectangle "CourtSync System" {
  usecase "Browse Courts" as UC_BC
  usecase "Check Availability" as UC_CA
  usecase "Book Court" as UC_BK
  usecase "Make Payment (Wallet)" as UC_MP
  usecase "View Booking History" as UC_VH
  
  usecase "Manage Courts" as UC_MC
  usecase "Monitor Bookings" as UC_MB
  usecase "Manage Users" as UC_MU
}

U -- UC_BC
U -- UC_CA
U -- UC_BK
U -- UC_MP
U -- UC_VH

A -- UC_MC
A -- UC_MB
A -- UC_MU
A -- UC_VH

@enduml
"""

try:
    data = json.dumps({
        "diagram_source": puml_text,
        "diagram_type": "plantuml",
        "output_format": "png"
    }).encode('utf-8')

    req = urllib.request.Request("https://kroki.io/plantuml/png", data=data, headers={
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    })

    with urllib.request.urlopen(req) as response:
        with open("use_case_diagram.png", "wb") as f:
            f.write(response.read())

    print("use_case_diagram.png created successfully")
except urllib.error.HTTPError as e:
    print(f"HTTP Error: {e.code} - {e.reason}")
    sys.exit(1)
except Exception as e:
    print(f"Error generating diagram: {e}")
    sys.exit(1)
